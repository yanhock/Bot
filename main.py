
# This is Main (Public) file

# Main liblaries
from aiogram import Bot, Dispatcher, executor, types

from aiogram.types import ReplyKeyboardMarkup
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
import asyncio
# import logging
# from aiogram.contrib.middlewares.logging import LoggingMiddleware

# Config Data
from config import *

# Media files (cloud import)
from clouds import *

from address import *

# This is Bot's Basic Settings !
API_TOKEN = Bot(token = BOT_TOKEN, parse_mode="HTML")
bot = Dispatcher(API_TOKEN)
botName = str("Hi Germany Bot")

# logging.basicConfig(level=logging.INFO)

# bot.middleware.setup(LoggingMiddleware())



try:
    # logging.basicConfig(level=logging.INFO)


    # This is Main Buttons
    couBut = InlineKeyboardButton(text="📚 Kurslar | Nemis tili", callback_data="cources")
    useBut = InlineKeyboardButton(text="💎 Foydali Ma'lumotlar", callback_data="usefull")
    AscBut = InlineKeyboardButton(text="☎️ Bog'lanish", callback_data="connect")
    aboutBut = InlineKeyboardButton(text="📝 Biz haqimizda", callback_data="about")
    keyboard_inline = InlineKeyboardMarkup().add(couBut, useBut, AscBut, aboutBut)

    keyboards = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True, row_width=2).add(couBut,
                                    useBut, AscBut, aboutBut)



    # This is "Follov" channel buttons function
    def followChannel():
        channel = InlineKeyboardButton(
            text="➡️ Obuna Bo'lish",
            url=CHANNEL_URLS
        )
        check_follow = InlineKeyboardButton(
            text="✅ Tekshirish",
            callback_data="subdone"
        )
        chAllBtn = InlineKeyboardMarkup(row_width=1).add(channel, check_follow)

        return chAllBtn


    @bot.message_handler(commands=['start', 'hello', 'hi', 'restart'])
    async def welcome(message: types.Message):
        checkSubChan = await API_TOKEN.get_chat_member(chat_id=CHANNEL_ID, user_id=message.from_user.id)

        userName = str(message.chat.first_name)
        welTo = f"<b><em>{ userName }</em>, <em>{ botName }</em> - ga xush kelibsiz</b>"

        if checkSubChan['status'] != 'left':
            await message.answer(
                welTo,
                reply_markup=keyboards
            )
        else:
            await message.answer(
                text = f"<b><em>{ userName }, { botName } ga xush kelibsiz.</em> \n\n❗️ <em>{ userName }</em>, Botdan foydalanish uchun Kanalimizga obuna bo'ling</b>",
                reply_markup=followChannel()
            )
            
    @bot.callback_query_handler(lambda checkSub: checkSub.data=="subdone")
    async def checkSubMes(callback: types.CallbackQuery):
        checkSubChan = await API_TOKEN.get_chat_member(chat_id=CHANNEL_ID, user_id=callback.from_user.id)
        userName = str(callback.message.chat.first_name)


        if callback.data == "subdone":
            if checkSubChan['status'] != 'left':
                await callback.message.answer(
                    text = f"<b>🎉 <em>{ userName }</em>, Tabriklaymiz endi botimizdan to'liq foydalanishingiz mumkin.</b>",
                    reply_markup=keyboards
                )
            else:
                await callback.message.answer(
                    text = f"<b>❌ <em>{ userName }</em>, hali kanalimizga obuna bo'lmadingiz.</b>",
                    reply_markup=followChannel()
                )

    
    @bot.message_handler(text="⬅️ Back menu")
    async def exitHome(message: types.Message):
    
        await message.answer(
            text="<b>🏠 Aosiy menu.</b>",
            reply_markup=keyboards
        )

    @bot.message_handler(text="☎️ Bog'lanish")
    async def connectCall(message: types.Message):
        cPost = str(
            f"<b>📲 { botName }</b> - xodimlar bilan bog'lanish. \n\n👤 <em><b>Murojaat uchun: @Mirzakhidov1ch</b></em> \n\n\n <b>💎 @hi_Germany - eng yaxshilarini sizga ulashamiz</b>"
        )
        
        await message.answer_photo(
            callCenter,
            cPost
        )
    @bot.message_handler(commands=['help'])
    async def connectCall(message: types.Message):
        cPost = str(
            f"<b>📲 { botName }</b> - xodimlar bilan bog'lanish. \n\n👤 <em><b>Murojaat uchun: @Mirzakhidov1ch</b></em> \n\n\n <b>💎 @hi_Germany - eng yaxshilarini sizga ulashamiz</b>"
        )
        
        await message.answer_photo(
            callCenter,
            cPost
        )

    @bot.message_handler(text="📝 Biz haqimizda")
    async def aboutG(message: types.Message):
        about = f"<b>{ botName } - <em>Biz sizga 🇩🇪 GERMANIYADA #Talim, #Sayohat va Boshqa maqsadlarda Maslahat va Yordam beramiz. \n\n👤 Murojaat uchun: @Mirzakhidov1ch \n\n\n 💎 @hi_Germany - eng yaxshilarini sizga ulashamiz</em></b>"

        await message.answer_photo(
            aboutAP,
            about
        )
    @bot.message_handler(commands=['about'])
    async def aboutG(message: types.Message):
        about = f"<b>{ botName } - <em>Biz sizga 🇩🇪 GERMANIYADA #Talim, #Sayohat va Boshqa maqsadlarda Maslahat va Yordam beramiz. \n\n👤 Murojaat uchun: @Mirzakhidov1ch \n\n\n 💎 @hi_Germany - eng yaxshilarini sizga ulashamiz</em></b>"

        await message.answer_photo(
            aboutAP,
            about
        )



    @bot.message_handler(text="🇺🇿 Nemis tilini 0 dan | Uzbek tilida o'rganish")
    async def on_nu_start(message: types.Message):
        keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=4, one_time_keyboard=True)
        buttons = [button for button in course_nu_data]
        keyboard.add(*buttons)

        homeOld = InlineKeyboardButton(text="⬅️ Orqaga qaytish", callback_data="back_old")
        homeExit = InlineKeyboardButton(text="⬅️ Back menu", callback_data="back_home")
        keyboard.add(homeOld, homeExit)

        await message.answer("Select", reply_markup=keyboard)

    @bot.message_handler(lambda message: message.text in course_nu_data)
    async def on_button_nu_click(message: types.Message):
        button_name = message.text
        button_info = course_nu_data[button_name]
        title = button_info["title"]
        address = button_info["address"]
        await message.answer(f"<b><em>{ title }</em></b>")
        await message.answer(f"<b><em>{ address }</em></b>")




    # German Languages


    @bot.message_handler(text="🇩🇪 Nemis tilini 0 dan | Nemis tilida o'rganish")
    async def on_nn__start(message: types.Message):
        keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=4, one_time_keyboard=True)
        buttons = [button for button in course_nn_data]
        keyboard.add(*buttons)

        homeOld = InlineKeyboardButton(text="⬅️ Orqaga qaytish", callback_data="back_old")
        homeExit = InlineKeyboardButton(text="⬅️ Back menu", callback_data="back_home")
        keyboard.add(homeOld, homeExit)

        await message.answer("Select", reply_markup=keyboard)

    @bot.message_handler(lambda message: message.text in course_nn_data)
    async def on_button_nn_click(message: types.Message):
        button_name = message.text
        button_info = course_nn_data[button_name]
        title = button_info["title"]
        address = button_info["address"]
        await message.answer(f"<b><em>{ title }</em></b>")
        await message.answer(f"<b><em>{ address }</em></b>")



    # "Ibrat Farzandlari" cources


    @bot.message_handler(text="🈹 Ibrat Farzandlari")
    async def on_ib__start(message: types.Message):
        keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=4, one_time_keyboard=True)
        buttons = [button for button in course_ib_data]
        keyboard.add(*buttons)

        homeOld = InlineKeyboardButton(text="⬅️ Orqaga qaytish", callback_data="back_old")
        homeExit = InlineKeyboardButton(text="⬅️ Back menu", callback_data="back_home")
        keyboard.add(homeOld, homeExit)

        await message.answer("Select", reply_markup=keyboard)

    @bot.message_handler(lambda message: message.text in course_ib_data)
    async def on_button_ib_click(message: types.Message):
        button_name = message.text
        button_info = course_ib_data[button_name]
        title = button_info["title"]
        address = button_info["address"]
        await message.answer(f"<b><em>{ title }</em></b>")
        await message.answer(f"<b><em>{ address }</em></b>")



    @bot.message_handler(text="⬅️ Orqaga qaytish")
    async def exitHome(message: types.Message):
        cource1 = InlineKeyboardButton(text="🇺🇿 Nemis tilini 0 dan | Uzbek tilida o'rganish", callback_data="cource1")
        cource2 = InlineKeyboardButton(text="🇩🇪 Nemis tilini 0 dan | Nemis tilida o'rganish", callback_data="cource2")
        cource3 = InlineKeyboardButton(text="🈹 Ibrat Farzandlari", callback_data="cource3")
        homeExit = InlineKeyboardButton(text="⬅️ Back menu", callback_data="back_home")
        course_buttons = InlineKeyboardMarkup().add(cource1, cource2, cource3, homeExit)

        keyboards = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True, row_width=1).add(cource1,
                                    cource2, cource3, homeExit)
    
        await message.answer(
            text="<b>📚 Kurslar | Nemis tili</b>",
            reply_markup=keyboards
        )


    
    @bot.message_handler(text="💎 Foydali Ma'lumotlar")
    async def usefullData(message: types.Message):
        useP1 = InlineKeyboardButton(text="💎 Foydali Ma'lumotlar | 1️⃣ Part", callback_data="useP1")
        useP2 = InlineKeyboardButton(text="💎 Foydali Ma'lumotlar | 2️⃣ Part", callback_data="useP2")
        homeExit = InlineKeyboardButton(text="⬅️ Back menu", callback_data="back_home")

        eyboard_inline = InlineKeyboardMarkup().add(useP1, useP2, homeExit)
        keyboards = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True, row_width=2).add(useP1,
                                            useP2, homeExit)
        
        await message.answer(
            text="<b>💎 Foydali Ma'lumotlar</b> \n\n▶️ Biron bir menuni tanlang.",
            reply_markup=keyboards
        )



    @bot.message_handler(text="💎 Foydali Ma'lumotlar | 1️⃣ Part")
    async def usefullData1(message: types.Message):
        usefull_data = [
                [
                    types.InlineKeyboardButton(text="📍GERMANIYAGA BORISH TALABLARI", callback_data="uDn1"),
                    types.InlineKeyboardButton(text="✅ AUPAIR HAQIDA TO'LIQ", callback_data="uDn2"),
                ],
                [
                    types.InlineKeyboardButton(text="✅ AUSBILDUNG HAQIDA MA'LUMOT", callback_data="uDn5"),
                    types.InlineKeyboardButton(text="📞 ELCHIXONA EMAILLARI TEL NOMERLARI", callback_data="uDn6"),
                ],
                [
                    types.InlineKeyboardButton(text="🎧 BARCHA SOHADA OVOZLI CHAT", callback_data="uDn7"),
                    types.InlineKeyboardButton(text="✅ FSJ HAQIDA MA'LUMOT: FSJ BFD", callback_data="uDn8"),
                ],
                [
                    types.InlineKeyboardButton(text="🟦 BLAU KARTA (moviy karta) Blaue_karte", callback_data="uDn9"),
                    types.InlineKeyboardButton(text="👨‍💻 FERIENJOB (Work_and_Travel_in_De)", callback_data="uDn10"),
                ],
                [
                    types.InlineKeyboardButton(text="🏦 BANKSHOT Bloklangan_hisob_raqam", callback_data="uDn11"),
                    types.InlineKeyboardButton(text="🏘 STUDIENKOLLEG # Studienkolleg", callback_data="uDn12"),
                ],
                [
                    types.InlineKeyboardButton(text="🎫 CHIPTA SOTIB OLISH", callback_data="uDn13"),
                    types.InlineKeyboardButton(text="✅ STIPENDIYA XOHLOVCHILAR UCHUN", callback_data="uDn14"),
                ],
                [
                    types.InlineKeyboardButton(text="♾ GERMANIYADA BEPUL BAKALAVR VA MAGISTRATURA ÒQISH SHARTLARI", callback_data="uDn15"),
                    types.InlineKeyboardButton(text="✅ GERMANIYADA AUSBILDUNG QILISH", callback_data="uDn16"),
                ],
                [
                    types.InlineKeyboardButton(text="🇺🇿 GERMANIYADA TAN OLINGAN UZB UNIVERSITUTLARI", callback_data="uDn17"),
                    types.InlineKeyboardButton(text="💉 GERMANIYADA TIBBIYOT SOHASIDA ÒQISH VA UZB DAN GERMANIYAGA ÒQISHINI KÒCHIRISH", callback_data="uDn18"),
                ],
                [
                    types.InlineKeyboardButton(text="🔎 GERMANIYADA IJARAGA UY IZLASH", callback_data="uDn19"),
                    types.InlineKeyboardButton(text="🧑‍🎓 GERMANIYADA BACHELOR YOKI MASTER ÒQIMOQCHI BÒLGANLARGA", callback_data="uDn20"),
                ],
            ]

        keyboards = types.InlineKeyboardMarkup(inline_keyboard=usefull_data)

        await message.answer(
            text="<b><em>🇩🇪 Germaniya haqida Foydali va Qiziqarli ma'lumotlar</em></b>",
            reply_markup=keyboards
        )


    @bot.callback_query_handler(lambda c: c.data in usefull_data1)
    async def handle_useful_data(callback_query: types.CallbackQuery):
        selected_data = callback_query.data
        if selected_data in usefull_data1:
            response = usefull_data1[selected_data]
            await callback_query.message.answer(f"<b>{ response }</b>")
        else:
            await callback_query.message.answer("Bunday ma'lumot topilmadi.")



    @bot.message_handler(text="💎 Foydali Ma'lumotlar | 2️⃣ Part")
    async def usefullData2(message: types.Message):
        usefull_data = [
                [
                    types.InlineKeyboardButton(text="🏡 GERMANIYA UNIVERSITETLARI RÒYXATI:", callback_data="uDn21"),
                    types.InlineKeyboardButton(text="🗂 TESTDAF HAQIDA MA'LUMOT", callback_data="uDn22"),
                ],
                [
                    types.InlineKeyboardButton(text="📖 ANTRAG NAMUNA", callback_data="uDn23"),
                    types.InlineKeyboardButton(text="❗️ GERMANIYA ORZUSIDA ALDANGANLAR: (OGOH BO'LING)", callback_data="uDn24"),
                ], 
                [
                    types.InlineKeyboardButton(text="❓ UZB PRAVASINI GERMANIYADA FOYDALANSA BÒLADIMI", callback_data="uDn25"),
                    types.InlineKeyboardButton(text="✅ WEITERBILDUNG", callback_data="uDn26"),
                ],
                [
                    types.InlineKeyboardButton(text="🦷 UZB DA STAMATOLOGIYADA O'QIB GERMANIYADA STAMATOLOG BO'LIB ISHLASH", callback_data="uDn27"),
                    types.InlineKeyboardButton(text="🇩🇪 SPRACHKURS (Til kursi)", callback_data="uDn4"),
                ],
                [
                    types.InlineKeyboardButton(text="💊 GERMANIYADA DAVOLANISH UCHUN NIMALAR QILISH KERAK", callback_data="uDn30"),
                    types.InlineKeyboardButton(text="✅ GERMANIYADA TIBBIY TA'LIM:", callback_data="uDn34"),
                ],
                [
                    types.InlineKeyboardButton(text="✅ GERMANIYADA OLIY TA'LIM OLISH: maktab, kollej, litseyni tamomlab Ger da òqish. Studienkolleg", callback_data="uDn31"),
                    types.InlineKeyboardButton(text="🏫 GERMANIYADA BAKALAVRDA O'QISH UCHUN TO'LIQ MA'LUMOT", callback_data="uDn32"),

                ],
                [
                    types.InlineKeyboardButton(text="✅ GERMANIYAGA QARINDOSHLARINI MEHMONGA CHAQIRISH:", callback_data="uDn35"),
                    types.InlineKeyboardButton(text="✅ O'zbekistonda tibbiyot sohasida bakalavrni bitirib, Germaniyada ishlash va mutaxassislikka (LOR, Kardiolog, Kardioxirurg va hkz) erishish haqidagi", callback_data="uDn36"),
                ],
                [
                    types.InlineKeyboardButton(text="✅ O'zbekistonda MEDKOLLEJ ni bitirib Germaniyada ishlash haqida", callback_data="uDn37"),
                    types.InlineKeyboardButton(text="✅ DAAD PORTALI ORQALI TURLI STIPENDIYALARGA HUJJAT TOPSHIRISH:", callback_data="uDn40"),
                ],
                [
                    types.InlineKeyboardButton(text="🇺🇿 UZB DAGI O'QISHINI GERMANIYAGA KO'CHIRISH. (PEREVOD) ", callback_data="uDn38"),
                    types.InlineKeyboardButton(text="🇩🇪 GERMANIYA FUQOROLIGINI OLISH:", callback_data="uDn39"),
                ],
        ]


        keyboards = types.InlineKeyboardMarkup(inline_keyboard=usefull_data)

        await message.answer(
            text="<b><em>🇩🇪 Germaniya haqida Foydali va Qiziqarli ma'lumotlar</em></b>",
            reply_markup=keyboards
        )

    @bot.callback_query_handler(lambda c: c.data in usefull_data2)
    async def handle_useful_data(callback_query: types.CallbackQuery):
        selected_data = callback_query.data
        if selected_data in usefull_data2:
            response = usefull_data2[selected_data]
            await callback_query.message.answer(f"<b>{ response }</b>")
        else:
            await callback_query.message.answer("Bunday ma'lumot topilmadi.")





    @bot.message_handler()
    async def kb_answer(message: types.Message):
        # Cources List
        cources_message = str(f"<em><b>🔎 { botName } - Kurslarimiz bilan tanishishingiz mumkin.</b></em>")

        cource1 = InlineKeyboardButton(text="🇺🇿 Nemis tilini 0 dan | Uzbek tilida o'rganish", callback_data="cource1")
        cource2 = InlineKeyboardButton(text="🇩🇪 Nemis tilini 0 dan | Nemis tilida o'rganish", callback_data="cource2")
        cource3 = InlineKeyboardButton(text="🈹 Ibrat Farzandlari", callback_data="cource3")
        homeExit = InlineKeyboardButton(text="⬅️ Back menu", callback_data="back_home")
        course_buttons = InlineKeyboardMarkup().add(cource1, cource2, cource3, homeExit)

        keyboards = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True, row_width=1).add(cource1,
                                    cource2, cource3, homeExit)
        
        # Connect

        if message.text == '📚 Kurslar | Nemis tili':
            await message.reply(
                cources_message,
                reply_markup=keyboards
            )
        else:
            await message.reply(f"{ message.chat.first_name }, Mavjud bo'lmaan buyruq kiritdingiz \"{ message.text }\" \nBosha so`z yozing...")


        
    

    # ALl errors
    # All posible errors will pass through here

    @bot.errors_handler(exception = ['BotBlocked', 'TimeoutError', 'TypeError'])
    async def bot_block(update: types.Update, excention: Exception):
        print(f"I think The Bot was blocked by the User { update } { excention }")
        return True

except:
    executor.start_polling(dispatcher=bot, skip_updates=True)



if __name__ == '__main__':
    executor.start_polling(dispatcher=bot, skip_updates=True)