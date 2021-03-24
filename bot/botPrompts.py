import discord
import Search

def searchPrompt(message):
  
    last_sale_price, nfty_name, listing_price, img_url, os_url = Search.searchNFT(message)

    #print("1: ", last_sale_price, "2: ",nfty_name, "3: ", listing_price, "4: ",img_url, "5: ", os_url)

    embed=discord.Embed(title=nfty_name, url=os_url, color=0xFF5733)
    embed.set_image(url=img_url)

    if listing_price == "No Current Listing Price":
      embed.add_field(name="Listing Price: ", value=str(listing_price))
    else:
      embed.add_field(name="Listing Price: ", value=str(listing_price) + " ETH")

    if str(last_sale_price) == 'None':
      embed.add_field(name="Previous Sale Price: ", value=str(last_sale_price))  
    else:
      embed.add_field(name="Previous Sale Price: ", value=str(last_sale_price) + " ETH")

    return embed