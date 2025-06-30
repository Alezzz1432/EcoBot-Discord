
import discord
from discord.ext import commands
import random
import time

intents = discord.Intents.default()
intents.message_content = True

client = commands.Bot(command_prefix='!', intents=intents)

RECICLAJE_IMAGENES = [
    "https://www.reciclajecontemar.es/wp-content/uploads/frases-motivadoras-para-reciclar-y-cuidar-el-planeta.jpg",
    "https://cdn0.ecologiaverde.com/es/posts/5/9/4/frases_de_reciclaje_que_rimen_1495_7_600.jpg",
    "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSdbp0G4hM69X5J8Vzs4sTZcFnzwHODgZ9jhQ&s",
    "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSstp3R0Jks_orndwz_8mNIF30k83hXjlHn2FjSBoev0DLC3Mu_z8Fw2_rWct2L4doniFE",
]

ultimo_envio = {}

@client.event
async def on_ready():
    print(f"Bot conectado como {client.user}")

@client.command(name='image')
async def enviar_imagen(ctx):
    ahora = time.time()
    print("Estado de ultimo_envio:", ultimo_envio) 
    disponibles = [img for img in RECICLAJE_IMAGENES if img not in ultimo_envio or ahora - ultimo_envio[img] > 300]
    print("Imágenes disponibles:", disponibles) 
    if not disponibles:
        await ctx.send("Todas las imágenes han sido enviadas recientemente. Por favor, espera unos minutos.")
        return
    imagen_url = random.choice(disponibles)
    ultimo_envio[imagen_url] = ahora
    await ctx.send(imagen_url)

client.run("BOT_TOKEN")