
studentName = input("Digite seu nome: ")
result=[]
loop = True

while(loop == True):

    for i in range(4):
        result.append(int(input("Digite seu nota: ")))
    
    media = sum(result)/4

    print(studentName)

    if media<6:
        print("Reprovadoo!")
    elif media>=6:
        print("Aprovadoo!")


    ans = int(input("Continuar ? 1-Sim 2-Nao "))
    if ans==1:
       loop = True
    else:
       break
