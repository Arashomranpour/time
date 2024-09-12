import streamlit as st
import base64

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
        flex-direction: column; /* Stack items vertically */
        justify-content: center; /* Centers horizontally */
        align-items: center;     /* Centers vertically */
        height: 100vh;           /* Full viewport height */
        position: relative;      /* Ensure the button can be positioned absolutely */
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
    a {
        color: black; /* Use the same color as the surrounding text */
        text-decoration: none; /* Remove underline */
    }
    .white-text {
        color: white;
    }
    </style>
""", unsafe_allow_html=True)

# Add spacing and button
st.markdown('<div style="height: 250px;"></div>', unsafe_allow_html=True)  # Adjust height as needed

# Define audio file URL
audio_file = "audio.mp3"

btn = st.button("Play Voice")

if btn:
    st.markdown(f"""
        <audio id="myAudio" src="{audio_file}" preload="auto"></audio>
        <script>
        document.getElementById('myAudio').play();
        </script>
    """, unsafe_allow_html=True)
