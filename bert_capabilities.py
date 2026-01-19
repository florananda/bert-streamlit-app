import pandas as pd
from tabulate import tabulate

# BERT capabilities data
data = {
    "Capability": [
        "Sentiment analysis",
        "Question answering",
        "Named entity recognition",
        "Text classification",
        "Text generation"
    ],
    "Status": [
        "✅ Supported",
        "✅ Supported",
        "✅ Supported",
        "✅ Supported",
        "❌ Not designed for this"
    ]
}

# Create DataFrame
df = pd.DataFrame(data)

# GPT capabilities data
gpt_data = {
    "Capability": [
        "Text generation",
        "Story writing",
        "Code completion",
        "Chatbots",
        "Creative writing",
        "Understanding"
    ],
    "Status": [
        "✅ Supported",
        "✅ Supported",
        "✅ Supported",
        "✅ Supported",
        "✅ Supported",
        "⚠️ Good but not primary design"
    ]
}

# Create GPT DataFrame
gpt_df = pd.DataFrame(gpt_data)

# General capabilities data
general_data = {
    "Capability": [
        "Translation",
        "Summarization",
        "Question answering",
        "Classification",
        "Any text transformation"
    ],
    "Status": [
        "✅ Supported",
        "✅ Supported",
        "✅ Supported",
        "✅ Supported",
        "✅ Supported"
    ]
}

# Create General DataFrame
general_df = pd.DataFrame(general_data)

def display_table():
    """Display the BERT capabilities table in terminal."""
    print("\n" + "="*100)
    print("BERT CAPABILITIES")
    print("="*100 + "\n")
    
    # Display using tabulate for better formatting
    print(tabulate(df, headers='keys', tablefmt='grid', showindex=False))
    print("\n" + "="*100 + "\n")
    
    print("GPT CAPABILITIES")
    print("="*100 + "\n")
    print(tabulate(gpt_df, headers='keys', tablefmt='grid', showindex=False))
    print("\n" + "="*100 + "\n")
    
    print("GENERAL CAPABILITIES")
    print("="*100 + "\n")
    print(tabulate(general_df, headers='keys', tablefmt='grid', showindex=False))
    print("\n" + "="*100 + "\n")

def display_table_streamlit():
    """Display the BERT capabilities table in Streamlit with styling."""
    import streamlit as st
    
    st.subheader("BERT CAPABILITIES")
    
    # Create styled HTML table
    html = """
    <style>
    .capability-table {
        width: 100%;
        border-collapse: collapse;
        margin: 20px 0;
        font-family: Arial, sans-serif;
    }
    .capability-table th {
        background-color: #1f1f1f;
        color: white;
        padding: 12px;
        text-align: left;
        font-weight: bold;
        border: 1px solid #ddd;
    }
    .capability-table td {
        padding: 12px;
        border: 1px solid #ddd;
        color: #1f1f1f;
        background-color: #ffffff;
    }
    .capability-table tr:nth-child(even) {
        background-color: #f9f9f9;
    }
    .capability-table tr:hover {
        background-color: #f0f0f0;
        transition: background-color 0.3s ease;
    }
    .supported {
        color: #2e7d32;
        font-weight: 500;
    }
    .not-supported {
        color: #c62828;
        font-weight: 500;
    }
    .warning {
        color: #f57c00;
        font-weight: 500;
    }
    </style>
    <table class="capability-table">
        <thead>
            <tr>
                <th>Capability</th>
                <th>Status</th>
            </tr>
        </thead>
        <tbody>
    """
    
    for _, row in df.iterrows():
        capability = row["Capability"]
        status = row["Status"]
        # Determine CSS class based on status
        status_class = "supported" if "✅" in status else "not-supported"
        # Escape HTML special characters
        capability_escaped = capability.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")
        status_escaped = status.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")
        html += f'<tr><td><strong>{capability_escaped}</strong></td><td class="{status_class}">{status_escaped}</td></tr>'
    
    html += """
        </tbody>
    </table>
    """
    
    st.markdown(html, unsafe_allow_html=True)
    
    # Also display as dataframe for better mobile compatibility
    with st.expander("View as DataFrame"):
        st.dataframe(df, use_container_width=True, hide_index=True)
    
    # Display GPT capabilities table
    st.subheader("GPT CAPABILITIES")
    
    # Create styled HTML table for GPT
    gpt_html = """
    <table class="capability-table">
        <thead>
            <tr>
                <th>Capability</th>
                <th>Status</th>
            </tr>
        </thead>
        <tbody>
    """
    
    for _, row in gpt_df.iterrows():
        capability = row["Capability"]
        status = row["Status"]
        # Determine CSS class based on status
        if "✅" in status:
            status_class = "supported"
        elif "⚠️" in status:
            status_class = "warning"
        else:
            status_class = "not-supported"
        # Escape HTML special characters
        capability_escaped = capability.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")
        status_escaped = status.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")
        gpt_html += f'<tr><td><strong>{capability_escaped}</strong></td><td class="{status_class}">{status_escaped}</td></tr>'
    
    gpt_html += """
        </tbody>
    </table>
    """
    
    st.markdown(gpt_html, unsafe_allow_html=True)
    
    # Also display as dataframe for better mobile compatibility
    with st.expander("View GPT as DataFrame"):
        st.dataframe(gpt_df, use_container_width=True, hide_index=True)
    
    # Display General capabilities table
    st.subheader("GENERAL CAPABILITIES")
    
    # Create styled HTML table for General
    general_html = """
    <table class="capability-table">
        <thead>
            <tr>
                <th>Capability</th>
                <th>Status</th>
            </tr>
        </thead>
        <tbody>
    """
    
    for _, row in general_df.iterrows():
        capability = row["Capability"]
        status = row["Status"]
        # Determine CSS class based on status
        if "✅" in status:
            status_class = "supported"
        elif "⚠️" in status:
            status_class = "warning"
        else:
            status_class = "not-supported"
        # Escape HTML special characters
        capability_escaped = capability.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")
        status_escaped = status.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")
        general_html += f'<tr><td><strong>{capability_escaped}</strong></td><td class="{status_class}">{status_escaped}</td></tr>'
    
    general_html += """
        </tbody>
    </table>
    """
    
    st.markdown(general_html, unsafe_allow_html=True)
    
    # Also display as dataframe for better mobile compatibility
    with st.expander("View General as DataFrame"):
        st.dataframe(general_df, use_container_width=True, hide_index=True)

def get_dataframe():
    """Return the BERT DataFrame for use in other scripts."""
    return df

def get_gpt_dataframe():
    """Return the GPT DataFrame for use in other scripts."""
    return gpt_df

def get_general_dataframe():
    """Return the General DataFrame for use in other scripts."""
    return general_df

if __name__ == "__main__":
    # Check if running in Streamlit
    try:
        import streamlit as st
        # If streamlit is imported, create a simple app
        st.set_page_config(page_title="Model Capabilities", page_icon="")
        st.title("Model Capabilities")
        display_table_streamlit()
    except:
        # Otherwise, display in terminal
        display_table()
