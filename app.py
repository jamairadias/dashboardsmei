# Run this app with `python app.py` and
# visit http://127.0.0.1:8050/ in your web browser.
import dash
from dash import Dash, html, dcc, Input, Output
import dash_bootstrap_components as dbc
import plotly.express as px
import pandas as pd


app = Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])
# assume you have a "long-form" data frame
# see https://plotly.com/python/px-arguments/ for more options

df = pd.read_excel("BASEMEI.xlsx")
fig = px.bar(df, x="REGIAO_ATUACAO", color="SETOR_ATIVIDADE", barmode="group")
opcoes = list(df['DESCRICAO_ATIVIDADE'].unique())
opcoes.append("Todas as atividades")

app.layout = html.Div(children=[
html.H1(children='Painel com análise de dados de MEI para MEI da cidade de São Paulo'),

html.H2(children='Gráfico com todas as atividades de MEIs ativos, segmentados por região em que estão sediados'),

html.Div(children=''' 
Obs: O gráfico apresenta a distribuição quantitativa amostral de MEIs, por atividade específica, distribuídos por região, de um total real maior que 1,17 milhão de MEIs em 2022.
'''),

dcc.Dropdown(opcoes, value='Todas as atividades', id='lista_atividades'),
dcc.Graph(
id='grafico Tipo de atividade por regiao',

figure=fig
)
])
@app.callback(
Output('grafico Tipo de atividade por regiao', 'figure'),
Input('lista_atividades', 'value')
)
def update_output(value):
    if value == "Todas as atividades":
        fig = px.bar(df, x="REGIAO_ATUACAO", color="SETOR_ATIVIDADE", barmode="group")
    else:
        tabela_filtrada = df.loc[df['DESCRICAO_ATIVIDADE']==value, :]
        fig = px.bar(tabela_filtrada, x="REGIAO_ATUACAO", color="SETOR_ATIVIDADE", barmode="group")
    return fig

if __name__ == '__main__':
    app.run_server(debug=True)