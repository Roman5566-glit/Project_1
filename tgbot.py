import base64
from Fusen_brain_ai import generate
from pyrogram import Client, filters
from pyrogram.types import ForceReply, ForceReply
import random
import json
import keyboards
import config



bot = Client(
    api_id=config.API_ID,
    api_hash=config.API_HASH,
    bot_token=config.BOT_TOKEN,
    name="my_bot"  # Указуем любое))
)


# Функция для пустых фильтров
def button_filter(button):
    async def func(_, __, msg):
        return msg.text == button.text
    return filters.create(func, "ButtonFilter", button=button)


# Функция для команды start
@bot.on_message(filters.command("start"))
async def start(bot, message):
    await message.reply('Здравствуйте! 😊 '
                        'Меня зовут Роман, и я учусь в школе RTS. Рад видеть вас здесь! 🎓 '
                        'Вас приветствует мой личный Telegram-помощник — **FunBot**! 🤖✨ '
                        'Он всегда готов помочь, развлечь и предложить увлекательные игры. 🎮🎲 '
                        'Не стесняйтесь задавать вопросы и наслаждайтесь общением с **FunBot**! 🚀 ', reply_markup=keyboards.kb_main)
    await bot.send_photo(message.chat.id, "images.jpg")

    with open("users.json", "r") as file:
        users = json.load(file)
    if str(message.from_user.id) not in users.keys():
        users[message.from_user.id] = 100
        with open("users.json", "w") as file:
            json.dump(users, file)


# Функция для команды info
@bot.on_message(filters.command("info") | button_filter((keyboards.btn_info)))
async def info(bot, message):
    await bot.send_message(message.chat.id ,'Вся информация о командах, находиться тут: start-старт бота, info-узнать информацию, Ещё в разработке (help-помощь в командах.)')


@bot.on_message(filters.command("help"))
async def profile(bot, message):
    await bot.send_message(message.chat.id, "Простите но это ещё в разработке....")


# Функция для команды send_stick
@bot.on_message(filters.command("send_stick"))
async def profile(bot, message):
    await bot.send_message(message.chat.id, "Простите но это ещё в разработке....")


# Функция для команды profile
@bot.on_message(filters.command("profile") | button_filter(keyboards.btn_profile))
async def profile(bot, message):
    await bot.send_message(message.chat.id, "Простите но это ещё в разработке....")


# Функция для команды games
@bot.on_message(filters.command("games") | button_filter(keyboards.btn_games))
async def games(bot, message):
    await message.reply("Выбери игру", reply_markup=keyboards.kb_games)

    with open("users.json", "r") as file:
        users = json.load(file)
    if users[str(message.from_user.id)] >= 10:
        await message.reply("Твой ход!", reply_markup=keyboards.kb_games)
    else:
        await message.reply(f"У вас не достаточно средств. На твоем счету {users[str(message.from_user.ip)]}. "
                            f"Минимальная сумма 10")


# Функция для команды game и её работы
@bot.on_message(filters.command("game") | button_filter(keyboards.btn_rps))
async def game(bot, message):
    await message.reply("Твой ход", reply_markup=keyboards.kb_game1)


# Функция для настройки игры камень, ножницы, бумага
@bot.on_message(button_filter(keyboards.btn_rock) | button_filter(keyboards.btn_scissors) | button_filter(keyboards.btn_paper))
async def choise_game1(bot, message):
    rock = keyboards.btn_rock.text
    scissors = keyboards.btn_scissors.text
    paper = keyboards.btn_paper.text
    user = message.text
    pc = random.choice([rock, scissors, paper])

    with open("users.json", "r") as file:
        users = json.load(file)

    if user == pc:
        await message.reply("НИЧЬЯ!")
    elif (user == rock and pc == scissors) or (user == paper and pc == rock) or (user == scissors and pc == paper):
        await message.reply(f"ВЫ ПОБЕДИЛИ! Бот выбрал {pc}", reply_markup=keyboards.kb_games)
        users[str(message.from_user.id)] += 10
    else:
        await message.reply(f"Вы проиграли!Бот выбрал {pc}", reply_markup=keyboards.kb_games)
        user[str(message.from_user.id)] -= 5

    with open("users.json", "w") as file:
        json.dump(users, file)


# Функция для команды back
@bot.on_message(filters.command("back") | button_filter(keyboards.btn_back))
async def back(bot, message):
    await message.reply("Возврат в главное меню", reply_markup=keyboards.kb_main)


