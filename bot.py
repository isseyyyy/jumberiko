from http import client
import discord
from discord.ext import commands

# Words
hello_words = [ 'hello', 'yo', 'zd' ]
bye_words = ['paka', 'kargad', 'bb']
sigma_words = ['meshinia' , 'bandzo', 'cringe']
sigma_answer = ['dedasheni', 'yleo', ]


prefix = "."

client = commands.Bot( command_prefix = prefix )

@client.event

async def on_ready():
    print('Connected')


#clear
@client.command( pass_context = True )

async def clear( ctx, amount = 100):
    await ctx.channel.purge( limit = amount )




@client.event

async def on_message( message ):
    msg = message.content.lower()
    if msg in hello_words:
        await message.channel.send('ზდაროვა ყლეო')

    if msg in sigma_words:
        await message.channel.send('რა იყო პატარავ ')

    if msg in sigma_answer:
        await message.channel.send('შე ღლაპო ეხა არ გაგიტეხო კომპიუტერი, ჩაიჯვი ')
    
    if msg in bye_words:
        await message.channel.send('დავაი დაახვიე ')




token = open('token.txt', 'r').readline()

client.run( token )
