import sys

lista = []
tupla = ()
dicto = {}

print(sys.getsizeof(lista), sys.getsizeof(tupla), sys.getsizeof(dicto))

lista = ['a', 'b', 'c', 'd', 'e']
tupla = ('a', 'b', 'c', 'd', 'e')
dicto = {'a', 'b', 'c', 'd', 'e'}

print(sys.getsizeof(lista), sys.getsizeof(tupla), sys.getsizeof(dicto))

for l in lista:
    print(sys.getsizeof(l))

data = []
for t in tupla:
    data.append(t.encode())
    print(sys.getsizeof(t))

print(sys.getsizeof(data))

tuplab = tuple(data)
print(tuplab)
print(sys.getsizeof(tuplab))

for d in dicto:
    print(sys.getsizeof(d))
