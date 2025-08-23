# plugins/ping.py (Versi Revisi)

import time
import asyncio
import random
from pyrogram import Client, filters
from pyrogram.types import Message

from core.client import VzoelUbot
from config import PREFIX
from core.decorators import owner_only
from core.string_manager import get_string # <-- Mengimpor get_string

@VzoelUbot.on_message(filters.command("ping", PREFIX) & filters.me)
@owner_only
async def ping_command(client: VzoelUbot, message: Message):
    start_time = time.time()
    
    # Mengambil daftar kata dari string manager
    processing_words = get_string("PING.PROCESSING_WORDS")
    animation_words = random.sample(processing_words, 2)
    
    try:
        for word in animation_words:
            await message.edit_text(word)
            await asyncio.sleep(0.5)
    except Exception:
        return

    end_time = time.time()
    latency = round((end_time - start_time) * 1000, 2)
    
    # Mengambil template hasil dan mengisinya dengan data
    result_template = get_string("PING.RESULT")
    await message.edit_text(result_template.format(latency=latency))
