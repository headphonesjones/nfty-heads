'''
Get the most current listing
'''

import getAsset

def searchNFT(asset_info):

  asset = getAsset.getAsset(asset_info)

  if len(asset["assets"]) > 0:
        last_sale = asset["assets"][0]["last_sale"]
        #last_sale_price = int(last_sale_price_long) / 1e18

  else:
    last_sale = "No Recent Sale"

  img_url = asset["assets"][0]["image_url"]
  nfty_name = asset["assets"][0]["name"]
  os_url = asset["assets"][0]["permalink"]
  current_price_full = asset["assets"][0]['sell_orders'][0]['current_price']
  current_price = int(current_price_full) / 1e18

  return last_sale, nfty_name, str(current_price), img_url, os_url