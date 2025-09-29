import streamlit as st 
import plotly.express as px 
def bar_plot():
    x_axis = st.selectbox("Select X-axis", options=st.session_state.df.columns, key="x_axis")
    y_axis = st.selectbox("Select Y-axis", options=st.session_state.df.columns, key="y_axis")
    if x_axis and y_axis:
        if st.session_state.axes == None:
            fig = px.bar(st.session_state.df, x=x_axis, y=y_axis, title="Bar Plot")
            st.session_state.figure = fig
        else:
            fig = px.bar(st.session_state.df, x=x_axis, y=y_axis, title="Bar Plot").update_layout(xaxis_title=st.session_state.axes['x_axis'], yaxis_title=st.session_state.axes['y_axis'])
            st.session_state.figure = fig 
        with st.container(height=500, border=False):
            st.plotly_chart(fig, use_container_width=True)
    else:
        st.write("Please select both X and Y axes to plot.")