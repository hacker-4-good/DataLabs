import streamlit as st
import pandas as pd
from plots.basic_charts.line_plot import line_plot
from plots.basic_charts.bar_plot import bar_plot
from plots.basic_charts.scatter_plot import scatter_plot
from agent import call_agent_bot

st.set_page_config(page_title="DataLabs Visualization Tool", layout="wide")

st.title(":blue[DataLabs] :green[Visualization] :red[Tool]")

data_tabs, plot_tabs = st.tabs(tabs=["Data", "Plot"])

@st.cache_data
def get_initial_dataframe():
    return pd.DataFrame(columns=[], index=pd.RangeIndex(start=0, stop=0, step=1))

if "df" not in st.session_state:
    st.session_state.df = get_initial_dataframe()

with data_tabs:
    st.write("Current DataFrame:")
    uploaded_csv = st.file_uploader("Upload Data", type="csv")
    if uploaded_csv is not None:
        dataframe = pd.read_csv(uploaded_csv)
        st.session_state.df = dataframe
    df = st.data_editor(st.session_state.df, num_rows="dynamic")

    if st.button("Add Column"):
        new_column_name = f"h({chr(65 + len(st.session_state.df.columns))})"
        st.session_state.df[new_column_name] = None
        st.rerun()

    if st.button("Add Row"):
        new_row_index = len(st.session_state.df)
        st.session_state.df.loc[new_row_index] = [None] * len(st.session_state.df.columns)
        st.rerun()

    if st.button("Save"):
        st.session_state.df = df

with plot_tabs:
    plot = st.selectbox("Select which type of plot", options = ("Line Plot", "Scatter Plot", "Bar Plot"))
    if "plot" not in st.session_state:
        st.session_state.plot = None 
    if "axes" not in st.session_state:
        st.session_state.axes = None
    if "figure" not in st.session_state:
        st.session_state.figure = None
    @st.dialog("Change the axis data")
    def change_data():
        st.write("Mention the x-axis and y-axis name")
        x_axis = st.text_input(label="Text to display on X-axis")
        y_axis = st.text_input(label="Text to display on Y-axis")
        if st.button("Make Changes"):
            st.session_state.axes = {"x_axis": x_axis, "y_axis": y_axis}
            st.rerun()
    st.session_state.plot = plot 
    st.write("Plotting")

    if st.session_state.plot == "Line Plot":
        if not st.session_state.df.empty:
            line_plot()
        else:
            st.write("DataFrame is empty. Please add data to plot.")
    elif st.session_state.plot == "Bar Plot":
        if not st.session_state.df.empty:
            bar_plot()
        else:
            st.write("DataFrame is empty. Please add data to plot.")
    elif st.session_state.plot == "Scatter Plot":
        if not st.session_state.df.empty:
            scatter_plot()
        else:
            st.write("DataFrame is empty. Please add data to plot.")
    call_agent_bot()
    if st.button("Edit Details"):
        change_data()
