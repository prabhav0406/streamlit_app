# -*- coding: utf-8 -*-
"""
Created on Mon Nov 11 14:57:08 2024

@author: prabh
"""

import streamlit as st
import pandas as pd
import seaborn as sns

# 1. Title and Subheader
st.title("Data Analysis")
st.subheader("Data Analysis using python and web-app")

# 2. Upload dataset
upload = st.file_uploader("Upload your dataset in csv format")

if upload is not None:
    data = pd.read_csv(upload)
    
# 3. Show dataset
# if st.checkbox("Preview Dataset"):
#    if st.button("Head"):
#        st.write(data.head())
#    if st.button("Tail"):
#        st.write(data.tail())
        
if upload is not None:
    if st.checkbox("Preview Dataset"):
        if st.button("Head"):
            st.write(data.head())
        if st.button("Tail"):
            st.write(data.tail())
            
# 4. Check datatyoe of the each columns
if upload is not None:
    if st.checkbox("Datatype of the each columns"):
        st.text("daratypes")
        st.write(data.dtypes)

# 5. Find the shape of the dataset
if upload is not None:
    data_shape = st.radio("What dimension do you want to check?", ('Rows','Columns'))
    
    if data_shape == 'Rows':
        st.text("Number of Rows")
        st.write(data.shape[0])
    if data_shape == 'Columns':
        st.text("Number of columns")
        st.write(data.shape[1])

# 6. Find null values present in the dataset or not
if upload is not None:
    st.text("Null values in the dataset")
    test = data.isnull().values.any()
    
    if test == True:
        if st.checkbox("Null values are there in the dataset"):
            st.text("Yes")
            sns.heatmap(data.isnull())
            st.pyplot()
    else:
        st.success("Congratulation! There is no missing value")
        
# 7. Handle duplicate values in the dataset
if upload is not None:
    test = data.duplicated().any() # nhi hoga to false
    
    if test == True:
        st.warning("The dataset contains some duplicate values")
        dup = st.selectbox("Do you want to remove duplicate values?",\
                           ('Select One', 'Yes', 'No'))
        if dup == 'Yes':
            data = data.drop_duplicates()
            st.text("Duplicated rows are removed")
        if dup == 'No':
            st.text("Okay Thank You")

# 8. Get overall statistics of the dataset
if upload is not None:
    if st.checkbox("Summary of the Dataset"):
        st.write(data.describe(include="all"))

# 9. About section
if st.button("About App"):
    st.text("Built with streamlit")
    st.text("Thanks to streamlit")
    
# 10. By
if st.checkbox("By"):
    st.success("Prabhav Singh")





















