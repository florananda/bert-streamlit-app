import pandas as pd
from tabulate import tabulate
import streamlit as st

def display_attention_patterns_streamlit():
    """Display attention patterns comparison in Streamlit."""
    st.subheader("ATTENTION PATTERNS")
    
    html = """
    <style>
    .attention-box {
        border: 2px solid #1f1f1f;
        border-radius: 5px;
        padding: 15px;
        margin: 15px 0;
        background-color: #f9f9f9;
        font-family: 'Courier New', monospace;
        font-size: 14px;
    }
    .attention-header {
        font-weight: bold;
        margin-bottom: 10px;
        color: #1f1f1f;
    }
    .attention-row {
        margin: 5px 0;
        padding: 3px;
    }
    .attention-label {
        display: inline-block;
        width: 60px;
        font-weight: bold;
    }
    .check-mark {
        color: #2e7d32;
        font-weight: bold;
    }
    .cross-mark {
        color: #c62828;
        font-weight: bold;
    }
    .divider {
        border-top: 1px solid #1f1f1f;
        margin: 15px 0;
    }
    </style>
    
    <div class="attention-box">
        <div class="attention-header">BERT (Bidirectional Encoder)</div>
        <div class="attention-row">
            <span style="width: 100px; display: inline-block;">&nbsp;</span>
            <span>The</span> <span>cat</span> <span>sat</span> <span>on</span> <span>mat</span>
        </div>
        <div class="attention-row">
            <span class="attention-label">The</span>
            <span class="check-mark">✅</span> <span class="check-mark">✅</span> <span class="check-mark">✅</span> <span class="check-mark">✅</span> <span class="check-mark">✅</span>
            <span style="color: #666; margin-left: 10px;">← Full context</span>
        </div>
        <div class="attention-row">
            <span class="attention-label">cat</span>
            <span class="check-mark">✅</span> <span class="check-mark">✅</span> <span class="check-mark">✅</span> <span class="check-mark">✅</span> <span class="check-mark">✅</span>
            <span style="color: #666; margin-left: 10px;">← Full context</span>
        </div>
        <div class="attention-row">
            <span class="attention-label">sat</span>
            <span class="check-mark">✅</span> <span class="check-mark">✅</span> <span class="check-mark">✅</span> <span class="check-mark">✅</span> <span class="check-mark">✅</span>
            <span style="color: #666; margin-left: 10px;">← Full context</span>
        </div>
        <div class="attention-row">
            <span class="attention-label">on</span>
            <span class="check-mark">✅</span> <span class="check-mark">✅</span> <span class="check-mark">✅</span> <span class="check-mark">✅</span> <span class="check-mark">✅</span>
            <span style="color: #666; margin-left: 10px;">← Full context</span>
        </div>
        <div class="attention-row">
            <span class="attention-label">mat</span>
            <span class="check-mark">✅</span> <span class="check-mark">✅</span> <span class="check-mark">✅</span> <span class="check-mark">✅</span> <span class="check-mark">✅</span>
            <span style="color: #666; margin-left: 10px;">← Full context</span>
        </div>
    </div>
    
    <div class="attention-box">
        <div class="attention-header">GPT (Causal Decoder)</div>
        <div class="attention-row">
            <span style="width: 100px; display: inline-block;">&nbsp;</span>
            <span>The</span> <span>cat</span> <span>sat</span> <span>on</span> <span>mat</span>
        </div>
        <div class="attention-row">
            <span class="attention-label">The</span>
            <span class="check-mark">✅</span> <span class="cross-mark">❌</span> <span class="cross-mark">❌</span> <span class="cross-mark">❌</span> <span class="cross-mark">❌</span>
            <span style="color: #666; margin-left: 10px;">← Past only</span>
        </div>
        <div class="attention-row">
            <span class="attention-label">cat</span>
            <span class="check-mark">✅</span> <span class="check-mark">✅</span> <span class="cross-mark">❌</span> <span class="cross-mark">❌</span> <span class="cross-mark">❌</span>
            <span style="color: #666; margin-left: 10px;">← Past only</span>
        </div>
        <div class="attention-row">
            <span class="attention-label">sat</span>
            <span class="check-mark">✅</span> <span class="check-mark">✅</span> <span class="check-mark">✅</span> <span class="cross-mark">❌</span> <span class="cross-mark">❌</span>
            <span style="color: #666; margin-left: 10px;">← Past only</span>
        </div>
        <div class="attention-row">
            <span class="attention-label">on</span>
            <span class="check-mark">✅</span> <span class="check-mark">✅</span> <span class="check-mark">✅</span> <span class="check-mark">✅</span> <span class="cross-mark">❌</span>
            <span style="color: #666; margin-left: 10px;">← Past only</span>
        </div>
        <div class="attention-row">
            <span class="attention-label">mat</span>
            <span class="check-mark">✅</span> <span class="check-mark">✅</span> <span class="check-mark">✅</span> <span class="check-mark">✅</span> <span class="check-mark">✅</span>
            <span style="color: #666; margin-left: 10px;">← Past only</span>
        </div>
    </div>
    
    <div class="attention-box">
        <div class="attention-header">T5 (Encoder-Decoder)</div>
        <div class="attention-row">
            <strong>ENCODER:</strong> Full bidirectional (like BERT)
        </div>
        <div class="attention-row">
            <strong>DECODER:</strong> Causal (like GPT)
        </div>
        <div class="attention-row">
            <strong>CROSS-ATTENTION:</strong> Decoder attends to encoder
        </div>
    </div>
    """
    
    st.markdown(html, unsafe_allow_html=True)

