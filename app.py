import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
from src import load_model, predict_cluster

# Load pre-trained KMeans model
kmeans_model = load_model('kmeans_model.pkl')

# Title for the Streamlit app
st.title("Customer Segmentation Prediction")

# Input form for user data
st.subheader("Enter Customer Data:")

# Collect the three features for input
income = st.number_input("Income", min_value=0, max_value=1000000, value=50000)
age = st.number_input("Age", min_value=18, max_value=100, value=35)
rfm_score = st.number_input(
    "RFM Score", min_value=0, max_value=1000, value=600)

# Combine input features into an array
input_features = np.array([[income, age, rfm_score]])

# Add a button to predict cluster
if st.button("Predict Cluster"):
    predicted_cluster = predict_cluster(kmeans_model, input_features)

    # Display the predicted cluster
    st.write(
        f"The predicted cluster for the customer is: {predicted_cluster[0]}")

    # Generate a simple scatter plot to visualize cluster distribution
    st.subheader("Cluster Distribution")

    # Generate some sample data for visualization (you can use real cluster centers if available)
    cluster_centers = kmeans_model.cluster_centers_
    income_data = cluster_centers[:, 0]
    age_data = cluster_centers[:, 1]
    rfm_data = cluster_centers[:, 2]

    # Create scatter plot
    fig, ax = plt.subplots()
    scatter = ax.scatter(income_data, age_data,
                         c=rfm_data, cmap='viridis', s=200)

    # Add color bar
    cbar = plt.colorbar(scatter)
    cbar.set_label('RFM Score')

    # Set axis labels and title
    ax.set_xlabel('Income')
    ax.set_ylabel('Age')
    ax.set_title('Cluster Centers')

    # Show plot in Streamlit
    st.pyplot(fig)
