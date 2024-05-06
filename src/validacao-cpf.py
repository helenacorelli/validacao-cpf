"""
Calculo do primeiro dígito do CPF
CPF: 746.824.890-70

Colete a soma dos 9 primeiros dígitos do CPF multiplicando cada um dos valores por uma
contagem regressiva começando de 10

Ex.:  746.824.890-70 (746824890)
   10  9  8  7  6  5  4  3  2
*  7   4  6  8  2  4  8  9  0
   70  36 48 56 12 20 32 27 0

Somar todos os resultados: 
70+36+48+56+12+20+32+27+0 = 301
Multiplicar o resultado anterior por 10
301 * 10 = 3010
Obter o resto da divisão da conta anterior por 11
3010 % 11 = 7
Se o resultado anterior for maior que 9:
    resultado é 0
contrário disso:
    resultado é o valor da conta

O primeiro dígito do CPF é 7
"""

# Coletar CPF
cpf = input ('Digite o seu CPF (Exemplo: 000.000.000-00): ')

# Validar se CPF foi inserido corretamente
if cpf == '':
    print('CPF não pode estar vazio!')
elif len(cpf) < 14 or len(cpf) > 14:
    print('Parece que seu CPF é menor ou maior que o esperado!')
else:
    # Tirar pontos do CPF
    cpf_formatado = ""

    for item in cpf:
        if item != "." and item != "-":
            cpf_formatado += item

    # Multiplicar valores por uma contagem regressiva começando de 10
    nove_digitos = cpf_formatado[:9]
    contador_regressivo_1 = 10
    resultado = 0

    for digito in nove_digitos:
        resultado += int(digito) * contador_regressivo_1
        contador_regressivo_1 -= 1
    
    # Multiplicar o resultado por 10 e obter o resto da divisão da conta anterior por 11
    digito_1 = (resultado * 10) % 11
    digito_1 = digito_1 if digito_1 <= 9 else 0
    print(digito_1)