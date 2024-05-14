# User Classification Using Enron Email Dataset

This project aims to predict the sender of emails within the Enron email dataset, which contains 500,000 emails from 150 users. Leveraging advanced machine learning and deep learning techniques, the project seeks to identify unique patterns in writing styles, grammatical differences, and overall sentiment to build a precise predictive model for sender classification.

## Project Overview

The primary goal of this project is to accurately predict email senders by leveraging distinct patterns found in the dataset. By focusing on individualized features such as writing habits and emotional tone, the project contributes to the broader field of sender classification and pattern recognition in textual data.

## Key Components

### Data Preparation and Cleaning

- **Data Conversion**: Emails were converted from text files to CSV format.
- **Cleaning**: Addressed missing values, removed duplicates, standardized text encoding, and optimized the dataset by eliminating redundant content. Text data was converted to lowercase, punctuation was removed, and stop words were eliminated.

### Feature Extraction

- **TF-IDF and Count Vectorization**: Transformed text data into numerical features using TF-IDF to capture word importance and count vectorization to represent word frequency.
- **Sentiment Analysis**: Performed using TextBlob and VADER to categorize emails as positive, negative, or neutral.

### Machine Learning Models

- **Multinomial Naïve Bayes (MNB)**
- **Random Forest Classifier**
- **Support Vector Machine (SVM) with a linear kernel**
- **Long Short-Term Memory (LSTM) Networks**

The LSTM model achieved the highest accuracy at 97.64%, effectively capturing sequential text patterns. The Random Forest and SVM models also performed well, with notable differences based on feature extraction methods.

## Results

- **LSTM Model**: Achieved the highest accuracy of 97.64%.
- **Random Forest Classifier**: Showed high accuracy with TF-IDF vectorization.
- **SVM**: Effective with high-dimensional data.
- **MNB**: Provided valuable insights despite slightly lower accuracy.

## Conclusions

The project highlighted the importance of text preprocessing and feature engineering in enhancing model performance. The deep learning approach, particularly with LSTM networks, proved highly effective for sender classification and textual data pattern recognition.

## Getting Started

Follow these steps to set up and run the project:

You will also need to install the required Python libraries, which are listed in the `requirements.txt` file.

### 1. Clone the Repository:

```bash
git clone https://https://github.com/MeryHarikaG/enron-email-classification.git
cd enron-email-classification
```

### 2. Create a virtual environment:

```
python -m venv venv
```

### 3. Activate the virtual environment:

- For Windows:

```
venv\Scripts\activate
```

- For Mac:

```
source venv/bin/activate
```

### 4. Install Required Packages:

```
pip install -r requirements.txt
```

### 5. Run the data preprocessing script to clean and prepare the dataset:

```
python utility.py
```

### 6. Run the Jupyter Notebook:

```
jupyter notebook EnronEmailClassification_P21.ipynb
```

This will open the Jupyter Notebook interface in your web browser. You can then run the cells in the notebook to execute the project.

## Future Work

- **Advanced Models**: Explore more advanced models like transformers.
- **Dataset Expansion**: Use more computational resources to expand the dataset.

For any questions or further assistance, please feel free to open an issue on the GitHub repository.
