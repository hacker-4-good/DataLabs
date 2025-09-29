import dspy 
import streamlit as st
llm = dspy.LM(model="gemini/gemini-2.0-flash", api_key=st.secrets["GOOGLE_API_KEY"])

dspy.settings.configure(lm=llm)

class PlotInsightSignature(dspy.Signature):
    """
    This signature aims to fetch the required insight for given plot
    **start by explaining the domain of plot**
    You are free to elaborate based upon your need just focus on respective domain of question
    """
    plot_figure = dspy.InputField(desc = "This will contain Plotly fig of the plot")
    data = dspy.InputField(desc="This will provide you the dataset on which analysis to be done")
    insights = dspy.OutputField(desc="Provide elaborated insight about the plot possibly in MARKDOWN")

agent = dspy.ChainOfThought(signature = PlotInsightSignature)

def call_agent_bot():
    with st.expander("Plot Insight"):
        bot_response = agent(plot_figure = st.session_state.figure, data = st.session_state.df).insights 
        st.markdown(bot_response)