import streamlit as st
from pint import UnitRegistry

def convert_units(value, from_unit, to_unit):
    ureg = UnitRegistry()
    try:
        result = (value * ureg(from_unit)).to(to_unit)
        return result.magnitude
    except Exception as e:
        return f"Error: {str(e)}"

def main():
    st.title("Google-Style Unit Converter")
    
    # Input Fields
    value = st.number_input("Enter value:", value=1.0, step=0.1)
    from_unit = st.text_input("From Unit (e.g., meters, kg, celsius):")
    to_unit = st.text_input("To Unit (e.g., feet, lb, fahrenheit):")
    
    if st.button("Convert"):
        if from_unit and to_unit:
            result = convert_units(value, from_unit, to_unit)
            st.success(f"{value} {from_unit} = {result} {to_unit}")
        else:
            st.warning("Please enter both units.")
    
if __name__ == "__main__":
    main()
