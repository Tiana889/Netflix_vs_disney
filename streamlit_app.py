import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

st.set_page_config(
    page_title="My Streamlit App",
    page_icon="🌟",
    layout="wide",
    initial_sidebar_state="expanded"
)

df=pd.read_csv(r"Data\netflix_disney.csv")


# INICIO
st.title("Netflix vs Disney+ : La batalla por la audiencia" )


# URLs de los logos
netflix_logo_url = "https://upload.wikimedia.org/wikipedia/commons/6/69/Netflix_logo.svg"
disney_logo_path = "disney_image.png"
vs_logo_path = "vs.png"


# Muestra los logos uno al lado del otro usando columnas
col1, col2, col3= st.columns(3)

with col1:
    st.image(netflix_logo_url, caption='Netflix', use_column_width=True)
   
with col2: 
    st.image(vs_logo_path, caption='VS', use_column_width=True)

with col3:
    st.image(disney_logo_path, caption='Disney', use_column_width=True)
    

st.title("¿Cómo  Disney+ se ha posicionado estratégicamente en un mercado de streaming cada vez más competitivo?")
st.subheader("En este informe estratégico, exploramos cómo las plataformas de streaming Netflix y Disney+ definen y diferencian sus catálogos, orientándose a su público objetivo y valor diferencial.")

# Ruta de la imagen (ajusta la ruta según sea necesario)
image_path = "C:/Users/thaty/OneDrive/Escritorio/BootCamp/IRONHACK/Netflix_vs_disney/image/monigotes.png"


# Crea las 3 columnas
col1, col2, col3 = st.columns(3)

# Verificación y muestra de imagen en la segunda columna
if os.path.exists(image_path):
    with col2:
        st.image(image_path, caption='Monigotes', use_column_width=True, width=150)
else:
    st.write(f"Imagen {image_path} no encontrada")
    


st.title("Objetivo del Análisis:")
st.subheader("Desvelar los patrones de contenido que influyen en la calidad percibida de las plataformas y su capacidad para atraer audiencias. Nos enfocamos en la estrategia de Disney+ que le ha llevado a un enorme crecimiento y alcanzar la rentabilidad en 2024, diferenciándose de Netflix.")
st.write("")
st.write("")
st.title("Hipótesis")
st.subheader("➤Los contenidos de Disney+ tienen una calidad más uniforme, mientras que en Netflix tendrá una variación más alta en las reseñas de sus contenidos.")
st.subheader("➤El catálogo de Disney+ está más enfocado a contenido familiar e infantil que el de Netflix, mientras que Netflix tiene una mayor diversidad de géneros y contenidos para adultos.")
st.subheader("➤En Disney+ genera más atractivo el contenido clásico, mientras que Netflix señala más a títulos modernos.")
st.subheader("➤Los contenidos infantiles en Disney+ tienen una mayor aceptación y valoración en IMDB que los contenidos infantiles en Netflix.")

st.write("")
st.write("")
st.title("GRAFICAS")
st.subheader(" Segun el estudio de EDA realizado, comprobamos las siguientes graficas:")


# Configurar la barra lateral para las selecciones del usuario
st.sidebar.title("Filtros")
platforms = df['plataforma'].unique().tolist()



# Selección múltiple de plataformas
selected_platforms = st.sidebar.multiselect('Selecciona Plataformas', platforms, default=platforms)

# Filtrar los datos con base en las selecciones del usuario
df_filtered = df[df['plataforma'].isin(selected_platforms)]




# Definir paleta de colores específica
palette = {'netflix': '#E50914', 'disney': '#006e99'}

# Crear la primera gráfica (Distribución de contenido por categorías de edad)
def grafica_categorias_edad():
    fig, ax = plt.subplots(figsize=(12, 6))
    sns.countplot(data=df_filtered[df_filtered['age_category'] != 'Desconocido'], x='age_category', hue='plataforma', palette=palette, ax=ax)
    ax.set_title('Distribución de contenido por categorías de edad entre Netflix y Disney+')
    ax.set_xlabel('Categoría de Edad')
    ax.set_ylabel('Cantidad')
    ax.legend(title='Plataforma')
    plt.xticks(rotation=45)  # Rotar las etiquetas del eje x para mejor legibilidad
    return fig

# Crear la segunda gráfica (Distribución de contenido entre Netflix y Disney+)
def grafica_distribucion_contenido():
    fig, ax = plt.subplots(figsize=(10, 6))
    sns.countplot(data=df_filtered, y='plataforma', palette=palette, ax=ax)
    ax.set_title('Distribución de contenido entre Netflix y Disney+')
    ax.set_xlabel('Cantidad de títulos')
    ax.set_ylabel('Plataforma')
    return fig

