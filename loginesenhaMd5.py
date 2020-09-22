def login():
    """
    modulo de cadastro e autenticação de usuario
    seus dados serão criptografados e gravados em um .txt
    :return: sem retorno
    """
    from hashlib import md5
    import sys

    def linhas():
        print('\033[1;90m==\033[m'*20)

    while True:  # início do programa
        linhas()
        print('[1] cadastrar\n'
              '[2] autenticar\n'
              '[3] sair')
        opcao = input('\033[1;34mo que você deseja fazer? \033[m')
        linhas()

        if opcao == '1':  # cadastrar usuário
            nome = input('Digite seu nome:')
            cpf = input('Digite seu cpf:')

            # encriptando os dados
            nomeMD5 = md5(nome.encode()).hexdigest()
            cpfMD5 = md5(str(cpf).encode()).hexdigest() + nome
            cpfMD5final = md5(cpfMD5.encode()).hexdigest()
            total = nomeMD5, cpfMD5final

            # armazenando os valores do usuario
            with open('dados_usuarios.txt', 'a') as valores:
                valores.write(str(total) + '\n')
                print('\033[1;33musuário adicionado\033[m')
                valores.close()

        if opcao == '2':  # autenticação de usuário
            autentica_nome = input('Digite seu nome: ')
            autentica_cpf = input('Digite seu cpf: ')
            # encriptando os dados
            autentica_nomeMD5 = md5(autentica_nome.encode()).hexdigest()
            autentica_cpfMD5 = md5(str(autentica_cpf).encode()).hexdigest() + autentica_nome
            autentica_cpfMD5final = md5(autentica_cpfMD5.encode()).hexdigest()
            autentica_total = autentica_nomeMD5, autentica_cpfMD5final
            # verificando os dados armazenados
            with open('dados_usuarios.txt', 'r') as valores:
                autenticado = 0
                for linha in valores:
                    if str(autentica_total) in linha:
                        autenticado = 1

                if autenticado == 1:  # o dado esta na lista
                    print('\033[1;33m usuário autenticado!\033[m')
                    break
                elif autenticado == 0:  # o dado não esta na lista
                    print('\033[1;31musuário não cadastrado\033[m')
                    continue

        if opcao == '3':  # sair
            sys.exit()

        if opcao not in '123':  # erro (opção não existe)
            print('\033[1;31mopção inválida!\033[m')
            continue

# problema com o cpf
# usuario já existente
