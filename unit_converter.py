import streamlit as st

def convert_units(value, from_unit, to_unit):
    conversions = {
        ('meters', 'feet'): 3.28084,
        ('feet', 'meters'): 0.3048,
        ('kilograms', 'pounds'): 2.20462,
        ('pounds', 'kilograms'): 0.453592,
        ('celsius', 'fahrenheit'): lambda c: (c * 9/5) + 32,
        ('fahrenheit', 'celsius'): lambda f: (f - 32) * 5/9
    }
    
    key = (from_unit, to_unit)
    
    if key in conversions:
        factor = conversions[key]
        return factor(value) if callable(factor) else value * factor
    else:
        return "Conversion not supported"

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
