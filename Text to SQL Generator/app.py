from dotenv import load_dotenv
load_dotenv()

import streamlit as st
import os
import sqlite3

import google.generativeai as genai

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

## Function To Load Goolge Gemini Model
def get_gemini_response(question, prompt):
    model=genai.GenerativeModel('gemini-pro')
    response=model.generate_content([prompt[0], question])
    print(response.text)
    return response.text


## Function to retrieve query from the database
def read_sql_query(sql, db):
    conn=sqlite3.connect(db)
    cur=conn.cursor()
    data=cur.execute(sql)
    data=cur.fetchall()
    st.header("Data :")
    for row in data:
        print(row)
        st.text(row)
    
    
    cur.close()
    conn.commit()
    conn.close()
    return data


prompt=[
    """
    You are an expert in transalating a query in English to equivalent SQL query!
    The name of the SQL database is STUDENT. It has the following columns - NAME, CLASS, SECTION, MARKS. 
    First three fields are of datatype varchar(25), MARKS is of INT type.

    
    Examples:

    Example 1:
    Q. There are how many entries in the database?
    A. SELECT COUNT(*) FROM student;

    Example 2:
    Q. How many students are in 'Data Science' class?
    A. SELECT COUNT(*) FROM student WHERE class='Data Science';

    Note: Generate only the SQL query without any extra information. The sql query should be compatible with SQLite and can be executed successfully.
    Donot add any ``` before or after the generated text. 
    """
]


# Streamlit App
st.set_page_config(page_title="Create Any SQL Query")
st.header("Gemini App to generate SQL queries")

question=st.text_input("Input: ", key="input")

submit=st.button("Ask the question")

# if submit is clicked
if question and submit:
    generated_sql=get_gemini_response(question, prompt)
    st.subheader("The Sql generted :")
    st.code(generated_sql)
    read_sql_query(generated_sql, "students.db")

user_sql=st.text_input("Test your own SQL: ", key="user_sql")

submit_user_sql=st.button("Enter your sql!")

# if submit_user_sql is clicked
if user_sql and submit_user_sql:
    read_sql_query(user_sql, "students.db")
