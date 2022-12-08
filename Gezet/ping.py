# gezet - Ubot
# Copyright (C) 2022-2023 @senaex
#
# This file is a part of < https://github.com/alvrnxz/Gzpyro-Bot >
# PLease read the GNU Affero General Public License in
# <https://www.github.com/alvrnxz/Gzpyro-Bot/blob/main/LICENSE/>.
#
# FROM Gzpyro-Bot <https://github.com/alvrnxz/Gzpyro-Bot>
# t.me/GzSupportGroup & t.me/eageza


# ========================×========================
#            Jangan Hapus Credit Ngentod
# ========================×========================

import time

from datetime import datetime

from fipper import Client
from fipper.types import Message

from pygezet import CMD_HELP
from pygezet.decorator import gezet

from . import *


@gezet(["ping", "yins"])
async def pingme(client: Client, message: Message):
    start = datetime.now()
    uptime = await yins.get_readable_time((time.time() - StartTime))
    xnxx = await message.reply("<b>✧</b>")
    await xnxx.edit("<b>✧✧</b>")
    await xnxx.edit("<b>✧✧✧</b>")
    await xnxx.edit("<b>✧✧✧✧</b>")
    await xnxx.edit("<b>✧✧✧✧✧</b>")
    end = datetime.now()
    duration = (end - start).microseconds / 1000
    await xnxx.edit(
        f"<b>✧ Gzpyro-Bot ✧</b>\n\n"
        f"<b>✧ Pinger :</b> <code>{duration}ms</code>\n"
        f"<b>✧ Uptime :</b> <code>{uptime}</code>"
    )


CMD_HELP.update(
    {"ping": (
        "ping",
        {
            "ping": "Check Ping Your Bot.",
        }
    )
    }
)
