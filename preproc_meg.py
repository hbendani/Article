# -*- coding: utf-8 -*-
"""
1- Convert MEG file to excel file
2- Run the script 
3- Execute in Notepad :
    * ctr + H 
    * search mode : Extended
    * in the "find what" cell : '\t 
    * in the "replace with" cell : (4 or 5 spaces)
    * Replace ALL
"""
from pandas import DataFrame
import pandas as pd 

#convert MEG file to excel
file = 'meg_file.xlsx'
df1 = pd.read_excel(file)
info=df1["#Mega"]
sequences=df1["Unnamed: 1"]
df_new=pd.DataFrame()
dict_countries={}
#write the header
df_new.loc[0,"#Mega"]="#Mega"
cond = df1.index < 3
rows = df1.loc[cond, :]
df_new = df_new.append(rows, ignore_index=True)
#change the name of the refer
df_new.loc[3,"#Mega"]="#NC'"
for i in range(4,len(info)):
    value=info[i].split("/")
    countries=value[0]
    countries=countries[1:] # to eliminate "#"countries
    #create abbrev
    if countries.find("_") != -1:
        #for composed name
        if countries=="South_Africa":
            new_countries="SAf"
        if countries=="Sri_Lanka":
            new_countries="Sri"
        if countries=="United_Arab_Emirates":
            new_countries="Uae"
        if countries=="Saudi_Arabia":
            new_countries="Sar"
        if countries=="South_Korea":
            new_countries="SKo"
        if countries=="Czech_Republic":
            new_countries="CRe"
        if countries=="Bosnia_and_Herzegovina":
            new_countries="BaH"
    else :
        #for same countries with identical first 3 letters
        if countries=="Australia":
            new_countries="Aul"
        elif countries=="Belarus":
            new_countries="blr"
        elif countries=="Chile":
            new_countries="Chl"
        elif countries=="Indonesia":
            new_countries="Ido"
        else :
            # for the rest of the countries
            new_countries=countries[:3]
    # dictinary to save and count the number of redondance for each country
    text=new_countries
    if text in  dict_countries:
        num=dict_countries[new_countries] +1
        dict_countries[new_countries]= num
        new_countries=new_countries+str(num)
    else:
        dict_countries[new_countries]=1
        new_countries=new_countries+str(1)
    #write in dataframe
    data_frame_value="#"+new_countries+"/"+value[1]+"'"
    df_new.loc[i,"#Mega"]=data_frame_value
    df_new.loc[i,"Unnamed: 1"]=sequences[i]
#convert dataFrame into meg format 
df_new.to_csv(r'meg_res.meg', header=None, index=None, sep='\t', mode='a')
