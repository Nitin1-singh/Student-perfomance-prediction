import streamlit as st 
import pandas as pd
import pickle as pk
data = pd.read_csv('./model/Student_Performance.csv')
st.title("Student Perfomance Prediction")

def eval_result():
    model = pk.load(open('./model.pkl','rb'))
    ans = model.predict([[selected_hrs_study,selected_prv_scr,selected_extra_cirr,selected_sleep_hr,selected_practice_paper]])
    return ans[0]

selected_hrs_study = st.selectbox('Hours Studied',data['Hours Studied'].sort_values().unique(),index=None)
selected_prv_scr = st.selectbox('Previous Score',data['Previous Scores'].sort_values().unique(),index=None)
selected_extra_cirr = st.selectbox('Extracurricular Activities',data['Extracurricular Activities'].unique(),index=None)
selected_sleep_hr = st.selectbox('Sleep Hours',data['Sleep Hours'].sort_values().unique(),index=None)
selected_practice_paper = st.selectbox('Sample Question Papers Practiced',data['Sample Question Papers Practiced'].sort_values().unique(),index=None)

col1, col2 = st.columns([1,1])
with col1:
    if st.button("Predict"):
        res = eval_result()
        st.write("Predicted Score = ,{:.2f}.format(res/10)")
    else:
        st.write('')
with col2:
    st.button("Reset")

