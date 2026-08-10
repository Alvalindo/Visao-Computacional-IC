from ultralytics import YOLO

# Carregando o modelo yolov8n.pt, sua velocidade para pequenas 
# quantidades de arquivos é mais eficiente do que os modelos novos. 

model = YOLO("yolov8n.pt")

results = model.train(
    data="data.yaml", # local para especificar o treinamento
    epochs=50, # quantidade de vezes que o modelo vai acessar os arquivos
    imgsz=640, # tamanho padrão das imagens
    batch=16, # modo automático para 60% de utilização da memória da GPU
    name="model_Fucinho" #
)