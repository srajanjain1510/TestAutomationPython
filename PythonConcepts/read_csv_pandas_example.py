from pathlib import Path

import pandas as pd

home = Path.home()

print(home)

csv_file_path = Path(home, 'Desktop', 'SampleData.csv')
print(csv_file_path)

# read csv file
csv_df = pd.read_csv(csv_file_path, usecols=['Focus Area', 'Skillset Requirement', 'Criteria'])
# print(csv_df)

csv_df.dropna(how='all')
filtered_csf_df = csv_df[csv_df['Criteria'] == "Very Important"]
print(filtered_csf_df)

# create dataframe

family_data = {
    'Name': ['SJ', 'AJ', 'Jr SJ', 'PJ'],
    'Age': [35, 35, 6, 2]

}

family_data_frame = pd.DataFrame(family_data)

#csv file
csv_file = Path(home,'Desktop','family_with_index.csv')

family_data_frame.to_csv(csv_file,index=True)