def display_use_case_strengths_streamlit():
    """Display use case strengths comparison table."""
    st.subheader("USE CASE STRENGTHS")
    
    # Create DataFrame
    data = {
        "Task": ["Classify", "Q&A", "Generate", "Chat", "Translate", "Summarize"],
        "BERT": ["⭐⭐⭐⭐⭐", "⭐⭐⭐⭐⭐", "⭐", "⭐⭐", "⭐⭐⭐", "⭐⭐"],
        "GPT": ["⭐⭐⭐", "⭐⭐⭐⭐", "⭐⭐⭐⭐⭐", "⭐⭐⭐⭐⭐", "⭐⭐⭐⭐", "⭐⭐⭐⭐"],
        "T5": ["⭐⭐⭐⭐", "⭐⭐⭐⭐⭐", "⭐⭐⭐⭐", "⭐⭐⭐⭐", "⭐⭐⭐⭐⭐", "⭐⭐⭐⭐⭐"]
    }
    
    df = pd.DataFrame(data)
    
    # Create styled HTML table
    html = """
    <style>
    .strength-table-container {
        overflow-x: auto;
        margin: 20px 0;
    }
    .strength-table {
        width: 100%;
        border-collapse: collapse;
        margin: 0;
        font-family: Arial, sans-serif;
        font-size: 14px;
        min-width: 400px;
    }
    .strength-table th {
        background-color: #1f1f1f;
        color: white;
        padding: 8px 6px;
        text-align: center;
        font-weight: bold;
        border: 1px solid #ddd;
        font-size: 12px;
    }
    .strength-table td {
        padding: 8px 6px;
        border: 1px solid #ddd;
        text-align: center;
        color: #1f1f1f;
        background-color: #ffffff;
        font-size: 12px;
    }
    .strength-table tr:nth-child(even) {
        background-color: #f9f9f9;
    }
    .strength-table tr:hover {
        background-color: #f0f0f0;
    }
    .task-col {
        font-weight: bold;
        text-align: left !important;
        font-size: 11px;
        padding: 8px 4px !important;
    }
    @media (max-width: 768px) {
        .strength-table {
            font-size: 11px;
            min-width: 350px;
        }
        .strength-table th {
            padding: 6px 4px;
            font-size: 10px;
        }
        .strength-table td {
            padding: 6px 4px;
            font-size: 10px;
        }
        .task-col {
            font-size: 9px;
            padding: 6px 3px !important;
        }
    }
    @media (max-width: 480px) {
        .strength-table {
            font-size: 10px;
            min-width: 300px;
        }
        .strength-table th {
            padding: 5px 3px;
            font-size: 9px;
        }
        .strength-table td {
            padding: 5px 3px;
            font-size: 9px;
        }
        .task-col {
            font-size: 8px;
            padding: 5px 2px !important;
        }
    }
    </style>
    <div class="strength-table-container">
    <table class="strength-table">
    <table class="strength-table">
        <thead>
            <tr>
                <th>Task</th>
                <th>BERT</th>
                <th>GPT</th>
                <th>T5</th>
            </tr>
        </thead>
        <tbody>
    """
    
    for _, row in df.iterrows():
        task = row["Task"]
        bert = row["BERT"]
        gpt = row["GPT"]
        t5 = row["T5"]
        html += f'<tr><td class="task-col">{task}</td><td>{bert}</td><td>{gpt}</td><td>{t5}</td></tr>'
    
    html += """
        </tbody>
    </table>
    </div>
    """
    
    st.markdown(html, unsafe_allow_html=True)
    
    # Also display as dataframe
    with st.expander("View as DataFrame"):
        st.dataframe(df, use_container_width=True, hide_index=True)

