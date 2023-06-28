while True:
    n1 = float(input("Insaira a nota do aluno: "))
    if n1 >= 0.0 and n1 <= 10.0:
        break
    else:
        print("Nota inválida.")
if n1 >= 8.5:
    print("A")
elif n1 >= 7.0 and n1 < 8.5:
    print("B")
elif n1 >= 5.0 and n1 < 7.0:
    print("C")
elif n1 >= 4.0 and n1 < 5.0:
    print("D")
elif n1 >= 0.0 and n1 < 4.0:
    print("E")
