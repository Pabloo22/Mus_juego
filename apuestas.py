from calculador import *
from IA import *
from random import random, choice


"""
Tras realizar una apuesta el contador sube o se queda pendiente de ser actualizado según si se ha pasado o si se ha visto un órdago (contador sube), o si se ha visto una apuesta n o se ha dejado en paso (pendiente).
"""

def ApuestaJug(apostado):
	# Esta función pide una apuesta al jugador. Tiene en cuenta lo apostado previamente para hacer las preguntas correctas.
	# Devuelve lo que el jugador ha apostado. 
	pasar = 0
	# ¿ordago?
	if apostado == "ordago":
		ver = 0
		while ver != 1 and ver != 2:
			try:
				ver = int(input("¿Desea ver el órdago?(1=Sí, 2=No) "))
			except:
				pass
		if ver == 1: #Quiere ver la puesta
			return "ver"
		else: # Quiere pasar
			return "pasar"
	elif apostado == 1: # No ha habido apuesta anterior -> no se puede ver
		# ¿pasa?
		while pasar != 1 and pasar != 2:
			try:
				pasar = int(input("¿Desea apostar?(1=Sí, 2=No) "))
			except:
				pass
		if pasar == 2: #No desea apostar
			return "pasar"
		else: #Desea apostar
			Ordago = 0
			while Ordago != 1 and Ordago != 2: # ¿ordago?
				try:
					Ordago = int(input("Desea tirar un órdago (1=Sí, 2=No) "))
				except:
					pass
			if Ordago == 1: # quiere ordago
				return "ordago"
			else: # No quiere ordago, solo apostar
				apuesta = 0
				while apuesta == 0:
					try:
						apuesta = int(input(f"(Apuesta actual: 1)¿Cuánto desa subir la apuesta? "))
					except:
						pass
				return apuesta

	else: # Ha habido apuesta anterior
		# ¿pasa?
		while pasar != 1 and pasar != 2:
			try:
				pasar = int(input("¿Desea subir la apuesta?(1=Sí, 2=No) "))
			except:
				pass
		if pasar == 2: #No desea apostar más
			if apostado == "pasar":
				return "pasar"
			ver = 0
			while ver != 1 and ver != 2:
				try:
					ver = int(input(f"(Apuesta actual: {apostado})¿Desea ver la apuesta?(1=Sí, 2=No) "))
				except:
					pass
			if ver == 1: #Quiere ver la puesta
				return "ver"
			else: # Quiere pasar
				return "pasar"
		else: #Desea apostar
			Ordago = 0
			while Ordago != 1 and Ordago != 2: # ¿ordago?
				try:
					Ordago = int(input("Desea tirar un órdago (1=Sí, 2=No) "))
				except:
					pass
			if Ordago == 1: # quiere ordago
				return "ordago"
			else: # No quiere ordago, solo apostar
				apuesta = 0
				while apuesta == 0:
					try:
						apuesta = int(input(f"(Apuesta actual {apostado})¿Cuánto desa subir la apuesta? "))
					except:
						pass
				return apuesta 

def ordago(jugador1, apuesta2, apostado):
	# Esta función recibe quien ha tirado el órdago (jugador1) y cuál ha sido la respuesta del rival (apuesta2)
	# Devuelve lo que la funcion apostar() y la utilizaremos para ahorrar repetir código. 
	# Representa la opción 2 del esquema

	pendiente = False

	if apuesta2 == "pasar":
		return pendiente, apostado, jugador1
	else:
		return pendiente, 30, "ordago"

def apuesta_n(manoIA, mano: str, apostado, nueva_apuesta, apostador: str, respuesta, lance):
	"""
	Esta función tiene en cuenta la apuesta previa, la apuesta n a la que se ha subido la anterior y quién ha sido el que ha subido a la apuesta.
	Además necesita manoIA y mano para calcular la nueva apuesta de la IA.
	Devuelve lo que necesita la función apostar().
	Representa la opcion 3 del esquema.

	Se trata de una función recursiva que consiste en un bucle del que no saldrá hasta que uno de los dos jugadores no pase, vea la apuesta o tire órdago.

	Es necesario diferenciar entre quién ha subido la apuesta
	"""
	if apostador == "Jug":

		apuestaIA = respuesta

		if apuestaIA == "pasar":
			return False, apostado, "Jug"

		elif apuestaIA == "ver":
			return True, nueva_apuesta, "pendiente"

		elif apuestaIA == "ordago":
			apuestaJug = ApuestaJug(apuestaIA)
			return ordago("IA", apuestaJug, nueva_apuesta)

		else: # Apuesta numerica
			apuestaIA += nueva_apuesta 
			return apuesta_n(manoIA, mano, nueva_apuesta, apuestaIA, "IA", ApuestaJug(apuestaIA), lance)

	else: # Apostador == "IA"

		apuestaJug = respuesta

		if apuestaJug == "pasar":
			return False, apostado, "IA"

		elif apuestaJug == "ver":
			return True, nueva_apuesta, "pendiente"

		elif apuestaJug == "ordago":
			
			return ordago("Jug", Apuesta_IA(manoIA, apuestaJug, mano, lance), nueva_apuesta)

		else: # Apuesta numerica
			apuestaJug += nueva_apuesta
			return apuesta_n(manoIA, mano, nueva_apuesta, apuestaJug, "Jug", Apuesta_IA(manoIA, apuestaJug, mano, lance), lance) 

