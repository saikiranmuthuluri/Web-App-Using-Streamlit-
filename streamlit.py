import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


# Title
st.title(" Web Application for Predicting Diamond Prices Using Streamlit ")

# Image
st.image("Streamlit background image.webp", width=500)

st.title("Exploring the Diamond Dataset")

# Load dataset
data = sns.load_dataset("diamonds")
st.write("Shape of a dataset",data.shape)

# Sidebar menu
menu = st.sidebar.radio("Menu", ["Home", "Price Prediction"])

if menu == "Home":
    st.image("Diamond image.jpg", width=450)
    st.header("Tabular Data Of a Diamond")
    if st.checkbox("Tabular Data"):
        st.table(data.head(150))
    st.header("Statistical Summary of a Dataset")    
    if st.checkbox("Statistics"): 
        st.table(data.describe())
    
    # Correlation Graph
    st.header("Correlation Graph")
    numeric_data = data.select_dtypes(include=['number'])
    fig, ax = plt.subplots(figsize=(5, 2.5))
    sns.heatmap(numeric_data.corr(), annot=True, cmap="coolwarm")
    st.pyplot(fig)

    # Graphs
    st.title("Graphs")  
    Graphs = st.selectbox("Choose the Graph",["Select a Graph","Scatter Plot", "Bar Graph", "Histogram","Pie Chart","Violin Plot","Box Plot"]) 
    
    if Graphs == "Scatter Plot":
        value = st.slider("Filter data using carat", 0, 6)
        data_filtered = data.loc[data["carat"] >= value]
        fig, ax = plt.subplots(figsize=(10, 5))
        sns.scatterplot(data=data_filtered, x="carat", y="price", hue="cut")
        st.pyplot(fig)

    if Graphs == "Bar Graph":
        fig, ax = plt.subplots(figsize=(4.2, 2))
        sns.barplot(x="cut", y=data.cut.index, data=data)
        st.pyplot(fig)    

    if Graphs == "Histogram":
        fig, ax = plt.subplots(figsize=(4, 3))
        sns.histplot(data.price, kde=True, ax=ax) 
        st.pyplot(fig)

    if Graphs == "Pie Chart":
            st.header("Pie Chart for Diamond Cuts")
            pie_data = data["cut"].value_counts()
            fig, ax = plt.subplots(figsize=(5.5,2.5))
            ax.pie(pie_data, labels=pie_data.index, autopct='%1.1f%%', startangle=90, colors=sns.color_palette("Set3", n_colors=len(pie_data)))
            ax.axis('equal')
            st.pyplot(fig) 

    if Graphs == "Violin Plot":
        st.header("Violin Plot for Diamond Prices")
        fig, ax = plt.subplots(figsize=(5.5,2.5,))
        sns.violinplot(x="cut", y="price", data=data, ax=ax)
        st.pyplot(fig)   

    if Graphs == "Box Plot":
        st.header("Box Plot for Diamond Prices")
        fig, ax = plt.subplots(figsize=(5.5,2.5))
        sns.boxplot(x="cut", y="price", data=data, ax=ax)
        st.pyplot(fig)    


elif menu == "Price Prediction":
    st.title("Price Prediction of a Diamond")   

    # Linear Regression for Price Prediction
    from sklearn.linear_model import LinearRegression 
    lr = LinearRegression()
    X = np.array(data['carat']).reshape(-1, 1)
    y = np.array(data['price']).reshape(-1, 1)
    lr.fit(X, y)  
    
    value = st.number_input("Carat", 0.20, 5.01, step=0.15)
    value = np.array(value).reshape(1, -1)
    Prediction = lr.predict(value)[0]
    
    if st.button("Price Prediction (₹)"):
        st.write(f"{Prediction}")
