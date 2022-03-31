import os
from discord.ext import commands
import discord
import random

# Database

yes_rep = ["C'est une certitude.", "Ma réponse est oui !",
           "Évidemment.", "J'en suis sûr et certain.", "Affirmatif camarade !"]

no_rep = ["Négatif camarade !", "Je ne pense pas que ce soit le cas.",
          "C'est non.", "Pas du tout !", "Je désapprouve."]

# Initialisation du bot

activity = discord.Game(name="la version 1.4")
# activity = discord.Activity(
#     type=discord.ActivityType.watching, name="ses tests")

status = discord.Status.online
# status = discord.Status.dnd

bot = commands.Bot(command_prefix="-", activity=activity,
                   status=status)


@bot.event
async def on_ready():
    print("Ready !")


# Commandes


@bot.command(name="ping")
async def ping(ctx):
    await ctx.message.reply(f"** Coucou {ctx.author.name} !**")


@bot.command(name="setup")
@commands.has_permissions(administrator=True)
async def setup(ctx):
    embed = discord.Embed(title="Vérfication",
                          description=f"Avant toute chose, il est important d'aller lire le <#926800649398648832> !\n\n Réagis avec <a:pain:957971542086656041> pour accéder au serveur !", color=0xffff8f)
    message = await ctx.send(embed=embed)
    emote = '<a:pain:957971542086656041>'
    await message.add_reaction(emote)


@bot.command(name="role1")
@commands.has_permissions(administrator=True)
async def role1(ctx):
    embed = discord.Embed(
        title="<:MANJI:953703544198955048>__Rôles Ping__", description="📢 : <@&926839189121675276> \n\n🎉 : <@&936407256117936158>\n\n🪄 : <@&954204704383062056>\n\n🪅 : <@&954425078869815366> \n\n📤 : <@&955068888897429594>", color=0xffff8f)
    embed.set_image(
        url="https://cdn.discordapp.com/attachments/953742282228641852/958877777887637504/a06c0b7af378d67ae81a339ab19cdc3a.gif")
    message = await ctx.send(embed=embed)
    emote1 = '📢'
    emote2 = '🎉'
    emote3 = '🪄'
    emote4 = '🪅'
    emote5 = '📤'
    await message.add_reaction(emote1)
    await message.add_reaction(emote2)
    await message.add_reaction(emote3)
    await message.add_reaction(emote4)
    await message.add_reaction(emote5)


@bot.command(name="role2")
@commands.has_permissions(administrator=True)
async def role2(ctx):
    embed = discord.Embed(
        title="<:MANJI:953703544198955048>__Autres Rôles__", description="📲 : <@&954427500841295954>  \n\n🎮 : <@&954427509359927377> \n\n⛩️ : <@&958870403189715075> \n\n👻 : <@&958870090286239764>", color=0xffff8f)
    embed.set_image(
        url="https://cdn.discordapp.com/attachments/953742282228641852/958877808074063952/688a5d4302fa35b5e140f2c8b4545a85.gif")
    message = await ctx.send(embed=embed)
    emote1 = '📲'
    emote2 = '🎮'
    emote3 = '⛩️'
    emote4 = '👻'
    await message.add_reaction(emote1)
    await message.add_reaction(emote2)
    await message.add_reaction(emote3)
    await message.add_reaction(emote4)


@bot.command(name="role3")
@commands.has_permissions(administrator=True)
async def role3(ctx):
    embed = discord.Embed(
        title="<:MANJI:953703544198955048>__Rôles Gang__", description="💛 : <@&957084786856452136> \n\n🤍 : <@&957084624088096768> ", color=0xffff8f)
    embed.set_image(
        url="https://cdn.discordapp.com/attachments/953742282228641852/958881332048568350/07fe2fd642b5adacfe061e747ffbd91d.gif")
    message = await ctx.send(embed=embed)
    emote1 = '💛'
    emote2 = '🤍'
    await message.add_reaction(emote1)
    await message.add_reaction(emote2)


