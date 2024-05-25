import discord, random
from bot_logic import gen_pass

# La variable intents almacena los privilegios del bot
intents = discord.Intents.default()
# Activar el privilegio de lectura de mensajes
intents.message_content = True
# Crear un bot en la variable cliente y transferirle los privilegios
client = discord.Client(intents=intents)



@client.event
async def on_ready():
    print(f'Hemos iniciado sesión como {client.user}')

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.content.startswith('$hola'):
        await message.channel.send("chao!")
    elif message.content.startswith('$bye'):
        await message.channel.send(":wave:")
    elif message.content.startswith('$wagh'):
        await message.channel.send("¡¡WAGH!!")
    elif message.content.startswith('$a mimir'):
        await message.channel.send(":zzz:")
    elif message.content.startswith('$moneda'):
        moneda = "random"
        a = random.randint(0,1)
        if a == 1:
            moneda = "aguila"
        elif a == 0:
            moneda = "cara"
        await message.channel.send(moneda)
    elif message.content.startswith('$dado'):
        b = random.randint(1,6)
        await message.channel.send(b)
    elif message.content.startswith('$mejor_del_chat?'):
        await message.channel.send("Avo")
    elif message.content.startswith('$contraseña'):
        await message.channel.send("tu contraseña es: " + gen_pass(12))

client.run("aqui va tu bot")
