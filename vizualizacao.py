import streamlit as st
import plotly.express as px
import plotly as plt

data = r'C:\Users\valde\Downloads\prova_dv\datasets\2024_medalists_all.csv'

# Streamlit Title
st.title('Olympic Medalists Data Visualization')

# 1. Medals by Country (Bar Graph)
st.subheader('Medals Won by Country')

# Simulação de um DataFrame para o exemplo (remover isso na sua implementação)
# import pandas as pd
# data = pd.DataFrame({
#    'country_medal': ['USA', 'China', 'Russia', 'Brazil', 'UK']*100
# })

# Obtendo a contagem de medalhas por país
medals_by_country = data['country_medal'].value_counts()

# Filtro para o número de países a serem exibidos
num_paises = st.selectbox('Selecione o número de países para exibir', [10, 20, 30, 40], index=0)

# Exibir os países selecionados pelo filtro
medals_by_country_filtered = medals_by_country.head(num_paises)

# Criando o gráfico
fig1, ax1 = plt.subplots()
medals_by_country_filtered.plot(kind='bar', color='gold', edgecolor='black', ax=ax1)
ax1.set_title(f'Medals Won by Top {num_paises} Countries')
ax1.set_xlabel('Country')
ax1.set_ylabel('Number of Medals')
ax1.set_xticklabels(ax1.get_xticklabels(), rotation=45)

# Exibindo o gráfico no Streamlit
st.pyplot(fig1)



# 3. Age Distribution (Histogram)
st.subheader('Age Distribution of Medalists')
fig3, ax3 = plt.subplots()
ax3.hist(data['age'].dropna(), bins=10, color='skyblue', edgecolor='black')
ax3.set_title('Age Distribution of Medalists')
ax3.set_xlabel('Age')
ax3.set_ylabel('Number of Medalists')
ax3.grid(axis='y')
st.pyplot(fig3)



# 5. Geographical Distribution (Scatter Plot)
st.subheader('Geographical Distribution of Medalists\' Places of Birth')
fig5, ax5 = plt.subplots()
ax5.scatter(data['lon'], data['lat'], alpha=0.5)
ax5.set_title('Geographical Distribution of Medalists\' Places of Birth')
ax5.set_xlabel('Longitude')
ax5.set_ylabel('Latitude')
ax5.grid()
st.pyplot(fig5)



# Lista de continentes e seus respectivos países (exemplo simplificado)
continentes = {
    'África': ['South Africa', 'Kenya', 'Egypt'],  # adicione mais países africanos
    'América do Norte': ['United States of America', 'Canada', 'Mexico'],
    'América do Sul': ['Brazil', 'Argentina', 'Colombia'],
    'Ásia': ['China', 'Japan', 'South Korea'],
    'Europa': ['France', 'Germany', 'United Kingdom'],
    'Oceania': ['Australia', 'New Zealand']
}

# Criar um filtro de continentes no Streamlit
st.sidebar.title("Filtros")
continente_selecionado = st.sidebar.selectbox("Selecione o continente", continentes.keys())

# Filtrar o DataFrame pelo continente selecionado
paises_selecionados = continentes[continente_selecionado]
df_filtrado = data[data['country_medal'].isin(paises_selecionados)]

# Plotar o mapa-múndi com os medalhistas filtrados
fig = px.scatter_geo(
    df_filtrado,
    lat='lat',
    lon='lon',
    hover_name='medalist_name',
    hover_data=['medal', 'delegation_name', 'event_name'],
    color='medal',
    title=f"Distribuição dos Medalhistas - {continente_selecionado}",
    projection='natural earth',
    template=None  # Sem template
)


# Exibir o gráfico no Streamlit
st.plotly_chart(fig)


