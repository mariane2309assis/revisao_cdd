resp= "sim"
while resp == "sim":

        num= float(input("digite um número"))

        if num >0:
            if num%2==0:
                print(" é positivo e par")
            else:
                print("é impar e positivo")
        else:
            if num%2==0:
                print(f" é par e negativo")
            else:
                print(f" é ímpar e negativo")

        resp = input("verificar novo numero? sim ou não?")