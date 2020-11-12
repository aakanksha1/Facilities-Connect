"""
This files originate from the "New-Empty-Python-Project-Base" template:
    https://github.com/Neuraxio/New-Empty-Python-Project-Base 
Created by Guillaume Chevalier at Neuraxio:
    https://github.com/Neuraxio 
    https://github.com/guillaume-chevalier 
License: CC0-1.0 (Public Domain)
"""

#https://www.datacamp.com/community/tutorials/python-excel-tutorial

# READ IN EXCEL FILES USING PANDAS
# FOR ROW IN BUILDING_CHARGED, ITERATE OVER JOB_ID
	# IF BLANK, SKIP
	# ELSE GRAB ROW INFORMATION
		#INITIALIZE [] = PROCEDURE_NUMBER
		#INITIALIZE [] = 
		#ITERATE THROUGH PROCEDURES_TRANSFER FILTER BY PROCEDURE_TITLE
		#FILL ARRAY WITH PROCEDURE_NUMBERS



# the run time for this 

# Import pandas
import pandas as pd

# Assign spreadsheet filename to `file`
file = 'example.xlsx'

# Load spreadsheet
xl = pd.ExcelFile(file)

# Print the sheet names
print(xl.sheet_names)

# Load a sheet into a DataFrame by name: df1
df1 = xl.parse('Sheet1')





def hello_world():
	print "Hello World!"
    


