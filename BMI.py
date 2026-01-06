import streamlit as st

st.title('Welcome to the BMI Calculator')

weight = st.number_input('Enter your weight in kilograms:', min_value=0.0, format="%.2f")
status=st.radio('Select your height format:', ('cms', 'meters', 'feet'))

if status=='cms':
    height_cm = st.number_input('Enter your height in centimeters:', min_value=0.0, format="%.2f")
    height = height_cm / 100  # Convert cm to meters
elif status=='meters':
    height = st.number_input('Enter your height in meters:', min_value=0.0, format="%.2f")
elif status=='feet':
    height_feet = st.number_input('Enter your height in feet:', min_value=0.0, format="%.2f")
    height = height_feet * 0.3048  # Convert feet to meters

calculate = st.button('Calculate BMI')

if calculate:
    if height > 0:
        bmi = weight / (height ** 2)
        st.success(f'Your BMI is: {bmi:.2f}')
        
        if bmi < 18.5:
            st.warning('You are underweight.')
        elif 18.5 <= bmi < 25:
            st.success('You have a normal weight.')
        elif 25 <= bmi < 30:
            st.warning('You are overweight.')
        else:
            st.error('You are obese.')
    else:
        st.error("Height must be greater than zero.")