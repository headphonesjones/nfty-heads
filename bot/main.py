import discord
import os
import discord
from botPrompts import searchPrompt
import requests
import json
import schedule
import time
import csv
import pandas


match =  'match.csv'

client = discord.Client()
token = os.getenv('TOKEN')

@client.event
async def on_ready():
  print("Connection Successful")

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    # if ! + variable... !1 - 264, else return error message of "Only 264 Super Nfty Floating Heads will ever be made. Please enter a number !1 - 264."
    if message.content.startswith('!') == False:
      pass

    elif message.content.startswith('!') and int(message.content[1:]) in range(1,265):

      await message.channel.send('Retrieving Super Nfty Floating Head ' + str(message.content[1:]))

      # check match.csv for matching ASSET_ID for entered MINT_NUMBER
      # pass that ASSET_ID through searchPrompt
      match_data = pandas.read_csv('match.csv', index_col='MINT_ID', names=['MINT_ID', 'ASSET_ID'])
      # gif_id = message.content[1:]
      matched_id = match_data['ASSET_ID'][message.content[1:]]

      print(matched_id)

      await message.channel.send(embed = searchPrompt(matched_id))



    else:
      await message.channel.send("Only 264 Super Nfty Floating Heads will ever be made. Please enter a number !1 - !264.")

server.server()
client.run(token)