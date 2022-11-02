import pandas as pd
import xlsxwriter as xl

path = ''
input_file = "input_data_lab_2.csv"
output_file = "output_data_lab_2.xlsx"

data_frame_1 = pd.read_csv(path+input_file)

wb = xl.Workbook(output_file)
writer = pd.ExcelWriter(output_file)

#writing each group of 100 columns to a seperate pages
for i in range(len(data_frame_1.columns)//100):
    sheet_name=i+1
    ws = wb.add_worksheet(str(sheet_name))

    tmpdf = data_frame_1.iloc[:,i*100:sheet_name*100]

    tmpdf.to_excel(writer,str(sheet_name),index=False)

writer.save()