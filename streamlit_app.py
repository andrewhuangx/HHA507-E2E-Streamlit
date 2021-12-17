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
st.write('6: What are the most common inpatient and outpatient services in New York?')

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
st.subheader('SBUH Inpatient DRGs Pivot Table')
sbu_drg_pivot = sbuinpatient.pivot_table(index=['provider_id','drg_definition'],values=['average_total_payments'])
sbu_drg_desc = sbu_drg_pivot.sort_values(['average_total_payments'], ascending=False)
st.markdown('DRG stands for diagnostic related group. This is a classification system standardizing prospective payment to hospitals.')
st.markdown('From the table the most expensive inpatient DRG code for SBUH is 003, ECMO OR TRACH W MV >96 HRS OR PDX EXC FACE, MOUTH & NECK W MAJ O.R.')
st.markdown('This is followed by DRG codes 004,TRACH W MV 96+ HRS OR PDX EXC FACE, MOUTH & NECK W/O MAJ O.R., and 834, ACUTE LEUKEMIA W/O MAJOR O.R. PROCEDURE W MCC.')
st.dataframe(sbu_drg_desc)

## Question 3 Prep
## Outpatient Data for SBU Hospital
sbuoutpatient = outpatient[outpatient['provider_id']==330393]
st.header('SBU Hospital Outpatient Data')
st.markdown('This shows outpatient data for Stony Brook University Hospital.')
st.dataframe(sbuoutpatient)

## Answer 3
st.header('Q3: What is the most expensive outpatient APCs for Stony Brook?')
st.subheader('SBUH Outpatient APCs Pivot Table')
sbu_apc_pivot = sbuoutpatient.pivot_table(index=['provider_id','apc'],values=['average_total_payments'])
sbu_apc_desc = sbu_apc_pivot.sort_values(['average_total_payments'], ascending=False)
st.markdown('APC stands for ambulatory payment classsifications. This is a classification system for outpatient services')
st.markdown('From the table the most expensive outpatient APCs code for SBUH is 0074, Level IV Endoscopy Upper Airway.')
st.markdown('This is followed by APC codes 0203, Level IV Nerve Injections, and 0377, Level II Cardiac Imaging.')
st.dataframe(sbu_apc_desc)

## Question 4 Prep/Answer
## Bar Graph Comparing Number of Hospitals in Each State
st.header('Q4: Which state has the most hospitals in the US?')
st.subheader('Hospitals Per State')
statehospitals = hospital['state'].value_counts().reset_index()
st.bar_chart(data=statehospitals, width=0, height=0, use_container_width=True)
st.markdown('With 449 hospitals Texas has the most hospitals. This is followed by California at 378 and Florida at 209.')

## Question 5 Prep
## Setting up a Map of NYS
st.header('Q5: What kind of hospital distribution does New York have?')
st.subheader('Map of New York Hospitals')
nyh_locations = newyork['location'].str.strip('()').str.split(' ', expand=True).rename(columns={0: 'Point', 1:'lon', 2:'lat'}) 	
nyh_locations['lon'] = nyh_locations['lon'].str.strip('(')
nyh_locations = nyh_locations.dropna()
nyh_locations['lon'] = pd.to_numeric(nyh_locations['lon'])
nyh_locations['lat'] = pd.to_numeric(nyh_locations['lat'])

## Answer 5
st.map(nyh_locations)
st.markdown('In NYS most hospitals are condensed around NYC followed by Buffalo, Rochester, and Albany.')

## Question 6 Prep
## Top 5 Common Inpatient Discharges
inpatient_discharges = inpatient[inpatient['provider_state'] == 'NY']
common_ipdischarges = inpatient_discharges.groupby('drg_definition')['total_discharges'].sum().nlargest(5)
st.header('Common New York Inpatient Discharges')
st.markdown('This disaplys the amount inpatient discharges for each DRG code in New York State.')
st.dataframe(common_ipdischarges)

## Top 5 Common Outpatient Services
outpatient_services = outpatient[outpatient['provider_state'] == 'NY']
common_opservices = outpatient_services.groupby('apc')['outpatient_services'].sum().nlargest(5)
st.header('Common New York Outpatient Services')
st.markdown('This displays the amount outpatient services for each APC code in New York State.')
st.dataframe(common_opservices)

## Answer 6
st.markdown('From the above charts we know DRG code 871, SEPTICEMIA OR SEVERE SEPSIS W/O MV 96+ HOURS W MCC, with 31,964 discharges is the most common inpatient discharge.')
st.markdown('We also know APC code 0634, Hospital Clinic Visits, with a count of 1,460,708 is the most common outpatient service.')