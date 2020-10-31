from calculador import *
from random import random, choice


def Apuesta_IA(manoIA, apostado, mano, lance, puntuacionJug, puntuacionIA, tantos):
	# Esta función devuelve la apuesta de la IA en función de lo apostado y la probabilidad de ganar a grande con sus cartas.

	if lance == "grande":
		prob_ganar = Prob_Ganar_Grande(manoIA, mano) 
	elif lance == "chica":
		prob_ganar = Prob_Ganar_Chica(manoIA, mano)
	elif lance == "pares":
		prob_ganar = Prob_Ganar_Pares(manoIA, mano)
	else:
		prob_ganar = Prob_Ganar_Juego(manoIA, mano)

	def desesperacion(apostado):
		if apostado == "ordago":
			print("La IA ha visto el órdago!")
			return "ver"
		else:
			print("La IA ha tirado un órdago!")
			return "ordago"

	def normal(apostado, prob_ganar):
		prob = random()
		envidar_fuerte = choice([3, 4, 5])
		envidar_flojo = choice([1, 2, 3])

		if prob_ganar > 0.9:
			if apostado == "ordago":
				print("La IA ha visto el órdago!")
				return "ver"
			elif apostado == "pasar": # Envidar fuerte 80%, flojo 10%, ordago 10%
				if prob < 0.1:
					print(f"La IA apuesta {envidar_flojo} más")
					print(f"Apuesta total actual: {envidar_flojo + 1}")
					return envidar_flojo
				elif prob < 0.9:
					print(f"La IA apuesta {envidar_fuerte} más")
					print(f"Apuesta total actual: {envidar_fuerte + 1}")
					return envidar_fuerte
				else:
					print("La IA ha tirado un órdago!")
					return "ordago"
			elif apostado <= 10: # Envidar fuerte 80%, flojo 10%, ordago 10%
				if prob < 0.1:
					print(f"La IA apuesta {envidar_flojo} más")
					print(f"Apuesta total actual: {envidar_flojo + apostado}")
					return envidar_flojo
				elif prob < 0.9:
					print(f"La IA apuesta {envidar_fuerte} más")
					print(f"Apuesta total actual: {envidar_fuerte + apostado}")
					return envidar_fuerte
				else:
					print("La IA ha tirado un órdago!")
					return "ordago"
			else:
				print("La IA ha visto la apuesta")
				return "ver"
		elif prob_ganar > 0.8:
			if apostado == "ordago": #50% ver, 50% pasar
				if prob < 0.5:
					print("La IA ha visto el órdago!")
					return "ver"
				else:
					print("La IA ha pasado")
					return "pasar"
			elif apostado == "pasar": # envidar flojo 80%, envidar fuerte 20%
				if prob < 0.2:
					print(f"La IA apuesta {envidar_fuerte} más")
					print(f"Apuesta total actual: {envidar_fuerte + 1}")
					return envidar_fuerte
				else:
					print(f"La IA apuesta {envidar_flojo} más")
					print(f"Apuesta total actual: {envidar_flojo + 1}")
					return envidar_flojo
			elif apostado <= 4: # envidar flojo 80%, envidar fuerte 20%
				if prob < 0.2:
					print(f"La IA apuesta {envidar_fuerte} más")
					print(f"Apuesta total actual: {envidar_fuerte + apostado}")
					return envidar_fuerte
				else:
					print(f"La IA apuesta {envidar_flojo} más")
					print(f"Apuesta total actual: {envidar_flojo + apostado}")
					return envidar_flojo
			else:	# 70% ver, 30% ordago
				if prob < 0.3:
					print("La IA ha tirado un órdago!")
					return "ordago"
				else:
					print("La IA ha visto la apuesta")
					return "ver"
		elif prob_ganar > 0.5:
			if apostado == "ordago": #pasar
				print("La IA ha pasado")
				return "pasar"
			elif apostado == "pasar": # envidar flojo 60%, envidar fuerte 20%, 20% pasar
				if prob < 0.2:
					print(f"La IA apuesta {envidar_fuerte} más")
					print(f"Apuesta total actual: {envidar_fuerte + 1}")
					return envidar_fuerte
				elif prob < 0.8:
					print(f"La IA apuesta {envidar_flojo} más")
					print(f"Apuesta total actual: {envidar_flojo + 1}")
					return envidar_flojo
				else:
					print("La IA ha pasado")	
					return "pasar"
			elif apostado >= 2 and apostado <= 4:
				print("La IA ha visto la apuesta")
				return "ver"
			elif apostado == 1: # envidar flojo 60%, envidar fuerte 20%, 20% pasar
				if prob < 0.2:
					print(f"La IA apuesta {envidar_fuerte} más")
					print(f"Apuesta total actual: {envidar_fuerte + apostado}")
					return envidar_fuerte
				elif prob < 0.8:
					print(f"La IA apuesta {envidar_flojo} más")
					print(f"Apuesta total actual: {envidar_flojo + apostado}")
					return envidar_flojo
				else:
					print("La IA ha pasado")	
					return "pasar"
			else:
				print("La IA ha pasado")	
				return "pasar"
		else:
			print("La IA ha pasado")
			return "pasar"

	def agresivo(apostado, prob_ganar):
		prob = random()
		envidar_fuerte = choice([4, 5, 6, 7])
		envidar_flojo = choice([1, 2, 3, 4])

		if prob_ganar > 0.85:
			if apostado == "ordago":
				print("La IA ha visto el órdago!")
				return "ver"
			elif apostado == "pasar": # Envidar fuerte 80%, flojo 10%, ordago 10%
				if prob < 0.1:
					print(f"La IA apuesta {envidar_flojo} más")
					print(f"Apuesta total actual: {envidar_flojo + 1}")
					return envidar_flojo
				elif prob < 0.9:
					print(f"La IA apuesta {envidar_fuerte} más")
					print(f"Apuesta total actual: {envidar_fuerte + 1}")
					return envidar_fuerte
				else:
					print("La IA ha tirado un órdago!")
					return "ordago"
			elif apostado <= 10: # Envidar fuerte 80%, flojo 10%, ordago 10%
				if prob < 0.1:
					print(f"La IA apuesta {envidar_flojo} más")
					print(f"Apuesta total actual: {envidar_flojo + apostado}")
					return envidar_flojo
				elif prob < 0.9:
					print(f"La IA apuesta {envidar_fuerte} más")
					print(f"Apuesta total actual: {envidar_fuerte + apostado}")
					return envidar_fuerte
				else:
					print("La IA ha tirado un órdago!")
					return "ordago"
			else:
				print("La IA ha visto la apuesta")
				return "ver"
		elif prob_ganar > 0.7:
			if apostado == "ordago": 
				print("La IA ha visto el órdago!")
				return "ver"
			elif apostado == "pasar": # envidar flojo 50%, envidar fuerte 20%, ordago 30%
				if prob < 0.5:
					print(f"La IA apuesta {envidar_fuerte} más")
					print(f"Apuesta total actual: {envidar_fuerte + 1}")
					return envidar_fuerte
				elif prob < 0.7:
					print(f"La IA apuesta {envidar_flojo} más")
					print(f"Apuesta total actual: {envidar_flojo + 1}")
					return envidar_flojo
				else:
					print("La IA ha tirado un órdago!")
					return "ordago"
			elif apostado <= 4: # envidar flojo 80%, envidar fuerte 20%
				if prob < 0.2:
					if apostado != 1:
						print(f"La IA apuesta {envidar_fuerte} más")
					else: 
						print(f"La IA apuesta {envidar_fuerte + 1}")
					print(f"Apuesta total actual: {envidar_fuerte + apostado}")
					return envidar_fuerte
				else:
					print(f"La IA apuesta {envidar_flojo} más")
					print(f"Apuesta total actual: {envidar_flojo + apostado}")
					return envidar_flojo
			else:
				print("La IA ha tirado un órdago!")
				return "ordago"

		elif prob_ganar > 0.4:
			if apostado == "ordago": #pasar
				print("La IA ha pasado")
				return "pasar"
			elif apostado == "pasar": # envidar flojo 20%, envidar fuerte 60%, 20% ordago
				if prob < 0.6:
					print(f"La IA apuesta {envidar_fuerte} más")
					print(f"Apuesta total actual: {envidar_fuerte + 1}")
					return envidar_fuerte
				elif prob < 0.8:
					print(f"La IA apuesta {envidar_flojo} más")
					print(f"Apuesta total actual: {envidar_flojo + 1}")
					return envidar_flojo
				else:
					print("La IA ha tirado un órdago!")
					return "ordago"
			elif apostado >= 2 and apostado <= 4:
				print("La IA ha visto la apuesta")
				return "ver"
			elif apostado == 1: # envidar flojo 60%, envidar fuerte 20%, 20% pasar
				if prob < 0.2:
					print(f"La IA apuesta {envidar_fuerte + 1}")
					print(f"Apuesta total actual: {envidar_fuerte + apostado}")
					return envidar_fuerte
				elif prob < 0.8:
					print(f"La IA apuesta {envidar_flojo + 1}")
					print(f"Apuesta total actual: {envidar_flojo + apostado}")
					return envidar_flojo
				else:
					print("La IA ha tirado un órdago!")
					return "ordago"
			else:
				if prob < 0.25:
					if apostado == "ordago": #pasar
						print("La IA ha pasado")
						return "pasar"
				else:
					print("La IA ha tirado un órdago!")
					return "ordago"
		else:
			print("La IA ha pasado")
			return "pasar"

	def pasivo_agresivo(apostado, prob_ganar):  # o ordago o pasa
		prob = random()

		if prob_ganar > 0.75:
			if apostado == "ordago":
				print("La IA ha visto el órdago!")
				return "ver"
			else:
				print("La IA ha tirado un órdago!")
				return "ordago"

		elif prob_ganar > 0.45:
			if apostado == "ordago":
				if prob_ganar > 0.65:
					print("La IA ha visto el órdago!")
					return "ver"
				else:
					print("La IA ha pasado")
					return "pasar"
			else:
				print("La IA ha tirado un órdago!")
				return "ordago"
		else:
			print("La IA ha pasado")
			return "pasar"


	# Si el rival está a punto de ganar se va a por todas
	if tantos - puntuacionJug == 1:
		return desesperacion(apostado)
	elif puntuacionIA - puntuacionJug > 4 and tantos - puntuacionJug < 5:
		return desesperacion(apostado)

	# Si vamos perdiendo por más de 6 se juega agresivo
	elif puntuacionJug - puntuacionIA > 8 or tantos - puntuacionJug <= 10:
		return pasivo_agresivo(apostado, prob_ganar)
	else:
		prob = random()
		if prob > 0.25:
			return normal(apostado, prob_ganar)
		else:
			return agresivo(apostado, prob_ganar)

	
