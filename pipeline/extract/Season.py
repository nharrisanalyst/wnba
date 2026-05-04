import os
from dataclasses import dataclass
from sqlalchemy import create_engine
import requests
from datetime import date, datetime
import pandas as pd 

db = os.environ["POSTGRES_DB"]
db_password = os.environ["POSTGRES_PASSWORD"]
db_username = os.environ["POSTGRES_USER"]

season_years = [1997, 1998, 1999, 2000, 2001, 2002, 2003, 2004, 2005, 
                2006, 2007, 2008, 2009, 2010, 2011, 2012, 2013, 2014, 
                2015, 2016,2017, 2018 , 2019, 2020, 2021, 2022, 2023, 2024, 2025, 2026]

url_template = "http://sports.core.api.espn.com/v2/sports/basketball/leagues/wnba/seasons/{0}"

@dataclass
class Season_Model:
  id:int
  year:int
  start_date:date;
  end_date:date;
  
class Extract_Request_Data:
  def __init__(self, url_template, requests, data_wanted):
    self.url_template = url_template
    self.request = requests;
    self.data_wanted = data_wanted
  
  def get_data(self):
    url = self.url_template.format(self.data_wanted);
    resp = self.request.get(url)
    return resp.json()
    
    
def extract_load_season_data():
  seasons =[]
  for season in season_years:
    extract_request_data = Extract_Request_Data(url_template,requests, season)
    season_data = extract_request_data.get_data()
    start_date = datetime.strptime(season_data['startDate'][:10], "%Y-%m-%d")
    end_date = datetime.strptime(season_data['endDate'][:10], "%Y-%m-%d")
    season = Season_Model(id=season, year=season, start_date=start_date, end_date=end_date)
    seasons.append(season);
  
  print('got season data from api')
  print(f'postgresql://{db_username}:{db_password}@localhost:5432/{db}')
  seasons_df = pd.DataFrame(seasons)
  engine = create_engine(f'postgresql://{db_username}:{db_password}@wnba-db:5432/{db}')
  seasons_df.to_sql('seasons', engine, if_exists="append", index=False)
  
    