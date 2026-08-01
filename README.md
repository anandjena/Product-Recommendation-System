# Product Recommendation System

A simple **Product Recommendation System** built with **Python** and **Streamlit** that recommends similar products based on a precomputed similarity matrix.

## Features

* Interactive web interface using Streamlit
* Select a product from a dropdown menu
* Recommends the top 5 most similar products
* Fast recommendations using a precomputed similarity matrix
* Lightweight and easy to run locally

## Project Structure

```text
Product-Recommendation-System/
│
├── app.py                  # Main Streamlit application
├── product.pickle          # Product dataset
├── similarity.joblib       # Precomputed similarity matrix
├── requirements.txt        # Project dependencies
└── README.md               # Project documentation
```

## Technologies Used

* Python
* Streamlit
* Pandas
* Pickle
* Joblib

## Installation

### 1. Clone the repository

```bash
git clone https://github.com/anandjena/Product-Recommend-System.git
cd product-recommendation-system
```

### 2. Create a virtual environment (Optional)

**Windows**

```bash
python -m venv venv
venv\Scripts\activate
```

**Linux / macOS**

```bash
python -m venv venv
source venv/bin/activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

## Run the Application

Start the Streamlit application:

```bash
streamlit run app.py
```

The application will open in your browser at:

```
http://localhost:8501
```

## How It Works

1. The application loads the product dataset from `product.pickle`.
2. It loads the similarity matrix from `similarity.joblib`.
3. The user selects a product from the dropdown list.
4. When the **Recommend** button is clicked:

   * The selected product's index is found.
   * Similarity scores are retrieved.
   * The products are sorted by similarity.
   * The top 5 most similar products are displayed.

## Recommendation Algorithm

The recommendation function:

* Finds the selected product's index.
* Retrieves similarity scores from the similarity matrix.
* Sorts products in descending order of similarity.
* Excludes the selected product itself.
* Returns the top five recommended products.

## Requirements

Example `requirements.txt`

```text
streamlit
pandas
joblib
```

