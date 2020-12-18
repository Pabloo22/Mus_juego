from random import shuffle, choice
from typing import List, Tuple

BARAJA = ["R", "R", "R", "R", "R", "R", "R", "R",
		1, 1, 1, 1, 1, 1, 1, 1,
		4, 4, 4, 4,
		5, 5, 5, 5,
		6, 6, 6, 6,
		7, 7, 7, 7,
		"S", "S", "S", "S",
		"C", "C", "C", "C"]

def repartir_rapido(cartasIA):
	"""
	Este generador está explicitamente creada para cuando la IA
	calcula las probabilidades de ganar. De esta forma es mucho
	más rápido y eficiente el programa.
	"""
	while True:
		# Creamos la baraja
		baraja = BARAJA.copy()
		for c in cartasIA:
			baraja.remove(c)
		
		shuffle(baraja)
		
		for c in baraja:
			yield c

def repartir(n_jugadores, baraja=BARAJA.copy()) -> Tuple[list]:

		# El nº es 1 cuando la IA juega contra sí misma en el cálculo de la probabilidad
	if n_jugadores == 1: 
		mano1 = [next(baraja) for _ in range(4)]
		return mano1

	else:
		# Barajeamos:
		shuffle(baraja)

		# Repartimos las cartas
		mano1 = baraja[:4]
		mano2 = baraja[4:8]

		return mano1, mano2


# Se declaran fuera porque son los mismos para grande que para chica
Valor = {"R": 8, "C": 7, "S": 6, 7: 5, 6: 4, 5: 3, 4: 2, 1: 1} 

def insertion_sort(lista):
	for j in range(1, len(lista)):
		key = lista[j]
		i = j - 1
		while i >= 0 and lista[i] < key:
			lista[i+1] = lista[i]
			i -= 1
		lista[i+1] = key
	return lista

def ordenar(mano) -> List[int]:
	# Cambiamos la lista de cartas por su valor (orden de victoria)
	valores = []
	for n in range(4):
		valores.append(Valor[mano[n]])

	return insertion_sort(valores)

def ganaGrande(manoIA, manoJug, mano) -> "IA" or "Jug":

	valoresIA = ordenar(manoIA)
	valoresJug = ordenar(manoJug)

	# Determinamos ganador

	if valoresIA[0] != valoresJug[0]:
		if valoresIA[0] > valoresJug[0]:
			return "IA"
		else:
			return "Jug"
	elif valoresIA[1] != valoresJug[1]:
		if valoresIA[1] > valoresJug[1]:
			return "IA"
		else:
			return "Jug"
	elif valoresIA[2] != valoresJug[2]:
		if valoresIA[2] > valoresJug[2]:
			return "IA"
		else:
			return "Jug"
	elif valoresIA[3] != valoresJug[3]:
		if valoresIA[3] > valoresJug[3]:
			return "IA"
		else:
			return "Jug"
	else: 
		return mano # A empate gana quien sea mano

def ganaChica(manoIA, manoJug, mano) -> "IA" or "Jug":

	valoresIA = ordenar(manoIA)
	valoresJug = ordenar(manoJug)

	# Determinamos ganador (proceso inverso)

	if valoresIA[3] != valoresJug[3]:
		if valoresIA[3] < valoresJug[3]:
			return "IA"
		else:
			return "Jug"
	elif valoresIA[2] != valoresJug[2]:
		if valoresIA[2] < valoresJug[2]:
			return "IA"
		else:
			return "Jug"
	elif valoresIA[1] != valoresJug[1]:
		if valoresIA[1] < valoresJug[1]:
			return "IA"
		else:
			return "Jug"
	elif valoresIA[0] != valoresJug[0]:

		if valoresIA[0] < valoresJug[0]:
			return "IA"
		else:
			return "Jug"
	else: 
		return mano # A empate gana quien sea mano
    
def devuelve_par(mano):
	""" Retornos:
	No par -> False
	par -> 1
	medias -> 2
	duples -> 3
	"""
	valores_mano = ordenar(mano)
	veces = [valores_mano.count(valores_mano[i]) for i in range(len(valores_mano))]

	# Compruebo si hay par
	if veces[0] == 1 and veces[1] == 1 and veces[2] == 1:
		return False
	# Si hay medias
	elif veces[0] == 3 or veces[1] == 3:
		return 2
	# Si hay duples
	elif (veces[0] == 2 and veces[1] == 2 and veces[2] == 2 and veces[3] == 2) or veces[0] == 4:
		return 3
	# Si no se ha cumplido nada de esto entonces tiene solo par
	else:
		return 1

