import streamlit as st

import matplotlib.pyplot as plt
import matplotlib
import seaborn as sns
import pandas as pd
import streamlit.components.v1 as stc
from eda_app import run_eda_app
from ml_app import run_ml_app






menu = ["Home", "EDA", "ML", "Info"]
opcion = st.sidebar.selectbox("Menu", menu)
st.title("App para la detección temprana de DM")
if opcion == "Home":
    st.subheader("Home")
    st.subheader("App para la detección temprana de DM")
    st.write("""
    	Dataset que contiene señales y síntomas que pueden indicar diabetes o posibilidad de diabetes.
    	""")
    st.subheader("Fuente de datos")
    user=st.code("https://archive.ics.uci.edu/ml/datasets/Early+stage+diabetes+risk+prediction")
    st.subheader("Contenidos de la App")
    texto=st.text_area(" ",''' 
     -EDA Section: Análisis exploratorio de los datos
     -ML Section: Predicción de Diabetes basada en ML (Machine Learning)
     ''', height=100)
elif opcion == "EDA":
	run_eda_app()
elif opcion == "ML":
	run_ml_app()
else:
	st.subheader("Info")
	st.text("MBIT, Proyecto de consolidación, librería Streamlit.")
	stc.iframe("https://www.mbitschool.com/",
		height=600,width=600,
		scrolling=True)    	








#run_eda_app()
#run_ml_app()




