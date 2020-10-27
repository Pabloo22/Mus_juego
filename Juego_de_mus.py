from calculador import *
from apuestas import *

"""
El juego original es para 4 jugadores. En este programa, para más simplicidad, y poder así ser jugable por un único jugador, el juego es por ahora jugable únicamente por 1 jugador vs la IA.

Cómo jugar al mus: https://es.wikipedia.org/wiki/Mus
"""

puntuacionIA = 0
puntuacionJug = 0
rondas = 1

def final(puntJug, puntIA):

	if puntJug >= 20 or puntIA >= 20:
		return True
	else:
		return False

while True:

	print("------------------ RONDA " + str(rondas) + " ------------------")

	manos = repartir(2)

	 # Par->mano = Jug; Impar->mano = IA
	if rondas%2 == 0:
		mano = "Jug"
	else:
		mano = "IA"

	manoIA = manos[0]
	manoJug = manos[1]
	print("El mano es " + mano)
	print("Tus cartas son: " + str(manoJug))

	# GRANDE
	Apuesta_Grande = apostar(manoJug, manoIA, mano, puntuacionJug, puntuacionIA, "grande")
	print(Apuesta_Grande)

	ganador_grande = Apuesta_Grande[2]

	if ganador_grande != "Jug" and ganador_grande != "IA":
		ganador_grande = GanaGrande(manoIA, manoJug, mano)


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
	Apuesta_Chica = apostar(manoJug, manoIA, mano, puntuacionJug, puntuacionIA, "chica")
	print(Apuesta_Chica)

	ganador_Chica = Apuesta_Chica[2]

	if ganador_Chica != "Jug" and ganador_Chica != "IA":
		ganador_Chica = GanaChica(manoIA, manoJug, mano)


	if not Apuesta_Chica[0]: # Pendiente
		if ganador_Chica == "Jug":
			puntuacionJug += Apuesta_Chica[1]
			print(f"Tu puntuación ha subido a: {puntuacionJug}")
		else:
			puntuacionIA += Apuesta_Chica[1]
			print(f"La puntuación de la IA ha subido a: {puntuacionIA}")
		if final(puntuacionJug, puntuacionIA):
			print("Cartas de la IA: " + str(manoIA))
			break

	# A PARES
	Apuesta_Pares = apostar(manoJug, manoIA, mano, puntuacionJug, puntuacionIA, "pares")
	print(Apuesta_Pares)

	ganador_Pares = Apuesta_Pares[2]

	if ganador_Pares != "Jug" and ganador_Pares != "IA":
		ganador_Pares = GanaPares(manoIA, manoJug, mano)


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
	Apuesta_Juego = apostar(manoJug, manoIA, mano, puntuacionJug, puntuacionIA, "juego")
	print(Apuesta_Juego)

	ganador_Juego = Apuesta_Juego[2]

	if ganador_Juego != "Jug" and ganador_Juego != "IA":
		ganador_Juego = GanaJuego(manoIA, manoJug, mano)

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
	print("El ganador de la grande es: " + GanaGrande(manoIA, manoJug, mano))
	print("El ganador de la chica es: " + GanaChica(manoIA, manoJug, mano))
	print("El ganador de los pares es: " + GanaPares(manoIA, manoJug, mano))
	print("El ganador de el juego es: " + GanaJuego(manoIA, manoJug, mano))

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
	if Apuesta_Chica[0]: 
		print("Tantos pendientes a CHICA:")
		if ganador_Chica == "Jug":
			puntuacionJug += Apuesta_Chica[1]
			print(f"Tu puntuación ha subido a: {puntuacionJug}")
		else: 
			puntuacionIA += Apuesta_Chica[1]
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
			ExtraJug = tanteo_juego(Contar_Juego(manoJug))
			print("Por el juego/punto:", ExtraJug)
			puntuacionJug += ExtraJug
			puntuacionJug += Apuesta_Juego[1]
			print(f"Tu puntuación ha subido a: {puntuacionJug}")
		elif ganador_Juego == "IA": 
			ExtraIA = tanteo_juego(Contar_Juego(manoIA))
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
			ExtraJug = tanteo_juego(Contar_Juego(manoJug))
			print("Por el juego/punto:", ExtraJug)
			puntuacionJug += ExtraJug
			print(f"Tu puntuación ha subido a: {puntuacionJug}")
		elif ganador_Juego == "IA": 
			ExtraIA = tanteo_juego(Contar_Juego(manoIA))
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

if puntuacionJug > 19:
	print("¡HAS GANADO!")
else:
	print("Has perdido... :(")

# print("Prob de ganar a grande con " + str(manoIA) + " " + str(Prob_Ganar_Grande(manoIA, mano)))
# print("Prob de ganar a chica con " + str(manoIA) + " " + str(Prob_Ganar_Chica(manoIA, mano)))
# print("Prob de ganar a pares con " + str(manoIA) + " " + str(Prob_Ganar_Pares(manoIA, mano)))
# print("Prob de ganar a juego/punto con " + str(manoIA) + " " + str(Prob_Ganar_Juego(manoIA, mano)))