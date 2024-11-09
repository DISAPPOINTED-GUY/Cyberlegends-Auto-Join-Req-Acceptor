try:
    from Tv.plugins.start import *
    logger.info("Plugins imported Succesfully")
except Exception as e:
    logger.info(f"Error while importing plugins : {e}")
    exit(1)
from .Tv import tv
from pyrogram import filters


@tv.on_message(filters.command("start"))
async def handle_start_command(tv, message):
   try:
      await start_command(tv, message)
   except Exception as e:
       print(f"Failed to import Start Command: {e}")

tv.run()
