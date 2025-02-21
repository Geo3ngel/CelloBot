import os
from dotenv import load_dotenv
load_dotenv()
from utils.args import args
from utils.coreManager import CoreManager
from utils.discord import DiscordBot
from webui import start_ui
from threading import Thread

core_manager = CoreManager(init_config_file=args.config)

# For Discord Bot
discord_bot = DiscordBot(core_manager)
discord_thread = Thread(target=discord_bot.run, args=[os.getenv("DISCORD_BOT_TOKEN")])
discord_thread.start()

# For Web UI
web_thread = Thread(target=start_ui, args=[core_manager])
web_thread.start()

# Keep running this main thread while others threads are active
discord_thread.join()
web_thread.join()