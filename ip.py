from streamlit_javascript import st_javascript
import streamlit as st

st.subheader("Javascript API call")

return_value = st_javascript(
    """await fetch("https://api.ipify.org?format=json").then(function(response) {
    return response.json();
}) """
)
print(type(return_value))
print(return_value)
if isinstance(return_value, dict) and "ip" in return_value:
    ip_address = return_value["ip"]
    print(ip_address)
    st.markdown(f"IP Address is: {ip_address}")
    print(f"IP Address is: {ip_address}")
else:
    st.error("Failed to get IP address. Please try again.")
    print("Failed to get IP address")
