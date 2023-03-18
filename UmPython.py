list = []
for i in range(5):
    list.append(int(input("Digite um numero: "))) 

pairsNumbs = []
nonPairNumbs = []
pairTotal = 0
nonPairTotal = 0

for numb in list:
    if numb % 2 == 0:
        pairsNumbs.append(numb)
        pairTotal += numb
    if numb % 2 != 0:
        nonPairNumbs.append(numb)
        nonPairTotal += numb

try:
    print("Numeros pares: ",pairsNumbs, "Media dos numeros pares: ",pairTotal/len(pairsNumbs))
    print("Numeros nao pares: ",nonPairNumbs,"Media dos numeros impares: ",nonPairTotal/len(nonPairNumbs) )
    print("Media total : ", (pairTotal+nonPairTotal)/len(list))
except:
    print("Os valores em uma lista nao podem ser 0!")