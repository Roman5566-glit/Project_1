from pyrogram.filters import inline_keyboard
from pyrogram.types import KeyboardButton, ReplyKeyboardMarkup, InlineKeyboardButton, InlineKeyboardMarkup
from pyrogram import emoji


# Функция для кнопок главной клавиатуры
btn_info = KeyboardButton(f'{emoji.INFORMATION} Инфо')
btn_games = KeyboardButton(f'{emoji.VIDEO_GAME} Игры')
btn_generate = KeyboardButton(f'{emoji.GLASSES} Сгенерировать изображение')
btn_profile = KeyboardButton(f'{emoji.PERSON} Профиль')

# Функция для выбора игры
btn_rps = KeyboardButton(f'{emoji.PLAY_BUTTON} Камень, ножницы, бумага')
btn_quest = KeyboardButton(f'{emoji.CITYSCAPE_AT_DUSK} Пройти квест')
btn_back = KeyboardButton(f'{emoji.BACK_ARROW} Назад')


# Функция для игровой клавиатуры
btn_rock = KeyboardButton(f'{emoji.ROCK} Камень')
btn_scissors = KeyboardButton(f'{emoji.SCISSORS} Ножници')
btn_paper = KeyboardButton(f'{emoji.NOTEBOOK} Бумага')
btn_back1 = KeyboardButton(f'{emoji.BACK_ARROW} Назад')

# Главная клавиатура
kb_main = ReplyKeyboardMarkup(
    keyboard=[
        [btn_info, btn_games, btn_profile],
        [btn_generate]
    ],
    resize_keyboard=True
)

# Клавиатура для выбора игры
kb_games = ReplyKeyboardMarkup(
    keyboard=[
            [btn_rps],
            [btn_quest, btn_back]
    ],
    resize_keyboard=True
)

# Игровая клавиатура №1
kb_game1 = ReplyKeyboardMarkup(
    keyboard=[
            [btn_rock, btn_scissors, btn_paper],
            [btn_back1]
    ],
    resize_keyboard=True
)


inline_kb_start_quest = InlineKeyboardMarkup([
    [InlineKeyboardButton('Пройти квест', callback_data='start_quest')]
])

inline_kb_choice = InlineKeyboardMarkup([
    [InlineKeyboardButton("Левая дверь", callback_data="left_door")],
    [InlineKeyboardButton("Правая дверь", callback_data="right_door")]
])

inline_kb_left_door = InlineKeyboardMarkup([
    [InlineKeyboardButton("Сражаться с драконом", callback_data="dragon")],
    [InlineKeyboardButton("Попытаться убежать", callback_data="run")]
])

inline_kb_right_door = InlineKeyboardMarkup([
    [InlineKeyboardButton("Золотая корона", callback_data="gold_crown")],
    [InlineKeyboardButton("Незеритовый меч", callback_data="netherite_dagger")],
    [InlineKeyboardButton("Серебрянный кинжал", callback_data="silver_dagger")],
    [InlineKeyboardButton("Старая книга", callback_data="old_book")]
])

inline_kb_netherite_dagger = InlineKeyboardMarkup([
    [InlineKeyboardButton("Ты берешь меч, покрыт сплавом незерита, слитком метала из другого измирения!", callback_data="netherite_dager_a")],
    [InlineKeyboardButton("Что-бы пользоваться мечом, тебе нужно выбрать сторону: Добро или Зло!", callback_data="dark_and_light")]
])

inline_kb_dark_and_light = InlineKeyboardMarkup([
    [InlineKeyboardButton("Добро", callback_data="light")],
    [InlineKeyboardButton("Зло", callback_data="dark")]
])