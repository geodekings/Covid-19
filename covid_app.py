import numpy as np
import pandas as pd 
import matplotlib.pyplot as plt
import streamlit as st
import time

st.title('Covid-19 APP')
st.image('pngwing.com (21).png', width=500)

# Insert containers separated into tabs:
tab1, tab2, tab3 = st.tabs(["Overview", "Prevention", "Symptoms"])
tab1.header('Corona Virus')
tab1.write('Coronavirus disease (COVID-19) is an infectious disease caused by the SARS-CoV-2 virus. Most people infected with the virus will experience mild to moderate respiratory illness and recover without requiring special treatment. However, some will become seriously ill and require medical attention. Older people and those with underlying medical conditions like cardiovascular disease, diabetes, chronic respiratory disease, or cancer are more likely to develop serious illness. Anyone can get sick with COVID-19 and become seriously ill or die at any age. The best way to prevent and slow down transmission is to be well informed about the disease and how the virus spreads. Protect yourself and others from infection by staying at least 1 metre apart from others, wearing a properly fitted mask, and washing your hands or using an alcohol-based rub frequently. Get vaccinated when it’s your turn and follow local guidance. The virus can spread from an infected person’s mouth or nose in small liquid particles when they cough, sneeze, speak, sing or breathe. These particles range from larger respiratory droplets to smaller aerosols. It is important to practice respiratory etiquette, for example by coughing into a flexed elbow, and to stay home and self-isolate until you recover if you feel unwell.')
tab2.image('pngwing.com (20).png', width=200)
tab2.markdown(
"""
**To prevent infection and to slow transmission of COVID-19, do the following:**
- Get vaccinated when a vaccine is available to you. 
- Stay at least 1 metre apart from others, even if they don’t appear to be sick. 
- Wear a properly fitted mask when physical distancing is not possible or when in poorly ventilated settings. 
- Choose open, well-ventilated spaces over closed ones. Open a window if indoors. 
- Wash your hands regularly with soap and water or clean them with alcohol-based hand rub. 
- Cover your mouth and nose when coughing or sneezing.If you feel unwell, stay home and self-isolate until you recover.""")
tab3.markdown(
"""
COVID-19 affects different people in different ways. Most infected people will develop mild to moderate illness and recover without hospitalization.
"""
)
col1, col2, col3 = tab3.columns(3)
col1.markdown(
    """
    **Most common symptoms:**
    - fever
    - Cough
    - Tiredness
    """
)
col2.markdown(
    """
    **Less common symptoms:**
    - sore throat
    - headache
    - aches and pains
    - diarrhoea
    - a rash on skin, or discolouration of fingers or toes
    - red or irritated eyes.
    """
)
col3.markdown(
    """
    **Serious symptoms:**
    - difficulty breathing or shortness of breath
    - loss of speech or mobility, or confusion
    - chest pain.
    - Seek immediate medical attention if you have serious symptoms. 
    - Always call before visiting your doctor or health facility. 
    """
)
tab3.markdown(
"""
- People with mild symptoms who are otherwise healthy should manage their symptoms at home. 
- On average it takes 5–6 days from when someone is infected with the virus for symptoms to show, however it can take up to 14 days.
""")




st.sidebar.image('pngwing.com (19).png', width=400)
st.sidebar.markdown(
    """
    Please be informed this app is not the actual Covid-19 case predictor, as covid-19 is gradually been eradicted.\n
    This APP serve a purpose of forcasted Covid cases from April-2023 through March-2026 for selected Countries *based on the assumptions* that Covid hasn't eradicated.\n
    """
)
Prediction = pd.read_csv('Prediction.csv', index_col=[0])
Prediction.index = Prediction.index.astype(str)

year = st.sidebar.selectbox('Pick a year', ['2023', '2024', '2025', '2026'])

if st.sidebar.button('Forcast'):
    st.write('Monthly Forcast')
    st.spinner(text='In progress')
    time.sleep(5)
    st.success('Done')
    if year == "2023":
        st.table(Prediction.loc[Prediction.index.str[:4] == '2023'])
        st.line_chart(Prediction.loc[Prediction.index.str[:4] == '2023'])
    elif year == "2024":
        st.table(Prediction.loc[Prediction.index.str[:4] == '2024'])
        st.line_chart(Prediction.loc[Prediction.index.str[:4] == '2024'])
    elif year == "2025":
        st.table(Prediction.loc[Prediction.index.str[:4] == '2025'])
        st.line_chart(Prediction.loc[Prediction.index.str[:4] == '2025'])
    elif year == "2026":
        st.table(Prediction.loc[Prediction.index.str[:4] == '2026'])
        st.line_chart(Prediction.loc[Prediction.index.str[:4] == '2026'])
