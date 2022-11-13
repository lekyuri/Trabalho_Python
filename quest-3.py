while True:
        hora = int(input("Informe a hora de 0 a 24 ou digite -1 para sair: "))
        if hora == -1:
                break
        min = int(input("Informe os minutos: "))
        if(hora<12):
                A= (f"{hora}:{min}A.M.")
                print(A)

        else:
                hora=hora-12
                P=(f"{hora}:{min}P.M.")
                print(P)
