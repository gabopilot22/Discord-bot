import discord
from discord.ext import commands
from model import get_class

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

@bot.command()
async def revisar(ctx):
    if ctx.message.attachments:
        for image in ctx.message.attachments:
            file_name = image.filename
            file_url = image.url
            await ctx.send(f"Imagen guardada en {file_name}")
            await image.save(file_name)
            
            try:
                class_name = get_class("keras_model.h5","labels.txt", file_name)
                if class_name[0] == "conejos" :
                    await ctx.send("Los conejos son mamíferos pequeños, de cuerpo compacto y orejas largas, que pertenecen a la familia Leporidae. Son animales herbívoros, conocidos por su reproducción rápida y su capacidad para adaptarse a diversos hábitats, como bosques, praderas y áreas urbanas. Se caracterizan por su comportamiento tímido y su habilidad para excavar madrigueras. Su dieta incluye pasto, hojas, flores y raíces. Tienen un sistema digestivo especializado que les permite extraer nutrientes de los alimentos al realizar la coprofagia, es decir, consumir parte de sus excrementos para una segunda digestión. Los conejos también son muy sociales y suelen vivir en colonias.")


                elif class_name[0] == "liebres" :
                    await ctx.send("Las liebres son mamíferos pertenecientes a la familia Leporidae, al igual que los conejos, pero difieren en varios aspectos significativos. Son animales más grandes, con patas traseras más largas y poderosas, adaptadas para correr a altas velocidades, lo que les permite escapar de depredadores en terrenos abiertos. También poseen orejas más largas, que ayudan a regular su temperatura corporal.")    

            except:
                await ctx.send("El formato de la imagen no funciona, o no se leyo bien la imagen. JPG, PNG o JPEG")

    else:
        await ctx.send("No subiste ninguna imagen :(")

bot.run("")