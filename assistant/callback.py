# gezet - Ubot
# Copyright (C) 2022-2023 @gezetXd
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
from pygezet.assistant import callback
from random import choice

from . import *
from .inline import help_string


@callback(pattern="plugins-tab")
async def plugins_page(_, cb: CallbackQuery):
    btn = yins.HelpXd(0, CMD_HELP, "xd")
    await cb.edit_message_text(
        text=help_string(),
        reply_markup=InlineKeyboardMarkup(btn)
    )


@callback(pattern="xd-next\\((.+?)\\)")
async def give_next_page(_, cb: CallbackQuery):
    current_page_number = int(cb.matches[0].group(1))
    btn = yins.HelpXd(current_page_number + 1, CMD_HELP, "xd")
    await cb.edit_message_reply_markup(reply_markup=InlineKeyboardMarkup(btn))


@callback(pattern="xd-prev\\((.+?)\\)")
async def give_old_page(_, cb: CallbackQuery):
    current_page_number = int(cb.matches[0].group(1))
    btn = yins.HelpXd(current_page_number - 1, CMD_HELP, "xd")
    await cb.edit_message_reply_markup(reply_markup=InlineKeyboardMarkup(btn))


@callback(pattern="back-to-plugins-page-(.*)")
async def get_back(_, cb: CallbackQuery):
    page_number = int(cb.matches[0].group(1))
    btn = yins.HelpXd(page_number, CMD_HELP, "xd")
    await cb.edit_message_text(text=help_string(), reply_markup=InlineKeyboardMarkup(btn))


@callback(pattern="pluginlist-(.*)")
async def give_plugin_cmds(_, cb: CallbackQuery):
    plugin_name, page_number = cb.matches[0].group(1).split("|", 1)
    plugs = await yins.PluginXd(CMD_HELP, plugin_name)
    cmd_string = f"<b>PLUGIN:</b> {plugin_name.capitalize()}\n<b>HNDLR:</b> <code>{choice(hndlr)}</code>\n\n" + "".join(plugs)
    await cb.edit_message_text(
        cmd_string,
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        text="Back",
                        callback_data=f"back-to-plugins-page-{page_number}",
                    )
                ]
            ]
        ),
    )
