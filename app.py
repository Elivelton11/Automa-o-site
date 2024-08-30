from selenium import webdriver
from selenium.webdriver.common.by import By
import openpyxl 

# acessar o site: https://www.digitusul.com.br/
driver = webdriver.Chrome()
driver.get('https://www.digitusul.com.br/')

 
# extrair todos os preços 

precos=driver.find_elements(By.XPATH,"//span[@class='price']")

# extrair todos os nomes 

titulos=driver.find_elements(By.XPATH,"//h2[@class='product-name']")

#criar a planilha
workbook=openpyxl.Workbook()
#criando a pagina produtos
workbook.create_sheet('produtos')
#seleciono a pagina produtos
sheet_produtos=workbook['produtos']
#inserir os titulos e preços na planilha
sheet_produtos['A1'].value='Produto'
sheet_produtos['B1'].value='Preço'

# converter os dados para a planilha em excel 

for titulo, preco in zip(titulos,precos):
    sheet_produtos.append([titulo.text,preco.text ])
    
workbook.save('produtos.xlsx')