import streamlit as st 
import numpy as np 
import pandas as pd 
import sqlite3
import matplotlib.pyplot as plt
import seaborn as sns



#getting the data from the database into a pandas data frame : 

def connectDB():
    con = sqlite3.connect("database.db")
    return con

def get_table_as_dataframe(table_name):
    con = connectDB()
    query = f"SELECT * FROM {table_name}"
    df = pd.read_sql_query(query, con)
    con.close()
    return df

# get the tables as data frames :
df_employee = get_table_as_dataframe('Employee')
df_attendance = get_table_as_dataframe('Attendance')
df_feedback = get_table_as_dataframe('Feedback')
df_employee_department = get_table_as_dataframe('EmployeeDepartment')

#merged the tables into one data frame :
merged_df = pd.merge(df_employee, df_employee_department, on='employee_id', how='inner')
merged_df = pd.merge(merged_df, df_attendance[['employee_id','day','time_per_day']], on='employee_id', how='inner')
merged_df = pd.merge(merged_df, df_feedback, on='employee_id', how='inner')

print(merged_df.columns)

# # vizualizing data : 
# def salary_by_departement():
# # Calculate the average salary by department :
#     salary_by_departement = merged_df.groupby('department_name')['salary'].mean()
# # Create the bar plot:
#     plt.figure(figsize=(10, 6))
#     sns.barplot(x='department_name', y='salary', data=salary_by_departement.reset_index())
#     plt.xlabel('Department')
#     plt.ylabel('Average Salary')
#     plt.title('Average Salary by Department')
#     plt.xticks(rotation=45)
#     # Display the plot using Streamlit
#     st.header("Average Salary by Department")
#     st.pyplot(plt)
 

# salary_by_departement()





