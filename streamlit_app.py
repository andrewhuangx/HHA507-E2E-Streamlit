# -*- coding: utf-8 -*-
"""
Created on Wed Dec 15 15:05:10 2021

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

st.title('HHA 507 Streamlit App')













