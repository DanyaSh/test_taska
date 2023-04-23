from test_taska import User
from config import CHANEL_ID, TOKEN
import keyboard
import logging
from aiogram import Bot, Dispatcher, types
from aiogram.dispatcher.filters import Text
logging.basicConfig(level=logging.INFO)

# __________________________________GLOBAL VARIABLES____________________________________

bot =   Bot(token=TOKEN, parse_mode=types.ParseMode.HTML)
dp  =   Dispatcher(bot)

# ______________________________________COMMANDS________________________________________

@dp.message_handler(commands='start')
async def cmd_start(message: types.Message):
    user=User(message)
    await user.rank()
    if user._rang==4:
        await user.registration()
    elif user._rang>4:
        await user.duragon()
    else:
        if message.text=='/start thanks':
            await user.gratitude()
        else:
            if user._rang==0 or user._rang==1:
                await user.start_admin()
            elif user._rang==2 or user._rang==3:
                await user.start_friendly()

@dp.message_handler(commands='help')
async def cmd_start(message: types.Message):
    user=User(message)
    await user.rank()
    if user._rang<4:
        await user.friendly_help(message)
    else:
        await user.try_answer(obj=message, text='Просто добавь воды...')

# __________________________________TEXT OF BUTTONS____________________________________

@dp.message_handler(Text(equals='❌ Нет, у меня параноя'))
async def telephone(message: types.Message):
    user=User(message)
    text='А ты не так прост 🧐'
    await user.try_answer(message, text=text)

# ________________________________________TEXT__________________________________________

@dp.message_handler()
async def echo(message: types.Message):
    user=User(message)
    await user.rank()
    print(f"user {user.id} type text")
    if user.route.process=='/wait_id_user_for_manager' and user._rang<2:
        await user.manage_user(message)
    else:
        await message.reply(f"Моя твоя не понимать...🧐\n{message.text}")


# __________________________________INLINE BUTTONS____________________________________

@dp.callback_query_handler(text='/duragon_answer')
async def duragon(call: types.CallbackQuery):
    user=User(call)
    await user.rank()
    if user._rang>4:
        await user.duragon_answer(call)
        await user.try_delete_message(call)
        await user.duragon()
    elif user._rang==4:
        await user.registration()
    elif user._rang<4:
        await user.friendly_help(call.message)

@dp.callback_query_handler(text='/cancel')
async def duragon(call: types.CallbackQuery):
    user=User(call)
    if call.message.chat.id==call.from_user.id:
        await user.cancel(call)

@dp.callback_query_handler(text='/start_friendly')
async def start_friendly(call: types.CallbackQuery):
    user=User(call)
    await user.rank()
    await user.try_call_answer(obj=call, text="🏁", show_alert=False)
    if user._rang==0 or user._rang==1:
        await user.start_admin()
    elif user._rang==2 or user._rang==3:
        await user.start_friendly(obj=call)
    elif user._rang==4:
        await user.registration()
    elif user._rang>4:
        await user.duragon()

@dp.callback_query_handler(text='/get_config')
async def get_config(call: types.CallbackQuery):
    user=User(call)
    await user.try_call_answer(obj=call, text="🔑", show_alert=False)
    await user.get_config(obj=call)

@dp.callback_query_handler(text='/get_link')
async def get_link(call: types.CallbackQuery):
    user=User(call)
    await user.get_link(call)

@dp.callback_query_handler(text='/instruction')
async def instruction(call: types.CallbackQuery):
    user=User(call)
    await user.try_call_answer(obj=call, text="📖", show_alert=False)
    await user.rank()
    if user._rang<4:
        await user.choice_device(call.message)
    else:
        await user.try_answer(obj=call, text='Просто добавь воды...')

@dp.callback_query_handler(text='/beer')
async def beer(call: types.CallbackQuery):
    user=User(call)
    await user.try_call_answer(obj=call, text="🍺", show_alert=False)
    await user.rank()
    if user._rang<4:
        await user.gratitude(obj=call)
    else:
        await user.try_answer(obj=call, text='Просто добавь воды...')

@dp.callback_query_handler(lambda call: call.data=='/wallet_btc' or call.data=='/wallet_eth' or call.data=='/wallet_xmr')
async def crypto_wallet(call: types.CallbackQuery):
    user=User(call)
    await user.try_call_answer(obj=call, text="🧡", show_alert=False)
    await user.rank()
    if user._rang<4:
        dict_wallet={'/wallet_btc':WALLET_BTC, '/wallet_eth':WALLET_ETH, '/wallet_xmr':WALLET_XMR}
        wallet=dict_wallet[call.data]
        await user.try_send_message(text=wallet, reply_markup=keyboard.k_help_friendly)
    else:
        await user.try_answer(obj=call, text='Просто добавь воды...')

