import pandas as pd
import os

file_name = os.environ.get('file_name')
exported_file_name = os.environ.get('exported_file_name')


dataframe = pd.read_csv(file_name)
print(f'{file_name} read in successfully')
clean_dataframe = dataframe[dataframe.SACTMIN.notnull()]
clean_dataframe.drop(["DATETIME", "SPOSTMIN"], axis = 1, inplace=True)
daily_average = clean_dataframe.groupby("DATE")["SACTMIN"].mean()
print('Daily Average Found')
daily_average_df = daily_average.to_frame()
daily_average_df.reset_index(inplace=True)
daily_average_df.to_csv(exported_file_name)
print('Results stored in {exported_file_name}')
