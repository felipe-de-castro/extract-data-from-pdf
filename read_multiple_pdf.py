# %%
import pandas as pd
import os
import re
from pdfminer.high_level import extract_text
from datetime import datetime
from datetime import date
import numpy as np

# %%

## Criando def para extrair nomes:
def extract_name(content):
    name = r'Nome:\s*(.*)'
    names = re.findall(name, content, re.IGNORECASE)
    return names

## Criado def para extrair data nascimento
def extract_birthday(birthday_content):
    birthday = r'Data de nascimento: \s*(.*)'
    birthdays = re.findall(birthday,birthday_content)
    return birthdays

## Criado def para extrair data nascimento
def extract_cpf(cpf_content):
    cpf = r'CPF: \s*(.*)'
    cpfs = re.findall(cpf,cpf_content)
    return cpfs


## Criando def para extrair julgados
def extract_julgado(julgo_content):
    search_phrases = [
        "JULGO PROCEDENTE",
        "JULGO IMPROCEDENTE",
        "JULGO PROCEDENTE EM PARTE",
        "JULGO PARCIALMENTE PROCEDENTE"
    ] 

    julgos = []

    sorted_phrases = sorted(search_phrases, key=len, reverse=True)
    pattern = '|'.join(re.escape(phrase) for phrase in sorted_phrases)

    matched_phrases = re.findall(pattern, julgo_content)
    julgos.extend(matched_phrases)

    return julgos


# %%
## Caminho dos arquivos para loops e pesquisa
path = 'pdfs/'
files= os.listdir(path)
all_names = []
all_birthdays = []
all_cpfs = []
all_julgos = []

for x in files:
    if x.endswith('.pdf'):
        pdf_path = os.path.join(path, x)
        pdf_content =  extract_text(pdf_path)
        #names
        names = extract_name(pdf_content)
        all_names.extend(names)
        #birthday
        birthdays = extract_birthday(pdf_content)
        all_birthdays.extend(birthdays)
        #cpfs
        cpfs = extract_cpf(pdf_content)
        all_cpfs.extend(cpfs)
       
        #julgado
        julgos = extract_julgado(pdf_content)
        all_julgos.extend(julgos)

        
        #for name in names:
        #    print(name)


# %%
## Creating Dataframe with data scrapping from PDFs
df = pd.DataFrame({ 'name': all_names, 
                   'birthday': all_birthdays, 
                   'CPF': all_cpfs, 
                   'age': np.nan, 
                   'Julgado' : all_julgos} )

# %%
## Cleaning the Brazilian Tax ID 
df.CPF = df.CPF.astype(str)
df.CPF = df.CPF.str.replace('.', '')
df.CPF = df.CPF.str.replace('-', '')
# df.Julgado = df.Julgado.str.replace('JULGO ','')
# %%
## Cleaning the birthday column 
df.birthday = df.birthday.str.replace('/', '')
# %%
## Converting birthday column to datetime
df['birthday'] = pd.to_datetime(df['birthday'], format='%d%m%Y')
# %%
## From the birth datetime column calculating the age of each
df["age"] = df["birthday"].apply(lambda x : (pd.datetime.now().year - x.year))
# %%
df
# %%
