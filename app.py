import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import streamlit as st
from plotly.subplots import make_subplots
import pickle

with open('battery_data.pkl', 'rb') as pickle_file:
    battery_dict = pickle.load(pickle_file)

df = pd.read_csv("updated_metadata.csv")
df_discharge = df[df['type'] == 'discharge']
def plot_battery_data(battery_id,battery_dict=battery_dict, df_discharge=df_discharge):

    # Check if battery_id exists in the dataset
    if battery_id not in battery_dict:
        print(f"Battery ID {battery_id} not found in the dataset.")
        return

    # Extract data
    data = battery_dict[battery_id]
    df_battery = df_discharge[df_discharge['battery_id'] == battery_id]

    # Create subplots
    fig = make_subplots(
        rows=3, cols=1,
        subplot_titles=('Re vs Cycle Number', 'Rct vs Cycle Number', 'Capacity vs Cycle Number'),
        vertical_spacing=0.15
    )
    
    # Plot Re
    fig.add_trace(
        go.Scatter(x=data['cycle'], y=data['Re'], name=f'{battery_id} - Re', mode='lines+markers'),
        row=1, col=1
    )
    
    # Plot Rct
    fig.add_trace(
        go.Scatter(x=data['cycle'], y=data['Rct'], name=f'{battery_id} - Rct', mode='lines+markers'),
        row=2, col=1
    )
    
    # Plot Capacity
    fig.add_trace(
        go.Scatter(x=df_battery["cycle"], y=df_battery["Capacity"], name=f'{battery_id} - Capacity', mode='lines+markers'),
        row=3, col=1
    )
    
    # Update layout
    fig.update_layout(
        height=1000,
        showlegend=True,
        title_text=f"Battery {battery_id} Parameters vs Cycle Number"
    )
    fig.update_xaxes(title_text="Cycle Number", row=1, col=1)
    fig.update_xaxes(title_text="Cycle Number", row=2, col=1)
    fig.update_xaxes(title_text="Cycle Number", row=3, col=1)
    fig.update_yaxes(title_text="Re (Ohms)", row=1, col=1)
    fig.update_yaxes(title_text="Rct (Ohms)", row=2, col=1)
    fig.update_yaxes(title_text="Capacity", row=3, col=1)

    return fig


# Streamlit Application
st.title("Battery Data Visualization")

# Input field for battery ID
battery_id = st.text_input("Enter Battery ID:")

# Check if battery ID is provided
if battery_id:
    fig = plot_battery_data(battery_id)
    if fig:
        st.plotly_chart(fig)

