from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart
from aiogram.dispatcher import FSMContext
from utils.db_api import database as commands
from loader import dp, bot
from utils.db_api.database import *
import datetime


@dp.channel_post_handler(lambda message: message.text in ['SendPostNotification'], state='*')
async def send_zikr(message: types.Message, state: FSMContext):
    now = datetime.datetime.now().minute
    if now == 0:
        users = await commands.get_users()
        for i in users:
            text = zikr = await get_zikr()
            try:
                await bot.send_message(chat_id=i.user_id, text=text)
            except:
                continue
    else:
        pass
        # try:
        #     text = 'f"10 marotaba'
        #     if zikr.zikr_arabic:
        #         text +=f"\n\n <b>{zikr.zikr_arabic}</b> "
        #     text += f"\n\n <k>{zikr.zikr}</k> "

        #     if zikr.zikr_mean:
        #         text += f"\n\n <k>{zikr.zikr_mean}</k> "
        #     await bot.send_message(chat_id=i.user_id, text=f"10 marotaba\n\n <b>{zikr}</b> \n\n takrorlang")
        # except:
        #     continue

@dp.channel_post_handler(lambda message: message.text in ['SendPostMessage'], state='*')
async def send_zikr(message: types.Message, state: FSMContext):
    users = await commands.get_users()
    for i in users:
        zikr = await get_zikr()
        await bot.send_message(chat_id=i.user_id, text=f"<b>Send Tests</b> \n\n takrorlang")
    


@dp.message_handler(CommandStart(), state='*')
async def bot_start(message: types.Message, state: FSMContext):
    await add_user(user_id=message.from_user.id, name=message.from_user.first_name)
    await message.answer(f"Assalomu alaykum, {message.from_user.first_name}. Zikr botimizga xush kelibsiz!\n\n⏳ Endilikda sizga botimiz orqali har soatda turli xildagi zikrlarni taqdim qilib boramiz.")
    await message.answer("https://telegra.ph/Allohni-ko%CA%BBp-zikr-qilishning-fazilati-07-23")


@dp.message_handler(lambda message: message.text in ['Yangilash'], state='*')
async def update_database(message: types.Message, state: FSMContext):
    await get_update()

@dp.message_handler(lambda message: message.text in ['/users'], state='*')
async def update_database(message: types.Message, state: FSMContext):
    count = await commands.get_users_count()
    await message.answer(text=f"foydalanuvchilar {count}")
