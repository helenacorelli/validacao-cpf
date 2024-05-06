"""
Exercício de validação de CPF em Python

Curso Udemy: Python 3 do básico ao avançado - com projetos reais
Instrutor: Luiz Otávio Miranda
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
    cpf_formatado = ''

    for item in cpf:
        if item != '.' and item != '-':
            cpf_formatado += item

    # Primeiro digito: Multiplicar valores por uma contagem regressiva começando de 10
    nove_digitos = cpf_formatado[:9]
    contador_regressivo = 10
    resultado_digito_1 = 0

    for digito in nove_digitos:
        resultado_digito_1 += int(digito) * contador_regressivo
        contador_regressivo -= 1
    
    # Primeiro digito: Multiplicar o resultado por 10 e obter o resto da divisão da conta anterior por 11
    digito_1 = (resultado_digito_1 * 10) % 11
    digito_1 = digito_1 if digito_1 <= 9 else 0

    # Segundo digito: Multiplicar valores por uma contagem regressiva começando de 11
    dez_digitos = cpf_formatado[:10]
    contador_regressivo = 11
    resultado_digito_2 = 0

    for digito in dez_digitos:
        resultado_digito_2 += int(digito) * contador_regressivo
        contador_regressivo -= 1
    
    # Segundo digito: Multiplicar o resultado por 10 e obter o resto da divisão da conta anterior por 11
    digito_2 = (resultado_digito_2 * 10) % 11
    digito_2 = digito_2 if digito_2 <= 9 else 0

    # Validar CPF
    cpf_calculado = f'{nove_digitos}{digito_1}{digito_2}'

    if cpf_formatado == cpf_calculado:
        print('CPF válido!')
    else:
        print('CPF inválido!')