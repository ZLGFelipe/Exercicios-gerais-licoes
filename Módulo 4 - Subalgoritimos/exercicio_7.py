'''7- Escreva uma função que dada uma nota entre 0.0 e 10.0 imprima na tela um conceito entre "A" e "E", 
segundo a tabela: A ≥ 9.0 9.0 > B ≥ 8.0 8.0 > C ≥ 7.0 7.0 > D ≥ 5.0 E < 5.0 O que acontece com o seu 
programa se for digitada nota menor que zero ou maior que dez?'''

def calcular_conceito(nota):
    if nota >= 9.0:
        return "A"
    elif nota >= 8.0:
        return "B"
    elif nota >= 7.0:
        return "C"
    elif nota >= 5.0:
        return "D"
    else:
        return "E"

nota = float(input("Digite a nota (entre 0.0 e 10.0): "))

if 0.0 <= nota <= 10.0:
    conceito = calcular_conceito(nota)
    print(f"O conceito correspondente à nota {nota:.1f} é {conceito}")
else:
    print("Nota inválida. Digite uma nota entre 0.0 e 10.0.")