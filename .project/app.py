"venv\Scripts\activate"
"install pandas as pd"
"install plotly-express as px"
"install streamlit as st"
car_data = pd.read_csv("vehicles_us.csv")
hist_button = st.button ("Construir histograma")
if hist_button:
    st.write("Creacion de un histograma para el conjunto de datos de anucios de venta de coches")
    fig=px.hisotgrama(car_data, x="odometer")
    st.plotly_chart(fig, use_container_width=True)

scatter_plot = st.button("Construir grafica de dispersion")
if scatter_plot:
    st.write("Creacion de una grafica de dispersion para el conjunto de datos")
    fig2=px.scatter(car_data, x="odometer", y="price")
    st.plotly_chart(fig2, use_container_width=True)


