import streamlit as st
import base64
from datetime import datetime
import streamlit.components.v1 as components

def add_bg_from_local(image_file):
    with open(image_file, "rb") as image_file:
        encoded_string = base64.b64encode(image_file.read())
    st.markdown(
        f"""
        <style>
        .stApp {{
            background-image: url(data:image/{"png"};base64,{encoded_string.decode()});
            background-size: cover;
            background-attachment: fixed; /* Optional: fix background image in place */
        }}
        </style>
        """,
        unsafe_allow_html=True
    )

# Add background image
add_bg_from_local('./image.jpg')

# Inline CSS for centering and styling
st.markdown("""
    <style>
    .center-container {
        display: flex;
        justify-content: center; /* Centers horizontally */
        align-items: center;     /* Centers vertically */
        height: 100vh;           /* Full viewport height */
    }
    .box {
        border: 2px solid black;
        padding: 20px;
        border-radius: 10px;
        background-color: white;
        box-shadow: 0px 4px 8px rgba(0, 0, 0, 0.1);
        max-width: 90%; /* Adjust as needed */
        text-align: center;
        height: auto;
    }
    </style>
""", unsafe_allow_html=True)

# Add centered box with text and countdown
specified_date = datetime(2024, 3, 10)
today = datetime.now()
days_passed = (today - specified_date).days

# Replace Sarina text with a clickable link
st.markdown(f"""
    <div class="center-container">
        <div class="box">
            <h4>I love you to the moon and back ❤️ <a href="https://sarinalove.streamlit.app/" target="_blank">Sarina</a> ❤️</h4>
            <p>20 Esfand 1402 (March 10, 2024)</p>
            <p>Days Passed: {days_passed} days</p>
            <button style="position: absolute; left: 10px;" id="hiddenButton">Click me</button>
    
        </div>
    </div>
""", unsafe_allow_html=True)

# JavaScript to show alert when hidden button is clicked
components.html("""
    <script>
        document.getElementById("hiddenButton").addEventListener("click", function() {
            alert("من برای تو ام و تو برای منی و هیچکس و هیچ چیز نمیتونه مارو ار هم جدا کنه");
        });
    </script>
""")
