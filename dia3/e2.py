#Concatenar listas (una lista dentro de otra)
list = [1, 2, 3.14, [True, False, "python"]]
print("Lista concatenada: ", list)
print("Elemento de mi lista concatenada: ", list[3][2])

list2 = [1, 2, 3, 4]
print("Lista original: ", list2)

#Append (agregar unicamente un elemento al final de la lista)
list2.append("hello")
print("Método append: ", list2)

#Extend (agrega varios elementos al final de la lista)
list2.extend([10, 11, True, "ESIME"])
print("Método extend: ", list2)

#Insert (inserta un elemento a la lista en la posición deseada)
list2.insert(2, "Posicion X")
print("Método insert: ", list2)

#Remove (remueve un elemento x de la lista)
list2.remove(1)
print("Método remove: ", list2)

#Pop (remueve un elemento de la lista de acuerdo a
# la posicion indicada y returna el elemento removido)
removed_element = list2.pop(1)
print("Elemento removido de la lista: ", removed_element)