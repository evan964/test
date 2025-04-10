import streamlit as st
from streamlit_javascript import st_javascript

st.title("IP Address Logger")

# JavaScript code to fetch IP address from our Flask endpoint
client_ip = st_javascript(
    """
    await fetch('http://localhost:5000/get_ip')
        .then(response => response.json())
        .then(data => data.ip);
"""
)

if client_ip:
    st.info("*IP Address Information*")
    st.write(f"*Your IP Address:* {client_ip}")
    print(f"User connected with IP address: {client_ip}")
else:
    st.warning("Waiting for IP address...")
