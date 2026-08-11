from inferencia import YOLOinferencia
import os
import sys

def limpa_tela():
    os.system('cls' if os.name == 'nt' else 'clear')

def atualizar_tela_sem_piscar():

    sys.stdout.write('\033[H')
    sys.stdout.write('\033[?25l')
    sys.stdout.flush()

def mostrar_cursor():
    sys.stdout.write('\033[?25h')
    sys.stdout.flush()

def menu_modelo():

    atualizar_tela_sem_piscar()

    print("╔════════════════════════════════════╗")
    print("║                                    ║")
    print("║      Detecção e classificação      ║")
    print("║         de estado de gado          ║")
    print("║                                    ║")
    print("║   1-Modelo com 25 epochs           ║")
    print("║   2-Modelo com 50 epochs           ║")
    print("║   3-Modelo com 100 epochs          ║")
    print("║                                    ║")
    print("║              4-Voltar              ║")
    print("║                                    ║")
    print("║                6567                ║")
    print("╚════════════════════════════════════╝")

def menu_infos():

    atualizar_tela_sem_piscar()

    print("Modelo utilizado (yolov8n.pt)")
    print("Saída do teste de inferência fica salvo\nna pasta runs/detect, pasta chamada ./saida")
    print("Nome: Alvaro de oliveira neto")
    print("Matrícula: 6567")
    print()
    print("1-VOLTAR")

def menu_dir_teste():

    atualizar_tela_sem_piscar()
    
    print("╔════════════════════════════════════╗")
    print("║                                    ║")
    print("║  Para selecionar outro diretório   ║")
    print("║   de teste cole a sua pasta de     ║")
    print("║  teste na pasta raiz do programa   ║")
    print("║                                    ║")
    print("║    Escreva o nome do diretório     ║")
    print("║                                    ║")
    print("║              1-Voltar              ║")
    print("║                                    ║")
    print("║                                    ║")
    print("║                6567                ║")
    print("╚════════════════════════════════════╝")    

# Caminho para o modelo
caminho_modelo = None
caminho_teste = 'teste' # Diretório /teste, selecionado por padrão


limpa_tela();

while True:

    atualizar_tela_sem_piscar()

    print("╔════════════════════════════════════╗")
    print("║                                    ║")
    print("║      Detecção e classificação      ║")
    print("║         de estado de gado          ║")
    print("║                                    ║")
    print("║   1-Selecionar qual modelo usar    ║")
    print("║   2-Fazer teste de inferência      ║")
    print("║   3-Informações de saída           ║")
    print("║   4-Selecionar dir. de teste       ║")
    print("║   5-Fechar programa                ║")
    print("║                                    ║")
    print("║                6567                ║")
    print("╚════════════════════════════════════╝")

    opcao = input("Escolha uma das opções: ")

    # Selecionar qual modelo usar 
    if opcao == '1':

        while True:

            limpa_tela();
        
            menu_modelo();

            opcao = input("Escolha uma das opções: ")

            if opcao == '1':
                caminho_modelo = 'runs/detect/model_Fucinho-25-epochs/weights/best.pt'
                print("Modelo com 25 epochs selecionado!")
                input("Presione ENTER para continuar!")

            elif opcao == '2':
                caminho_modelo = 'runs/detect/model_Fucinho-50-epochs/weights/best.pt'
                print("Modelo com 50 epochs selecionado!")
                input("Presione ENTER para continuar!")

            elif opcao == '3':
                caminho_modelo = 'runs/detect/model_Fucinho-100-epochs/weights/best.pt'
                print("Modelo com 100 epochs selecionado!")
                input("Presione ENTER para continuar!")

            elif opcao == '4':
                break

    # Fazer teste de inferência 
    elif opcao == '2':

        if caminho_modelo == None:
            print("Selecione um modelo!")
            input("Presione ENTER para continuar!")
            limpa_tela();
        else:
            # verifica se o caminho de teste é valido

            dir = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
            print(f"Raiz do projeto: {dir}")

            passou = None
            for arquivos in os.listdir(dir):
            
                if caminho_teste == arquivos:
                    passou = YOLOinferencia(caminho_modelo,caminho_teste)
                    input("Presione ENTER para continuar!")
                    limpa_tela();
                
            if passou == None:
                print("Diretório não encontrado!")
                input("Presione ENTER para continuar!")
                limpa_tela()

    # Informações de saída
    elif opcao == '3':

        limpa_tela();

        while True:

            menu_infos();

            opcao = input("Escolha uma das opções: ")

            if opcao == '1':
                limpa_tela();
                break

    # Selecionar dir. de teste
    elif opcao == '4':

        limpa_tela();

        while True:

            menu_dir_teste();
            mostrar_cursor();
            opcao = input("Digite o nome da pasta ou '1' para voltar: ")  

            if opcao == '1':
                limpa_tela();
                break     
            else:
                yorn = input("Confirmar mudança de diretorio de teste? y/n: ")

                if yorn == 'y':
                    caminho_teste = opcao
                    print(f"Alteração concluida com sucesso! Novo diretório selecionado: {caminho_teste}")
                    input("Presione ENTER para continuar!")
                    limpa_tela();
                elif yorn == 'n':
                    print("Nada foi alterado!")
                    input("Presione ENTER para continuar!")
                    limpa_tela();
                else:
                    print("Digite algo valido!")
                    input("Presione ENTER para continuar!")
                    limpa_tela();
              
    # Fechar programa
    elif opcao == '5':
            print("Finalizando...")
            mostrar_cursor();
            break