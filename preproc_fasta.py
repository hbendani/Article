"""
1- Using FASTA file
2- Run the script 
3- Execute in Notepad :
    * ctr + H 
    * search mode : Extended
    * in the "find what" cell : '\t 
    * in the "replace with" cell : (4 or 5 spaces)
    * Replace ALL
"""
import Bio
from Bio import SeqIO
import pandas as pd

#init all the files
fasta=open("aligned.fasta","r")
newfil=open("aligned_as_meg.fasta","w")
dict_countries={}
found=0 
for record in Bio.SeqIO.parse(fasta,'fasta'):
    if found!=0:
        ident = record.id
        countries=ident.split("/")[0]
        #for comp name
        if countries.find("_") != -1:
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
        if new_countries in  dict_countries:
            num=dict_countries[new_countries] +1
            dict_countries[new_countries]= num
            new_countries=new_countries+str(num)
        else:
            dict_countries[new_countries]=1
            new_countries=new_countries+str(1)
        #write in file
        data_val=">"+new_countries+"/"+ident.split("/")[1]+"'\t"
        newfil.write(data_val)
        newfil.write(str(record.seq) + "\n")
    found=found+1
fasta.close()
newfil.close()
