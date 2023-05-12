print("Atividade 02 - Calculo do IMC no Python")

def main():
    peso = float(input("Informe o seu peso\n"))
    altura = float(input("Informe a sua altura\n"))
    imcCalculado = calcularImc(peso , altura)
    descricao = labelImc(imcCalculado)
    print(f'Peso:{peso} - Altura: {altura} - IMC: {imcCalculado} - Resultado: {descricao}')


def calcularImc(peso , altura):
    return round(peso / altura ** 2 , 2)

def labelImc(imc):
    if imc < 18.5: return "Magreza"
    if imc < 24.9: return "Normal"
    if imc < 30: return "Sobrepeso"
    return "Obesidade"

main()
