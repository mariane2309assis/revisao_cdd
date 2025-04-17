peso= float(input("digite seu peso: "))
altura = float(input("digite sua altura: "))

imc= peso/(altura*altura)
print(f"Seu imc é: {imc:.2f}")
if imc < 18.6 :
        print("abaixo do peso")
elif imc < 24.9:
    print("peso ideal")
elif imc <29.9:
    print("levemente acima do peso")
elif imc  <34.9:
    print("obesidade grau I")
elif imc < 39.9:
    print("obesidade grau II(severa)")
else:
    print("obesidade grau III(mórbida)")