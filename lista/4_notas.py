alunos = ["Maria", "Pietra", "Kaue", "Lucas"]
notas = [6.3, 5.6, 9.5, 10]
media_turma = sum(notas) / len(notas)

for i in range(len(alunos)):
    print(f"{alunos[i]}: {notas[i]}")

print(f"\nMédia da turma: {media_turma:.2f}")
print(f"Maior nota: {max(notas)}")
print(f"Menor nota: {min(notas)}")
