# OCR with Tesseract and OpenCV

This project uses **Tesseract OCR** and **OpenCV** to extract text from images and display detailed information about the recognized characters. The script allows drawing rectangles around the detected words and displays the words directly on the image.

## Features

- **Text Extraction**: Converts the content of an image into text using Tesseract OCR.
- **Character Localization**: Identifies the position of characters within the image.
- **Data Analysis**: Provides detailed information, including recognized words and their locations.
- **Result Visualization**: Displays the detected characters on the original image with rectangles and overlayed text.

## Requirements

- **Python 3.8**: This project was developed and tested with Python version 3.8.
- **Libraries**:
  - **OpenCV** (`cv2`): Used for image manipulation, drawing rectangles, and displaying results.
  - **Pytesseract** (`pytesseract`): Interface to use Tesseract OCR in Python.

## Installation

1. Install Python 3.8:
   - [Download Python](https://www.python.org/downloads/)

2. Install the required libraries:
   ```bash
   pip install opencv-python pytesseract
    ```

## Download and install Tesseract OCR:
Download Tesseract OCR
Make sure to note the installation path (e.g., C:\Program Files (x86)\Tesseract-OCR\tesseract.exe).
How to Use
Clone the repository:

  ```bash
git clone https://github.com/your_username/your_repository.git
cd your_repository
 ```

  - Add the image you want to process to the same folder as the script with the name imgteste.JPG.

### Configure the Tesseract executable path in the script:

 ```bash
pt.pytesseract.tesseract_cmd = "C:\\Program Files (x86)\\Tesseract-OCR\\tesseract.exe"
```
Run the script:

 ```bash
python ocr_script.py
```

### The script will:

### Display the recognized words in the image.
 - Draw rectangles around the detected words.
 - Show the processed image in a window.
 - Technical Details
 - Libraries Used
 - OpenCV (cv2) and tesseract

### Handles image manipulation and processing.
 - Displays results graphically with rectangles and text.
 - OpenCV Documentation
 - Pytesseract (pytesseract):

### Python interface for Tesseract OCR.
 - Extracts text and localization data.
 - Pytesseract Documentation
 - Tesseract Version
 - It is recommended to use version 4.x or higher for better performance and support for multiple languages.

### Code Structure
 - Image Loading: Uses cv2.imread to load the input image.
 - Language Configuration: Configures Tesseract to process text in Portuguese (lang='por').

### Word Detection:
 - pytesseract.image_to_string(img, lang='por'): Extracts text from the image.
 - pytesseract.image_to_boxes(img): Retrieves the location of characters.
 - pytesseract.image_to_data(img): Returns detailed data, including recognized words and their positions.
 - Drawing Rectangles: Uses cv2.rectangle to mark detected words on the image.
 - Displaying Results: Uses cv2.imshow to display the processed image.

## Output
 - The script displays the processed image with detected words highlighted by rectangles and overlayed with text, providing a visual analysis of the extracted information.

#### Feel free to contribute improvements to the code or report issues in the repository!

---
#### Portugues

# OCR com Tesseract e OpenCV

Este projeto utiliza o **Tesseract OCR** e **OpenCV** para realizar a extração de texto de imagens e apresentar informações detalhadas sobre os caracteres extraídos. O script permite desenhar retângulos em torno das palavras identificadas, além de exibir as palavras diretamente na imagem.

## Funcionalidades

- **Extração de texto**: Converte o conteúdo de uma imagem em texto usando o Tesseract OCR.
- **Localização de caracteres**: Identifica a posição dos caracteres dentro da imagem.
- **Análise de dados**: Gera informações detalhadas, incluindo as palavras reconhecidas e suas localizações na imagem.
- **Visualização de resultados**: Exibe os caracteres detectados sobre a imagem original com retângulos e textos desenhados.

## Requisitos

- **Python 3.8**: Este projeto foi desenvolvido e testado com a versão 3.8 do Python.
- **Bibliotecas**:
  - **OpenCV** (`cv2`): Utilizada para manipulação de imagens, desenho de retângulos e exibição de resultados.
  - **Pytesseract** (`pytesseract`): Interface para usar o Tesseract OCR no Python.

## Instalação

1. Instale o Python 3.8:
   - [Download Python](https://www.python.org/downloads/)

2. Instale as bibliotecas necessárias:
   ```bash
   pip install opencv-python pytesseract

Faça o download e instale o Tesseract OCR:
Download Tesseract OCR
Certifique-se de anotar o caminho de instalação (exemplo: C:\Program Files (x86)\Tesseract-OCR\tesseract.exe).
Como Usar
Clone o repositório:

bash
Copiar código
git clone https://github.com/seu_usuario/seu_repositorio.git
cd seu_repositorio
Adicione a imagem que deseja processar na mesma pasta do script com o nome imgteste.JPG.

Configure o caminho do executável do Tesseract no script:

python
Copiar código
pt.pytesseract.tesseract_cmd = "C:\\Program Files (x86)\\Tesseract-OCR\\tesseract.exe"
Execute o script:

bash
Copiar código
python ocr_script.py
O script irá:

Exibir as palavras reconhecidas na imagem.
Desenhar retângulos em torno das palavras detectadas.
Mostrar a imagem processada em uma janela.
Detalhes Técnicos
Bibliotecas Utilizadas
OpenCV (cv2):

Manipula e processa imagens.
Exibe resultados graficamente com retângulos e textos.
Documentação do OpenCV
Pytesseract (pytesseract):

Interface do Python para o Tesseract OCR.
Realiza a extração de texto e informações de localização.
Documentação do pytesseract
Versão do Tesseract
Recomenda-se o uso da versão 4.x ou superior para melhor desempenho e suporte a múltiplos idiomas.

Estrutura do Código
Carregamento da imagem: Utiliza cv2.imread para carregar a imagem de entrada.
Configuração do idioma: Configura o Tesseract para processar texto em português (lang='por').
Detecção de palavras:
pytesseract.image_to_string(img, lang='por'): Extrai o texto da imagem.
pytesseract.image_to_boxes(img): Obtém a localização dos caracteres.
pytesseract.image_to_data(img): Retorna dados detalhados, incluindo as palavras e suas posições.
Desenho de retângulos: Utiliza cv2.rectangle para marcar as palavras detectadas na imagem.
Exibição de resultados: Utiliza cv2.imshow para mostrar a imagem processada.
Resultado
O script exibe a imagem processada com as palavras detectadas destacadas por retângulos e sobrepostas por texto, fornecendo uma análise visual das informações extraídas.

Sinta-se à vontade para contribuir com melhorias no código ou relatar problemas no repositório!

---


- #### My LinkedIn - [![Linkedin Badge](https://img.shields.io/badge/-LucianaDiemert-blue?style=flat-square&logo=Linkedin&logoColor=white&link=https://www.linkedin.com/in/lucianadiemert/)](https://www.linkedin.com/in/lucianadiemert/)

#### Contact

<img align="left" src="https://www.github.com/ludiemert.png?size=150">

#### [**Luciana Diemert**](https://github.com/ludiemert)

🛠 Full-Stack Developer <br>
🖥️ Python Enthusiast | Computer Vision | AI Integrations <br>
📍 São Jose dos Campos – SP, Brazil

<a href="https://www.linkedin.com/in/lucianadiemert" target="_blank"><img src="https://img.shields.io/badge/LinkedIn-0077B5?style=flat&logo=linkedin&logoColor=white" alt="LinkedIn Badge" height="25"></a>&nbsp;
<a href="mailto:lucianadiemert@gmail.com" target="_blank"><img src="https://img.shields.io/badge/Gmail-D14836?style=flat&logo=gmail&logoColor=white" alt="Gmail Badge" height="25"></a>&nbsp;
<a href="#"><img src="https://img.shields.io/badge/Discord-%237289DA.svg?logo=discord&logoColor=white" title="LuDiem#0654" alt="Discord Badge" height="25"></a>&nbsp;
<a href="https://www.github.com/ludiemert" target="_blank"><img src="https://img.shields.io/badge/GitHub-100000?style=flat&logo=github&logoColor=white" alt="GitHub Badge" height="25"></a>&nbsp;

<br clear="left"/>


   
