
# PROYECTO DE CONSOLIDACION STREAMLIT: FUNCION eda_app.py

import matplotlib.pyplot as plt
import matplotlib
import seaborn as sns
import pandas as pd
import plotly.express as px
import streamlit as st



# Datos


#st.subheader("SECCIÓN EDA")



# datos


df = pd.read_csv("C:/Users/jeann/masterdc/PROTOTIPADOVIZ/JeanethConsolidacion/data/diabetes_data_upload.csv")
dfClean = pd.read_csv("C:/Users/jeann/masterdc/PROTOTIPADOVIZ/JeanethConsolidacion/data/diabetes_data_upload_clean.csv")
dfFreq = pd.read_csv("C:/Users/jeann/masterdc/PROTOTIPADOVIZ/JeanethConsolidacion/data/freqdist_of_age_data.csv")
	
# Función principal que emplearemos en la APP

def run_eda_app():
	submenu = ["Descriptivo","Gráficos"]
	submenu2 = st.sidebar.selectbox("SubMenu", submenu)
	if submenu2 == "Descriptivo":
		st.subheader("Analisis descriptivo")
		st.dataframe(df)
		with st.expander("Tipos de datos"):
			st.dataframe(df.dtypes.astype(str))
		with st.expander("Resumen descriptivo"):
			st.dataframe(dfClean.describe())
		with st.expander("Distribución por género (Gender)"):
			st.dataframe(df["Gender"].value_counts())
		with st.expander("Distribución por clase/label (Class)"):
			st.dataframe(df["class"].value_counts())
	else:
		st.subheader("Análisis gráfico")
		col1,col2 = st.columns([2,1])
		with col1:
			with st.expander("Gráfico de distribución por género (Gender)"):
				figura1 = plt.figure()
				sns.countplot(df['Gender'])
				st.pyplot(figura1)
			with st.expander("Gráfico de distribución por clase (Class)"):
				figura2 = plt.figure()
				sns.countplot(x=df['Gender'])
				st.pyplot(figura2)
		with col2:
			with st.expander("Distribución por Gender"):
				st.dataframe(df["Gender"].value_counts())
			with st.expander("Distribución por Class"):
				st.dataframe(df["class"].value_counts())
		with st.expander("Frequency Dist Plot of Age"):
			figura3 = plt.figure()
			sns.barplot(x=dfFreq["Age"], y=dfFreq["count"], data=dfFreq)
			plt.ylabel("Counts")
			plt.title("Conteo de frecuencia por Edad")
			st.pyplot(figura3)
		with st.expander("Outlier Detection Plot"):
			figura4 = plt.figure()
			sns.boxplot(x=df["Gender"],y=df["Age"])
			st.pyplot(figura4)
		with st.expander("Correlation Plot"):
			matrizCorr = dfClean.corr()
			figura5 = plt.figure(figsize=(30,25))
			sns.heatmap(matrizCorr,annot=True)
			st.pyplot(figura5)


