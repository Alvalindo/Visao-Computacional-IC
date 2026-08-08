from ultralytics import YOLO
import os

# Função para inferência dos modelos

def YOLOinferencia(caminho_modelo, caminho_teste):

    print("Iniciando a inferência...")

    # Caminho do modelo para ser utilizado
    modelo_fucinho = YOLO(caminho_modelo)

    #lista todas as pastas dentro da pasta teste
    for cor in os.listdir(caminho_teste):

        cor_diretorio = os.path.join(caminho_teste, cor)

        resultado = modelo_fucinho.predict(
            source=cor_diretorio, # O diretorio onde estão as imagens de test
            conf=0.60, # Define o limiar de confiança mínimo para deteções
            save=True, # True para salvar o resultado da inferência
            project='saida', 
            name=f'saida_{cor}'
            )
        
    print("\nOs arquivos foram salvos na pasta /saida_teste\nInferência finlizada com sucesso!")
   