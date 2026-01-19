import pandas as pd
from tabulate import tabulate

# Task examples data
data = {
    "Task": [
        "TRANSLATION",
        "SUMMARIZATION",
        "CLASSIFICATION",
        "Q&A",
        "GRAMMAR CORRECTION"
    ],
    "Input": [
        "translate English to French: Hello, world!",
        "summarize: [1000 word article]",
        "sst2 sentence: This movie is great!",
        "question: What is the capital? context: France is a country. Paris is its capital.",
        "grammar: She go to school yesterday"
    ],
    "Output": [
        "Bonjour, le monde!",
        "[50 word summary]",
        "positive",
        "Paris",
        "She went to school yesterday"
    ]
}

# Create DataFrame
df = pd.DataFrame(data)

def display_table():
    """Display the task examples table in terminal."""
    print("\n" + "="*100)
    print("TASK EXAMPLES")
    print("="*100 + "\n")
    
    # Display using tabulate for better formatting
    print(tabulate(df, headers='keys', tablefmt='grid', showindex=False))
    print("\n" + "="*100 + "\n")

def display_table_streamlit():
    """Display the task examples table in Streamlit with styling."""
    import streamlit as st
    
    st.subheader("TASK EXAMPLES")
    
    # Create styled HTML table
    html = """
    <style>
    .task-table {
        width: 100%;
        border-collapse: collapse;
        margin: 20px 0;
        font-family: Arial, sans-serif;
    }
    .task-table th {
        background-color: #1f1f1f;
        color: white;
        padding: 12px;
        text-align: left;
        font-weight: bold;
        border: 1px solid #ddd;
    }
    .task-table td {
        padding: 12px;
        border: 1px solid #ddd;
        color: #1f1f1f;
        background-color: #ffffff;
    }
    .task-table tr:nth-child(even) {
        background-color: #f9f9f9;
    }
    .task-table tr:hover {
        background-color: #f0f0f0;
        transition: background-color 0.3s ease;
    }
    </style>
    <table class="task-table">
        <thead>
            <tr>
                <th>Task</th>
                <th>Input</th>
                <th>Output</th>
            </tr>
        </thead>
        <tbody>
    """
    
    for _, row in df.iterrows():
        task = row["Task"]
        input_text = row["Input"].replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")
        output = row["Output"].replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")
        html += f'<tr><td><strong>{task}</strong></td><td>{input_text}</td><td>{output}</td></tr>'
    
    html += """
        </tbody>
    </table>
    """
    
    st.markdown(html, unsafe_allow_html=True)
    
    # Also display as dataframe for better mobile compatibility
    with st.expander("View as DataFrame"):
        st.dataframe(df, use_container_width=True, hide_index=True)

def get_dataframe():
    """Return the DataFrame for use in other scripts."""
    return df

if __name__ == "__main__":
    # Check if running in Streamlit
    try:
        import streamlit as st
        # If streamlit is imported, create a simple app
        st.set_page_config(page_title="Task Examples", page_icon="")
        st.title("Task Examples")
        display_table_streamlit()
    except:
        # Otherwise, display in terminal
        display_table()
