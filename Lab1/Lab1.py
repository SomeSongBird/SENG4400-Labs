import pandas as pd

path = ''
filename = 'lab_1_input_data.csv'
data_frame_1 = pd.read_csv(path + filename)

print("Number of rows: "+str(len(data_frame_1.index))+"\n")
print("Number of columns: "+str(len(data_frame_1.columns))+"\n")

data_frame_1["Sales"] = data_frame_1['quantity']*data_frame_1['per_unit_price']

print(data_frame_1['Sales'])

data_frame_1.to_csv(path + 'output_report_lab_1.csv', index = False, header = True)

#ABC Retailer total sales
tmpdf = data_frame_1.groupby(['retailer_name']).sum()
print("\nABC Retailer total sales: "+str(tmpdf.Sales[0])+"\n")

abcveg = data_frame_1.where((data_frame_1['category']=='Vegetables') & (data_frame_1['retailer_name']=="ABC Retailer")).dropna()
print("ABC Retailer total vegetable sales: "+str(abcveg['Sales'].sum())+"\n")

xyzmeat = data_frame_1.where((data_frame_1['category']=='Meat') & (data_frame_1['retailer_name']=="XYZ Retailer")).dropna()
print("XYZ Retailer total meat sales: "+str(xyzmeat['Sales'].sum())+"\n")