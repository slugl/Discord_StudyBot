from bot_class.study_bot import StudyBot
import os

# Token값 가져오기
# TOKEN = os.environ.get("TOKEN")

TOKEN = "OTMxNDMyMDkyNTMxODM5MDM2.YeEVvA.rj9PWf2_la3wb5CClKAWDIlMu-w"

discord_bot = StudyBot('!')

for filename in os.listdir("src/Cogs"):
    if filename.endswith(".py"):
        discord_bot.load_extension(f"Cogs.{filename[:-3]}")

discord_bot.initialize()
discord_bot.add_schedule()
discord_bot.run(TOKEN)