# Функция для команды back1
@bot.on_message(filters.command("back1") | button_filter(keyboards.btn_back1))
async def back1(bot, message):
    await message.reply("Возврат в меню выбора игры", reply_markup=keyboards.kb_games)


# Функция для игры в квест
@bot.on_message(filters.command("quest") | button_filter(keyboards.btn_quest))
async def quest(bot, message):
    await message.reply_text("Хотите ли вы отправиться в увлекательное путешествие, полное приключений и загадок?", reply_markup=keyboards.inline_kb_start_quest)

# Функция для условий игры квест
@bot.on_callback_query()
async def handle_query(bot, query):
    if query.data == 'start_quest':
        await bot.answer_callback_query(query.id, text="Добро пожаловать в игру квест!", show_alert=True)
        await query.message.reply_text("Ты стоишь перед двумя дверьми. Какую из них выберишь?", reply_markup=keyboards.inline_kb_choice)
    elif query.data == 'left_door':
        await  query.message.reply_text("Ты входишь в комнату, и видишь злого дракона! У тебя есть два варианта действий:", reply_markup=keyboards.inline_kb_left_door)
    elif query.data == 'right_door':
        await query.message.reply_text("Ты входишь в комнату, наполненную сокровищами! Тебе нужно выбрать только одно сокровище", reply_markup=keyboards.inline_kb_right_door)
    elif query.data == 'dragon':
        await bot.answer_callback_query(query.id, text="Ты сражаешься с драконом, но он оказываеться слишком сильным. Ты погибаешь", show_alert=True)
    elif query.data == 'run':
        await bot.answer_callback_query(query.id, text="Ты пытаешься убежать, но дракон догоняет тебя и съедает!((", show_alert=True)
    elif query.data == 'gold_crown':
        await bot.answer_callback_query(query.id, text="Ты берешь золотую корону и выходишь из комнаты. Поздравляю! Ты выиграл игру", show_alert=True)
    elif query.data == 'netherite_dagger':
        await bot.answer_callback_query(query.id, text="Ты берешь меч, покрыт сплавом незерита, слитком метала из другого измирения!", show_alert=True)
        await query.message.reply_text("Что-бы пользоваться мечом, тебе нужно выбрать сторону: Добро или Зло!", reply_markup=keyboards.inline_kb_dark_and_light)
    elif query.data == 'dark_and_light':
        await bot.answer_callback_query(query.id, text="Что-бы пользоваться мечом, тебе нужно выбрать сторону: Добро или Зло!", show_alert=True)
    elif query.data == 'light':
        await bot.answer_callback_query(query.id, text="Вы выбрали добро! Вы взяли меч, и пошли к своему королю, где с помощью доброй магии защищаете королевсто от злобных варваров! После по беды вы стаёте новым корольом и ваше королевство процветает!", show_alert=True)
    elif query.data == 'dark':
        await bot.answer_callback_query(query.id, text="Вы выбрали зло! Вы взяли меч, и пошли к своему королю, и вас начала поглащать тьма, вы уббиваете короля и все королество стаёт вашим! Но к сожалению вас быстро поглощает тьма и вы умираете!", show_alert=True)
    elif query.data == 'silver_dagger':
        await bot.answer_callback_query(query.id, text="Ты берешь серебрянний кинжал и выходишь из комнаты. К сожалению, кинжал ничего не стоит", show_alert=True)
    elif query.data == 'old_book':
        await bot.answer_callback_query(query.id, text="Ты берешь старую книгу и выходишь из комнаты. Книга оказываеться магической! Ты открываешь страницу и по являешся в другуом измерении где видешь....", show_alert=True)


query_text = 'Введи запрос для генерации изображения'
@bot.on_message(button_filter(keyboards.btn_generate))
async def image(bot, message):
    await message.reply(query_text, reply_markup=ForceReply(True))

@bot.on_message(filters.reply)
async def reply(bot, message):
    if message.reply_to_message.text == query_text:
        query = message.text
        await message.reply_text(f"Генерирую изображение по запросу: '{query}', подождите немного....")
        image = await generate(query)
        if image:
            image_data = base64.b64decode(image[0])
            with open(f'images/image.jpg', "wb") as file:
                file.write(image_data)
            await bot.send_photo(message.chat.id, f'images/image.jpg', reply_to_message_id=message.id)
        else:
            await message.reply_text("Возникла ошибка,  попробуйте ещё раз", reply_to_message_id=message.id)

    else:
        await message.reply_text("Введите запрос: ")

bot.run()




