import streamlit as st

# Conversion functions
def convert_length(value, from_unit, to_unit):
    # Conversion logic for length
    length_conversions = {
        'meter': 1.0,
        'kilometer': 1000.0,
        'centimeter': 0.01,
        'millimeter': 0.001,
        'mile': 1609.34,
        'yard': 0.9144,
        'foot': 0.3048,
        'inch': 0.0254
    }
    return value * length_conversions[from_unit] / length_conversions[to_unit]

def convert_weight(value, from_unit, to_unit):
    # Conversion logic for weight
    weight_conversions = {
        'kilogram': 1.0,
        'gram': 0.001,
        'milligram': 0.000001,
        'pound': 0.453592,
        'ounce': 0.0283495
    }
    return value * weight_conversions[from_unit] / weight_conversions[to_unit]

def convert_temperature(value, from_unit, to_unit):
    # Conversion logic for temperature
    if from_unit == 'celsius':
        if to_unit == 'fahrenheit':
            return (value * 9/5) + 32
        elif to_unit == 'kelvin':
            return value + 273.15
    elif from_unit == 'fahrenheit':
        if to_unit == 'celsius':
            return (value - 32) * 5/9
        elif to_unit == 'kelvin':
            return (value - 32) * 5/9 + 273.15
    elif from_unit == 'kelvin':
        if to_unit == 'celsius':
            return value - 273.15
        elif to_unit == 'fahrenheit':
            return (value - 273.15) * 9/5 + 32
    return value

def convert_time(value, from_unit, to_unit):
    # Conversion logic for time
    time_conversions = {
        'second': 1.0,
        'minute': 60.0,
        'hour': 3600.0,
        'day': 86400.0,
        'week': 604800.0,  # Approximate
        'month': 2629800.0,  # Approximate
        'year': 31557600.0   # Approximate
    }
    return value * time_conversions[from_unit] / time_conversions[to_unit]

# Streamlit app
def main():
    # App title with emoji
    st.title("🌍 Unit Converter App ")

    # Subheader with emoji
    st.write("Convert units effortlessly across the globe! 🌎")

    # Select the type of conversion with emoji
    conversion_type = st.selectbox(
        " Select Conversion Type",
        ["Length 📏", "Weight ⚖️", "Temperature 🌡️", "Time ⏳"]
    )

    # Define units based on conversion type
    if conversion_type == "Length 📏":
        units = ['meter', 'kilometer', 'centimeter', 'millimeter', 'mile', 'yard', 'foot', 'inch']
    elif conversion_type == "Weight ⚖️":
        units = ['kilogram', 'gram', 'milligram', 'pound', 'ounce']
    elif conversion_type == "Temperature 🌡️":
        units = ['celsius', 'fahrenheit', 'kelvin']
    elif conversion_type == "Time ⏳":
        units = ['second', 'minute', 'hour', 'day', 'week', 'month', 'year']

    # Input value with emoji
    value = st.number_input(" Enter the value to convert", value=1.0)

    # Select 'from' unit with emoji
    from_unit = st.selectbox("From", units)

    # Select 'to' unit with emoji
    to_unit = st.selectbox("To", units)

    # Perform conversion
    if conversion_type == "Length 📏":
        result = convert_length(value, from_unit, to_unit)
    elif conversion_type == "Weight ⚖️":
        result = convert_weight(value, from_unit, to_unit)
    elif conversion_type == "Temperature 🌡️":
        result = convert_temperature(value, from_unit, to_unit)
    elif conversion_type == "Time ⏳":
        result = convert_time(value, from_unit, to_unit)

    # Display the result with emoji
    st.success(f"✅ Converted value: **{result:.2f} {to_unit}**")

if __name__ == "__main__":
    main()