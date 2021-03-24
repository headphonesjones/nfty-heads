import getAsset
import getOrder

def searchNFT(asset_info):

  asset = getAsset.getAsset(asset_info)
  order = getOrder.getOrderFromID(asset_info)
  
  if len(asset["assets"]) > 0:
        last_sale = asset["assets"][0]["last_sale"]["total_price"]
        last_sale = int(last_sale) / 1e18

  else:
    last_sale = "No Recent Sale"
  
  img_url = asset["assets"][0]["image_url"]
  # img_url = "heads/001.gif"
  # img_url = "https://media.giphy.com/media/sAsKZFmlJhc08eD9wp/giphy.gif"
  nfty_name = asset["assets"][0]["name"]
  os_url = asset["assets"][0]["permalink"]
  if len(order["orders"]) > 0: 
    listing_price = order["orders"][0]['current_price']
    listing_price = int(listing_price) / 1e18
  else:
    listing_price = "No Current Listing Price"
  

  return last_sale, nfty_name, str(listing_price), img_url, os_url