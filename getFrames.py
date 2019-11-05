import cv2
import os

# Path de onde estao as imagens
videosPath= 'DatasetVideos\AbrirTampa'
# Tamanho da imagem modificada
dim = (60, 60)

# Taxa de frames (ex.: 0.5 significa 1 frame a cada 0.5 segundos)
frameRate = 0.5

# Pega os nomes dos arquivos contidos na pasta
filenames = next(os.walk(videosPath))[2]
#print(filenames)

for video in filenames:
    #Cria o path do video
    arqPath= videosPath + "\\" + video
    #Cria o path dos frames do video
    framesPath =  (arqPath.replace(".mp4", "")) + '\\frames'
    #Cria o path dos frames modificados do video
    resized_framesPath =  (arqPath.replace(".mp4", "")) + '\\resized_frames'
  

    #Cria as pastas dos frames e dos frames modificados caso nao existam
    if not os.path.exists(framesPath):
            os.makedirs(framesPath)
    if not os.path.exists(resized_framesPath):
            os.makedirs(resized_framesPath)

    # Abre o video do path passado como parametro
    vidcap = cv2.VideoCapture(arqPath)

    # Pega o frame de um momento especifico
    def getFrame(sec):
        # define a posicao atual do video em segundos
        vidcap.set(cv2.CAP_PROP_POS_MSEC,sec*1000)

        # Retorna se existe uma imagem, e a propria imagem
        hasFrames,image = vidcap.read()

        # Verifica se existe imagem neste momento
        if hasFrames:
            # Cria o arquivo do frame
            cv2.imwrite((framesPath +"\\frame["+str(count)+"].jpg"), image)     # save frame as JPG file
            
            # Deixa a imagem em tons de cinza
            gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

            # Modifica o tamanho da imagem para o configurado em dim
            resized = cv2.resize(gray_image, dim, interpolation = cv2.INTER_AREA)
            
            # Cria o arquivo do frame modificado
            cv2.imwrite((resized_framesPath +"\\frame["+str(count)+"].jpg"), resized)
        return hasFrames

    # Define como ponto inicial o segundo 0
    sec = 0

    # Cria variavel para contar os frames
    count=1

    # Verifica se o primeiro frame foi pego com sucesso
    success = getFrame(sec)

    # Passa por todos os frames do video
    while success:
        count = count + 1
        sec = sec + frameRate
        sec = round(sec, 2)
        success = getFrame(sec)