def display_training_efficiency_streamlit():
    """Display training efficiency comparison."""
    st.subheader("TRAINING EFFICIENCY")
    
    html = """
    <style>
    .efficiency-container {
        margin: 20px 0;
        font-family: Arial, sans-serif;
    }
    .efficiency-item {
        margin: 15px 0;
        padding: 10px;
    }
    .efficiency-label {
        display: inline-block;
        width: 80px;
        font-weight: bold;
        color: #1f1f1f;
    }
    .efficiency-bar {
        display: inline-block;
        height: 25px;
        background-color: #4CAF50;
        border-radius: 3px;
        margin-left: 10px;
        vertical-align: middle;
        line-height: 25px;
        color: white;
        padding: 0 10px;
        font-weight: bold;
        font-size: 12px;
    }
    .bar-80 {
        width: 80%;
    }
    .bar-100 {
        width: 100%;
    }
    .bar-90 {
        width: 90%;
    }
    </style>
    <div class="efficiency-container">
        <div class="efficiency-item">
            <span class="efficiency-label">BERT:</span>
            <span class="efficiency-bar bar-80">████████░░ (80% - masked tokens only)</span>
        </div>
        <div class="efficiency-item">
            <span class="efficiency-label">GPT:</span>
            <span class="efficiency-bar bar-100">██████████ (100% - every token predicted)</span>
        </div>
        <div class="efficiency-item">
            <span class="efficiency-label">T5:</span>
            <span class="efficiency-bar bar-90">█████████░ (90% - flexible masking)</span>
        </div>
    </div>
    """
    
    st.markdown(html, unsafe_allow_html=True)

def display_all_streamlit():
    """Display all architecture comparison sections."""
    st.title("🎭 ARCHITECTURE COMPARISON")
    
    display_attention_patterns_streamlit()
    st.markdown("---")
    display_use_case_strengths_streamlit()
    st.markdown("---")
    display_training_efficiency_streamlit()

def display_all_terminal():
    """Display all architecture comparison in terminal."""
    print("\n" + "="*100)
    print("🎭 ARCHITECTURE COMPARISON")
    print("="*100 + "\n")
    
    print("ATTENTION PATTERNS:")
    print("┌──────────────────────────────────────────────────┐")
    print("│ BERT (Bidirectional Encoder)                    │")
    print("│      The  cat  sat  on  mat                     │")
    print("│ The  ✅   ✅   ✅   ✅   ✅  ← Full context     │")
    print("│ cat  ✅   ✅   ✅   ✅   ✅  ← Full context     │")
    print("│ sat  ✅   ✅   ✅   ✅   ✅  ← Full context     │")
    print("│ on   ✅   ✅   ✅   ✅   ✅  ← Full context     │")
    print("│ mat  ✅   ✅   ✅   ✅   ✅  ← Full context     │")
    print("├──────────────────────────────────────────────────┤")
    print("│ GPT (Causal Decoder)                            │")
    print("│      The  cat  sat  on  mat                     │")
    print("│ The  ✅   ❌   ❌   ❌   ❌  ← Past only        │")
    print("│ cat  ✅   ✅   ❌   ❌   ❌  ← Past only        │")
    print("│ sat  ✅   ✅   ✅   ❌   ❌  ← Past only        │")
    print("│ on   ✅   ✅   ✅   ✅   ❌  ← Past only        │")
    print("│ mat  ✅   ✅   ✅   ✅   ✅  ← Past only        │")
    print("├──────────────────────────────────────────────────┤")
    print("│ T5 (Encoder-Decoder)                            │")
    print("│ ENCODER: Full bidirectional (like BERT)         │")
    print("│ DECODER: Causal (like GPT)                      │")
    print("│ CROSS-ATTENTION: Decoder attends to encoder     │")
    print("└──────────────────────────────────────────────────┘")
    print("\n")
    
    print("USE CASE STRENGTHS:")
    data = {
        "Task": ["Classify", "Q&A", "Generate", "Chat", "Translate", "Summarize"],
        "BERT": ["⭐⭐⭐⭐⭐", "⭐⭐⭐⭐⭐", "⭐", "⭐⭐", "⭐⭐⭐", "⭐⭐"],
        "GPT": ["⭐⭐⭐", "⭐⭐⭐⭐", "⭐⭐⭐⭐⭐", "⭐⭐⭐⭐⭐", "⭐⭐⭐⭐", "⭐⭐⭐⭐"],
        "T5": ["⭐⭐⭐⭐", "⭐⭐⭐⭐⭐", "⭐⭐⭐⭐", "⭐⭐⭐⭐", "⭐⭐⭐⭐⭐", "⭐⭐⭐⭐⭐"]
    }
    df = pd.DataFrame(data)
    print(tabulate(df, headers='keys', tablefmt='grid', showindex=False))
    print("\n")
    
    print("TRAINING EFFICIENCY:")
    print("BERT:  ████████░░ (80% - masked tokens only)")
    print("GPT:   ██████████ (100% - every token predicted)")
    print("T5:    █████████░ (90% - flexible masking)")
    print("\n" + "="*100 + "\n")

if __name__ == "__main__":
    # Check if running in Streamlit
    try:
        import streamlit as st
        st.set_page_config(page_title="Architecture Comparison", page_icon="🎭", layout="wide")
        display_all_streamlit()
    except:
        # Otherwise, display in terminal
        display_all_terminal()
