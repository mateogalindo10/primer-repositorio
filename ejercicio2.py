def calculadora(num1, num2, operacion):
    if operacion == 'suma':
        return num1 + num2
    elif operacion == 'resta':
        return num1 - num2
    elif operacion == 'multiplicación':
        return num1 * num2
    elif operacion == 'división':
        if num2 == 0:
            return "Error: División por cero."
        return num1 / num2
    else:
        return "Operación no válida."

# Solicitar datos al usuario
numero1 = float(input("Introduce el primer número: "))
numero2 = float(input("Introduce el segundo número: "))
operacion = input("Introduce la operación (suma, resta, multiplicación, división): ").lower()

resultado = calculadora(numero1, numero2, operacion)
print(f"El resultado de la {operacion} es: {resultado}")
