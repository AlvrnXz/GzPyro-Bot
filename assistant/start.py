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

from fipper import filters
from fipper.types import (
    InlineKeyboardButton,
    InlineKeyboardMarkup,
)

from pygezet import __version__
from pygezet import tgbot
from pygezet.assistant import callback


START = """
❏ Haii {}
╭╼┅━━━━━╍━━━━━┅━━━━━━━┅╾
├▹ {} Adalah Ubot Pyrogram Telegram
├▹ Yang Dibuat Untuk Bersenang-Senang
├▹ Dan Memiliki Modul Yg Bisa Anda Gunakan
├▹ Bisa Membuat Ubot Sampai Dengan 10 String 
╰╼┅━━━━━╍━━━━━┅━━━━━━━┅╾
❏ © py-gezet v{}
"""


@tgbot.on_message(filters.private & filters.incoming &
                  filters.command("start"))
async def start(bot, msg):
    user = await bot.get_me()
    mention = user.mention
    buttons = [
        [
            InlineKeyboardButton(
                "☞︎︎︎ Create Gz Ubot ☜︎︎︎", callback_data="multi_client")
        ],
        [
            InlineKeyboardButton(
                "Help & Command", callback_data="help_or_command"), InlineKeyboardButton(
                "About", callback_data="about")
        ],
    ]
    await bot.send_message(
        msg.chat.id,
        START.format(msg.from_user.mention, mention, __version__),
        reply_markup=InlineKeyboardMarkup(buttons)
    )


@callback("help_or_command")
async def added_to_group_msg(client, cq):
    await cq.answer(
        "Sedang Tahap Percobaan...",
        show_alert=True,
    )


@callback("about")
async def added_to_group_msg(client, cq):
    await cq.answer(
        "Sedang Tahap Percobaan...",
        show_alert=True,
    )


@callback("multi_client")
async def added_to_group_msg(client, cq):
    await cq.message.reply(
        f"Silahkan Pilih Metode Dibawah Ini",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton("Buat Ubot", callback_data="gen_string"),
                    InlineKeyboardButton("Kirim String", callback_data="sending_string"),
                ]
            ]
        )
    )


@callback("gen_string")
async def added_to_group_msg(_, cq):
    await cq.answer(
        "Modul Buat String Belum Tersedia....",
        show_alert=True,
    )


@callback("sending_string")
async def added_to_group_msg(_, cq):
    await cq.answer(
        "Modul Kirim String Belum Tersedia....",
        show_alert=True,
    )