def apostar(manoJug, manoIA, mano, puntuacionJug, puntuacionIA, lance):
	"""
	Es la función principal de las apuestas y a la que llamaremos en el archivo Juego_de_mus.py 
	Devuelve una lista de 3 elementos: [¿pendiente?, apostado, ganador] el primero es de tipo boolean que indica si se deben sumar ya los puntos o no. El segundo son los puntos que se deben sumar al ganador y el tercero es el ganador (en caso de no verse la apuesta)
	Diferenciamos 2 casos. En el primero la mano es Jug, y en el segundo la mano es la IA.
	La mano tiene 3 posibles acciones: pasar, apostar, ordaguear. Comenzando aquí un arbol de decisión.
	ESQUEMA:
	Opción 1, Pasar: 
		pasar --> se acaba el bucle
		apuesta n --> continua el bucle... (Opción 2)
		órdago --> ordago()
	Opción 2, Órdago:
		ordago()
	Opción 3, apuesta n:
		ver --> se acaba el bucle. (Queda pendiente)
		pasar --> se acaba el bucle. (El ganador se lleva la apuesta n previa o en su defecto 1)
		órdago --> ordago()
		apuesta n --> Se repite el bucle.
	"""
	apostado = 1
	print("")
	if lance == "grande":
		print("A GRANDE: ")
	elif lance == "chica":
		print("A CHICA:")
	elif lance == "pares":
		print("A PARES:")

		parIA = devuelve_par(manoIA)
		parJug = devuelve_par(manoJug)

		if not parIA:
			print("La IA no tiene pares")
			if not parJug:
				print("Tú tampoco tienes pares")
				return True, 0, "n/a"
			else:
				return True, 0, "Jug"
		else:
			print("La IA tiene pares")
			if not parJug:
				print("Tú no tienes pares")
				return True, 0, "IA"
			else:
				print("Tú tambien tienes pares")

	else:
		print("A JUEGO:")
		JuegoIA = Contar_Juego(manoIA)
		JuegoJug = Contar_Juego(manoJug)

		if JuegoIA < 31:
			print("La IA no tiene juego")
			if JuegoJug < 31:
				print(f"Tú tampoco tienes juego ({JuegoJug})")
				print("AL PUNTO:")
			else:
				print(f"Tú tienes juego ({JuegoJug})")
				return True, 0, "Jug"
		else:
			print("La IA tiene juego")
			if JuegoJug < 31:
				print("Tú no tienes juego")
				return True, 0, "IA"
			else:
				print("Tú también tienes juego")

	if mano == "Jug":
		# PEDIMOS APUESTAS:
		# Apuesta el jugador
		apuestaJug = ApuestaJug(apostado)

		if type(apuestaJug) == int:
			apuestaJug += apostado # Ej: apuestaJug = 1+1 = 2

		# Apuesta la IA
		apuestaIA = Apuesta_IA(manoIA, apuestaJug, mano, lance)

		# OPCIÓN 1:
		if apuestaJug == "pasar":

			if apuestaIA == "pasar":
				pendiente = True

				ganador = "pendiente"
				return pendiente, apostado, ganador
					
			elif apuestaIA == "ordago":
				apuestaJug = ApuestaJug(apostado)
				return ordago("IA", apuestaJug, apostado)
				
			else: # apuesta numerica
				apuestaIA += apostado
				return apuesta_n(manoIA, mano, apostado, apuestaIA, "IA", ApuestaJug(apuestaIA), lance)

		# OPCIÓN 2: ordago
		elif apuestaJug == "ordago":
			return ordago("Jug", apuestaIA, apostado)

		# OPCIÓN 3: apuesta numerica
		else:
			return apuesta_n(manoIA, mano, apostado, apuestaJug, "Jug", apuestaIA, lance)
			
	else:
		# PEDIMOS APUESTAS:
		
		# Apuesta la IA
		apuestaIA = Apuesta_IA(manoIA, apostado, mano, lance)
		if type(apuestaIA) == int:
			apuestaIA += apostado # Ej: apuestaJug = 1+1 = 2

		# Apuesta el jugador
		apuestaJug = ApuestaJug(apuestaIA)
		if type(apuestaJug) == int:
			apuestaJug += apostado # Ej: apuestaJug = 1+1 = 2

		# OPCIÓN 1:
		if apuestaIA == "pasar":

			if apuestaJug == "pasar":
				pendiente = True

				ganador = "pendiente"
				return pendiente, apostado, ganador
					
			elif apuestaJug == "ordago":
				apuestaIA = Apuesta_IA(manoIA, apuestaJug, mano, lance)
				return ordago("Jug", apuestaIA, apostado)
				
			else: # apuesta numerica
				apuestaJug += apostado
				return apuesta_n(manoIA, mano, apostado, apuestaJug, "Jug", Apuesta_IA(manoIA, apostado, mano, lance), lance)

		# OPCIÓN 2: ordago
		elif apuestaIA == "ordago":
			return ordago("IA", apuestaJug, apostado)

		# OPCIÓN 3: apuesta numerica
		else:
			return apuesta_n(manoIA, mano, apostado, apuestaIA, "IA", apuestaJug, lance)