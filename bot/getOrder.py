'''
Class requests OpenSea API and return JSON object containing relevant information.

'''
import requests
import json


def getOrder(asset_id):
  url = "https://api.opensea.io/wyvern/v1/orders"
  querystring = {"collection_slug":"super-nfty-floating-heads","bundled":"false","include_bundled":"false","include_invalid":"false","limit":"1","offset":"0","order_by":"created_date","order_direction":"desc"}

  response = requests.request("GET", url, params=querystring)
  json_data = json.loads(response.text)
  # print(json_data)
  
  return json_data

def getOrderFromID(asset_id):
  url = "https://api.opensea.io/wyvern/v1/orders"
  querystring = {"collection_slug":"super-nfty-floating-heads","bundled":"false","include_bundled":"false", "token_id": asset_id, "include_invalid":"false","limit":"1","offset":"0","order_by":"created_date","order_direction":"desc"}

  response = requests.request("GET", url, params=querystring)
  json_data = json.loads(response.text)
  # print(json_data)
  
  return json_data