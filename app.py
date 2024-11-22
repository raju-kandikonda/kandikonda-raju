import streamlit as st

# Title and Description
st.title("Cricket Score Predictor 🏏")
st.markdown("""
Welcome to the **Cricket Score Predictor**! 
Input the current overs, current runs, and total overs to predict the possible final score of the team. 🚀
""")

# Input Section
st.header("Input Match Details")
total_overs = st.number_input("Enter Total Overs in the Match:", min_value=1, max_value=50, value=20, step=1)
current_overs = st.number_input("Enter Current Overs Completed:", min_value=0.0, max_value=float(total_overs), value=5.0, step=0.1)
current_runs = st.number_input("Enter Current Runs Scored:", min_value=0, value=30, step=1)

# Simple Run Rate Extrapolation Logic
if current_overs > 0:
    current_run_rate = current_runs / current_overs
    projected_score = current_run_rate * total_overs
else:
    current_run_rate = 0
    projected_score = 0

# Display Results
st.header("Predicted Final Score")
if current_overs <= total_overs and current_runs >= 0:
    st.metric("Current Run Rate", f"{current_run_rate:.2f} runs/over")
    st.metric("Predicted Score", f"{int(projected_score)} runs")
else:
    st.error("Please check your inputs. Overs or runs entered seem invalid!")

# Extra Feature: Information Section
st.sidebar.title("About the App")
st.sidebar.info("""
This app uses a basic **run-rate extrapolation model** to predict the final score.
Future versions may include more advanced models considering fall of wickets, historical data, and pitch conditions.
""")
st.sidebar.markdown("Developed by: Raju")
