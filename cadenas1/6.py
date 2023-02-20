def tiempo():
	palabra=input('ingrese palabra:')
	past='io', 'ieron', 'iste', 'i', 'te', 'o', 'aron', 'do', 'aste'
	present='ais', 'es', 'en', 'imos', 'is', 'amos','nar'
	future='e', 'as', 'a', 'emos', 'eis', 'an'

	if palabra.endswith(tuple(past)):
		return 'pasado'
	elif palabra.endswith(tuple(present)):
		return 'presente'
	elif palabra.endswith(tuple(future)):
		return 'futuro'
	else:
		return 'irreconocible'
		
print('La palabra esta en',tiempo())