# Crear la tercera gráfica (Distribución de contenido por tipo)
def grafica_distribucion_tipo():
    fig, ax = plt.subplots(figsize=(10, 6))
    sns.countplot(data=df_filtered, x='type', hue='plataforma', palette=palette, ax=ax)
    ax.set_title('Distribución de contenido por tipo entre Netflix y Disney+')
    ax.set_xlabel('Tipo de contenido')
    ax.set_ylabel('Cantidad')
    ax.legend(title='Plataforma')
    return fig

# Crear la cuarta gráfica (Número de títulos por año de lanzamiento últimos 25 años)
def grafica_lanzamiento_anos():
    # Filtrar datos para los últimos 25 años
    current_year = pd.to_datetime('today').year
    df_last_25_years = df_filtered[df_filtered['release_year'] >= (current_year - 25)]
    fig, ax = plt.subplots(figsize=(12, 6))
    sns.countplot(data=df_last_25_years, x='release_year', hue='plataforma', palette=palette, ax=ax)
    ax.set_title('Número de títulos por año de lanzamiento (últimos 25 años)')
    ax.set_xlabel('Año de lanzamiento')
    ax.set_ylabel('Cantidad')
    plt.xticks(rotation=90)  # Rotar las etiquetas del eje x para mejor legibilidad
    ax.legend(title='Plataforma')
    return fig
# Crear dos columnas en Streamlit
col1, col2 = st.columns(2)

# Generar y mostrar las gráficas en las columnas correspondientes
with col1:
    st.pyplot(grafica_categorias_edad())
    st.pyplot(grafica_distribucion_tipo())

with col2:
    st.pyplot(grafica_distribucion_contenido())
    st.pyplot(grafica_lanzamiento_anos())

st.write("")
st.write("")

st.title("Modelo K-Means")
st.subheader("Utilizamos el algoritmo de K-means para agrupar títulos de nuestra plataforma basándonos en diversas características, como el género, la duración y el año de lanzamiento. Nuestro objetivo es identificar grupos de títulos similares para mejorar la recomendación de contenido.")
st.write("")
st.title("Descripción de los Datos")
st.subheader("Para este análisis, tomamos en cuenta características como el género, la categoría de edad, la duración y el año de lanzamiento. Estas características nos permiten agrupar títulos que comparten similitudes.")

# 2. Aplicación del algoritmo K-means

# Definir número de clústeres (ejemplo k=4)
kmeans_code = '''
from sklearn.cluster import KMeans

# Definir número de clústeres (ejemplo k=4)
kmeans = KMeans(n_clusters=4, random_state=42)

# Ajustar K-means al conjunto de datos
df['cluster'] = kmeans.fit_predict(X_scaled)

# Ver los resultados del clustering
print(df[['title', 'cluster','genres']].head())
'''

st.code(kmeans_code, language='python')

st.write("")
st.title("Resultados de clasificación de peliculas por plataformas.")
st.markdown(
    """
    <h1 style='color: #E50914;'>NETFLIX:</h1>
    """,
    unsafe_allow_html=True
)


# URLs de los logos con rutas absolutas
peli1_path = "C:/Users/thaty/OneDrive/Escritorio/BootCamp/IRONHACK/Netflix_vs_disney/image/Peli1.png"
peli2_path = "C:/Users/thaty/OneDrive/Escritorio/BootCamp/IRONHACK/Netflix_vs_disney/image/Peli2.png"
peli3_path = "C:/Users/thaty/OneDrive/Escritorio/BootCamp/IRONHACK/Netflix_vs_disney/image/Peli3.png"
peli4_path = "C:/Users/thaty/OneDrive/Escritorio/BootCamp/IRONHACK/Netflix_vs_disney/image/Peli4.png"
peli5_path = "C:/Users/thaty/OneDrive/Escritorio/BootCamp/IRONHACK/Netflix_vs_disney/image/Peli5.png"

# Función para verificar y mostrar imágenes
def display_image(column, file_path, caption):
    if os.path.exists(file_path):  # Verifica si el archivo existe
        column.image(file_path, caption=caption, use_column_width=True)
    else:
        column.write(f"Imagen {file_path} no encontrada")

# Muestra los logos uno al lado del otro usando 5 columnas
col1, col2, col3, col4, col5 = st.columns(5)

