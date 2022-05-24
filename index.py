from pywebio import start_server
from pywebio.input import *
from pywebio.output import *
from pywebio.session import *
from pywebio.pin import *

from sklearn.preprocessing import StandardScaler
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import matplotlib.pyplot as plt  # plotting
import numpy as np  # linear algebra
import os  # accessing directory structure
import pandas as pd  # data processing, CSV file I/O (e.g. pd.read_csv)


def genre_recommendations(i, M, items, k=10):
    ix = M.loc[:, i].to_numpy().argpartition(range(-1, -k, -1))
    closest = M.columns[ix[-1:-(k + 2):-1]]
    closest = closest.drop(i, errors='ignore')
    return pd.DataFrame(closest).merge(items).head(k)


nRowsRead = 1000  # specify 'None' if want to read whole file
# interactions_test.csv has 12455 rows in reality, but we are only loading/previewing the first 1000 rows
df1 = pd.read_csv(filepath_or_buffer='C:\dataset\RAW_recipes.csv', delimiter=',', nrows=nRowsRead)
df1.dataframeName = 'RAW_recipes.csv'
nRow, nCol = df1.shape
# put_text(f'There are {nRow} rows and {nCol} columns')

tfidf = TfidfVectorizer(stop_words='english')
tfidf_matrix = tfidf.fit_transform(df1['ingredients'])
tfidf_matrix.shape

cosine_sim = cosine_similarity(tfidf_matrix)
cosine_sim_df = pd.DataFrame(cosine_sim, index=df1['name'], columns=df1['name'])
print('Shape:', cosine_sim_df.shape)
cosine_sim_df.sample(5, axis=1).round(2)

# Design

put_image(open('logoSC.png', 'rb').read());

put_text('Precisando daquela sugestão do chefe? Encontre as melhores receitas aqui e aprovete!').style(
    'color: #025D00; font-size:25px; margin-top:25px; margin-bottom:30px');

text = textarea('Pesquisar receita', rows=3, placeholder='Nome da Receita')

receitas_recomendadas = genre_recommendations(text, cosine_sim_df, df1[['name', 'ingredients']])
# put_text(receitas_recomendadas)

matriz = [[receitas_recomendadas]]
put_table(matriz)

put_row([
    put_column([
        put_row([
            put_table([['Nome receita', 'Ingredientes'], [put_text('%r' % text), 'D']]),
            put_image(open('chefLogo.png', 'rb').read())
            ,
        ]),
    ]),

])

# start_server(main, port=8080, debug=True)