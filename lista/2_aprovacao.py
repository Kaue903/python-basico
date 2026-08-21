notas = 6, 5, 9, 10
faltas = 1, 2, 3, 1
media_notas = sum(notas) / 4
media_faltas = sum(faltas) / 4



if media_notas >= 6 and media_faltas <= 2.5:
    print("Aprovado")
elif media_notas >= 6 and media_faltas > 2.5:
    print("Reprovado")