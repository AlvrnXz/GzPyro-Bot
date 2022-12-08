# gezet - Ubot
# Copyright (C) 2022-2023 @senaex
#
# This file is a part of < https://github.com/alvrnxz/Gzpyro-Bot >
# PLease read the GNU Affero General Public License in
# <https://www.github.com/alvrnxz/Gzpyro-Bot/blob/main/LICENSE/>.
#
# FROM Gzpyro-Bot <https://github.com/gezetXd/gezetUbot>
# t.me/GzSupportGroup & t.me/eageza


# ========================×========================
#            Jangan Hapus Credit Ngentod
# ========================×========================

from fipper.types import *

from pygezet import CMD_HELP
from pygezet.assistant import inline

from config import Var

from . import yins


handler = f"{Var.HNDLR[0]} {Var.HNDLR[1]} {Var.HNDLR[2]} {Var.HNDLR[3]} {Var.HNDLR[4]} {Var.HNDLR[5]}"

def help_string():
    text = f"""
<b>Help Module</b>
    <b>Prefixes:</b> <code>{handler}</code>
"""

    return text


@inline(pattern="help")
async def inline_result(_, inline_query):
    rslts=[
        (
            InlineQueryResultArticle(
                title="gezet Ubot!",
                reply_markup=InlineKeyboardMarkup(
                    yins.HelpXd(0, CMD_HELP, "xd")
                ),
                input_message_content=InputTextMessageContent(help_string()),
            )
        )
    ]
    await inline_query.answer(
        rslts,
        cache_time=0
    )


@inline(pattern="paste")
async def inline_result(_, iq):
    query = iq.query
    ok = query.split("-")[1]
    rslts=[
        (
            InlineQueryResultArticle(
                title="Paste gezet Ubot!",
                reply_markup=InlineKeyboardMarkup(
                    [
                        [
                            InlineKeyboardButton(
                                text="• SpaceBin •",
                                url=f"https://spaceb.in/{ok}",
                            ),
                            InlineKeyboardButton(
                                text="• Raw •",
                                url=f"https://spaceb.in/api/v1/documents/{ok}/raw",
                            ),
                        ]
                    ]
                ),
                input_message_content=InputTextMessageContent("Pasted to Spacebin 🌌"),
            )
        )
    ]
    await iq.answer(
        rslts,
        cache_time=0
    )
