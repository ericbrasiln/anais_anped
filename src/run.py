#from revistas import revistas
#from reports import report_scrape
import time, os
from selenium import webdriver
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.support.ui import WebDriverWait 
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service

timestr = time.strftime("%Y-%m-%d")
saveMode = ''
def main():
    url_base = 'http://anais.anped.org.br/'
    # Definição da área do conhecimento para raspagem
    print('-=-Definição do evento-=-\n')
    event = str(input(
                '- Opções:\n'
                '38 - 2021\n'
                '39 - 2019\n'
                '40 - 2017\n'
                'Digite o número correspondente ao evento que deseja raspar: \n'))
    print('-='*50)
    diretorio = os.path.join(f'anped-{event}',timestr)
    if not os.path.exists(diretorio):
        #Se a pasta ainda não existir, cria a pasta
        os.makedirs(diretorio)
    url = f'{url_base}p/{event}reuniao/trabalhos'
    # Definição das opções do driver
    firefox_options = Options()
    firefox_options.add_argument('-lang=pt-BR')
    #firefox_options.add_argument("--headless")
    firefox_options.add_argument("--no-sandbox")
    firefox_options.add_argument("--start-maximized")
    s=Service(GeckoDriverManager().install())
    driver = webdriver.Firefox(service=s, options=firefox_options)
    driver.get(url)
##################continuar daqui######################################
    ''''journal_table = driver.find_element(By.ID,'journals_table_body')
    tematica = journal_table.find_element(By.ID,f"heading-{area}")
    print(f'\n-=-{tematica.text}-=-')
    btn = tematica.find_element(By.TAG_NAME,'a').click()
    time.sleep(1)
    area_box = driver.find_element(By.ID,f'collapseContent-{area}')
    journal_list = area_box.find_elements(By.CLASS_NAME,'collectionLink ')
    report_scrape(diretorio, timestr, area, saveMode)
    for journal in journal_list:
        link = journal.get_attribute("href")
        link_final = link+'grid'
        #Função para acessar o grid
        name = journal.find_element(By.CLASS_NAME,"journalTitle").text
        revistas(diretorio, link, link_final, name, saveMode)
    print('fim da raspagem')'''

if __name__ == "__main__":
    main()