class Calculadora:
    def __init__(self, a: int, b: int):
        if not isinstance(a, int):
            raise TypeError("'a' inválido, deve ser inteiro")
        if not isinstance(b, int):
            raise TypeError("'b' inválido, deve ser inteiro")
        self.a = a
        self.b = b

    def somar(self):
        resultado = self.a + self.b
        print(f"Resultado: {resultado}")
        return resultado

    def subtrair(self):
        resultado = self.a - self.b
        print(f"Resultado: {resultado}")
        return resultado

    def multiplicar(self):
        resultado = self.a * self.b
        print(f"Resultado: {resultado}")
        return resultado

    def dividir(self):
        if self.b == 0:
            raise ZeroDivisionError("'b' Não pode ser 0")
        resultado = self.a / self.b
        print(f"Resultado: {resultado:.2f}")
        return resultado


def main():
    a = input("Digite o primeiro valor: ")
    b = input("Digite o segundo valor: ")

    calculo = Calculadora(a, b)

    while True:
        operacao = input("Digite a operação (somar, subtrair, multiplicar, dividir) ou 'off' para desligar: ").lower()
        if operacao == 'off':
            break
        elif operacao == 'somar':
            calculo.somar()
        elif operacao == 'subtrair':
            calculo.subtrair()
        elif operacao == 'multiplicar':
            calculo.multiplicar()
        elif operacao == 'dividir':
            try:
                calculo.dividir()
            except ZeroDivisionError as e:
                print(e)
        else:
            print("Operação inválida. Tente novamente.")


main()
