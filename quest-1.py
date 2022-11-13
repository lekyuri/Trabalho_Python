def calcula_area(base_maior,base_menor,altura):
    return ((base_maior + base_menor) * altura)/2

altura = float(input("Informe o valor da altura: "))
base_maior = float(input("Informe o valor da base maior: "))
base_menor = float(input("Informe o valor da base menor: "))

area = calcula_area(base_maior,base_menor,altura)
print(f"A área do trapézio é: {area:.2f}")