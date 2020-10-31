from random import choice, sample

def repartir(n_jugadores):
	# Creamos la baraja
	baraja = ["R" for i in range(8)]

	for i  in range(8):
		baraja.append(1)
	for i  in range(4):
		baraja.append("C")
		baraja.append("S")
		baraja.append(7)
		baraja.append(6)
		baraja.append(5)
		baraja.append(4)
	# Hay ocho reyes y ocho pitos (1's). No hay doses ni treses.

	# Repartimos las cartas
	mano1 = [baraja.pop(choice([carta for carta in range(len(baraja))])), 
			 baraja.pop(choice([carta for carta in range(len(baraja))])), 
			 baraja.pop(choice([carta for carta in range(len(baraja))])), 
			 baraja.pop(choice([carta for carta in range(len(baraja))]))]

	if n_jugadores == 1: # El nº es 1 cuando la IA juega contra sí misma en el cálculo de la probabilidad
		return mano1

	mano2 = [baraja.pop(choice([carta for carta in range(len(baraja))])), 
			baraja.pop(choice([carta for carta in range(len(baraja))])), 
			baraja.pop(choice([carta for carta in range(len(baraja))])), 
			baraja.pop(choice([carta for carta in range(len(baraja))]))]

	if n_jugadores == 4:
		mano3 = [baraja.pop(choice([carta for carta in range(len(baraja))])), 
				baraja.pop(choice([carta for carta in range(len(baraja))])), 
				baraja.pop(choice([carta for carta in range(len(baraja))])), 
				baraja.pop(choice([carta for carta in range(len(baraja))]))]
		mano4 = [baraja.pop(choice([carta for carta in range(len(baraja))])), 
				baraja.pop(choice([carta for carta in range(len(baraja))])), 
				baraja.pop(choice([carta for carta in range(len(baraja))])), 
				baraja.pop(choice([carta for carta in range(len(baraja))]))]
		return mano1, mano2, mano3, mano4
	else:
		return mano1, mano2


Valor = {"R":8, "C":7, "S":6, 7:5, 6:4, 5:3, 4:2, 1:1} # Se declaran fuera porque son los mismos para grande que para chica

def insertion_sort(lista):
		for j in range(1, len(lista)):
			key = lista[j]
			i = j - 1
			while i >= 0 and lista[i] < key:
				lista[i+1] = lista[i]
				i -= 1
			lista[i+1] = key
		return lista

def ordenar(mano):
	# Cambiamos la lista de cartas por su valor (orden de victoria)
	valores = []
	for n in range(4):
		valores.append(Valor[mano[n]])

	return insertion_sort(valores)

def GanaGrande(manoIA, manoJug, mano):

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

def GanaChica(manoIA, manoJug, mano):

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
	No par --> False
	par --> 2
	medias --> 3
	duples --> 4
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

def GanaPares(manoIA, manoJug, mano): 
    
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

def Contar_Juego(mano):
	Valores = {"R": 10, "C":10,"S": 10, 7:7, 6:6, 5:5, 4:4, 1:1}

	valores_mano = []
	for n in range(4):
		valores_mano.append(Valores[mano[n]])

	Juego = 0
	for valor in valores_mano:
		Juego += valor
	return Juego

def tanteo_juego(juego):
	if juego > 30:
		if juego == 31:
			return 3
		else:
			return 2
	else:
		return 1

def GanaJuego(manoIA, manoJug, mano):

	JuegoIA = Contar_Juego(manoIA)
	JuegoJug = Contar_Juego(manoJug)

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

def Prob_Ganar_Grande(manoIA, mano):

	rep = 100000
	casos_favorables = 0
	for i in range(rep):
		manoJug = repartir(1)
		ganador = GanaGrande(manoIA, manoJug, mano)
		if ganador == "IA":
			casos_favorables += 1

	return casos_favorables/rep

def Prob_Ganar_Chica(manoIA, mano):

	rep = 100000
	casos_favorables = 0
	for i in range(rep):
		manoJug = repartir(1)
		ganador = GanaChica(manoIA, manoJug, mano)
		if ganador == "IA":
			casos_favorables += 1

	return casos_favorables/rep

def Prob_Ganar_Pares(manoIA, mano):

	rep = 50000
	total = rep
	casos_favorables = 0
	
	for i in range(rep):

		manoJug = repartir(1)
		while not devuelve_par(manoJug):
			manoJug = repartir(1)

		ganador = GanaPares(manoIA, manoJug, mano)

		if ganador == "IA":
			casos_favorables += 1

	return casos_favorables/total


def Prob_Ganar_Juego(manoIA, mano):

	JuegoIA = Contar_Juego(manoIA)
	rep = 50000
	if JuegoIA > 30: 
		casos_favorables = 0
		for i in range(rep):
			manoJug = repartir(1)
			while Contar_Juego(manoJug) <= 30:
				manoJug = repartir(1)
			ganador = GanaJuego(manoIA, manoJug, mano)

			if ganador == "IA":
				casos_favorables += 1
	else:
		casos_favorables = 0
		for i in range(rep):
			manoJug = repartir(1)
			while Contar_Juego(manoJug) > 30:
				manoJug = repartir(1)

			ganador = GanaJuego(manoIA, manoJug, mano)

			if ganador == "IA (punto)":
				casos_favorables += 1

	return casos_favorables/rep






	





	


	# for carta in manoIA:

	# 	veces = manoIA.count(carta)

	# 	if veces == 2:

	# 		parIA = True
	# 		carta_parIA = carta

	# 	elif veces == 3:

	# 		mediasIA == 3:
	# 		carta_par










