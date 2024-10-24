import streamlit as st
import plotly.express as px
import plotly as plt

data = r'C:\Users\valde\Downloads\prova_dv\datasets\2024_medalists_all.csv'

# Streamlit Title
st.title('Olympic Medalists Data Visualization')

# 1. Medals by Country (Bar Graph)
st.subheader('Medals Won by Country')

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


