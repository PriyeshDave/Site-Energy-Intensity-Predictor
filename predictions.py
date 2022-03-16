
def encodeBuildingClass(value):
  mapper = {
     'Commercial' : 85.176286,
     'Residential' : 78.229497
   }
  return mapper[value]

def encodeStateFactor(value):
  mapper = {'State_6': 87.481012,
 'State_11': 54.063412,
 'State_4': 94.106161,
 'State_1': 62.022310,
 'State_2': 76.886316,
 'State_8': 84.930852,
 'State_10': 66.481569
}
  return mapper[value]

def encodeFacilityType(value):
  mapper = {'Multifamily_Uncategorized': 83.18453431827938,
 'Office_Uncategorized': 75.79725349959234,
 'Education_Other_classroom': 69.12513889606197,
 '2to4_Unit_Building': 31.88786293258562,
 'Lodging_Hotel': 103.20319664945116,
 'Commercial_Other': 94.08358266935531,
 '5plus_Unit_Building': 36.36878893112065,
 'Warehouse_Nonrefrigerated': 36.87803631594659,
 'Retail_Uncategorized': 78.88347211705016,
 'Education_College_or_university': 107.42073300753296,
 'Nursing_Home': 126.82324214323036,
 'Mixed_Use_Commercial_and_Residential': 90.59464626306816,
 'Lodging_Dormitory_or_fraternity_sorority': 80.76976493622722,
 'Education_Uncategorized': 46.55875376304007,
 'Warehouse_Distribution_or_Shipping_center': 38.828697938082726,
 'Warehouse_Selfstorage': 20.981256819909497,
 'Grocery_store_or_food_market': 239.38808821318494,
 'Office_Medical_non_diagnostic': 113.51456323322472,
 'Religious_worship': 43.873971534873604,
 'Warehouse_Uncategorized': 36.24978755155692,
 'Health_Care_Inpatient': 242.36048444809896,
 'Industrial': 128.82155085165905,
 'Mixed_Use_Predominantly_Commercial': 69.6919229577094,
 'Parking_Garage': 66.04516285886689,
 'Office_Bank_or_other_financial': 88.8667151770474,
 'Public_Assembly_Library': 107.2458178973689,
 'Public_Safety_Fire_or_police_station': 128.4162255371988,
 'Retail_Enclosed_mall': 103.38235919540834,
 'Laboratory': 328.8271684311959,
 'Retail_Strip_shopping_mall': 106.88463799089126,
 'Public_Assembly_Other': 125.76086197881833,
 'Service_Vehicle_service_repair_shop': 131.86760279274057,
 'Warehouse_Refrigerated': 97.85580861838756,
 'Public_Assembly_Entertainment_culture': 115.86854161989889,
 'Commercial_Unknown': 114.7913639981253,
 'Education_Preschool_or_daycare': 60.690404104757896,
 'Public_Assembly_Social_meeting': 78.08226844489512,
 'Public_Assembly_Recreation': 118.35926491644004,
 'Food_Sales': 132.6746957760931,
 'Retail_Vehicle_dealership_showroom': 45.804244813558476,
 'Public_Assembly_Drama_theater': 83.14052824688622,
 'Lodging_Other': 114.80245827702088,
 'Service_Uncategorized': 115.25772332205693,
 'Food_Service_Restaurant_or_cafeteria': 194.90262676769,
 'Health_Care_Outpatient_Clinic': 99.50862170903923,
 'Public_Safety_Uncategorized': 81.63304218496295,
 'Health_Care_Uncategorized': 180.3502973716617,
 'Public_Assembly_Movie_Theater': 103.90205662781288,
 'Public_Safety_Penitentiary': 172.68989941684305,
 'Public_Safety_Courthouse': 101.13159263397921,
 'Health_Care_Outpatient_Uncategorized': 183.81343933759752,
 'Public_Assembly_Uncategorized': 62.04001607029897,
 'Data_Center': 335.1672800430479,
 'Office_Mixed_use': 82.61183680568746,
 'Food_Service_Uncategorized': 124.57696492237065,
 'Food_Service_Other': 31.183758448862452,
 'Mixed_Use_Predominantly_Residential': 76.33757110219699,
 'Public_Assembly_Stadium': 149.2624540203461,
 'Service_Drycleaning_or_Laundry': 41.23169781947623,
 'Lodging_Uncategorized': 61.86270317211861
 }

  return mapper[value]
  
def get_prediction(data, model):
  prediction = model.predict(data)
  return prediction


