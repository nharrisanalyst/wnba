A repository dedicated to WNBA stats analytics and predictions


test scripts
docker compose build test-wnba-pipeline
docker compose up -d test-wnba-pipleline 
docker compose exec test-wnba-pipeline pytest -q

espn api look
root → league → seasons → season → types → events → event → stats

play by play data 
league → seasons → types → events → event → competitions → playByPlay