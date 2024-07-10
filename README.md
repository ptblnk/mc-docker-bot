# What is it?
A self-hosted discord bot that enables Minecraft server administrators to execute server commands from Discord for servers using the [itzg/minecraft](https://github.com/itzg/docker-minecraft-server) docker image.

# Discord set up
This bot is self-hosted. You must run it on the same server from which you host your docker Minecraft server. 
To start, log in to the [Discord Developer Portal](https://discord.com/developers). 
1. Ensure the bot is private (installation > install link > none).
2. Make sure the bot has server members intent, and message content intent privileges. (under bot tab).
3. Click on the OAuth2 tab, click on 'bot', click on 'Administrator' then copy the link into your search bar. Hit enter and add the bot to your desired server.

# Bot set up
The Python script assumes that the Minecraft server docker image is being run on a Linux server with sudo installed. It also assumes that running any docker command requires super user privileges. If this is not the case for your server, feel free to modify the script, or change your server configuration. 

1. Download the bot.py file.
2. Ensure pip is installed (search how to do this on your distro).
3. Install discord.py with `pip install discord.py`
4. Change the token at the very bottom to match your Discord bot's token.
5. Run `sudo python3 bot.py`.

# Troubleshooting
>"Externally managed environment" error when attempting to install discord.py with pip.
Your chosen distro may use its own package manager to handle Python packages. To fix this, either modify the way your server is configured, or append the --break-system-packages flag to the end of your `pip install ... ` command. 