@bot.event
async def on_raw_reaction_add(payload):
    id_message = [958867543261601843, 958878862605951036,
                  958882348466855966, 958882463109742692]
    if payload.message_id in id_message:
        member = payload.member
        guild = member.guild

        emoji = payload.emoji.name
        if emoji == "pain":
            role = discord.utils.get(guild.roles, id=946400877814640640)
            await member.add_roles(role)
        if emoji == "📢":
            role = discord.utils.get(guild.roles, id=926839189121675276)
            await member.add_roles(role)
        if emoji == "🎉":
            role = discord.utils.get(guild.roles, id=936407256117936158)
            await member.add_roles(role)
        if emoji == "🪄":
            role = discord.utils.get(guild.roles, id=954204704383062056)
            await member.add_roles(role)
        if emoji == "🪅":
            role = discord.utils.get(guild.roles, id=954425078869815366)
            await member.add_roles(role)
        if emoji == "📤":
            role = discord.utils.get(guild.roles, id=955068888897429594)
            await member.add_roles(role)
        if emoji == "📲":
            role = discord.utils.get(guild.roles, id=954427500841295954)
            await member.add_roles(role)
        if emoji == "🎮":
            role = discord.utils.get(guild.roles, id=954427509359927377)
            await member.add_roles(role)
        if emoji == "⛩️":
            role = discord.utils.get(guild.roles, id=958870403189715075)
            await member.add_roles(role)
        if emoji == "👻":
            role = discord.utils.get(guild.roles, id=958870090286239764)
            await member.add_roles(role)
        if emoji == "💛":
            role = discord.utils.get(guild.roles, id=957084786856452136)
            await member.add_roles(role)
        if emoji == "🤍":
            role = discord.utils.get(guild.roles, id=957084624088096768)
            await member.add_roles(role)


@bot.command(name="rules")
@commands.has_permissions(administrator=True)
async def rules(ctx):
    embed = discord.Embed(title="Hey, bienvenue à toi sur le serveur !",
                          description=f"Je te prie de lire le règlement attentivement <a:ping:958506589067829320>\n\n\n1/ <a:white_right_arrow:957288255458521194> Toute insulte, manque de respect, etc.. sera suivi d'une sanction.\n\n\n2/ <a:white_right_arrow:957288255458521194> Le troll est formellement interdit sur le serveur et sera suivi d'un ban.\n\n\n3/ <a:white_right_arrow:957288255458521194> Toute pub d'un serveur menant à autre serveur que Kanna sera suivie d'un ban idd.\n\n\n4/ <a:white_right_arrow:957288255458521194> Tout spam sera suivi d'un ban y compris le spam de tickets.\n\n\n5/ <a:white_right_arrow:957288255458521194> Tout abus de pouvoir sera suivi d'un derank.\n\n\n6/ <a:white_right_arrow:957288255458521194> Toute photo inappropriée sera suivie d'un ban.\n\n\n7/ <a:white_right_arrow:957288255458521194> Le nsfw est interdit sur le serveur ! \n\n\n8/ <a:white_right_arrow:957288255458521194> Il est interdit de divulguer des informations personnelles sur qui que ce soit.\n\n\n9/ <a:white_right_arrow:957288255458521194> Toute personne qui ne respectera pas les salons sera warn, et à 3 warns c'est un mute\n\n\n10/ <a:white_right_arrow:957288255458521194> Le vol de mudae n'est pas autorisé; si on vous vole un perso je vous invite à nous faire un ticket et la personne devra rendre le perso + warn. Si ça se reproduit, c'est kick", color=0xffff8f)
    embed.set_image(
        url="https://cdn.discordapp.com/attachments/950176106592501760/958499750372573234/banner_rules_kanna.png")

    await ctx.send(embed=embed)


@bot.command(name="clean")
async def clean(ctx, *arg):
    if arg == ():
        await ctx.channel.send("**Veuillez entrer le nombre de messages à nettoyer !**")
    else:
        messages = await ctx.channel.history(limit=int(arg[0]) + 1).flatten()
        for each_msg in messages:
            await each_msg.delete()
        await ctx.channel.send(f"**{int(arg[0])} message(s) cleaned !**", delete_after=5)


@bot.command(name="question")
async def question(ctx, *arg):
    if arg == ():
        await ctx.channel.send("**Veuillez entrer une question !**")

    else:
        switch = 0
        for i in arg:
            if i == '?':
                switch = 1

        if switch == 1:
            alea = random.randint(1, 100)
            alea2 = random.randint(0, 4)

            if alea > 50:
                answer = yes_rep[alea2]
            else:
                answer = no_rep[alea2]
            await ctx.message.reply(answer)
        else:
            await ctx.channel.send("**Vous ne savez pas faire une question ?**")


