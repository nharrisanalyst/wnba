from dataclasses import dataclass
from datetime import date
from typing import Optional

@dataclass
class Teams:
  team_id:int
  name:str
  
  
@dataclass
class Seasons:
  season_id:int
  season: int
  
  
@dataclass
class Players:
  player_id:int
  first_name: str
  last_name:str
  birthdate: date
  
  
@dataclass
class Season_Teams:
  season_teams_id:int
  season_id: int
  team_id:int
  season:Seasons
  team:Teams

@dataclass
class Season_Team_Players:
  season_team_players_id:int
  season_teams_id:int
  player_id:int 
  start_date:date
  end_date:Optional[date] = None
  