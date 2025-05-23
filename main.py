import streamlit as st
import requests

# Base URL of the API
BASE_URL = "https://business-analytics-3xje54mc2-trevors-projects-1a39e4d2.vercel.app"

# List of available endpoints
endpoints = {
    "/": "Root - Health Check",
    "/api/health": "API Health",
    "/api/endpoints": "List All Endpoints",
    "/api/costs/by-category": "Cost: By Category",
    "/api/costs/monthly": "Cost: Monthly",
    "/api/costs/by-product": "Cost: By Product",
    "/api/costs/top-products": "Cost: Top Products (limit)",
    "/api/costs/cost-per-unit": "Cost: Per Unit (limit)",
    "/api/costs/cost-revenue-ratio": "Cost: Revenue Ratio",
    "/api/analysis/profitability": "Profitability Analysis",
    "/api/costs/summary": "Cost Summary",
    "/api/costs/fixed-variable": "Fixed vs Variable Costs",
    "/api/cashflow/flow-types": "Cash Flow: Flow Types",
    "/api/cashflow/flow-type-counts": "Cash Flow: Flow Type Counts",
    "/api/cashflow/summary": "Cash Flow Summary",
    "/api/cashflow/monthly-net": "Cash Flow: Monthly Net",
    "/api/cashflow/by-type": "Cash Flow: By Type",
    "/api/cashflow/top-sources": "Cash Flow: Top Sources (limit)",
    "/api/cashflow/health-indicators": "Cash Flow: Health Indicators",
    "/api/cashflow/total-by-type": "Cash Flow: Total by Type",
}

st.title("📊 Business Analytics API Tester")

# Select endpoint
selected_endpoint = st.selectbox("Choose an endpoint to test", list(endpoints.keys()), format_func=lambda x: endpoints[x])

# Query parameters
params = {}
if "limit" in selected_endpoint:
    limit = st.number_input("Enter limit (optional)", min_value=1, step=1, value=5)
    params["limit"] = limit

# Trigger request
if st.button("Send Request"):
    try:
        url = BASE_URL + selected_endpoint
        response = requests.get(url, params=params)
        response.raise_for_status()
        json_data = response.json()

        st.success("✅ Request successful")
        st.json(json_data)
    except requests.exceptions.RequestException as e:
        st.error(f"❌ Request failed: {e}")





# import streamlit as st
# import requests

# BASE_URL = "https://business-analytics-3xje54mc2-trevors-projects-1a39e4d2.vercel.app"

# endpoints = {
#     "/": "Root - Health Check",
#     "/api/health": "API Health",
#     "/api/endpoints": "List All Endpoints",
#     "/api/costs/by-category": "Cost: By Category",
#     "/api/costs/monthly": "Cost: Monthly",
#     "/api/costs/by-product": "Cost: By Product",
#     "/api/costs/top-products": "Cost: Top Products (limit)",
#     "/api/costs/cost-per-unit": "Cost: Per Unit (limit)",
#     "/api/costs/cost-revenue-ratio": "Cost: Revenue Ratio",
#     "/api/analysis/profitability": "Profitability Analysis",
#     "/api/costs/summary": "Cost Summary",
#     "/api/costs/fixed-variable": "Fixed vs Variable Costs",
#     "/api/cashflow/flow-types": "Cash Flow: Flow Types",
#     "/api/cashflow/flow-type-counts": "Cash Flow: Flow Type Counts",
#     "/api/cashflow/summary": "Cash Flow Summary",
#     "/api/cashflow/monthly-net": "Cash Flow: Monthly Net",
#     "/api/cashflow/by-type": "Cash Flow: By Type",
#     "/api/cashflow/top-sources": "Cash Flow: Top Sources (limit)",
#     "/api/cashflow/health-indicators": "Cash Flow: Health Indicators",
#     "/api/cashflow/total-by-type": "Cash Flow: Total by Type",
# }

# st.title("📊 Business Analytics API Tester")

# # Auth input
# auth_method = st.selectbox("Authentication method", ["None", "API Key (Header)", "Bearer Token"])
# headers = {}

# if auth_method == "API Key (Header)":
#     api_key_name = st.text_input("Header Name", "x-api-key")
#     api_key_value = st.text_input("API Key Value", type="password")
#     if api_key_name and api_key_value:
#         headers[api_key_name] = api_key_value

# elif auth_method == "Bearer Token":
#     token = st.text_input("Bearer Token", type="password")
#     if token:
#         headers["Authorization"] = f"Bearer {token}"

# # Endpoint selection
# selected_endpoint = st.selectbox("Choose an endpoint to test", list(endpoints.keys()), format_func=lambda x: endpoints[x])

# # Query params
# params = {}
# if "limit" in selected_endpoint:
#     params["limit"] = st.number_input("Enter limit", min_value=1, value=5)

# # Send request
# if st.button("Send Request"):
#     try:
#         url = BASE_URL + selected_endpoint
#         response = requests.get(url, headers=headers, params=params)
#         response.raise_for_status()
#         st.success("✅ Request successful")
#         st.json(response.json())
#     except requests.exceptions.HTTPError as e:
#         st.error(f"❌ HTTP error: {e.response.status_code} - {e.response.reason}")
#         st.text(response.text)
#     except Exception as e:
#         st.error(f"❌ Error: {e}")



# import streamlit as st
# import requests
# import json

# # Base URL of the API
# BASE_URL = "https://business-analytics-3xje54mc2-trevors-projects-1a39e4d2.vercel.app"

