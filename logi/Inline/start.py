from pyrogram.types import (CallbackQuery, InlineKeyboardButton,
                            InlineKeyboardMarkup, InputMediaPhoto, Message)

from config import MUSIC_BOT_NAME, SUPPORT_CHANNEL, SUPPORT_GROUP , OWNER_USERNAME
from logi import BOT_USERNAME


def setting_markup2():
    buttons = [
        [
            InlineKeyboardButton(text="🔈 Audio Quality", callback_data="AQ"),
            InlineKeyboardButton(text="🎚 Audio Volume", callback_data="AV"),
        ],
        [
            InlineKeyboardButton(
                text="👥 Authorized Users", callback_data="AU"
            ),
            InlineKeyboardButton(
                text="💻 Dashboard", callback_data="Dashboard"
            ),
        ],
        [
            InlineKeyboardButton(text="✖️ Close", callback_data="close"),
        ],
    ]
    return f"🔧  **{MUSIC_BOT_NAME} Settings**", buttons


def start_pannel():
    if not SUPPORT_CHANNEL and not SUPPORT_GROUP:
        buttons = [
            [
                InlineKeyboardButton(
                    text="Commands", callback_data="shikhar"
                ),
            ],
            [
                InlineKeyboardButton(
                    text="settings", callback_data"=settingm"
                )
            ],
            
        ]
        return f"🎛  **This is {MUSIC_BOT_NAME}**", buttons
    if not SUPPORT_CHANNEL and SUPPORT_GROUP:
        buttons = [
            [
                InlineKeyboardButton(
                    text="Commands", callback_data="shikhar"
                ),
            ],
            [
                InlineKeyboardButton(
                    text="settings", callback_data="settingm"
                )
            ],
            [
                InlineKeyboardButton(
                    text="official Group", url=f"{SUPPORT_GROUP}"
                ),
            ],
           [
          InlineKeyboardButton(
                text="OWNER",
                url=f"https://t.me/{OWNER_USERNAME}",
            ),
        ],
          [

       
                    InlineKeyboardButton(
                        "source code", url="http://github.com/UnoDark/Music-Bot"
                    )
                ],
        ]
        return f"🎛  **This is {MUSIC_BOT_NAME}*", buttons
    if SUPPORT_CHANNEL and not SUPPORT_GROUP:
        buttons = [
            [
                InlineKeyboardButton(
                    text="Commands", callback_data"shikhar"
                ),
            ],
            [
                InlineKeyboardButton(
                    text="settings", callback_data"settingm"
                )
            ],
            [
                InlineKeyboardButton(
                    text="official channel", url=f"{SUPPORT_CHANNEL}"
                ),
            ],
           [
          InlineKeyboardButton(
                text="OWNER",
                url=f"https://t.me/{OWNER_USERNAME}",
            ),
        ],
          [

       
                    InlineKeyboardButton(
                        "source code", url="https://github.com/UnoDark/Music-Bot"
                    )
                ],
        ]
        return f"🎛  **This is {MUSIC_BOT_NAME}**", buttons
    if SUPPORT_CHANNEL and SUPPORT_GROUP:
        buttons = [
            [
                InlineKeyboardButton(
                    text="Commands", callback_data="shikhar"
                ),
            ],
            [
                InlineKeyboardButton(
                    text="settings", callback_data="settingm"
                )
            ],
            [
                InlineKeyboardButton(
                    text="official channel", url=f"{SUPPORT_CHANNEL}"
                ),
                InlineKeyboardButton(
                    text="official Group", url=f"{SUPPORT_GROUP}"
                ),
            ],
           [
          InlineKeyboardButton(
                text="OWNER",
                url=f"https://t.me/{OWNER_USERNAME}",
            ),
        ],
          [

       
                    InlineKeyboardButton(
                        "source code", url="https://github.com/UnoDark/Music-Bot"
                    )
                ],
        ]
        return f"🎛  **This is {MUSIC_BOT_NAME}**", buttons


