import streamlit as st
import pandas as pd

st.set_page_config(
    page_title="GPT Model Analysis",
    page_icon="🤖",
    layout="wide"
)

st.title("🤖 GPT Model Analysis")

# Prepare data
data = {
    "Category": [
        "WHY IT WORKS",
        "WHY IT WORKS",
        "WHY IT WORKS",
        "WHY IT WORKS",
        "LIMITATIONS",
        "LIMITATIONS",
        "LIMITATIONS"
    ],
    "Point": [
        "Natural text generation",
        "No mismatch between training and inference",
        "Every token contributes to training",
        "Scales to arbitrary lengths",
        "Only left-to-right context",
        "Can't revise earlier predictions",
        "May generate inconsistent text"
    ]
}

df = pd.DataFrame(data)

# Function to create styled HTML table
def create_styled_table(df):
    html = """
    <style>
    .GPT-table {
        width: 100%;
        border-collapse: collapse;
        margin: 20px 0;
        font-family: Arial, sans-serif;
    }
    .GPT-table th {
        background-color: #1f1f1f;
        color: white;
        padding: 12px;
        text-align: left;
        font-weight: bold;
        border: 1px solid #ddd;
    }
    .GPT-table td {
        padding: 12px;
        border: 1px solid #ddd;
    }
    .why-it-works {
        background-color: #E8F5E9;
        transition: background-color 0.3s ease, transform 0.2s ease, box-shadow 0.3s ease;
    }
    .why-it-works:hover {
        background-color: #C8E6C9;
        transform: scale(1.01);
        box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2);
        cursor: pointer;
    }
    .limitations {
        background-color: #FFEBEE;
        transition: background-color 0.3s ease, transform 0.2s ease, box-shadow 0.3s ease;
    }
    .limitations:hover {
        background-color: #FFCDD2;
        transform: scale(1.01);
        box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2);
        cursor: pointer;
    }
    </style>
    <table class="GPT-table">
        <thead>
            <tr>
                <th>Category</th>
                <th>Point</th>
            </tr>
        </thead>
        <tbody>
    """
    
    for _, row in df.iterrows():
        category = row["Category"]
        point = row["Point"]
        css_class = "why-it-works" if category == "WHY IT WORKS" else "limitations"
        html += f'<tr class="{css_class}"><td>{category}</td><td>{point}</td></tr>'
    
    html += """
        </tbody>
    </table>
    """
    
    return html

# Function to export table as CSV
def export_to_csv(df):
    """Export DataFrame to CSV format."""
    return df.to_csv(index=False).encode('utf-8')

# Display styled table
st.markdown(create_styled_table(df), unsafe_allow_html=True)

# CSV Export button
csv = export_to_csv(df)
st.download_button(
    label="📥 Download table as CSV",
    data=csv,
    file_name="GPT_model_analysis.csv",
    mime="text/csv",
    help="Click to download the table as a CSV file"
)

# Optional: Display dataframe as well (for reference)
with st.expander("View as DataFrame"):
    st.dataframe(df, use_container_width=True)
