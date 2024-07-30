from tqdm import tqdm


def calcular_digito_verificador(cpf):
    def calcular_primeiro_digito(cpf):
        pesos = list(range(10, 1, -1))
        soma = sum(int(cpf[i]) * pesos[i] for i in range(9))
        resto = soma % 11
        return 0 if resto < 2 else 11 - resto

    def calcular_segundo_digito(cpf, primeiro_digito):
        pesos = list(range(11, 1, -1))
        soma = sum(int(cpf[i]) * pesos[i] for i in range(9)) + primeiro_digito * 2
        resto = soma % 11
        return 0 if resto < 2 else 11 - resto

    primeiro_digito = calcular_primeiro_digito(cpf)
    segundo_digito = calcular_segundo_digito(cpf, primeiro_digito)
    return primeiro_digito, segundo_digito


def gerar_cpfs_validos():
    total_cpfs = 1000000000
    with open('cpfs_validos.txt', 'w') as file:
        for i in tqdm(range(total_cpfs), desc="Gerando CPFs", unit="cpf"):
            cpf = f"{i:09d}"
            primeiro_digito, segundo_digito = calcular_digito_verificador(cpf)
            cpf_completo = f"{cpf}{primeiro_digito}{segundo_digito}"
            file.write(cpf_completo + '\n')


gerar_cpfs_validos()
