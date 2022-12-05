import pandas as pd


dataframe = pd.read_csv('slinky_dog_dash.csv')
print('Slinky Dog Dash File Read')
clean_dataframe = dataframe[dataframe.SACTMIN.notnull()]
clean_dataframe.drop(["datetime", "SPOSTMIN"], axis = 1, inplace=True)
daily_average = clean_dataframe.groupby("DATE")["SACTMIN"].mean()
print('Daily Average Found')
daily_average_df = daily_average.to_frame()
daily_average_df.reset_index(inplace=True)
daily_average_df.to_csv('daily_average_for_slinky_dog_dash.csv')
print('Results stored in daily_average_for_slinky_dog_dash.csv')
