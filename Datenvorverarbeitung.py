import pandas as pd
from sklearn.preprocessing import StandardScaler

data1 = pd.read_csv('Data1/acc_data.csv')
data1 = data1.rename(columns={'acc_time': 'Time'})

data2 = pd.read_csv('Data2/acc_data.csv')
data2 = data2.rename(columns={'acc_time': 'Time'})

data3 = pd.read_csv('Data3/acc_data.csv')
data3 = data3.rename(columns={'acc_time': 'Time'})

data4 = pd.read_csv('Data4/acc_data.csv')
data4 = data4.rename(columns={'acc_time': 'Time'})

data5 = pd.read_csv('Data5/acc_data.csv')
data5 = data5.rename(columns={'acc_time': 'Time'})

data6 = pd.read_csv('Data6/acc_data.csv')
data6 = data6.rename(columns={'acc_time': 'Time'})

data7 = pd.read_csv('Data7/acc_data.csv')
data7 = data7.rename(columns={'acc_time': 'Time'})

data8 = pd.read_csv('Data8/acc_data.csv')
data8 = data8.rename(columns={'acc_time': 'Time'})

data9 = pd.read_csv('Data9/acc_data.csv')
data9 = data9.rename(columns={'acc_time': 'Time'})

data10 = pd.read_csv('Data10/acc_data.csv')
data10 = data10.rename(columns={'acc_time': 'Time'})

data11 = pd.read_csv('Data11/acc_data.csv')
data11 = data11.rename(columns={'acc_time': 'Time'})

merged_data = pd.concat([data1, data2, data3, data4, data5, data6, data7, data8, data9, data10, data11], axis=0, join='outer')

merged_data['label'] = merged_data['label'].replace('', method='ffill')
merged_data['Vorheriges_Label'] = merged_data['label'].shift(1)
merged_data[['accX', 'accY', 'accZ']] = merged_data[['accX', 'accY', 'accZ']].fillna(0)
merged_data['Label_Wechsel'] = (merged_data['label'] != merged_data['label'].shift(1)).astype(int)

group_key = merged_data['Label_Wechsel'].cumsum()

aggregated_data = merged_data.groupby(group_key).agg({
    'accX': 'std',
    'accY': 'std',
    'accZ': 'std',
    'label': 'first',
    'Vorheriges_Label': 'first'
})

scaler = StandardScaler()

columns_to_standardize = aggregated_data.columns[1:3]

aggregated_data[columns_to_standardize] = scaler.fit_transform(aggregated_data[columns_to_standardize])
cleaned_data = aggregated_data.dropna()

# aggData enthält alle Daten und ist für random Test/Train-Split geeignet
cleaned_data.to_csv('aggData.csv')


# Aggregation von Daten die einen begrenzten Raum beinhalten(weniger Features)
merged_data = pd.concat([data1, data2, data3], axis=0, join='outer')

merged_data['label'] = merged_data['label'].replace('', method='ffill')
merged_data['Vorheriges_Label'] = merged_data['label'].shift(1)
merged_data[['accX', 'accY', 'accZ']] = merged_data[['accX', 'accY', 'accZ']].fillna(0)
merged_data['Label_Wechsel'] = (merged_data['label'] != merged_data['label'].shift(1)).astype(int)

group_key = merged_data['Label_Wechsel'].cumsum()

aggregated_data = merged_data.groupby(group_key).agg({
    'accX': 'std',
    'accY': 'std',
    'accZ': 'std',
    'label': 'first',
    'Vorheriges_Label': 'first'
})

scaler = StandardScaler()

columns_to_standardize = aggregated_data.columns[1:3]

aggregated_data[columns_to_standardize] = scaler.fit_transform(aggregated_data[columns_to_standardize])
cleaned_data = aggregated_data.dropna()

# aggData enthält alle Daten und ist für random Test/Train-Split geeignet
cleaned_data.to_csv('small_aggData.csv')
