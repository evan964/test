import streamlit as st
from datetime import datetime
import requests

st.set_page_config(page_title="IP Address Detector", page_icon="🔍")

st.title("IP Address Detector")

# Get IP address server-side and store in variable
try:
    response = requests.get('https://api.ipify.org?format=json')
    ip_data = response.json()
    ip_address = ip_data['ip']
    # Print to terminal
    print(f"IP Address detected: {ip_address}")
except Exception as e:
    ip_address = "Failed to detect"
    print(f"Error detecting IP: {e}")

# Display the server-detected IP
st.subheader("Your IP Address (detected server-side)")
st.write(ip_address)

# Create HTML/JS component to get client IP without the key parameter
def get_client_ip_component():
    html_code = """
    <div style="padding: 10px; background-color: #f0f2f6; border-radius: 5px;">
        <p style="font-weight: bold;">Your IP Address (client-side): <span id="ip-result">Detecting...</span></p>
    </div>
    
    <script>
    async function getIP() {
        try {
            const response = await fetch('https://api.ipify.org?format=json');
            const data = await response.json();
            
            // Display the IP
            document.getElementById('ip-result').innerHTML = data.ip;
            
            // Log to console
            console.log('Client IP:', data.ip);
        } catch (error) {
            document.getElementById('ip-result').innerHTML = 'Error: ' + error;
        }
    }
    
    // Run when loaded
    getIP();
    </script>
    """
    
    st.components.v1.html(html_code, height=100)

# Show the IP component (client-side detection)
st.subheader("Client-side Detection")
get_client_ip_component()

# Alternative method using iframe to ipify.org
st.subheader("Alternative Method (iframe)")
st.markdown('<iframe src="https://api.ipify.org" width="100%" height="50"></iframe>', unsafe_allow_html=True)

# Add a refresh button
if st.button("Refresh"):
    st.experimental_rerun()

# Print to console log (server-side)
print(f"Page loaded at: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")