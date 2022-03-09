'''Script to scrape all pdf and infos from Anais Anped (2017-2021)
'''
from urllib.request import Request, urlopen
from bs4 import BeautifulSoup
import pandas as pd
from datetime import datetime
import os
import wget
import re

dic = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.163 Safari/537.36'}
now = datetime.now()
date = now.strftime("%Y-%m-%d_%H-%M-%S")

def csv_file(final_list,event):
    """Exports infos to csv file."""
    print('Salvando arquivo .csv com todas as informações: autores, título, tipo, evento, ano, link do pdf')
    # create dataframe with pandas and export to csv
    df = pd.DataFrame(final_list, columns=['Autor principal', 'Título', 'GT', 'Evento', 'Ano', 'Link do Arquivo'])
    df.to_csv(f'anais-anped-{event}_{date}.csv')
    print('Raspagem completa.')

def next_page(bs, url_base):
    """Returns the next page link."""
    try:
        next_page = bs.find('li', class_='next')
        next_page_link = next_page.find('a')['href']
        next_page_link = url_base+next_page_link
        print(f'\nProxima pagina: {next_page_link}')
        return next_page_link
    except:
        print('Não há mais páginas')
        return False

def get_pdf(diretorio, pdf_link, title):
    """Download pdf in a specific directory."""
    # clean title
    change = re.sub(r"[(:\(\)<>?/\\|@+)]", "", title)
    full_name = re.sub(r"\s+", "_", change)
    pdf_name = f'{full_name}.pdf'
    # create directory if not exists
    path_final_pdf = os.path.join(diretorio, 'PDF')
    if not os.path.exists(path_final_pdf):
        os.makedirs(path_final_pdf)
    out_pdf = os.path.join(path_final_pdf, pdf_name)
    # download pdf
    if not os.path.exists(out_pdf):
        try:
            wget.download(pdf_link, out_pdf)
        except Exception as e:
            print(f'Erro: {e}')
    else:
        print('\nPDF já existe.')

def paper_infos(papers, final_list, diretorio, event):
    """Collects infos from each paper."""
    for paper in papers:
        #find all divs in paper
        divs = paper.find_all('div')
        for div in divs:
            # find title
            if div.find('h4', class_='anais-trabalho-titulo text-warning'):
                title = div.find('h4', class_='anais-trabalho-titulo text-warning').text
            # find authors (different tags for event 38 and th rest)
            if event =='38':
                if div.find('em', class_='anais-trabalho-autor'):
                    authors=div.find('em', class_='anais-trabalho-autor').text
            else:
                if div.find('em', class_='anais-trabalho-autor'):
                    #get next div
                    next_div = div.find_next('div')
                    authors = next_div.find('em',class_='field-content')
                    try:
                        author_text = authors.text
                    except:
                        author_text = ''
                    authors = author_text
            # find pdf link
            if div.find('h4'):
                try:
                    link = div.find('a')['href']
                except:
                    pass
        # find gt title
        spans = paper.find_all('span')
        gt_title = spans[0].find('span').text
        #call get_pdf function
        get_pdf(diretorio, link, title)
        if event == '38':
            year = '2017'
        elif event == '39':
            year = '2019'
        elif event == '40':
            year = '2021'
        # add infos to list
        paper_infos = [authors, title, gt_title, event, year, link]
        # add infos to final list
        final_list.append(paper_infos)

def request (url, dic):
    """Open url and return a beautifulsoup object."""
    reqopen = Request(url, headers=dic)
    req = urlopen(reqopen)
    bs = BeautifulSoup(req.read(), 'lxml')
    return bs

def config_event():
    """Configure parameters for scraping."""
    print('-=-Definição do evento-=-\n')
    event = str(input(
                '- Opções:\n'
                '38 - 2017\n'
                '39 - 2019\n'
                '40 - 2021\n'
                'Todos\n'
                'Digite o número correspondente ao evento que deseja raspar: \n')).lower()
    print('-='*50)
    if event == '38':
        print('Evento escolhido: 38 - 2017\n')
    elif event == '39':
        print('Evento escolhido: 39 - 2019\n')
    elif event == '40':
        print('Evento escolhido: 40 - 2021\n')
    elif event == 'todos':
        print('Evento escolhido: Todos\n')
        event='38-39-40'
    else:
        print('Opção inválida')
        quit()
    return event

def main():
    """Main function.Executes all functions."""
    url_base = 'http://anais.anped.org.br'
    event_base = config_event()
    final_list=[]
    if event_base == '38-39-40':
        events = ['38', '39', '40']
        for event in events:
            diretorio = os.path.join(f'anped-{event}')
            if not os.path.exists(diretorio):
                # if directory doesn't exist, create it
                os.makedirs(diretorio)
            url = f'{url_base}/p/{event}reuniao/trabalhos?field_prog_gt_target_id_entityreference_filter=All'
            # create a while loop to get all pages
            while True:
                # call request function
                bs = request(url, dic)
                papers = bs.find_all('div', class_='well anais-trabalhos col-xs-12 col-sm-12 col-md-6 col-lg-6')
                paper_infos(papers, final_list, diretorio, event)
                #call next_page function
                url = next_page(bs, url_base)
                if url == False:
                    break
    else:
        diretorio = os.path.join(f'anped-{event_base}')
        if not os.path.exists(diretorio):
            # if directory doesn't exist, create it
            os.makedirs(diretorio)
        url = f'{url_base}/p/{event_base}reuniao/trabalhos?field_prog_gt_target_id_entityreference_filter=All'
        # create a while loop to get all pages
        while True:
            # call request function
            bs = request(url, dic)
            papers = bs.find_all('div', class_='well anais-trabalhos col-xs-12 col-sm-12 col-md-6 col-lg-6')
            paper_infos(papers, final_list, diretorio, event_base)
            #call next_page function
            url = next_page(bs, url_base)
            if url == False:
                break
    # call csv_file function
    csv_file(final_list,event_base)

if __name__ == "__main__":
    main()  
