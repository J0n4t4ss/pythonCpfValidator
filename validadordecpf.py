
while True:
    cpf = input('Digite um CPF:')
    new_cpf = cpf[:-2]
    contrary = 10
    total = 0
    for index in range(19):
        if index > 8:
            index -= 9

        total += int(new_cpf[index]) * contrary

        contrary -= 1
        if contrary < 2:
            contrary = 11
            d = 11 - (total % 11)

            if d > 9:
                d = 0
            total = 0
            new_cpf += str(d)
     #   print(new_cpf)
    sequence = new_cpf == str(new_cpf[0] * 11)
    if cpf == new_cpf and not sequence:
        print('O CPF é válido!')
    else:
        print('O CPF é invalido!')