# # List of available endpoints
# endpoints = {
#     "/": "Root - Health Check",
#     "/api/health": "API Health",
#     "/api/endpoints": "List All Endpoints",
#     "/api/costs/by-category": "Cost: By Category",
#     "/api/costs/monthly": "Cost: Monthly",
#     "/api/costs/by-product": "Cost: By Product",
#     "/api/costs/top-products": "Cost: Top Products (limit)",
#     "/api/costs/cost-per-unit": "Cost: Per Unit (limit)",
#     "/api/costs/cost-revenue-ratio": "Cost: Revenue Ratio",
#     "/api/analysis/profitability": "Profitability Analysis",
#     "/api/costs/summary": "Cost Summary",
#     "/api/costs/fixed-variable": "Fixed vs Variable Costs",
#     "/api/cashflow/flow-types": "Cash Flow: Flow Types",
#     "/api/cashflow/flow-type-counts": "Cash Flow: Flow Type Counts",
#     "/api/cashflow/summary": "Cash Flow Summary",
#     "/api/cashflow/monthly-net": "Cash Flow: Monthly Net",
#     "/api/cashflow/by-type": "Cash Flow: By Type",
#     "/api/cashflow/top-sources": "Cash Flow: Top Sources (limit)",
#     "/api/cashflow/health-indicators": "Cash Flow: Health Indicators",
#     "/api/cashflow/total-by-type": "Cash Flow: Total by Type",
# }

# st.title("📊 Business Analytics API Tester")

# # Debug mode toggle
# debug_mode = st.checkbox("Enable Debug Mode", value=True)

# # Select endpoint
# selected_endpoint = st.selectbox(
#     "Choose an endpoint to test", 
#     list(endpoints.keys()), 
#     format_func=lambda x: endpoints[x]
# )

# # Query parameters
# params = {}
# if "limit" in selected_endpoint:
#     limit = st.number_input("Enter limit (optional)", min_value=1, step=1, value=5)
#     params["limit"] = limit

# # Headers options
# st.subheader("Request Configuration")
# header_option = st.radio(
#     "Choose header configuration:",
#     ["Minimal Headers", "Browser-like Headers", "Custom Headers"]
# )

# # Define different header sets
# if header_option == "Minimal Headers":
#     headers = {}
# elif header_option == "Browser-like Headers":
#     headers = {
#         'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
#         'Accept': 'application/json, text/plain, */*',
#         'Accept-Language': 'en-US,en;q=0.9',
#         'Accept-Encoding': 'gzip, deflate, br',
#         'Connection': 'keep-alive',
#         'Upgrade-Insecure-Requests': '1'
#     }
# else:  # Custom Headers
#     st.write("Add custom headers (one per line, format: key: value)")
#     custom_headers_text = st.text_area("Custom Headers", "")
#     headers = {}
#     if custom_headers_text:
#         for line in custom_headers_text.strip().split('\n'):
#             if ':' in line:
#                 key, value = line.split(':', 1)
#                 headers[key.strip()] = value.strip()

# # Timeout setting
# timeout = st.slider("Request Timeout (seconds)", min_value=5, max_value=60, value=30)

# # Trigger request
# if st.button("Send Request"):
#     try:
#         url = BASE_URL + selected_endpoint
        
#         if debug_mode:
#             st.subheader("🔍 Debug Information")
#             st.write(f"**Full URL:** {url}")
#             st.write(f"**Parameters:** {params if params else 'None'}")
#             st.write(f"**Headers:**")
#             if headers:
#                 for key, value in headers.items():
#                     st.write(f"  - {key}: {value}")
#             else:
#                 st.write("  - No custom headers")
        
#         # Make the request with detailed error handling
#         response = requests.get(
#             url, 
#             params=params, 
#             headers=headers,
#             timeout=timeout,
#             allow_redirects=True
#         )
        
#         if debug_mode:
#             st.write(f"**Response Status Code:** {response.status_code}")
#             st.write(f"**Response Headers:**")
#             for key, value in response.headers.items():
#                 st.write(f"  - {key}: {value}")
        
#         # Check if the response is successful
#         response.raise_for_status()
        
#         # Try to parse JSON
#         try:
#             json_data = response.json()
#             st.success("✅ Request successful")
#             st.json(json_data)
#         except json.JSONDecodeError:
#             st.success("✅ Request successful (Non-JSON response)")
#             st.text(response.text)
            
#     except requests.exceptions.Timeout:
#         st.error("⏰ Request timed out")
#     except requests.exceptions.ConnectionError:
#         st.error("🔌 Connection error - Unable to reach the server")
#     except requests.exceptions.HTTPError as e:
#         st.error(f"❌ HTTP Error: {e}")
#         if debug_mode and hasattr(e, 'response'):
#             st.write(f"**Response Status:** {e.response.status_code}")
#             st.write(f"**Response Text:** {e.response.text}")
#     except requests.exceptions.RequestException as e:
#         st.error(f"❌ Request failed: {e}")
#         if debug_mode:
#             st.write(f"**Error Type:** {type(e).__name__}")
#             st.write(f"**Error Details:** {str(e)}")

# # Test with curl command
# st.subheader("🔧 Alternative: Test with cURL")
# curl_url = BASE_URL + selected_endpoint
# if params:
#     param_string = "&".join([f"{k}={v}" for k, v in params.items()])
#     curl_url += f"?{param_string}"

# st.code(f'curl -X GET "{curl_url}"', language='bash')

# # Quick connectivity test
# if st.button("Test Base URL Connectivity"):
#     try:
#         response = requests.get(BASE_URL, timeout=10)
#         st.success(f"✅ Base URL accessible - Status: {response.status_code}")
#     except Exception as e:
#         st.error(f"❌ Base URL not accessible: {e}")