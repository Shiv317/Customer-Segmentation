from setuptools import setup

# Read the contents of the README file
with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()
SRC_repo = 'src'
setup(
    name="customer_segmentation_app",  # Name of your project
    version="0.1.0",  # Initial version
    author="Shivail Anand",  # Your name or organization
    author_email="shivailanand2003@gmail.com",  # Your contact email
    # Short project description
    description="A Streamlit app for customer segmentation using KMeans clustering and PCA",
    long_description=long_description,  # A detailed description from README
    long_description_content_type="text/markdown",  # README format
    # Link to your project (GitHub, etc.)
    url="https://github.com/shiv317/customer-segmentation-app",
    packages=[SRC_repo],  # Automatically find all packages
    install_requires=[
        "streamlit>=1.0",  # Streamlit as a required dependency
        "numpy>=1.18.5",  # Numpy for array handling
        "pandas>=1.0",  # Pandas for data handling
        "scikit-learn>=0.24.1",  # Scikit-learn for machine learning
        "matplotlib>=3.1",  # Matplotlib for visualization
        "seaborn>=0.11",  # Seaborn for enhanced visualizations
    ],
    classifiers=[
        "Programming Language :: Python :: 3",  # Supported Python versions
        "License :: OSI Approved :: MIT License",  # License type
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",  # Specify the minimum Python version
    entry_points={  # Optional entry points for command line tools
        "console_scripts": [
            # Replace 'app' with the actual Python file name
            "customer-segmentation-app=app:main",
        ],
    },
)
