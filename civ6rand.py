import random as rd

liste_civ = ["American","Arabian","Aztec","Brazilian","Chinese","Egyptian","English","French","German","Greek","Indian","Japanese","Kongolese","Norwegian","Roman","Russian","Scythian","Spanish","Sumerian"]

ban=["American","Arabian","Roman","Sumerian","Chinese"]

for i in ban:
    liste_civ.remove(i)

equipe1,equipe2=[],[]
for i in range(0,7):
    value=rd.randint(0,len(liste_civ)-1)
    equipe1.append(liste_civ[value])
    liste_civ.remove(liste_civ[value])

print("Equipe 1 :" ,equipe1)
print("Equipe 2 :" ,liste_civ)

input("Press enter to quit")