@bot.command(name="ban")
@commands.has_permissions(ban_members=True)
async def ban(ctx, user: discord.User, *, reason="Aucune raison n'a été donné."):
    await ctx.guild.ban(user, reason=reason)

    embed = discord.Embed(title="**Bannissement**",
                          description=f"{user.name} a été banni !", color=0xffff8f)
    embed.set_author(name=ctx.author.name, icon_url=ctx.author.avatar_url)
    embed.set_thumbnail(
        url="https://cdn.discordapp.com/attachments/950176106592501760/955633376075874344/952598944528072794.png")
    embed.add_field(name="Raison", value=reason, inline=True)
    #embed.set_footer(text = "Est-ce que je mets qlq chose là ?")

    await ctx.send(embed=embed)


@bot.command(name="unban")
@commands.has_permissions(ban_members=True)
async def unban(ctx, user: discord.User, *, reason="Aucune raison n'a été donné"):
    await ctx.guild.unban(user, reason=reason)

    embed = discord.Embed(title="**Débannissement**",
                          description=f"{user.name} a été débanni !", color=0xffff8f)
    embed.set_author(name=ctx.author.name, icon_url=ctx.author.avatar_url)
    embed.set_thumbnail(
        url="https://cdn.discordapp.com/attachments/950176106592501760/955978194819883008/955976022749249576.png")
    embed.add_field(name="Raison", value=reason, inline=True)

    await ctx.send(embed=embed)


@bot.command(name="kick")
@commands.has_permissions(kick_members=True)
async def kick(ctx, user: discord.User, *, reason="Aucune raison n'a été donné"):
    await ctx.guild.kick(user, reason=reason)

    embed = discord.Embed(
        title="**Exclu**", description=f"{user.name} a été expulsé !", color=0xffff8f)
    embed.set_author(name=ctx.author.name, icon_url=ctx.author.avatar_url)
    embed.set_thumbnail(
        url="https://cdn.discordapp.com/attachments/950176106592501760/956333889603903498/tokyo-revengers-png-29.png")
    embed.add_field(name="Raison", value=reason, inline=True)

    await ctx.send(embed=embed)


async def createdMutedRole(ctx):
    mutedRole = await ctx.guild.create_role(name="muted", permissions=discord.Permissions(send_messages=False, speak=False, add_reactions=False), reason="Création du rôle muted")

    for channel in ctx.guild.channels:
        await channel.set_permissions(mutedRole, send_messages=False, speak=False, add_reactions=False)
    return mutedRole


async def getMutedRole(ctx):
    roles = ctx.guild.roles
    for role in roles:
        if role.name == "muted":
            return role

    return await createdMutedRole(ctx)


@bot.command(name="mute")
@commands.has_any_role(938563308347355137, 953706352969138218, 941936882776965212, 926805088931029012, 954439468331450370)
async def mute(ctx, member: discord.Member, *, reason="Aucune raison n'a été donné"):
    muted_role = await getMutedRole(ctx)
    await member.add_roles(muted_role, reason=reason)

    embed = discord.Embed(
        title="**Muted**", description=f"{member.name} a été mute !", color=0xffff8f)
    embed.set_author(name=ctx.author.name, icon_url=ctx.author.avatar_url)
    embed.set_thumbnail(
        url="https://cdn.discordapp.com/attachments/950176106592501760/956334711049977866/tokyo-revengers-png-34.png")
    embed.add_field(name="Raison", value=reason, inline=True)

    await ctx.send(embed=embed)


@bot.command(name="unmute")
@commands.has_any_role(938563308347355137, 953706352969138218, 941936882776965212, 926805088931029012, 954439468331450370)
async def unmute(ctx, member: discord.Member, *, reason="Aucune raison n'a été donné"):
    muted_role = await getMutedRole(ctx)
    await member.remove_roles(muted_role, reason=reason)

    embed = discord.Embed(
        title="**Unmuted**", description=f"{member.name} a été unmute !", color=0xffff8f)
    embed.set_author(name=ctx.author.name, icon_url=ctx.author.avatar_url)
    embed.set_thumbnail(
        url="https://cdn.discordapp.com/attachments/950176106592501760/956345838576238592/IMG_20220324_011637.png")
    embed.add_field(name="Raison", value=reason, inline=True)

    await ctx.send(embed=embed)


# Lancement

bot.run(os.environ["DISCORD_TOKEN"])
