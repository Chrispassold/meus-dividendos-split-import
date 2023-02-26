# Separador de arquivos para importar no site [Meus dividendos](https://portal.meusdividendos.com/)

## Requisitos
- Python instalado
    - Recomendado instalar via [choco](https://chocolatey.org/install) e após instalado, usar o comando `choco install python` para instalar o python
    - Pode-se instalar via [site oficial](https://www.python.org/downloads/)

## Como usar?

1. Executar o comando `pip install -r requirements.txt` para instalar as dependencias do projeto
2. Criar um arquivo **CSV** com todas as movimentações, seguindo as colunas e padrão abaixo:

    ```
    Codigo,Data,Valor,Quantidade,Tipo,Despesas
    ABEV3,21/03/2016,"18,62",10,Compra,"0,82"
    ABEV3,22/03/2016,"18,62",10,Venda,"0,82"
    ```
3. Criar um arquivo na raiz do projeto chamado `local.properties` com o conteudo abaixo:
    ```properties
    FULL_RECORDS_CSV=caminho/para/seu/arquivo/com/todas/movimentacoes
    ```

4. Por fim, executar o comando `python -u ./main.py`, o comando dividirá o csv completo em N partes para que seja possível importar no site, os arquivos estarão em sequencia na pasta `./output`.