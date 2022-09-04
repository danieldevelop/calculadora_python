def sumar(valorUno, valorDos):
    return "\nEl valor de la suma es: {0}".format((valorUno + valorDos));

def restar(valorUno, valorDos):
    return "\nEl valor de la resta es: {0}".format((valorUno - valorDos));

def multiplicar(valorUno, valorDos):
    return "\nEl valor de la multiplicación es: {0}".format((valorUno * valorDos));

def dividir(valorUno, valorDos):
    if (valorDos == 0):
        return "\nNo se puede dividir entre cero";
    else:
        return "\nEl valor de la división es: {0}".format((float) (round((valorUno / valorDos), 3)));


if __name__ == "__main__":

    numeroUno = int(input("Ingrese el primer numero: "));
    numeroDos = int(input("Ingrese el segundo numero: "));

    print("\nMENU \n"+
        "1. Sumar \n"+
        "2. Restar \n"+ 
        "3. Multiplicar \n"+
        "4. Dividir"
    );
    opcion = int(input("elija una opción: "));

    # todo: Condicional Switch Case, en el que se evalúa la opción y se ejecuta el método correspondiente
    match opcion:
        case 1:
            print(sumar(numeroUno, numeroDos));
        case 2:
            print(restar(numeroUno, numeroDos));
        case 3:
            print(multiplicar(numeroUno, numeroDos));
        case 4:
            print(dividir(numeroUno, numeroDos));

        case _:
            print("Opción no valida!!");    



    input("\nPresione una tecla para salir...");