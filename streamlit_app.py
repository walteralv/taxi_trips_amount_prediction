import streamlit as st
import pickle
import numpy as np
import pandas as pd

# Load Regression Tree Model 
filename = 'finalized_regtree.sav' 
model = pickle.load(open(filename, 'rb'))  

rate_dict={
    "Standard rate":1,
    "JFK":2,
    "Newark":3,
    "Nassau or Westchester":4,
    "Negotiated fare":5,
    "Group ride":6
}
borugh_dict ={
    "Manhattan":1,
    "Brooklyn":2,
    "Bronx":3,
    "Queens":4,
    "Staten Island":5
}


st.write("## ")
with st.container():  # About me    
    rate = st.selectbox(
        'Cual es su código de Tarifas?',
        list(rate_dict.keys())
    )
    trip_distance = st.number_input(
        'Cual es la distancia (en Millas) aproximada del viaje?',
        value=5,
        min_value=0,
        max_value=100,
        step=1)
    pu_borough = st.selectbox(
        'En que Ciudad se Encuentra?',
        list(borugh_dict.keys())
    )
    
    do_borough = st.selectbox(
        'A que Ciudad se Dirige?',
        list(borugh_dict.keys())
    )

    if st.button('Calcular Tarifa'):
        
        X_new=pd.DataFrame(
            [[
                rate_dict[rate],
                trip_distance,
                borugh_dict[pu_borough],
                borugh_dict[do_borough]
            ]]
            ,columns=["id_rate","trip_distance","pu_borough","do_borough"])

        pred=np.round(model.predict(X_new)[0],2)
        st.write("## La tarifa Aproximada por el viaje es:",pred)
    else:
        st.write("## La tarifa Aproximada por el viaje es:")

    # st.write('The current number is ', number)
    # st.write('You selected:', rate_dic[option])