display_image(col1, peli1_path, 'Peli1')
display_image(col2, peli2_path, 'Peli2')
display_image(col3, peli3_path, 'Peli3')
display_image(col4, peli4_path, 'Peli4')
display_image(col5, peli5_path, 'Peli5')

st.subheader("Comprobamos que se basa la clasificación en adultos, centrándose en un genero de drama y un tema social.") 
st.write("")
st.write("")
st.markdown(
    """
    <h1 style='color: #006E99;'>DISNEY +:</h1>
    """,
    unsafe_allow_html=True
)


# URLs de los logos con rutas absolutas
peli6_path = "C:/Users/thaty/OneDrive/Escritorio/BootCamp/IRONHACK/Netflix_vs_disney/image/Peli6.png"
peli7_path = "C:/Users/thaty/OneDrive/Escritorio/BootCamp/IRONHACK/Netflix_vs_disney/image/Peli7.png"
peli8_path = "C:/Users/thaty/OneDrive/Escritorio/BootCamp/IRONHACK/Netflix_vs_disney/image/Peli8.png"
peli9_path = "C:/Users/thaty/OneDrive/Escritorio/BootCamp/IRONHACK/Netflix_vs_disney/image/Peli9.png"
peli10_path = "C:/Users/thaty/OneDrive/Escritorio/BootCamp/IRONHACK/Netflix_vs_disney/image/Peli10.png"

# Función para verificar y mostrar imágenes
def display_image(column, file_path, caption):
    if os.path.exists(file_path):  # Verifica si el archivo existe
        column.image(file_path, caption=caption, use_column_width=True)
    else:
        column.write(f"Imagen {file_path} no encontrada")

# Muestra los logos uno al lado del otro usando 5 columnas
col1, col2, col3, col4, col5 = st.columns(5)

display_image(col1, peli6_path, 'Peli6')
display_image(col2, peli7_path, 'Peli7')
display_image(col3, peli8_path, 'Peli8')
display_image(col4, peli9_path, 'Peli9')
display_image(col5, peli10_path, 'Peli10')

st.write("")
st.write("")

st.subheader("Comprobamos que la clasificación en Disney + nos arroja un resultado diferente, ya que tiene una clasificación mas familiar, centrándose en la navidad, ya sea a través de una historia navideña, personajes navideños o música navideña.")

st.write("")
st.write("")
st.title("Análisis de reseñas:")
st.subheader("Como resultado del web scrapping hemos obtenido las reseñas de 2075 títulos de Disney y Netflix. Después hemos realizado un merge con el dataframe original para tener la información de esos títulos con valoración. Analizando estos datos por plataforma, obtenemos la media de cada una, su desviación estándar y su nota en contenidos infantiles o para todos los públicos.")

# Ruta de la imagen (ajusta la ruta según sea necesario)
image_path2 = "C:/Users/thaty/OneDrive/Escritorio/BootCamp/IRONHACK/Netflix_vs_disney/image/reseñas.png"


# Crea las 3 columnas
col1, col2, col3 = st.columns(3)

# Verificación y muestra de imagen en la segunda columna
if os.path.exists(image_path2):
    with col2:
        st.image(image_path2, caption='Reseñas', use_column_width=True, width=150)
else:
    st.write(f"Imagen {image_path2} no encontrada")

st.write("")

# Crear dos columnas en Streamlit
col1, col2 = st.columns(2)

# Generar y mostrar las gráficas en las columnas correspondientes
with col1:
    st.markdown(
    """
    <h1 style='color: #006E99;'>DISNEY +:</h1>
    """,
    unsafe_allow_html=True
)
    st.subheader("➤Media: 87.91")
    st.subheader("➤Desviación estándar: 8.64")
    st.subheader("➤Media para contenidos infantiles: 89.13")

with col2:
    st.markdown(
    """
    <h1 style='color: #E50914;'>NETFLIX:</h1>
    """,
    unsafe_allow_html=True
)
    st.subheader("➤Media: 80.92")
    st.subheader("➤Desviación estándar: 19.63")
    st.subheader("➤Media para contenidos infantiles: 88.70")

st.write("")   
st.write("")
st.write("")
st.title("Conclusiones del análisis:")
st.subheader("1. Disney+: foco en la calidad uniforme y contenidos familiares")
st.markdown("Disney+ ha consolidado su éxito y diferenciación con un catálogo centrado en **contenido familiar** y **animación**. Ofreciendo una **calidad más uniforme**, como demuestra su menor desviación estándar en las puntuaciones de Rotten Tomatoes. Además, de consolidarse como una **plataforma segura para todos los públicos**, al no tener contenidos solo para adultos.")

