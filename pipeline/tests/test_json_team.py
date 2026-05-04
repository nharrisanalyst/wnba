import os
import json

BASE_DIR = os.path.dirname(os.path.dirname(__file__))
path = os.path.join(BASE_DIR, "json", "wnba.json")


def test_json_has_wnba():
  with open(path, 'r') as file:
    wnba_json = json.load(file)
    assert "wnba" in wnba_json
    
def test_json_has_years():
  with open(path, 'r') as file:
     wnba_json = json.load(file)
     
    