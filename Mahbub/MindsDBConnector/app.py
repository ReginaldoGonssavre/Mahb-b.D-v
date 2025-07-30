import mindsdb_sdk
import streamlit as st

# Connect to MindsDB
server = mindsdb_sdk.connect()

# Get a project
project = server.get_project()

# Get a model
model = project.get_model('financial_forecasting')

# Make a prediction
df = pd.DataFrame({'date': ['2023-10-01']})
prediction = model.predict(df)

st.title('Financial Forecasting')
st.write(prediction)