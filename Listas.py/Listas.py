Lista1 = [ 1 , 3 , 5 , 3  ,6 , 13 , 20 , 3 , -2 , 14 ]


print(u"\n\t\tEjemplo listas")
print("\nLista Original")
print(Lista1)

Lista1.append(21)
print(u"\n\"Lista.append(21)\" Agrega el número 21 al final: ")
print(Lista1)

print(u"\n \"Lista1.insert(2, 99)\" Ingresa el numero 99 en posición 2: ")
Lista1.insert(2, 99)
print(Lista1)

print("\n\"Lista1.remove(5)\" Quita el primer 5 de la Lista1: ")
Lista1.remove(5)
print(Lista1)

print("\n\"Lista1.count(3)\"  Cuenta la cantidad de 3 que hay: ")
print(Lista1.count(3))
print(Lista1)

print(u"\n\"Lista1.pop()\"Elimina el último número: ")
Lista1.pop()
print(Lista1)


print(u"\n\"Lista1.index()\"Muestra la posición del primer término 3 en la Lista1: ")
print(Lista1.index(3))
print(Lista1)

print(u"\"Lista1.reverse()\"Invierte el orden de Lista1: ")
Lista1.reverse()
print(Lista1)

print(u"\n\"Lista1.sort()\"Reordena la lista de menor a mayor:")
Lista1.sort()
print(Lista1)

print(u"\n\"Lista1.clear()\"Elimina todo")
Lista1.clear()
print(Lista1)

#__________________________________Parte 2_______________________________
#Ejemplos con string



ListaCompras = ['Leche', 'Pan', 'Detergente', 'Queso', ' Papas Fritas']


print("\n\n\n\t\t\tLista de Compras")

print("Mi lista de compras\n" , ListaCompras)


print(u"\n\n\"Lista.append('Peras')\" Agrega las Peras al final: ")
ListaCompras.append('Peras')
print(ListaCompras)

print(u"\n\n \"Lista1.insert(2, 'Manzanas')\" Ingresa el numero 99 en posición 2: ")
ListaCompras.insert(4, 'Manzanas')
print(ListaCompras)

print("\n\n\"Lista1.remove(\'Detergente\')\" Quita el primer \'Detergente\': ")
ListaCompras.remove('Detergente')
print(ListaCompras)

print("\n\n\"Lista1.count('Manzanas')\"  Cuenta la cantidad de Manzanas que hay: ")
print(ListaCompras.count( 'Manzanas'))
print(ListaCompras)

print(u"\n\n\"Lista1.pop()\"Elimina último término (Las Peras): ")
ListaCompras.pop()
print(ListaCompras)


print(u"\n\n\"Lista1.index()\"Muestra la posición del primer término  'Queso' en la ListaCompras: ")
print(ListaCompras.index('Queso'))
print(ListaCompras)

print(u"\n\n\"Lista1.reverse()\"Invierte el orden de ListaCompras: ")
ListaCompras.reverse()
print(ListaCompras)

print(u"\n\n\"Lista1.sort()\"Reordena la lista de menor a mayor:")
ListaCompras.sort()
print(ListaCompras)

print(u"\n\n\"Lista1.clear()\"Elimina todo")
ListaCompras.clear()
print(ListaCompras)