# Ruta de la imagen (ajusta la ruta según sea necesario)
disney1_path = "C:/Users/thaty/OneDrive/Escritorio/BootCamp/IRONHACK/Netflix_vs_disney/image/disney1.png"


# Crea las 3 columnas
col1, col2, col3 = st.columns(3)

# Verificación y muestra de imagen en la segunda columna
if os.path.exists(disney1_path):
    with col2:
        st.image(disney1_path, caption='disney1', use_column_width=True, width=150)
else:
    st.write(f"Imagen {disney1_path} no encontrada")


st.subheader("2. Netflix: diversidad y experimentación")
st.markdown("➤Por otro lado, Netflix ofrece una mayor **diversidad de géneros** y un enfoque más amplio hacia distintos públicos: niños, adolescentes o adultos.")
st.markdown("➤Esta estrategia también refleja una **mayor dispersión en la calidad** de sus contenidos, como demuestra su alta desviación estándar en las notas de sus contenidos.")

 # Ruta de la imagen (ajusta la ruta según sea necesario)
netflix1_path = "C:/Users/thaty/OneDrive/Escritorio/BootCamp/IRONHACK/Netflix_vs_disney/image/netflix1.png"


# Crea las 3 columnas
col1, col2, col3 = st.columns(3)

# Verificación y muestra de imagen en la segunda columna
if os.path.exists(netflix1_path):
    with col2:
        st.image(netflix1_path, caption='netflix1', use_column_width=True, width=150)
else:
    st.write(f"Imagen {netflix1_path} no encontrada")

st.subheader("3. El poder del catálogo como reflejo de la propuesta de valor")
st.markdown("➤El catálogo de cada plataforma actúa como **un reflejo tangible de su valor diferencial**. Disney+ no se limita a ofrecer entretenimiento sin más, sino un **entretenimiento familiar** y su estrategia de contenido respalda su identidad. Contribuyendo a una imagen de marca y reputación consistentes.")
st.markdown("➤Netflix ha priorizado la **diversificación** y se ve cómo su catálogo se enfoca en la amplitud de géneros y segmentos de público. Su capacidad para llegar también a adolescentes y adultos, así como su experimentación con contenido, es lo que la mantiene como la plataforma líder en términos de cuota de mercado.")

# Ruta de la imagen (ajusta la ruta según sea necesario)
mixto1_path = "C:/Users/thaty/OneDrive/Escritorio/BootCamp/IRONHACK/Netflix_vs_disney/image/mixto1.png"


# Crea las 3 columnas
col1, col2, col3 = st.columns(3)

# Verificación y muestra de imagen en la segunda columna
if os.path.exists(mixto1_path):
    with col2:
        st.image(mixto1_path, caption='mixto1', use_column_width=True, width=150)
else:
    st.write(f"Imagen {mixto1_path} no encontrada")


st.subheader("4. Diferenciación estratégica: contenido clásico vs. títulos modernos")
st.markdown("Disney+ se apoya en su extenso catálogo de **clásicos y franquicias** que generan un gran atractivo. Netflix, por su parte, se ha destacado por su enfoque en títulos **originales, modernos y variados**. Los clusters extraídos reflejan claramente esta diferencia.")

# Ruta de la imagen (ajusta la ruta según sea necesario)
mixto2_path = "C:/Users/thaty/OneDrive/Escritorio/BootCamp/IRONHACK/Netflix_vs_disney/image/mixto2.png"


# Crea las 3 columnas
col1, col2, col3 = st.columns(3)

# Verificación y muestra de imagen en la segunda columna
if os.path.exists(mixto2_path):
    with col2:
        st.image(mixto2_path, caption='mixto2', use_column_width=True, width=150)
else:
    st.write(f"Imagen {mixto2_path} no encontrada")

st.subheader("5. Conclusión final: el valor intangible reflejado en lo tangible")
st.markdown("Aunque la **propuesta de valor** de una plataforma es algo intangible, nuestro análisis muestra cómo este valor se refleja directamente en **el catálogo**, la esencia de cualquier plataforma de streaming.")
st.markdown("La apuesta de Disney+ por la **calidad, seguridad y familiaridad** le ha permitido diferenciarse y alcanzar la rentabilidad en un tiempo récord, mientras que Netflix sigue siendo sinónimo de **variedad y novedad**, consolidando su posición de líder.")

# Ruta de la imagen (ajusta la ruta según sea necesario)
mixto3_path = "C:/Users/thaty/OneDrive/Escritorio/BootCamp/IRONHACK/Netflix_vs_disney/image/mixto3.png"


