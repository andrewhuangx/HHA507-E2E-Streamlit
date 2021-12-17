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
st.markdown('This dataset displays information on inpatient locations.')
st.dataframe(load_inpatient())

st.header('Outpatient Preview')
st.markdown('This dataset displays infomration on outpatient locations.')
st.dataframe(load_outpatient())

## Question 1 Prep
## SBU Hospital Data
sbu = hospital[hospital['hospital_name'] == 'SUNY/STONY BROOK UNIVERSITY HOSPITAL']
st.header('SBU Hospital Info')
st.markdown('This shows information on Stony Brook University Hospital')
st.dataframe(sbu)

## New York Hospital Data
newyork = hospital[hospital['state'] == 'NY']
st.header('New York Hospital Info')
st.markdown('This dataset shows hospitals located in New York')
st.dataframe(newyork)

## Answer 1
q1table = newyork['hospital_overall_rating'].value_counts().reset_index()
st.header('Q1: How does Stony Brook University Hospital compare to other hospitals in New York?')
st.subheader('New York Hospital Ratings')
st.markdown('From the SBU Hospital Data we know SBU Hospital has an overall ranking of 4. Looking at the distribution of hospital rankings across NYS we can conlcude SBU Hospital is among the top hospitals, roughly about the top 10%.')
st.dataframe(q1table)

## Question 2 Prep
## Inpatient Data for SBU Hospital
sbuinpatient = inpatient[inpatient['provider_id']==330393]
st.header('SBU Hospital Inpatient Data')
st.markdown('This shows inpatient data for Stony Brook University Hospital.')
st.dataframe(sbuinpatient)

## Answer 2
st.header('Q2: What is the most expensive inpatient DRGs for Stony Brook?')
st.subheader('SBUH IP DRGs Pivot Table')
sbu_drg_pivot = sbuinpatient.pivot_table(index=['provider_id','provider_name','drg_definition'],values=['average_total_payments'])
sbu_drg_desc = sbu_drg_pivot.sort_values(['average_total_payments'], ascending=False)
st.markdown('DRG stands for diagnostic related group. This is a classification system standardizing prospective payment to hospitals.')
st.markdown('From the table the most expensive inpatient DRG code for Stony Brook Univeristy Hospital is 003, ECMO OR TRACH W MV >96 HRS OR PDX EXC FACE, MOUTH & NECK W MAJ O.R., where the average total payment is $21,667.00.')
st.dataframe(sbu_drg_desc)

