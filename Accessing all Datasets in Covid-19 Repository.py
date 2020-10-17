import pandas as pd
from github import Github
g = Github("NairSiddharth","MasterSamurai2423")
base = g.get_repo("NairSiddharth/COVID-19")
contents = base.get_contents("csse_covid_19_data/csse_covid_19_daily_reports_us")
filepaths = []
for file in contents:
  filepaths.append(file.path)
for filepath in filepaths: 
  url = 'https://raw.githubusercontent.com/NairSiddharth/COVID-19/master/'+filepath
  #if filepath == 'csse_covid_19_data/csse_covid_19_daily_reports_us/README.md':
  #  break
  if filepath != 'csse_covid_19_data/csse_covid_19_daily_reports_us/README.md':
    df = pd.read_csv(url)
    df.head()
  else:
    break