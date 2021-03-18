#!/usr/bin/env python3
import os
import psutil
import discord
from psutil._common import bytes2human

discordTokenFile = open("token.env")
discordToken = discordTokenFile.read()
discordTokenFile.close()

class statsQuery(discord.Client):
    async def on_ready(self):
        print('Logged on as', self.user)

    async def on_message(self, message):
        if message.author == self.user:
            return

        if message.content == '/ram':
            mem_usage = psutil.virtual_memory()
            total_mem = bytes2human(mem_usage[0])
            used_mem = bytes2human(mem_usage[3])
            await message.channel.send(used_mem + " of " + total_mem + " of RAM used")

        if message.content == '/cpu':
            fetchCPU = psutil.cpu_freq()
            currCPU = str(fetchCPU[0]) 
            maxCPU = str(fetchCPU[2])
            loadAvg = str(psutil.getloadavg())
            await message.channel.send("Clock Speed: " + currCPU[0:1] + "." + currCPU[1:2] + "Ghz" + " of " + maxCPU[0:1] + "." + maxCPU[1:2] + "Ghz")
            await message.channel.send("Load Average: " + loadAvg)
            
client = statsQuery()
client.run(discordToken)