import pandas as pd
import xlwings as xw



# Sample DataFrames for when not on windows (comment out when in windows)

file_path = "/home/ale/Downloads/Conductor_House_Proforma.xlsm"

construction_costs = pd.read_excel(file_path, "Construction_Costs")

construction_draw_pre = pd.read_excel(file_path, "Construction_Draw")
    construction_draw = construction_draw_pre.iloc[:,range(1,len(construction_draw_pre.iloc[1]))]

#Construction Costs

## Creating the Construction Schedule

