import streamlit as st
import pandas as pd
import plotly.express as px

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
    df = st.data_editor(st.session_state.df, num_rows="dynamic")

    if st.button("Add Column"):
        new_column_name = f"h({chr(65 + len(st.session_state.df.columns))})" # Generate column names like h(C), h(D), etc.
        st.session_state.df[new_column_name] = None
        st.rerun()

    if st.button("Add Row"):
        new_row_index = len(st.session_state.df)
        st.session_state.df.loc[new_row_index] = [None] * len(st.session_state.df.columns)
        st.rerun()

    if st.button("Save"):
        st.session_state.df = df

with plot_tabs:
    st.write("Plotting")

    if not st.session_state.df.empty:
        x_axis = st.selectbox("Select X-axis", options=st.session_state.df.columns, key="x_axis")
        y_axis = st.selectbox("Select Y-axis", options=st.session_state.df.columns, key="y_axis")

        if x_axis and y_axis:
            fig = px.line(st.session_state.df, x=x_axis, y=y_axis, title="Line Plot")
            with st.container(height=500, border=False):
                st.plotly_chart(fig, use_container_width=True)
        else:
            st.write("Please select both X and Y axes to plot.")
    else:
        st.write("DataFrame is empty. Please add data to plot.")