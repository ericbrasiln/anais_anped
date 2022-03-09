<p align="center"><img src="https://github.com/ericbrasiln/Anais-Anpuh/blob/7002907c1393f62567eb74f360385cd84ced309b/images/labhd.png?raw=true" height="256" width="256"/></p>

[![DOI:EM BREVE]]()
 [![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg)](https://www.python.org/) [![MIT license](https://img.shields.io/badge/License-MIT-blue.svg)](https://lbesson.mit-license.org/)

# Ferramenta Anais Anped

Projeto de script para web scraping da página de [Anais da Associação Nacional de Pós-Graduação e Pesquisa em Educação - Anped](http://anais.anped.org.br/).

Seu objetivo é compor a base de dados do [Repositório Digital das Humanidades (pt-BR)](https://labhdufba.github.io/redhbr/) e foi desenvolvida por [Eric Brasil](https://ericbrasiln.github.io/) (IHLM/UNILAB) em parceria com o [Laboratório de Humanidades Digitais da Ufba](http://labhd.ufba.br/).

*O script Anais-Anped realiza a raspagem dos papers em pdf dos encontros nacionais 38, 39 e 40, dos anos 2017, 2019 e 2021, respectivamente, (disponíveis atualmente na site).*
___

**A ferramenta foi desenvolvida apenas para pesquisas acadêmicas, sem fins lucrativos.**
___

## Índice

- [Anais_Anped](#anais_anped)
  - [Índice](#índice)
  - [Instalação](#instalação)
  - [Utilização](#utilização)
  - [Resultados](#resultados)
  - [Como citar?](#citação)
  - [Licença](#licença)


## Instalação

Para executar a ferramenta é preciso clonar ou fazer download do repositório para sua máquina. Antes de executar os scripts, é preciso preparar seu computador, como mostramos abaixo.

A ferramentas desse projeto foram escritas em [Python 3.9.7](https://www.python.org/). Portanto, para executar o arquivo .py é preciso instalar o Python3 em seu computador.

[Clique aqui](https://python.org.br/instalacao-windows/) para acessar um tutorial de instalação do Python no Windows, [clique aqui](https://python.org.br/instalacao-linux/) para Linux e [clique aqui](https://python.org.br/instalacao-mac/)
para Mac.

Após a instalação do Python é preciso instalar as bibliotecas necessárias para a ferramenta ser executada. Para isso, basta executar o comando `pip install -r requirements.txt` no terminal, a partir da pasta onde está o arquivo.  Para saber mais sobre instalação de bibliotecas com pip, veja essa lição do [Programming Historian](https://programminghistorian.org/pt/licoes/instalacao-modulos-python-pip).

1. Acesse o diretório em que o arquivo `requirements.txt` está salvo:
   ```{.sh .bash}
   $ cd <caminho para a pasta>
   ```
2. Instale as bibliotecas requeridas com o seguinte comando:
   ```{.python}
   pip install -r requirements.txt
   ```

Agora é possível executar a ferramenta direto do prompt de comando do Windows ou pelo terminal do Linux, ou utilizar as diversas [IDE](https://pt.wikipedia.org/wiki/Ambiente_de_desenvolvimento_integrado) disponíveis.

## Utilização

Na pasta da ferramenta existem dois arquivos python que permitem a execução de opções distintas de raspagem. O primeiro, `scielo_v2.py`, permite a raspagem de todas as revistas de uma determinada área do conhecimento. O segundo, `scielo_rev_v2.py`, permite a raspagem por revista ou lista de revistas específicas.

Esse script permite ao usuário selecionar qual evento pretende raspar (ou se pretende raspar todos de uma vez).

Para isso é preciso executar o seguinte comando, do interior da pasta onde o arquivo está localizado:

```{.sh}
python scrape_anped.py
```

A seguinte mensagem será exibida:

```{.python}
-=-Definição do evento-=-

- Opções:
38 - 2017
39 - 2019
40 - 2021
Todos
Digite o número correspondente ao evento que deseja raspar: 
```

## Resultados

O script retorna para o usuário **todos os pdfs disponíveis em todas as páginas dos eventos selecionados**. São criadas pastas com o número de cada evento para o armazenamento dos arquivos em PDF.

O script também gera um arquivo **CSV** (*comma-separated values*) contendo os seguintes valores para cada paper: Autores, Título, GT, Evento, Ano, Link.

O script está funcionando perfeitamente. Qualquer alteração no site percebida pelos usuários ou sugestões de aprimoramento são bem vindas.

## Citação

Como citar essa ferramenta?

É possível clicar em `Cite this repository` na aba à direita da página inicial do repositório no GitHub para acessar a citação nos formatos APA e BibTex, ou ainda acessar o [arquivo da citação](CITATION.cff) em formato .cff.

Abaixo a citação no formato BibTex:

```
cff-version: 1.2.0
title: Ferramenta Anais Anped
message: >-
  If you use this software, please cite it using the
  metadata from this file.
type: software
authors:
  - given-names: Eric
    family-names: Brasil
    email: ericbrasiln@gmail.com
    affiliation: IHLM/UNILAB
    orcid: 'https://orcid.org/0000-0001-5067-8475'
```

## Licença

MIT licensed

Copyright (C) 2022 [Eric Brasil](https://github.com/ericbrasiln)
