from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA


def scale_data(scaler, data):
    """Scale the input data using a previously fitted scaler."""
    return scaler.transform(data)


def apply_pca(pca, data):
    """Apply PCA to reduce dimensions."""
    return pca.transform(data)

# Example of initializing and using the functions


def preprocess_and_reduce(data):
    """Example function to demonstrate scaling and PCA."""
    scaler = StandardScaler()
    pca = PCA(n_components=3)

    # Fit and transform the data with the scaler and PCA
    scaled_data = scaler.fit_transform(data)
    pca_data = pca.fit_transform(scaled_data)

    return pca_data