def ganaPares(manoIA, manoJug, mano) -> "IA" or "Jug": 
    
	valoresIA = ordenar(manoIA) # [8, 8, 1, 1]
	valoresJug = ordenar(manoJug)

	parIA = devuelve_par(manoIA)
	parJug = devuelve_par(manoJug)

	# mayor_parIA = mayor_par(valoresIA, parIA)
	# mayor_parJug = mayor_par(valoresJug, parJug)

	if parIA and parJug:  # Si ambos tienen pares
		if parIA > parJug:
			return "IA"
		elif parJug > parIA:
			return "Jug"
		else:  # Mismo par !!!
			if parIA == 2 or parIA == 3:
				if valoresIA[1] > valoresJug[1]:
					return "IA"
				elif valoresIA[1] < valoresJug[1]:  
					return "Jug"
				elif valoresIA[2] > valoresJug[2]: # Sirve si hay duples
				# Comprueba los valores de la 2a pareja
					return "IA"
				elif valoresIA[2] < valoresJug[2]:
					return "Jug"
				else:
					return mano
			else:  # Par simple
				# Posibilidades: abbc, aabc, abcc
				if valoresIA[1] == valoresIA[2]:  # abbc
					parIA = valoresIA[1]
				elif valoresIA[0] == valoresIA[1]:  # aabc
					parIA = valoresIA[0]
				else:  # abcc
					parIA = valoresIA[2]

				if valoresJug[1] == valoresJug[2]:  # abbc
					parJug = valoresJug[1]
				elif valoresJug[0] == valoresJug[1]:  # aabc
					parJug = valoresJug[0]
				else:  # abcc
					parJug = valoresJug[2]

				if parIA > parJug:
					return "IA"
				elif parJug > parIA:
					return "Jug"
				else:  # Si hay empate
					return mano

	elif parIA and not parJug:
		return "IA"
	elif not parIA and parJug:
		return "Jug"
	else:
		return "nadie"

def contar_juego(mano) -> int:
	VALORES = {"R": 10, "C": 10, "S": 10, 7: 7, 6: 6, 5: 5, 4: 4, 1: 1}

	valores_mano = []
	for n in range(4):
		valores_mano.append(VALORES[mano[n]])

	Juego = 0
	for valor in valores_mano:
		Juego += valor
	return Juego

def tanteo_juego(juego) -> 1 or 2 or 3:
	if juego > 30:
		if juego == 31:
			return 3
		else:
			return 2
	else:
		return 1

def ganaJuego(manoIA, manoJug, mano) -> "IA" or "Jug":

	JuegoIA = contar_juego(manoIA)
	JuegoJug = contar_juego(manoJug)

	if JuegoIA > 30 and JuegoJug > 30:

		if JuegoIA == JuegoJug:
			return mano 
		elif JuegoIA == 31:
			return "IA"
		elif JuegoJug == 31:
			return "Jug"
		elif JuegoIA == 32:
			return "IA"
		elif JuegoJug == 32:
			return "Jug"
		elif JuegoIA > JuegoJug:
			return "IA"
		else:
			return "Jug"
	elif JuegoIA > 30:
		return "IA"
	elif JuegoJug > 30:
		return "Jug"
	else:
		if JuegoIA == JuegoJug:
			return mano
		elif JuegoIA > JuegoJug:
			return "IA"
		else:
			return "Jug"

def prob_ganar_grande(manoIA, mano):

	rep = 10_000
	casos_favorables = 0
	baraja = repartir_rapido(manoIA)

	for i in range(rep):
		manoJug = repartir(1, baraja)
		ganador = ganaGrande(manoIA, manoJug, mano)
		if ganador == "IA":
			casos_favorables += 1

	return casos_favorables/rep

def prob_ganar_chica(manoIA, mano):

	rep = 10_000
	casos_favorables = 0
	baraja = repartir_rapido(manoIA)

	for i in range(rep):
		manoJug = repartir(1, baraja)
		ganador = ganaChica(manoIA, manoJug, mano)
		if ganador == "IA":
			casos_favorables += 1

	return casos_favorables/rep

def prob_ganar_pares(manoIA, mano):

	rep = 10_000
	total = rep
	casos_favorables = 0
	baraja = repartir_rapido(manoIA)

	for i in range(rep):

		manoJug = repartir(1, baraja)
		while not devuelve_par(manoJug):
			manoJug = repartir(1, baraja)

		ganador = ganaPares(manoIA, manoJug, mano)

		if ganador == "IA":
			casos_favorables += 1

	return casos_favorables/total


def prob_ganar_juego(manoIA, mano):

	JuegoIA = contar_juego(manoIA)
	rep = 10_000
	baraja = repartir_rapido(manoIA)

	if JuegoIA > 30: 
		casos_favorables = 0
		for i in range(rep):
			manoJug = repartir(1, baraja)
			while contar_juego(manoJug) <= 30:
				manoJug = repartir(1, baraja)
			ganador = ganaJuego(manoIA, manoJug, mano)

			if ganador == "IA":
				casos_favorables += 1
	else:
		casos_favorables = 0
		baraja = repartir_rapido(manoIA)
		for i in range(rep):
			manoJug = repartir(1, baraja)
			while contar_juego(manoJug) > 30:
				manoJug = repartir(1, baraja)

			ganador = ganaJuego(manoIA, manoJug, mano)

			if ganador == "IA":
				casos_favorables += 1

	return casos_favorables/rep











