begin;

CREATE TABLE IF NOT EXISTS teams (
    team_id int primary key,
    name varchar(100) not null unique
); 


CREATE TABLE IF NOT EXISTS seasons (
season_id int primary key,
season smallint not null
);

create table if not exists players (
  player_id int primary key,
  first_name varchar(25) not null,
  last_name varchar(25) not null,
  birthdate date not null
);

create table if not exists season_teams (
 season_teams_id int primary key,
 season_id int references seasons(season_id),
 team_id int references teams(team_id)
);

create table if not exists season_team_players (
  season_team_players_id int primary key,
  season_teams_id int references season_teams(season_teams_id),
  player_id int references players(player_id),
  start_date date not null,
  end_date  date not null
)

commit;


rollback;