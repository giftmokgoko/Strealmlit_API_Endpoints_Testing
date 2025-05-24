import streamlit as st
import requests
import pandas as pd
from io import StringIO


# Base URL of the API
BASE_URL = "https://business-analytics-api-ten.vercel.app"

# List of available endpoints organized by category
endpoints = {
    # Health and Info
    "/": "Root - Health Check",
    "/api/health": "API Health",
    "/api/endpoints": "List All Endpoints",
    
    # Costs Analytics
    "/api/costs/by-category": "Cost: By Category",
    "/api/costs/monthly": "Cost: Monthly",
    "/api/costs/by-product": "Cost: By Product",
    "/api/costs/top-products": "Cost: Top Products (limit)",
    "/api/costs/cost-per-unit": "Cost: Per Unit (limit)",
    "/api/costs/cost-revenue-ratio": "Cost: Revenue Ratio",
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
    "/api/products/low-stock": "Products: Low Stock Alerts",
    "/api/products/profit-margins": "Products: Profit Margins",
    "/api/products/expiring": "Products: Expiring in 30 Days",
    "/api/products/analytics": "Products: Combined Analytics",
    "/api/transactions/revenue": "Transactions: Total Revenue",
    "/api/transactions/top-products": "Transactions: Top Products (limit)",
    "/api/transactions/sales-trends": "Transactions: Monthly Sales Trends",
    "/api/transactions/analytics": "Transactions: Combined Analytics",
    "/api/analytics/dashboard": "Combined: Complete Dashboard",
    "/api/analytics/profitability": "Profitability Analysis",
    "/api/reports/low-stock-csv": "Report: Low Stock Products",
    "/api/reports/expiring-products-csv": "Report: Expiring Products",
    "/api/reports/profit-margins-csv": "Report: Profit Margins",
    "/api/reports/total-revenue-csv": "Report: Total Revenue",
    "/api/reports/top-products-csv": "Report: Top Products (limit)",
    "/api/reports/sales-trends-csv": "Report: Monthly Sales Trends",
    "/api/reports/cost-breakdown-csv": "Report: Cost Breakdown",
    "/api/reports/cost-to-revenue-csv": "Report: Cost-to-Revenue Ratio",
    "/api/reports/net-cash-flow-csv": "Report: Net Cash Flow",
    "/api/reports/cash-flow-trends-csv": "Report: Cash Flow Trends",
    "/api/reports/profit-by-product-csv": "Report: Profit by Product",
    "/api/reports/slow-moving-csv": "Report: Slow-Moving Inventory (threshold)",
    "/api/reports/complete-report": "Report: Complete Analytics Report"
}

st.title("📊 Business Analytics API Tester")


selected_endpoint = st.selectbox("Choose an endpoint to test", list(endpoints.keys()), format_func=lambda x: endpoints[x])

# Query parameters
params = {}
if "limit" in selected_endpoint:
    limit = st.number_input("Enter limit (optional)", min_value=1, step=1, value=5)
    params["limit"] = limit
    
if "threshold" in selected_endpoint:
    threshold = st.number_input("Enter threshold (days)", min_value=1, step=1, value=30)
    params["threshold"] = threshold



# Trigger request
if st.button("Send Request"):
    try:
        url = BASE_URL + selected_endpoint
        response = requests.get(url, params=params)
        response.raise_for_status()
        
        # Handle CSV responses
        if "csv" in selected_endpoint:
            st.success("✅ Request successful")
            st.download_button(
                label="Download CSV",
                data=response.content,
                file_name=selected_endpoint.split("/")[-1] + ".csv",
                mime="text/csv"
            )
        else:
            # Handle JSON responses
            json_data = response.json()
            
            # Display the raw JSON
            st.success("✅ Request successful")
            st.json(json_data)
            
            # Convert to DataFrame 
            try:
                if isinstance(json_data, dict):
                    # Handle different JSON structures
                    if 'data' in json_data and isinstance(json_data['data'], (list, dict)):
                        df = pd.DataFrame(json_data['data'])
                    elif all(isinstance(v, (list, dict)) for v in json_data.values()):
                        df = pd.DataFrame(json_data)
                    else:
                        df = pd.DataFrame([json_data])
                elif isinstance(json_data, list):
                    df = pd.DataFrame(json_data)
                else:
                    df = pd.DataFrame({'value': [json_data]})
                
                # Download for JSON responses for CSV
                csv_data = df.to_csv(index=False)
                st.download_button(
                    label="Download as CSV",
                    data=csv_data,
                    file_name=selected_endpoint.split("/")[-1] + ".csv",
                    mime="text/csv"
                )
                
                st.dataframe(df)
                
            except Exception as e:
                st.warning(f"⚠️ Could not convert response to table format: {str(e)}")
                st.info("Showing raw JSON response only")
                
    except requests.exceptions.RequestException as e:
        st.error(f"❌ Request failed: {e}")


