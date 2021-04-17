import discord
from discord.ext import commands

import requests
import json
import re


class OMDb(commands.Cog):
    def __init__(self, bot, omdb_api_key):
      self.bot = bot
      self._base_url = 'http://www.omdbapi.com/'
      self.omdb_api_key = omdb_api_key


    def get_search_string(self, *args):
        regex = re.findall('tt\d{7,}', args[0])
        if len(args) == 1 and regex:
            return f'?i={regex[0]}'
        else:
            return f'?t={"+".join(args)}'


    def get_url(self, search_string):
        return f'{self._base_url}{search_string}&apikey={self.omdb_api_key}'


    def get_omdb(self, url):
        response = requests.get(url)
        if response.status_code == 200:
            json_data = json.loads(response.text)
            return json_data
        else:
            return None


    def get_embed(self, json_data):
        embed = discord.Embed(
            title = json_data['Title'],
            description = json_data['Plot'],
            url = f'https://www.imdb.com/title/{json_data["imdbID"]}'
        )

        poster = json_data.get("Poster")
        if poster and poster != 'N/A':
            embed.set_thumbnail(url=poster)

        embed.set_footer(text=f'{json_data["Rated"]}  |  {json_data["Runtime"]}  |  {json_data["Genre"]}  |  {json_data["Year"]}')

        return embed


    @commands.command()
    async def omdb(self, ctx, *args):
        if not len(args) > 0:
            await ctx.send('Please provide a name or IMDb identifier.')
            return

        search_string = self.get_search_string(*args)
        url = self.get_url(search_string)
        json_data = self.get_omdb(url)
        
        if json_data == None:
            await ctx.send('Something went wrong.')
        elif json_data['Response'] == 'False':
            await ctx.send(json_data['Error'])
        else:
            embed = self.get_embed(json_data)
            await ctx.send(embed=embed)   