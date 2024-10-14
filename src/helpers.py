import pickle


def load_model(model_path):
    """Load a saved model from a pickle file."""
    with open(model_path, 'rb') as file:
        model = pickle.load(file)
    return model


def preprocess_data(data):
    """Preprocess user input data (e.g., handle missing values, scaling)."""
    # Add any preprocessing logic here (e.g., handling NaNs, etc.)
    return data
