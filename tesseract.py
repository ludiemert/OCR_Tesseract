import cv2
import pytesseract as pt

# Caminho para o executável do Tesseract
pt.pytesseract.tesseract_cmd = "C:\\Program Files\\Tesseract-OCR\\tesseract.exe"

# Carregar a imagem
img = cv2.imread('imgteste.JPG')
if img is None:
    raise FileNotFoundError("Imagem não encontrada. Verifique o caminho para imgteste.JPG.")

# Extrair dados do Tesseract
dados = pt.pytesseract.image_to_data(img)

# Dimensões da imagem
imH, imW, _ = img.shape

# Analisar dados extraídos
for i, linha in enumerate(dados.splitlines()):  # Enumerar os dados
    if i == 0:  # Ignorar o cabeçalho
        continue
    linha = linha.split()
    if len(linha) == 12:  # Garantir que a linha contém todas as informações
        x, y, w, h = map(int, (linha[6], linha[7], linha[8], linha[9]))
        palavra = linha[11]
        # Desenhar retângulo e exibir palavra
        cv2.rectangle(img, (x, y), (x + w, y + h), (0, 0, 255), 1)
        cv2.putText(img, palavra, (x, y - 5), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)

# Exibir imagem processada
cv2.imshow('Imagem', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
