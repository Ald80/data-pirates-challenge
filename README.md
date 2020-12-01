# Data Pirates challenge

## Requerimentos:

* **[python]**(https://www.python.org/)
* **selenium**
* **beautifulsoup4**
* **requests**
* **python-dotenv**

## Instalação de ambiente:

È recomendado instalar as bibliotecas do projeto através da criação de uma virtual environment, acesse [link](https://packaging.python.org/guides/installing-using-pip-and-virtual-environments/#creating-a-virtual-environment) com as instruções de como criar um ambiente virtual. 

Para instalar as bibliotecas do projeto basta executar o comando `pip install -r requirements.txt`

Caso não tenha o navegador Chrome instalado, segue o [link](https://www.google.com/intl/pt-BR/chrome/) para fazer o download.

Para que o **selenium** consiga fazer uso do navegador, é necessário baixar o driver do navegador, através do [link](https://chromedriver.storage.googleapis.com/index.html) é possível baixar o driver de várias versões do Chrome, faça o download conforme a versão do Chrome instalado no seu computador.

Depois de ter feito o download do driver, insira o caminho o qual foi extraído o driver no valor da variável `executable_path` do arquivo `config.env`

**Exemplo:**

`executable_path = C:\Program Files (x86)\webdriver\chromedriver.exe`

## Execução:

Para rodar o projeto, execute o comando `python main.py`

O arquivo de saída contendo os dados extraídos é o `data.jsonl`

OBS: **As vezes o site do correios tem problemas de redirecionamento em excesso, ficando inviável extrair os dados, por sorte ele retorna ao normal dentre de poucos minutos.**
