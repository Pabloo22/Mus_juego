from calculador import *
from apuestas import *

"""
El juego original es para 4 jugadores. 
En este programa, para más simplicidad, y poder así ser 
jugable por un único jugador, el juego es por ahora 
jugable únicamente por 1 jugador vs la IA.

Cómo jugar al mus: https://es.wikipedia.org/wiki/Mus
"""

puntuacionIA = 0
puntuacionJug = 0
rondas = 1
tantos = 30  # A cuánto hay que llegar para ganar
tantos = int(input("¿A cuántos puntos desea jugar? ")) 

# Estadistica
GrandeIA = 0
GrandeJug = 0
ChicaIA = 0
ChicaJug = 0
ParesIA = 0
ParesJug = 0
JuegoIA = 0
JuegoJug = 0

def final(puntJug, puntIA):

	if puntJug >= tantos or puntIA >= tantos:
		return True
	else:
		return False

while True:


	print("------------------ RONDA " + str(rondas) + " ------------------")

	manoIA, manoJug = repartir(2)

	 # Par->mano = Jug; Impar->mano = IA
	if rondas%2 == 0:
		mano = "Jug"
	else:
		mano = "IA"

	print("El mano es " + mano)
	print("Tus cartas son: " + str(manoJug))

	# ESTADISTICAS:
	gana_grande = ganaGrande(manoIA, manoJug, mano)
	gana_chica = ganaChica(manoIA, manoJug, mano)
	gana_pares = ganaPares(manoIA, manoJug, mano)
	gana_juego = ganaJuego(manoIA, manoJug, mano)

	if gana_grande == "IA":
		GrandeIA += 1
	elif gana_grande == "Jug":
		GrandeJug += 1
	if gana_chica == "IA":
		ChicaIA += 1
	elif gana_chica == "Jug":
		ChicaJug += 1
	if gana_pares == "IA":
		ParesIA += 1
	elif gana_pares == "Jug":
		ParesJug += 1
	if gana_juego == "IA":
		JuegoIA += 1
	elif gana_juego == "Jug":
		JuegoJug += 1

	# GRANDE
	Apuesta_Grande = apostar(manoJug, manoIA, mano, "grande", puntuacionJug, puntuacionIA, tantos)
	print(Apuesta_Grande)

	ganador_grande = Apuesta_Grande[2]

	if ganador_grande != "Jug" and ganador_grande != "IA":
		ganador_grande = gana_grande


	if not Apuesta_Grande[0]: # Pendiente
		if ganador_grande == "Jug":
			puntuacionJug += Apuesta_Grande[1]
			print(f"Tu puntuación ha subido a: {puntuacionJug}")
		else:
			puntuacionIA += Apuesta_Grande[1]
			print(f"La puntuación de la IA ha subido a: {puntuacionIA}")
		if final(puntuacionJug, puntuacionIA):
			print("Cartas de la IA: " + str(manoIA))
			break

	# CHICA
	apuesta_chica = apostar(manoJug, manoIA, mano, "chica", puntuacionJug, puntuacionIA, tantos)
	print(apuesta_chica)

	ganador_Chica = apuesta_chica[2]

	if ganador_Chica != "Jug" and ganador_Chica != "IA":
		ganador_Chica = gana_chica


	if not apuesta_chica[0]: # Pendiente
		if ganador_Chica == "Jug":
			puntuacionJug += apuesta_chica[1]
			print(f"Tu puntuación ha subido a: {puntuacionJug}")
		else:
			puntuacionIA += apuesta_chica[1]
			print(f"La puntuación de la IA ha subido a: {puntuacionIA}")
		if final(puntuacionJug, puntuacionIA):
			print("Cartas de la IA: " + str(manoIA))
			break

	# A PARES
	Apuesta_Pares = apostar(manoJug, manoIA, mano, "pares", puntuacionJug, puntuacionIA, tantos)
	print(Apuesta_Pares)

	ganador_Pares = Apuesta_Pares[2]

	if ganador_Pares != "Jug" and ganador_Pares != "IA":
		ganador_Pares = gana_pares


	if not Apuesta_Pares[0]: # Pendiente
		if ganador_Pares == "Jug":
			puntuacionJug += Apuesta_Pares[1]
			print(f"Tu puntuación ha subido a: {puntuacionJug}")
		else:
			puntuacionIA += Apuesta_Pares[1]
			print(f"La puntuación de la IA ha subido a: {puntuacionIA}")
		if final(puntuacionJug, puntuacionIA):
			print("Cartas de la IA: " + str(manoIA))
			break

	# A JUEGO
	Apuesta_Juego = apostar(manoJug, manoIA, mano, "juego", puntuacionJug, puntuacionIA, tantos)
	print(Apuesta_Juego)

	ganador_Juego = Apuesta_Juego[2]

	if ganador_Juego != "Jug" and ganador_Juego != "IA":
		ganador_Juego = gana_juego

	if not Apuesta_Juego[0]: # Pendiente
		if ganador_Juego == "Jug":
			puntuacionJug += Apuesta_Juego[1]
			print(f"Tu puntuación ha subido a: {puntuacionJug}")
		else:
			puntuacionIA += Apuesta_Juego[1]
			print(f"La puntuación de la IA ha subido a: {puntuacionIA}")
		if final(puntuacionJug, puntuacionIA):
			print("Cartas de la IA: " + str(manoIA))
			break

	# else: queda pendiente
	print("")
	print("Cartas de la IA: " + str(manoIA))
	print("El ganador de la grande es: " + gana_grande)
	print("El ganador de la chica es: " + gana_chica)
	print("El ganador de los pares es: " + gana_pares)
	print("El ganador de el juego es: " + gana_juego)

	print("")

