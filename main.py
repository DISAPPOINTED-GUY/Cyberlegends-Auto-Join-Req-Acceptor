try:
    from tv.plugins.start import *
    logger.info("Plugins imported Succesfully")
except Exception as e:
    logger.info("Error while importing plugins")

from pyrogram import filters
