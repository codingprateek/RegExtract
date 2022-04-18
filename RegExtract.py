import re
import os
import pandas as pd
import yfinance as yf
import streamlit as st

names = ""
roles = ""
emails = ""
contacts = ""

def wr(text):
    file = open("output.txt", "a+")
    # file.write("%d" % (i+1))
    # file.write("\t")
    file.write(text)
    

def wrt(info):
    file = open("output.txt", "a+")
    # file.write("\t")
    file.write(info)

st.header('RegExtract')

input_type=st.sidebar.selectbox("Enter type of Input data",['Text area','File Upload'])
if input_type=='Text area':
    strin=st.text_area("Write Your text here")
else:
    input_file=st.file_uploader("Enter txt file")
result = st.sidebar.button('Generate TXT')
csv_gen = st.sidebar.download_button('Generate CSV', data='output.csv')

if result:
    if input_type=='Text area':
        if os.path.exists("input.txt"):
            os.remove("input.txt")
        file=open("input.txt",'a+')
        file.write(strin)
        file.close()
        input_file=open('input.txt', "r")
        

    if os.path.exists("output.txt"):
        os.remove("output.txt")

    st.write("Data Successfully extracted and written to output.txt")
    while True:
        file_content=""
        
        if input_type=='File Upload':
            file_content = input_file.readline().decode("utf-8") 
        else:
            print("Error")

        names = re.findall(r"[A-Za-z]*\s?\-?[A-Za-z]+\,\s?[A-Za-z]+\-?\.?\s?[A-Za-z]*\.?", file_content)
        roles = re.findall(r'\b([A-Z]?[a-z]*\s?[A-Z]?[a-z]*\s?[A-Z][a-z]+\s?[A-Z]?[a-z]*)<br\b', file_content)
        emails = re.findall(r'\b([A-Za-z0-9]+\.?[A-Za-z0-9]*\.?[A-Za-z0-9]*@[a-z]*\.?utdallas.edu)\s?</a\b', file_content)
        contacts = re.findall(r'\-([0-9]{4})', file_content)

        if names:
            wr(",")
            wr("\n")
            wr(names.pop(0))
        if roles:
            wrt(",")
            wrt(roles.pop(0))
        if emails:
            wrt(",")
            wrt(emails.pop(0))
        if contacts:
            wrt(",")
            wrt(contacts.pop(0))
        if file_content == "</html>":
            break
            
if csv_gen:
    if os.path.exists("output.csv"):
        os.remove("output.csv")
    os.rename('output.txt', 'output.csv')
    st.write("Text file is successfully converted to CSV file: output.csv")

