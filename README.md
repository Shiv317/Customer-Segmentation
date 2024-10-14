# Customer Segmentation Streamlit App

This is a **Streamlit** web application that allows users to perform **customer segmentation** using **KMeans clustering** and **PCA (Principal Component Analysis)**. The app allows users to input customer data and predicts the segment or cluster to which the customer belongs.

## Project Overview

Customer segmentation is a crucial aspect of targeted marketing and customer relationship management (CRM). This project leverages machine learning (KMeans clustering) to categorize customers into segments based on their behavior, such as spending habits, family size, and recency of purchases.

The application:
- Takes customer data as input.
- Applies scaling and PCA to reduce the dimensionality of the data.
- Predicts the customer’s cluster using a pre-trained **KMeans** model.

## Features

- **Input Interface**: Users can input various customer features such as income, recency, age, and spending.
- **Clustering**: The app uses **KMeans clustering** to predict which customer segment the input data belongs to.
- **Dimensionality Reduction**: Uses **PCA** to reduce the complexity of the data.
- **Real-time Predictions**: Provides real-time cluster predictions as users modify their inputs.

## Technologies Used

- **Python**
- **Streamlit**: To build the web application interface.
- **scikit-learn**: For machine learning models (KMeans clustering, PCA, and scaling).
- **pandas**: For data handling and processing.
- **numpy**: For numerical computations.
- **matplotlib** and **seaborn**: For data visualization.

## Setup Instructions

Follow these steps to get the app running locally on your machine.

### Prerequisites

- **Python 3.6+**
- **Virtual environment** (optional but recommended)

### Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/shiv317/customer-segmentation-app.git
    ```

2. Navigate to the project directory:

    ```bash
    cd customer-segmentation-app
    ```

3. Create a virtual environment (optional but recommended):

    ```bash
    python -m venv myenv
    source myenv/bin/activate  # For Windows use: myenv\Scripts\activate
    ```

4. Install the required dependencies:

    ```bash
    pip install -r requirements.txt
    ```

5. Run the Streamlit app:

    ```bash
    streamlit run app.py
    ```

This will launch the Streamlit app, which you can access via your web browser at `http://localhost:8501`.

## How to Use the App

1. **Enter customer data**: Provide values for features like income, recency, age, family size, and total spending.
2. **Real-time prediction**: As you input or modify the customer data, the app will predict the customer’s segment in real time.
3. **View Results**: The app will display the predicted cluster/segment that the customer belongs to.

## Model Details

- **KMeans Clustering**: The model was trained on a dataset containing customer behavioral data such as income, age, and spending. The clustering algorithm groups similar customers into segments based on this data.
- **PCA**: PCA was used to reduce the number of features while retaining important information about customer behavior.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.

## Contact

For any questions or collaboration inquiries, please reach out to:

- **Shivail Anand**: shivailanand2003@gmail.com
- **GitHub**: [shiv317](https://github.com/shiv317)