@dp.callback_query_handler(lambda call: call.data=='/qiwi_50' or call.data=='/qiwi_200' or call.data=='/qiwi_500')
async def qiwi_pay(call: types.CallbackQuery):
    user=User(call)
    await user.try_call_answer(obj=call, text="🧡", show_alert=False)
    await user.rank()
    if user._rang<4:
        dict_amount={'/qiwi_50':50, '/qiwi_200':200, '/qiwi_500':500}
        amount=dict_amount[call.data]
        await user.qiwi_pay(amount)
    else:
        await user.try_answer(obj=call, text='Просто добавь воды...')

@dp.callback_query_handler(text='/qiwi_other_amount')
async def qiwi_other_amount(call: types.CallbackQuery):
    user=User(call)
    await user.try_call_answer(obj=call, text="💰", show_alert=False)
    await user.rank()
    if user._rang<4:
        send_gratitude = await user.try_answer(obj=call, text='Отлично, тогда пришли мне сумму (в рублях), чтоб мы могли подготовить ссылку перевода.', reply_markup=keyboard.k_cancel)
        user.route.update(obj=send_gratitude, process='/wait_qiwi_amount')
        user.post()
    else:
        await user.try_answer(obj=call, text='Просто добавь воды...')

@dp.callback_query_handler(lambda call: call.data=='/help_apple' or call.data=='/help_android')
async def instruction(call: types.CallbackQuery):
    user=User(call)
    await user.rank()
    if user._rang<4:
        # await user.try_delete_message(call.message)
        await user.instruction(call)
    else:
        await user.try_call_answer(obj=call, text="🚰", show_alert=True)
        await user.try_answer(obj=call, text='Просто добавь воды...')

@dp.callback_query_handler(text='/manage')
async def manage(call: types.CallbackQuery):
    user=User(call)
    await user.rank()
    if user._rang<2:
        await user.try_call_answer(obj=call, text="👑🔐", show_alert=False)
        await user.manage(call)
    else:
        await user.try_call_answer(obj=call, text="📛", show_alert=False)

@dp.callback_query_handler(text='/change_rang')
async def change_rang(call: types.CallbackQuery):
    user=User(call)
    await user.rank()
    if user._rang<2:
        await user.try_call_answer(obj=call, text="〽️🔐", show_alert=False)
        await user.change_rang(call)
    else:
        await user.try_call_answer(obj=call, text="📛", show_alert=False)

@dp.callback_query_handler(text='/deactivate')
async def deactivate(call: types.CallbackQuery):
    user=User(call)
    await user.rank()
    if user._rang<2:
        await user.try_call_answer(obj=call, text="🚷🔐", show_alert=False)
        await user.deactivate(call)
    else:
        await user.try_call_answer(obj=call, text="📛", show_alert=False)

@dp.callback_query_handler(text='/unban')
async def unban(call: types.CallbackQuery):
    user=User(call)
    await user.rank()
    if user._rang<2:
        await user.try_call_answer(obj=call, text="♻️🔐", show_alert=False)
        await user.unban(call)
    else:
        await user.try_call_answer(obj=call, text="📛", show_alert=False)

@dp.callback_query_handler(text='/question')
async def question(call: types.CallbackQuery):
    user=User(call)
    await user.rank()
    if user._rang<2:
        await user.try_call_answer(obj=call, text="❔🔐", show_alert=False)
        await user.add_question(call)
    else:
        await user.try_call_answer(obj=call, text="📛", show_alert=False)

@dp.callback_query_handler(text='/answer')
async def answer(call: types.CallbackQuery):
    user=User(call)
    await user.rank()
    if user._rang<2:
        await user.try_call_answer(obj=call, text="❔🔐", show_alert=False)
        await user.add_answer(call)
    else:
        await user.try_call_answer(obj=call, text="📛", show_alert=False)
    

# __________________________________CONTACT____________________________________

@dp.message_handler(content_types='contact')
async def telephone(message: types.Message):
    user=User(message)
    user.contact=message.contact.phone_number
    await user.rank()
    if 1<user._rang<4:
        text='Скорость доверия, как говориться 😇'
        await user.try_answer(message, text=text)
        await user.friendly_help(message)
    else:
        text='Что-то идет не так, похоже ты нарушил 3️⃣ правило бойцовского клуба...'
        await user.try_answer(message, text=text)

# __________________________________INVITE____________________________________
@dp.chat_join_request_handler()
async def new_members_handler(update: types.ChatJoinRequest):
    await update.approve()
    user=User(update.from_user.id)
    user.links.source_link=update.invite_link.invite_link
    user.find_source_id(update.invite_link.invite_link)
    user.post()
    await bot.revoke_chat_invite_link(chat_id=CHANEL_ID, invite_link=update.invite_link.invite_link)
    await user.rank()
    if user._rang==0 or user._rang==1:
        await user.start_admin()
    elif user._rang==2 or user._rang==3:
        await user.start_friendly()
    elif user._rang==4:
        await user.registration()
    elif user._rang>4:
        await user.duragon()
