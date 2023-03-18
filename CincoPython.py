mult = [[0 for _ in range(4)] for _ in range(3)] # matriz "bidimensional"
student = []
medias = []

# preenchendo nomes e notas
for i in range(3):
    student.append(input("Digite Seu Nome: "))
    for j in range(4):
        mult[i][j] = int(input("Sua nota: "))

# adicionando na lista a media de cada aluno
medias.append(sum(mult[0])/4)
medias.append(sum(mult[1])/4)
medias.append(sum(mult[2])/4)

# pegando a index da maior e menor media na lista
maxIndex = medias.index(max(medias))
minIndex = medias.index(min(medias))

# chamando o estudante com a index da maior media
print("O/A estudante: ",student[maxIndex], "Teve a maior media, com: ",max(medias))
print("O/A estudante: ",student[minIndex], "Teve a menor media, com: ",min(medias))