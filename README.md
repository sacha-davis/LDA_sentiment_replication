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
 
2. Untar data
	```bash
    cd data
    tar xvf processed_acl.tar.gz
    cd ..
	```
 
3. Parse input data
	```bash
    python parse_data.py data\processed_acl
	```
 
 ## Data