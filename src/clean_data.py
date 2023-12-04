import pandas as pd
def main():
  data = read_all()
  sort(data)

def dfmerger (start):
  # set season ending year
  end = str(start + 1)
  start = str(start)
  # set path name 
  salary_path = "salary_" + start + "_" + end
  stats_path = "stats_" + start + "_" + end
  # read two datasets and exclude index from csv
  df_salary=pd.read_csv(salary_path,index_col='Unnamed: 0')
  df_stats=pd.read_csv(stats_path, index_col='Unnamed: 0')
  # normalize salary column to salary
  df_salary = df_salary.rename(columns={df_salary.columns[0]: "Player", df_salary.columns[1]: "salary"})
  
  # split name to two columns "first_name" and "last_name" for salary dataset
  a = df_salary['Player'].values.tolist()
  # convert name to lower and keep only first and last name by index
  for i in range(len(a)):
    a[i]= a[i].lower()
    a[i] = a[i].split(" ")
    if(len(a[i]))!=2:
        a[i]=a[i][:2]
  df_salary["first_name"]=[first[0] for first in a]
  df_salary["last_name"]=[last[1] for last in a]
  
  # split name to two columns "first_name" and "last_name" for stats dataset
  b = df_stats['Player'].values.tolist()
  # convert name to lower and keep only first and last name by index
  for i in range(len(b)):
    b[i]= b[i].lower()
    b[i] = b[i].split(" ")
    if(len(b[i]))!=2:
        b[i]=b[i][:2]
  df_stats["first_name"]=[first[0] for first in b]
  df_stats["last_name"]=[last[1] for last in b]
  df_salary.rename({df_salary.columns[1]: "salary"})

  # inner join by match first and last name
  merged_df = pd.merge(df_salary, df_stats, on=['first_name', 'last_name'], how='inner')
  # re-format salary from string to float
  merged_df['salary'] = merged_df['salary'].str.replace('$', '').str.replace(',', '').astype(float)
  #save file for each season
  merge_name = "merged" + start + "_" + end + ".csv"
  merged_df.to_csv(merge_name)
  return merged_df

def read_all():
  df1 = dfmerger (2019)
  df1['season'] = '2019'
  df2 = dfmerger (2020)
  df2['season'] = '2020'
  df3 = dfmerger (2021)
  df3['season'] = '2021'
  df4 = dfmerger (2022)
  df4['season'] = '2022'
  df5 = dfmerger (2023)
  df5['season'] = '2023'
  ## Merge all datafram from 2019-2020 until 2023-2024
  combined_df = pd.concat([df1, df2, df3, df4, df5], ignore_index=True)
  return combined_df

def sort(data):
  data = data.sort_values(by=['salary'], ascending=False)
  data = data.drop(columns ="Player_y")
  data = data.rename(columns = {"Player_x": "Player"})
  data.to_csv("meta_data",index=False)  #export player stats
  print(data)

if __name__ == "__main__":
   main()