# Conteo de tantos pendientes:
	# Grande:
	if Apuesta_Grande[0]: 
		print("Tantos pendientes a GRANDE:")
		if ganador_grande == "Jug":
			puntuacionJug += Apuesta_Grande[1]
			print(f"Tu puntuación ha subido a: {puntuacionJug}")
		else: 
			puntuacionIA += Apuesta_Grande[1]
			print(f"La puntuación de la IA ha subido a: {puntuacionIA}")
		if final(puntuacionJug, puntuacionIA):
			print("Cartas de la IA: " + str(manoIA))
			break
	# Chica:
	if apuesta_chica[0]: 
		print("Tantos pendientes a CHICA:")
		if ganador_Chica == "Jug":
			puntuacionJug += apuesta_chica[1]
			print(f"Tu puntuación ha subido a: {puntuacionJug}")
		else: 
			puntuacionIA += apuesta_chica[1]
			print(f"La puntuación de la IA ha subido a: {puntuacionIA}")
		if final(puntuacionJug, puntuacionIA):
			print("Cartas de la IA: " + str(manoIA))
			break
	# A pares
	if Apuesta_Pares[0]: 
		print("Tantos pendientes a PARES:")
		if ganador_Pares == "Jug":
			print("Por tener pares:", devuelve_par(manoJug))
			puntuacionJug += devuelve_par(manoJug)
			puntuacionJug += Apuesta_Pares[1]
			print(f"Tu puntuación ha subido a: {puntuacionJug}")
		elif ganador_Pares == "IA": 
			print("Por tener pares:", devuelve_par(manoIA))
			puntuacionIA += devuelve_par(manoIA)
			puntuacionIA += Apuesta_Pares[1]
			print(f"La puntuación de la IA ha subido a: {puntuacionIA}")
		else:
			print("ninguno")
		if final(puntuacionJug, puntuacionIA):
			print("Cartas de la IA: " + str(manoIA))
			break
	else: 
		print("Tantos pendientes a PARES:")
		if ganador_Pares == "Jug":
			print("Por tener pares:", devuelve_par(manoJug))
			puntuacionJug += devuelve_par(manoJug)
			print(f"Tu puntuación ha subido a: {puntuacionJug}")
		elif ganador_Pares == "IA": 
			print("Por tener pares:", devuelve_par(manoIA))
			puntuacionIA += devuelve_par(manoIA)
			print(f"La puntuación de la IA ha subido a: {puntuacionIA}")
		if final(puntuacionJug, puntuacionIA):
			print("Cartas de la IA: " + str(manoIA))
			break

	# A Juego
	if Apuesta_Juego[0]:  # Si quedaba pendiente
		print("Tantos pendientes a JUEGO:")
		if ganador_Juego == "Jug":
			ExtraJug = tanteo_juego(contar_juego(manoJug))
			print("Por el juego/punto:", ExtraJug)
			puntuacionJug += ExtraJug
			puntuacionJug += Apuesta_Juego[1]
			print(f"Tu puntuación ha subido a: {puntuacionJug}")
		elif ganador_Juego == "IA": 
			ExtraIA = tanteo_juego(contar_juego(manoIA))
			print("Por el juego/punto:", ExtraIA)
			puntuacionIA += ExtraIA
			puntuacionIA += Apuesta_Juego[1]
			print(f"La puntuación de la IA ha subido a: {puntuacionIA}")
		else:
			print("ninguno")
		if final(puntuacionJug, puntuacionIA):
			print("Cartas de la IA: " + str(manoIA))
			break
	else: 
		print("Tantos pendientes a JUEGO:")
		if ganador_Juego == "Jug":
			ExtraJug = tanteo_juego(contar_juego(manoJug))
			print("Por el juego/punto:", ExtraJug)
			puntuacionJug += ExtraJug
			print(f"Tu puntuación ha subido a: {puntuacionJug}")
		elif ganador_Juego == "IA": 
			ExtraIA = tanteo_juego(contar_juego(manoIA))
			print("Por el juego/punto:", ExtraIA)
			puntuacionIA += ExtraIA
			print(f"La puntuación de la IA ha subido a: {puntuacionIA}")
		if final(puntuacionJug, puntuacionIA):
			print("Cartas de la IA: " + str(manoIA))
			break


	print(f"Tu puntuación: {puntuacionJug}")
	print(f"puntuación de la IA: {puntuacionIA}")
	print("")
	rondas += 1

print("")
if puntuacionJug >= tantos:
	print("¡HAS GANADO!")
else:
	print("Has perdido... :(")

print("")

# Damos las estadísticas de la partida
print("ESTADISTICAS DE LA PARTIDA:")
porcentaje_grande = GrandeJug / (GrandeIA + GrandeJug)
porcentaje_chica = ChicaJug / (ChicaIA + ChicaJug)
try:
	porcentaje_pares = ParesJug / (ParesIA + ParesJug)
except:
	porcentaje_pares = "sin datos"
porcentaje_juego = JuegoJug / (JuegoIA + JuegoJug)

print("Porcentaje de veces que tuviste mejores cartas que la IA: ")
print("   - En grande:", porcentaje_grande)
print("   - En chica:", porcentaje_chica)
print("   - En pares:", porcentaje_pares)
print("   - En juego:", porcentaje_juego)

