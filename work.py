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
            x_axis = st.selectbox("Select X-axis", options=st.session_state.df.columns, key="x_axis")
            y_axis = st.selectbox("Select Y-axis", options=st.session_state.df.columns, key="y_axis")
            if x_axis and y_axis:
                if st.session_state.axes == None:
                    fig = px.line(st.session_state.df, x=x_axis, y=y_axis, title="Line Plot")
                else:
                    fig = px.line(st.session_state.df, x=x_axis, y=y_axis, title="Line Plot").update_layout(xaxis_title=st.session_state.axes['x_axis'], yaxis_title=st.session_state.axes['y_axis'])
                with st.container(height=500, border=False):
                    st.plotly_chart(fig, use_container_width=True)
            else:
                st.write("Please select both X and Y axes to plot.")
        else:
            st.write("DataFrame is empty. Please add data to plot.")
    elif st.session_state.plot == "Bar Plot":
        if not st.session_state.df.empty:
            x_axis = st.selectbox("Select X-axis", options=st.session_state.df.columns, key="x_axis")
            y_axis = st.selectbox("Select Y-axis", options=st.session_state.df.columns, key="y_axis")
            if x_axis and y_axis:
                if st.session_state.axes == None:
                    fig = px.bar(st.session_state.df, x=x_axis, y=y_axis, title="Bar Plot")
                else:
                    fig = px.bar(st.session_state.df, x=x_axis, y=y_axis, title="Bar Plot").update_layout(xaxis_title=st.session_state.axes['x_axis'], yaxis_title=st.session_state.axes['y_axis'])
                with st.container(height=500, border=False):
                    st.plotly_chart(fig, use_container_width=True)
            else:
                st.write("Please select both X and Y axes to plot.")
        else:
            st.write("DataFrame is empty. Please add data to plot.")
    elif st.session_state.plot == "Scatter Plot":
        if not st.session_state.df.empty:
            x_axis = st.selectbox("Select X-axis", options=st.session_state.df.columns, key="x_axis")
            y_axis = st.selectbox("Select Y-axis", options=st.session_state.df.columns, key="y_axis")
            if x_axis and y_axis:
                if st.session_state.axes == None:
                    fig = px.scatter(st.session_state.df, x=x_axis, y=y_axis, title="Line Plot")
                else:
                    fig = px.scatter(st.session_state.df, x=x_axis, y=y_axis, title="Line Plot").update_layout(xaxis_title=st.session_state.axes['x_axis'], yaxis_title=st.session_state.axes['y_axis'])
                with st.container(height=500, border=False):
                    st.plotly_chart(fig, use_container_width=True)
            else:
                st.write("Please select both X and Y axes to plot.")
        else:
            st.write("DataFrame is empty. Please add data to plot.")
    if st.button("Edit Details"):
        change_data()