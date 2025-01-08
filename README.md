# Web-App-Using-Streamlit-
An interactive Streamlit web app that predicts diamond prices based on carat weight using machine learning algorithms


**Diamond Price Prediction Web App**

This is a Streamlit web application that predicts diamond prices based on the carat weight. The app uses a Linear Regression model to predict the price of a diamond and displays the results interactively.


Features

**Home Page**:

  Displays the dataset information, including shape and statistics of the diamond dataset.
  
  Interactive graphs, such as scatter plots, bar charts, and histograms, for visual data analysis.

**Price Prediction:**

  Input the carat value of a diamond to get its predicted price.
  
  The app uses a Linear Regression model trained on the dataset to predict the price based on the entered carat value.
  
  Price prediction is displayed with the ₹ (Rupee) symbol.

**Requirements**

    Python 3.x
    Streamlit
    Pandas
    NumPy
    Matplotlib
    Seaborn
    Scikit-learn


**Functionality**

**1. Home Page:**

  **The Home page displays the shape of the dataset and allows users to view:**
  
  **Tabular Data:** Displays the first 150 rows of the diamond dataset.
  
  **Statistical Summary:** Shows the descriptive statistics of the dataset.
  
  **Correlation Graph:** Visualizes the correlation between numerical variables in the dataset.
  
  **Various Graphs:** Users can choose from different types of graphs such as scatter plot, bar graph, histogram, violin plot, and pie 
   chart to visualize the data.

**2. Prediction Page:**

  Users can input the carat value of a diamond, and the app predicts its price using a Linear Regression model.
  
  The predicted price is displayed with the ₹ (Rupee) symbol.


**Data**

The app uses the diamonds dataset, which contains various attributes of diamonds, including:

  **carat:** Weight of the diamond.
  **price:** Price of the diamond.
  **cut:** Quality of the cut (Fair, Good, Ideal, Premium, Ideal).
  **color:** Diamond color rating (D, E, F, etc.).
  **clarity:** Clarity of the diamond (SI1, VS2, etc.).


**Future Enhancements**

  Adding more machine learning models for price prediction.
  
  Enhancing the data visualizations for better user experience.
  
  Deploying the app to cloud platforms like Streamlit Cloud.
