import streamlit as st
import pandas as pd
import numpy as np
import joblib
from sklearn.ensemble import RandomForestClassifier
from predictions import *
from PIL import Image

model = joblib.load('Model/gridSearch.pkl')

st.set_page_config(page_title="Site Energy Intensity Prediction",
                   page_icon="🏢⚡", layout="wide")


#creating option list for dropdown menu
options_state_factor = ['State_1', 'State_2', 'State_4', 'State_6', 'State_8', 'State_10',
       'State_11']
options_building_class = ['Commercial', 'Residential']
options_facility_type = ['Grocery_store_or_food_market',
       'Warehouse_Distribution_or_Shipping_center',
       'Retail_Enclosed_mall', 'Education_Other_classroom',
       'Warehouse_Nonrefrigerated', 'Warehouse_Selfstorage',
       'Office_Uncategorized', 'Data_Center', 'Commercial_Other',
       'Mixed_Use_Predominantly_Commercial',
       'Office_Medical_non_diagnostic', 'Education_College_or_university',
       'Industrial', 'Laboratory',
       'Public_Assembly_Entertainment_culture',
       'Retail_Vehicle_dealership_showroom', 'Retail_Uncategorized',
       'Lodging_Hotel', 'Retail_Strip_shopping_mall',
       'Education_Uncategorized', 'Health_Care_Inpatient',
       'Public_Assembly_Drama_theater', 'Public_Assembly_Social_meeting',
       'Religious_worship', 'Mixed_Use_Commercial_and_Residential',
       'Office_Bank_or_other_financial', 'Parking_Garage',
       'Commercial_Unknown', 'Service_Vehicle_service_repair_shop',
       'Service_Drycleaning_or_Laundry', 'Public_Assembly_Recreation',
       'Service_Uncategorized', 'Warehouse_Refrigerated',
       'Food_Service_Uncategorized', 'Health_Care_Uncategorized',
       'Food_Service_Other', 'Public_Assembly_Movie_Theater',
       'Food_Service_Restaurant_or_cafeteria', 'Food_Sales',
       'Public_Assembly_Uncategorized', 'Nursing_Home',
       'Health_Care_Outpatient_Clinic', 'Education_Preschool_or_daycare',
       '5plus_Unit_Building', 'Multifamily_Uncategorized',
       'Lodging_Dormitory_or_fraternity_sorority',
       'Public_Assembly_Library', 'Public_Safety_Uncategorized',
       'Public_Safety_Fire_or_police_station', 'Office_Mixed_use',
       'Public_Assembly_Other', 'Public_Safety_Penitentiary',
       'Health_Care_Outpatient_Uncategorized', 'Lodging_Other',
       'Mixed_Use_Predominantly_Residential', 'Public_Safety_Courthouse','Public_Assembly_Stadium', 'Lodging_Uncategorized',
       '2to4_Unit_Building', 'Warehouse_Uncategorized']

# st.markdown(
#     """
# <style>
# .reportview-container .markdown-text-container {
#     font-family: serif;
# }
# .sidebar .sidebar-content {
#     background-image: linear-gradient(#cf872e,#2e7bcf);
#     color: white;
# }
# .Widget>label {
#     color: white;
#     font-family: serif;
# }
# [class^="st-b"]  {
#     color: white;
#     font-family: monospace;
# }
# .st-bb {
#     background-color: transparent;
# }
# .st-at {
#     background-color: #0c0080;
# }
# footer {
#     font-family: monospace;
# }
# .reportview-container .main footer, .reportview-container .main footer a {
#     color: #0c0080;
# }
# header .decoration {
#     background-image: none;
# }

# </style>
# """,
#     unsafe_allow_html=True,
# )

st.markdown("<h1 style='text-align: center;'>Site Energy Intensity Prediction Application 🏢⚡</h1>", unsafe_allow_html=True)

image = Image.open('Site1.jpg')
col1, col2, col3 = st.columns([0.2, 5, 0.2])
col2.image(image, use_column_width=True)
def main():
    with st.form('prediction_form'):

        st.subheader("Enter the input for following features:")

        march_min = st.text_input(label='Enter march min temp')
        march_avg = st.text_input(label='Enter march avg temp')
        march_max = st.text_input(label='Enter march max temp')
        
        aug_min = st.text_input(label='Enter august min temp')
        aug_avg = st.text_input(label='Enter august avg temp')
        aug_max = st.text_input(label='Enter august max temp')

        oct_min = st.text_input(label='Enter october min temp')
        oct_avg = st.text_input(label='Enter october avg temp')
        oct_max = st.text_input(label='Enter october max temp')

        nov_min = st.text_input(label='Enter november min temp')
        nov_avg = st.text_input(label='Enter november avg temp')
        nov_max = st.text_input(label='Enter november max temp')

        dec_min = st.text_input(label='Enter december min temp')
        dec_avg = st.text_input(label='Enter december avg temp')
        dec_max = st.text_input(label='Enter december max temp')

        floor_area = st.text_input(label='Enter floor area')
        elevation = st.text_input(label='Enter building\'s elevation')

        ratings = st.slider("Pickup energy star rating: ", 0, 100, value=0, format="%f")
        year_built = st.slider("Pickup year in which building was built ", 1900, 2039, value=0, format="%f")

        year_factor = st.slider("Pickup year factor: ", 1, 7, value=1, format="%d")
        state_factor = st.selectbox("Select state factor: ", options=options_state_factor)
        building_class = st.selectbox("Select building class: ", options=options_building_class)
        facility_type = st.selectbox("Select facility type: ", options=options_facility_type)

        submit = st.form_submit_button("Predict")

    if submit:
       march_min = np.int64(march_min)
       march_avg = np.float64(march_avg)
       march_max = np.int64(march_max)

       aug_min = np.int64(aug_min)
       aug_avg = np.float64(aug_avg)
       aug_max = np.int64(aug_max)

       oct_min = np.int64(oct_min)
       oct_avg = np.float64(oct_avg)
       oct_max = np.int64(oct_max)

       nov_min = np.int64(nov_min)
       nov_avg = np.float64(nov_avg)
       nov_max = np.int64(nov_max)

       dec_min = np.int64(dec_min)
       dec_avg = np.float64(dec_avg)
       dec_max = np.int64(dec_max)
       
       floor_area = np.float64(floor_area)
       elevation = np.float64(elevation)
      
       state_factor = encodeStateFactor(state_factor)
       building_class = encodeBuildingClass(building_class)
       facility_type = encodeFacilityType(facility_type)

       data = np.array([march_min, march_avg, march_max, aug_min,
       aug_avg, aug_max, oct_min,
       oct_avg, oct_max, nov_min,
       nov_avg, nov_max, dec_min,
       dec_avg, dec_max, floor_area,
       elevation, ratings,
       year_built, year_factor, state_factor, building_class, facility_type
       ]).reshape(1,-1)

       pred = get_prediction(data, model=model)

       
       st.write('Site\'s Energy Use Intensity is: {}'.format(pred[0]))
       #st.write(f"The predicted severity is:  {pred}")

if __name__ == '__main__':
    main()