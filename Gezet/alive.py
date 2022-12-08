# gezet - Ubot
# Copyright (C) 2022-2023 @senaex
#
# This file is a part of < https://github.com/alvrnxz/GzPyro-Bot >
# PLease read the GNU Affero General Public License in
# <https://www.github.com/gezetXd/gezetUbot/blob/main/LICENSE/>.
#
# FROM Gzpyro-Bot <https://github.com/alvrnxz/Gzpyro-Bot>
# t.me/GzSupportGroup & t.me/eageza


# ========================×========================
#            Jangan Hapus Credit Ngentod
# ========================×========================

import time

from fipper import Client, __version__ as fip_ver
from fipper.types import Message
from platform import python_version

from pygezet import __version__, gezet_ver
from pygezet import CMD_HELP, HOSTED_ON, adB
from pygezet.decorator import gezet


from . import *


@gezet(["alive", "yins"])
async def aliveme(client: Client, message: Message):
    chat_id = message.chat.id
    user = await client.get_me()
    output = (
        f"**Tʜᴇ [Gzpyro-Bot](https://github.com/alvrnxz/Gzpyro-Bot)**\n\n"
        f"**{var.ALIVE_TEXT}**\n\n"
        f"╭✠╼━━━━━━━━━━━━━━━✠╮\n"
        f"≽ **Base On :** •[{adB.name}]•\n"
        f"≽ **Owner :** [{user.first_name}](tg://user?id={user.id}) \n"
        f"≽ **Modules :** `{len(CMD_HELP)} Modules` \n"
        f"≽ **Python Version :** `{python_version()}`\n"
        f"≽ **Py-Gezet Pyrogran :** `{fip_ver}`\n"
        f"≽ **Py-Gezet Version :** `{__version__}`\n"
        f"≽ **Gezet Version :** `{gezet_ver}` [{HOSTED_ON}]\n"
        "╰✠╼━━━━━━━━━━━━━━━✠╯\n\n"
    )
    await message.delete()
    try:
        if var.ALIVE_PIC:
            endsw = (".mp4", ".gif")
            if var.ALIVE_PIC.endswith(endsw):
                await client.send_video(chat_id=chat_id, video=var.ALIVE_PIC, caption=output)
            else:
                await client.send_photo(chat_id=chat_id, photo=var.ALIVE_PIC, caption=output)
        else:
            await message.reply_text(output)
    except BaseException as xd:
        await message.reply(xd)


CMD_HELP.update(
    {"alive": (
        "alive",
        {
            "alive": "Chech Your Userbot.",
        }
    )
    }
)
