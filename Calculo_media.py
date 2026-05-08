try:
n1 = float(input("Nota 1: "))
n2 = float(input("Nota 2: "))
n3 = float(input("Nota 3: "))
# Validação de intervalo
if any(n < 0 or n > 10 for n in [n1, n2, n3]):
 print("Erro: Notas inválidas detectadas.")
else:
 media = (n1 + n2 + n3) / 3
 print(f"Média: {media:.1f}")
 if media >= 7:
 print("Status: Aprovado")
 elif 5 <= media < 7:
 print("Status: Recuperação")
 else:
 print("Status: Reprovado")
except ValueError: print("Erro: Digite apenas números.")
