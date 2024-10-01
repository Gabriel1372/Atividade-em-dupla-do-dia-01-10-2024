import os
os.system("cls || clear")

 while True:
        limpar_terminal()
        print("Menu:")
        print("1 | Adicionar família")
        print("2 | Exibir resultados")
        print("3 | Sair")
        
        opcao = input("Escolha uma opção: ")

        if opcao == '1':
            adicionar_familia(dados)
        elif opcao == '2':
            exibir_resultados(dados)
            input("Pressione Enter para continuar...")
        elif opcao == '3':
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()
