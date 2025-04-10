import streamlit as st
from requests import get

st.title("IP Address Logger")

def get_public_ip():
    try:
        ip = get('https://api.ipify.org').text
        return ip
    except Exception as e:
        st.error(f"Error getting public IP: {e}")
        return "Could not retrieve public IP"

public_ip = get_public_ip()


st.info("**IP Address Information**")
st.write(f"**Your IP Address:** {public_ip}")


print(f"User connected with IP address: {public_ip}")


if st.button("Refresh IP"):
    st.experimental_rerun()


from datetime import datetime
current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
st.write(f"Last checked: {current_time}")