def private_panel():
    if not SUPPORT_CHANNEL and not SUPPORT_GROUP:
        buttons = [
            [
                InlineKeyboardButton(
                    text="Commands", callback_data="shikhar"
                ),
            ],
            [
                InlineKeyboardButton(
                    "➕ Add me to your Group",
                    url=f"https://t.me/{BOT_USERNAME}?startgroup=true",
                )
            ],
           [
          InlineKeyboardButton(
                text="OWNER",
                url=f"https://t.me/{OWNER_USERNAME}",
            ),
                InlineKeyboardButton(
                    text="ᴄᴏᴅᴇ ᴏᴡɴᴇʀ", url="https://t.me/OneUnoOnly"
                )            
            
        ],       
        ]
        return f"🎛  **This is {MUSIC_BOT_NAME}**", buttons
    if not SUPPORT_CHANNEL and SUPPORT_GROUP:
        buttons = [
            [
                InlineKeyboardButton(
                    text="Commands", callback_data="shikhar"
                ),
            ],
            [
                InlineKeyboardButton(
                    "➕ Add me to your Group",
                    url=f"https://t.me/{BOT_USERNAME}?startgroup=true",
                )
            ],
            [
                InlineKeyboardButton(
                    text="official Group", url=f"{SUPPORT_GROUP}"
                ),
            ],
           [
          InlineKeyboardButton(
                text="OWNER",
                url=f"https://t.me/{OWNER_USERNAME}",
            ),
                InlineKeyboardButton(
                    text="ᴄᴏᴅᴇ ᴏᴡɴᴇʀ", url="https://t.me/OneUnoOnly"
                )              
        ],
          [

       
                    InlineKeyboardButton(
                        "source code", url="http://github.com/UnoDark/Music-Bot"
                    )
                ],
        ]
        return f"🎛  **This is {MUSIC_BOT_NAME}*", buttons
    if SUPPORT_CHANNEL and not SUPPORT_GROUP:
        buttons = [
            [
                InlineKeyboardButton(
                    text="Commands", callback_data="shikhar"
                ),
            ],
            [
                InlineKeyboardButton(
                    "➕ Add me to your Group",
                    url=f"https://t.me/{BOT_USERNAME}?startgroup=true",
                )
            ],
            [
                InlineKeyboardButton(
                    text="official channel", url=f"{SUPPORT_CHANNEL}"
                ),
            ],
           [
          InlineKeyboardButton(
                text="OWNER",
                url=f"https://t.me/{OWNER_USERNAME}",
            ),
        ],
          [

       
                    InlineKeyboardButton(
                        "source code", url="https://github.com/UnoDark/Music-Bot"
                    )
                ],
        ]
        return f"🎛  **This is {MUSIC_BOT_NAME}**", buttons
    if SUPPORT_CHANNEL and SUPPORT_GROUP:
        buttons = [
            [
                InlineKeyboardButton(
                    text="Commands", callback_data="shikhar"
                ),
            ],
            [
                InlineKeyboardButton(
                    "➕ Add me to your Group",
                    url=f"https://t.me/{BOT_USERNAME}?startgroup=true",
                )
            ],
            [
                InlineKeyboardButton(
                    text="official channel", url=f"{SUPPORT_CHANNEL}"
                ),
                InlineKeyboardButton(
                    text="official Group", url=f"{SUPPORT_GROUP}"
                ),
            ],
           [
          InlineKeyboardButton(
                text="OWNER",
                url=f"https://t.me/{OWNER_USERNAME}",
            ),
        ],
          [

       
                    InlineKeyboardButton(
                        "source code", url="https://github.com/UnoDark/Music-Bot"
                    )
                ],
        ]
        return f"🎛  **This is {MUSIC_BOT_NAME}**", buttons


def setting_markup():
    buttons = [
        [
            InlineKeyboardButton(text="🔈 Audio Quality", callback_data="AQ"),
            InlineKeyboardButton(text="🎚 Audio Volume", callback_data="AV"),
        ],
        [
            InlineKeyboardButton(
                text="👥 Authorized Users", callback_data="AU"
            ),
            InlineKeyboardButton(
                text="💻 Dashboard", callback_data="Dashboard"
            ),
        ],
        [
            InlineKeyboardButton(text="✖️ Close", callback_data="close"),
            InlineKeyboardButton(text="🔙 Go Back", callback_data="okaybhai"),
        ],
    ]
    return f"🔧  **{MUSIC_BOT_NAME} Settings**", buttons


def volmarkup():
    buttons = [
        [
            InlineKeyboardButton(
                text="🔄 Reset Audio Volume 🔄", callback_data="HV"
            )
        ],
        [
            InlineKeyboardButton(text="🔈 Low Vol", callback_data="LV"),
            InlineKeyboardButton(text="🔉 Medium Vol", callback_data="MV"),
        ],
        [
            InlineKeyboardButton(text="🔊 High Vol", callback_data="HV"),
            InlineKeyboardButton(text="🔈 Amplified Vol", callback_data="VAM"),
        ],
        [
            InlineKeyboardButton(
                text="🔽 Custom Volume 🔽", callback_data="Custommarkup"
            )
        ],
        [InlineKeyboardButton(text="🔙 Go back", callback_data="settingm")],
    ]
    return f"🔧  **{MUSIC_BOT_NAME} Settings**", buttons


def custommarkup():
    buttons = [
        [
            InlineKeyboardButton(text="+10", callback_data="PTEN"),
            InlineKeyboardButton(text="-10", callback_data="MTEN"),
        ],
        [
            InlineKeyboardButton(text="+25", callback_data="PTF"),
            InlineKeyboardButton(text="-25", callback_data="MTF"),
        ],
        [
            InlineKeyboardButton(text="+50", callback_data="PFZ"),
            InlineKeyboardButton(text="-50", callback_data="MFZ"),
        ],
        [InlineKeyboardButton(text="🔼Custom Volume 🔼", callback_data="AV")],
    ]
    return f"🔧  **{MUSIC_BOT_NAME} Settings**", buttons


def usermarkup():
    buttons = [
        [
            InlineKeyboardButton(text="👥 Everyone", callback_data="EVE"),
            InlineKeyboardButton(text="🙍 Admins", callback_data="AMS"),
        ],
        [
            InlineKeyboardButton(
                text="📋 Authorized Users Lists", callback_data="USERLIST"
            )
        ],
        [InlineKeyboardButton(text="🔙 Go back", callback_data="settingm")],
    ]
    return f"🔧  **{MUSIC_BOT_NAME} Settings**", buttons


def dashmarkup():
    buttons = [
        [
            InlineKeyboardButton(text="✔️ Uptime", callback_data="UPT"),
            InlineKeyboardButton(text="💾 Ram", callback_data="RAT"),
        ],
        [
            InlineKeyboardButton(text="💻 Cpu", callback_data="CPT"),
            InlineKeyboardButton(text="💽 Disk", callback_data="DIT"),
            InlineKeyboardButton(text="UNO", url="https://t.me/OneUnoOnly"),
         
        ],
        [InlineKeyboardButton(text="🔙 Go back", callback_data="settingm")],
    ]
    return f"🔧  **{MUSIC_BOT_NAME} Settings**", buttons
