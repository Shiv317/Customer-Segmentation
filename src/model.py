def predict_cluster(model, data):
    """Predict the cluster for the input data using the KMeans model."""
    return model.predict(data)
