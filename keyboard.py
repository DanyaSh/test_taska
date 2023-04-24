from aiogram import types

# ______________________________________INLINE_KEYBOARDS________________________________________
k_cancel = types.InlineKeyboardMarkup()
b_cancel = types.InlineKeyboardButton(text='❌ Cancel', callback_data='/cancel')
k_cancel.add(b_cancel)

k_help_friendly = types.InlineKeyboardMarkup()
b_start_friendly = types.InlineKeyboardButton(text='🏠 Home', callback_data='/start')
k_help_friendly.add(b_start_friendly)

k_functions = types.InlineKeyboardMarkup()
b_weather = types.InlineKeyboardButton(text='🌦 Weather', callback_data='/fun_weather')
b_exchange = types.InlineKeyboardButton(text='🏧 Exchange', callback_data='/fun_exchange')
b_animal = types.InlineKeyboardButton(text='🐱 Cute animal', callback_data='/fun_animal')
b_polls = types.InlineKeyboardButton(text='📝 Poll', callback_data='/fun_poll')
k_functions.add(b_weather, b_exchange)
k_functions.add(b_animal, b_polls)

k_exchange = types.InlineKeyboardMarkup()
b_usd_rub = types.InlineKeyboardButton(text='🇺🇸USD 🔜 🇷🇺RUB', callback_data='/usd_rub')
b_rub_usd = types.InlineKeyboardButton(text='🇷🇺RUB 🔜 🇺🇸USD', callback_data='/rub_usd')
b_eur_rub = types.InlineKeyboardButton(text='🇪🇺EUR 🔜 🇷🇺RUB', callback_data='/eur_rub')
b_rub_eur = types.InlineKeyboardButton(text='🇷🇺RUB 🔜 🇪🇺EUR', callback_data='/rub_eur')
k_exchange.add(b_usd_rub, b_rub_usd)
k_exchange.add(b_eur_rub, b_rub_eur)

k_answer_exchange= types.InlineKeyboardMarkup()
b_home = types.InlineKeyboardButton(text='💱change pair', callback_data='/change_pair')
b_change = types.InlineKeyboardButton(text='🏠Home', callback_data='/start')
k_answer_exchange.add(b_change, b_home)

k_start_friendly = types.InlineKeyboardMarkup()
b1 = types.InlineKeyboardButton(text='🔑 Получить файл-доступ', callback_data='/get_config')
b2 = types.InlineKeyboardButton(text='🤝 Пригласить друга', callback_data='/get_link')
b3_man = types.InlineKeyboardButton(text='📖 Инструкция', callback_data='/instruction')
b4_beer = types.InlineKeyboardButton(text='🍺 На пиво!', callback_data='/beer')
k_start_friendly.add(b1, b2)
k_start_friendly.add(b3_man, b4_beer)

k_only_man = types.InlineKeyboardMarkup()
k_only_man.add(b3_man)

k_start_admin = types.InlineKeyboardMarkup()
b4 = types.InlineKeyboardButton(text='👑 Управление🔐', callback_data='/manage')
b5 = types.InlineKeyboardButton(text='❔ question🔐', callback_data='/question')
b6 = types.InlineKeyboardButton(text='❕ answer🔐', callback_data='/answer')
k_start_admin.add(b1, b2)
k_start_admin.add(b3_man)
k_start_admin.add(b4)
k_start_admin.add(b5, b6)

k_manage_user = types.InlineKeyboardMarkup()
b1 = types.InlineKeyboardButton(text='〽️ Изменить rang🔐', callback_data='/change_rang')
b2 = types.InlineKeyboardButton(text='🚷 Деактивировать🔐', callback_data='/deactivate')
k_manage_user.add(b1, b2)
k_manage_user.add(b_cancel)

k_manage_user_unban = types.InlineKeyboardMarkup()
b3 = types.InlineKeyboardButton(text='♻️ Разбанить🔐', callback_data='/unban')
k_manage_user_unban.add(b1, b2)
k_manage_user_unban.add(b3)

k_choice_device = types.InlineKeyboardMarkup()
b1 = types.InlineKeyboardButton(text='🍏 Apple', callback_data='/help_apple')
b2 = types.InlineKeyboardButton(text='🤖 Android', callback_data='/help_android')
k_choice_device.add(b1, b2)
k_choice_device.add(b_cancel)

# ______________________________________KEYBOARDS________________________________________
k_location = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
b1 = types.KeyboardButton(text='📍 Отправить локацию телефона', request_location=True)
k_location.add(b1)

k_poll = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
b_create_poll = types.KeyboardButton(text="✅Create poll", request_poll=types.KeyboardButtonPollType(type=types.PollType.REGULAR))
b_cancel_poll = types.KeyboardButton(text="❌ Cancel")
k_poll.add(b_cancel_poll, b_create_poll)
# _______________________________________________________________________________________