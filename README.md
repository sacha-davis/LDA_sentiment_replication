# LDA Sentiment Replication — CMPUT 501 Term Project
By: Sarah Davis and Henry Tang

The objective of this project is to replicate the work published by Onan et al. in 
*LDA-based Topic Modelling in Text Sentiment Classification: An Empirical Analysis* (2016).

## Introduction


## Installation and execution

1. Activate virtual environment and install dependencies 
	```bash
    python3 -m venv venv
 
    venv\Scripts\activate.bat  # windows
    source venv/bin/activate  # unix
 
    pip install -r requirements.txt
	```
 
2. Unzip data files
	```bash
    cd data
    tar -xf multi-domain-sentiment.arff.zip
    tar -xf IrishEconomicSentiment.arff.zip
    cd ..
	```
 
3. Create *document x term* .csv from .arff for each dataset
	```bash
    python src\arff_convert.py data\multi-domain-sentiment.arff data\multidomain_df.csv
    python src\arff_convert.py data\IrishEconomicSentiment.arff data\irish_df.csv
	```
 
 ## Data