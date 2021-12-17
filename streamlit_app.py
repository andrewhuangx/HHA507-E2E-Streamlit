# -*- coding: utf-8 -*-
"""
Created on Wed Dec 16 15:05:10 2021

@author: andre
"""

## Import the Required Packages

import streamlit as st
import pandas as pd
import numpy as np
import time

## Load in CSVs 
@st.cache
def load_hospitals():
   hospital = pd.read_csv('https://raw.githubusercontent.com/hantswilliams/AHI_DataSci_507/main/Deployment_Streamlit/hospital_info.csv')
   return hospital

@st.cache
def load_inpatient():
    inpatient = pd.read_csv('https://raw.githubusercontent.com/hantswilliams/AHI_DataSci_507/main/Deployment_Streamlit/inpatient_2015.csv')
    return inpatient

@st.cache
def load_outpatient():
    outpatient = pd.read_csv('https://raw.githubusercontent.com/hantswilliams/AHI_DataSci_507/main/Deployment_Streamlit/outpatient_2015.csv')
    return outpatient

## Loading Bar

my_bar = st.progress(0)
for percent_complete in range(100):
     time.sleep(0.1)
     my_bar.progress(percent_complete + 1)
     
## Streamlit App Title/Questions

st.title('HHA 507 Streamlit App')
st.write('Andrew Huang') 
st.write('This page answers the following questions:')
st.write('1: How does Stony Brook University Hospital compare to other hospitals in New York?')
st.write('2: What is the most expensive inpatient DRGs for Stony Brook?')
st.write('3: What is the most expensive outpatient APCs for Stony Brook?')
st.write('4: Which state has the most hospitals in the US?')
st.write('5: What kind of hospital distribution does New York have?')
st.write('6: ')

## Load Datasets

hospital = load_hospitals()

outpatient = load_outpatient()

inpatient = load_inpatient()

## Dataframe Previews 
st.header('Hospital Preview')
st.markdown('This dataset displays hospitals in the United States.')
st.dataframe(load_hospitals())

st.header('Inpatient Preview')
st.markdown('This dataset displays drg codes for multiple inpatient locations.')
st.dataframe(load_inpatient())

st.header('Outpatient Preview')
st.markdown('This dataset displays apc codes for multiple outpatient locations.')
st.dataframe(load_outpatient())


## SBU Data
sbu = hospital[hospital['hospital_name'] == 'SUNY/STONY BROOK UNIVERSITY HOSPITAL']
st.header('Stony Brook University Hospital')
st.markdown('This shows information on Stony Brook University Hospital')
st.dataframe(SBU)



