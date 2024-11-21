import cv2
import pytesseract as pt


pt.pytesseract.tesseract_cmd = "C:\\Program Files (x86)\\Tesseract-OCR\\tesseract.exe"


# carregar a img
img = cv2.imread('imgteste.JPG')

#tesseract possui 3 funcoes importantes
#retirar o texto da img, como ele so le ingles e port nao tem que config para ler ,lang='por'
# print(pt.pytesseract.image_to_string(img, lang='por'))  A versão recomendada é 4.x ou superior.
#print(pt.pytesseract.image_to_string(img))

#extrair caracter e localizacao dentro da imagem
boxes = (pt.pytesseract.image_to_boxes(img)) #variavel
dados = (pt.pytesseract.image_to_data(img))  #variavel = da informacoes incluindo a palavra
#print(type(dados))

#colocar um retangulo em alguns caracter
imH, imW,_ = img.shape #variavel = tamanho da img e diminuir o H


#para fazer o retangulo nas letras e reescrever
#for b in boxes.splitlines(): #dividir elas em linhas
#    b = b.split(' ')
    #print(b)

#    letra,x,y,w,h = b[0], int(b[1]),int(b[2]),int(b[3]),int(b[4]) #desmembrar o array e colocar dentro de variaveis
#    cv2.rectangle(img,(x,imH-y),(w,imH-h),(0,0,255),1) #a localizacao exata da letra e retangulo

    #colocar a letra de baixo do retangulo
#    cv2.putText(img,letra,(x,imH-y+25),cv2.FONT_HERSHEY_SIMPLEX,1,(0,0,255),2)


#para fazer a analise de dados
for x,linha in enumerate(dados.splitlines()): #fazer enumeracao dos dados(um indice para cada objeto dessa variavel)
    if x!=0:  #se x for diferente de 0 executa as demais operacoes
        #print(linha)
        linha = linha.split()
        print(linha)
        if len(linha)==12:
            x,y,w,h = int(linha[6]), int(linha[7]),int(linha[8]),int(linha[9])
            palavra= linha[11]

            cv2.rectangle(img,(x,y),(w+x,h+y),(0,0,255),1)
            cv2.putText(img,palavra,(x,y-5),cv2.FONT_HERSHEY_SIMPLEX,1,(0,0,255),2)

cv2.imshow('Imagem', img)
cv2.waitKey(0)