# Crea las 3 columnas
col1, col2, col3 = st.columns(3)

# Verificación y muestra de imagen en la segunda columna
if os.path.exists(mixto3_path):
    with col2:
        st.image(mixto3_path, caption='mixto3', use_column_width=True, width=150)
else:
    st.write(f"Imagen {mixto3_path} no encontrada")

st.write("")   
st.write("")
st.write("")
st.title("Conclusiones técnicas:")
st.subheader("1.Mejora en K-Means: ")
st.markdown("Nos hemos aventurado de forma **autodidacta** en el Machine Learning. ")
st.markdown("Nos hemos quedado con el **K-Means** por su simplicidad, aunque también hemos probado el método **Elbow**.")
st.markdown("Una futura mejora sería probar los distintos modelos para ver cuál es el más ajustado y tiene menos dispersión en los resultados de clasificación.")



# Ruta de la imagen (ajusta la ruta según sea necesario)
kmeans_path = "C:/Users/thaty/OneDrive/Escritorio/BootCamp/IRONHACK/Netflix_vs_disney/image/k-means.png"


# Crea las 3 columnas
col1, col2, col3 = st.columns(3)

# Verificación y muestra de imagen en la segunda columna
if os.path.exists(kmeans_path):
    with col2:
        st.image(kmeans_path, caption='k-mean', use_column_width=True, width=150)
else:
    st.write(f"Imagen {kmeans_path} no encontrada")

st.subheader("2.Organización del código: ")
st.markdown("Dividir el código en archivos habría mejorado la limpieza y estructura del proyecto, facilitando su comprensión y mantenimiento.")

# Ruta de la imagen (ajusta la ruta según sea necesario)
organizacion_path = "C:/Users/thaty/OneDrive/Escritorio/BootCamp/IRONHACK/Netflix_vs_disney/image/organizacion.png"


# Crea las 3 columnas
col1, col2, col3 = st.columns(3)

# Verificación y muestra de imagen en la segunda columna
if os.path.exists(organizacion_path):
    with col2:
        st.image(organizacion_path, caption='k-mean', use_column_width=True, width=150)
else:
    st.write(f"Imagen {organizacion_path} no encontrada")

st.subheader("3.Problemas con Web Scraping: ")
st.markdown("Inicialmente probamos a extraer las puntuaciones de la **web de IMBd**, no conseguimos que funcionase del todo y el proceso era bastante complejo. ")
st.markdown("**La API oficial de IMBd** es parte de AWS y necesitábamos pedir permiso para su uso (que tardaría un tiempo en procesarse que no teníamos).")
st.markdown("Encontramos una **API no oficial de IMBd**, intentamos usarla, pero daba fallos y su configuración era muy compleja al haber sido creada por un usuario.")
st.markdown("Finalmente nos quedamos con el web scraping en **Rotten Tomatoes**, una página de reseñas mucho más sencilla. Aunque fuimos **bloqueados** tras obtener solo el 20% de los datos (2075 títulos).")
st.markdown("Próximamente probaremos una **API no oficial de IMDd** que nos han recomendado más sencilla para completar el análisis, ya hemos obtenido el permiso de uso.")



# Ruta de la imagen (ajusta la ruta según sea necesario)
web_path = "C:/Users/thaty/OneDrive/Escritorio/BootCamp/IRONHACK/Netflix_vs_disney/image/web_scrap.png"


# Crea las 3 columnas
col1, col2, col3 = st.columns(3)

# Verificación y muestra de imagen en la segunda columna
if os.path.exists(web_path):
    with col2:
        st.image(web_path, caption='k-mean', use_column_width=True, width=150)
else:
    st.write(f"Imagen {web_path} no encontrada")

st.write("")   
st.write("")
st.write("")

st.subheader("Queremos agradecer el proyecto a Santiago por sus explicaciones precisas y entendibles, a Toño por encender hogueras sin chimeneas, y forzarnos a construirlas, y a Nicolas por avivar las hogueras de Toño con mas leña.")

st.title("MUCHAS GRACIAS!")

# Ruta de la imagen (ajusta la ruta según sea necesario)
end_path = "C:/Users/thaty/OneDrive/Escritorio/BootCamp/IRONHACK/Netflix_vs_disney/image/fin.png"


# Crea las 3 columnas
col1, col2, col3 = st.columns(3)

# Verificación y muestra de imagen en la segunda columna
if os.path.exists(end_path):
    with col2:
        st.image(end_path, caption='k-mean', use_column_width=True, width=150)
else:
    st.write(f"Imagen {end_path} no encontrada")