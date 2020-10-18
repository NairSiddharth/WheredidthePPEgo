import pandas as pd
from github import Github

g = Github("NairSiddharth","MasterSamurai2423")

base = g.get_repo("NairSiddharth/COVID-19")
contents = base.get_contents("csse_covid_19_data/csse_covid_19_daily_reports_us")
filepaths = []
for file in contents:
  filepaths.append(file.path)
  
concat = []
for filepath in filepaths: 
  url = 'https://raw.githubusercontent.com/NairSiddharth/COVID-19/master/'+filepath
  #if filepath == 'csse_covid_19_data/csse_covid_19_daily_reports_us/README.md':
  #  break
 # print(url)
  if filepath != 'csse_covid_19_data/csse_covid_19_daily_reports_us/README.md':
   # print("1")
    df = pd.read_csv(url)
    concat.append(df)
    #concat.sort()
   # print(df.head())
  else:
    #print("1")
    break
frame = pd.concat(concat,axis=0,ignore_index=True)
frame.sort_values(by=["State"],inplace=True)

 
