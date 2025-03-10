import streamlit as st

from llm_utils import generate_output
from prompts import python_assistant_prompts

st.set_page_config(page_title="Techolution ", page_icon="image.png", layout="wide", initial_sidebar_state="auto", menu_items=None)
# st.image("image.png", "Sky is the limit")
st.title('Techolution Python Assistant')

problem_lst  = [None, "Factorial of Number using Recurrison",
 "Read CSV file, filter rows where a column name is age and value is greater than 30. Writer result to new CSV file",
 "Python solution for knapsack problem using Dynamic programming also explain the time complexity"]

problem = st.selectbox(
        'Select the problem from Listed below',
        problem_lst
    )

model = ["o1-preview", "gpt-3.5-turbo", "gpt-4", "gpt-4o-mini"]

question = st.text_area("Enter your custom Python statement" , problem)

option = st.selectbox(
        'Select the model',
        model
    )

submit_button = st.button('Submit')


if submit_button:

    res = generate_output(python_assistant_prompts + problem, model=option)
    st.write(res)
