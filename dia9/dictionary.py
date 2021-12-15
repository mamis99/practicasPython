dictionary = {}   #diccionario vacío

#Así se agregan definiciones al diccionario
dictionary['superman'] = 'it is very strong'
dictionary['flash'] = 'it is very fast'

#Quitar definición
dictionary.pop('superman')

#Imprimir diccionario completo
print(dictionary)

#Diccionario ya con definiciones
dictionary = {'superman':'he is very strong','flash':'he is the fastest man in the word',
              'green lantern':'he is the choosen one'}

for key in dictionary:   #Por cada palabra clave del diccionario
    print(key)     #imprime la palabra clave
    print(dictionary[key])    #e imprime la definición de esa palabra clave

#Diccionarios anidados
dictionary2 = {'superman':{'power1':'he can fly','power2':'he is strong'},'flash':'he is the fastest man in the word',
              'green lantern':'he is the choosen one'}

for key in dictionary2:   #Por cada palabra clave del diccionario
    print(key)     #imprime la palabra clave
    print(dictionary2[key])    #e imprime la definición de esa palabra clave