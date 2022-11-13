def soma_imposto(taxa, custo_do_produto):
    return custo_do_produto + (custo_do_produto * (taxa/100))
taxa = float(input("Informe o valor  da taxa: "))
custo_do_produto = float(input("Informe  o valor do produto: "))
print(soma_imposto(taxa, custo_do_produto))
