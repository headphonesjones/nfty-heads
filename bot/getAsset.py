import requests
import json


def getAsset(asset_id):
  url = "https://api.opensea.io/api/v1/assets"
  print(asset_id)
  querystring = {"token_ids": asset_id,"collection":"super-nfty-floating-heads","order_direction":"desc","offset":"0", "limit": '1'}

  response = requests.request("GET", url, params=querystring)
  json_data = json.loads(response.text)

  # # searching query  for name 
  # for i in range(0,len(json_data)):
  #   print(json_data["assets"][i]["name"])
  #   if json_data["assets"][i]["name"] == qName:
  #     return json_data["assets"][i]
  #   else:
  #     print(json_data["assets"][i]["name"])
  return json_data