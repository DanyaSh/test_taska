'''
Примечания к версии:
    🔵 Приветствовать пользователя, выбор функции бота
    🔵 OpenWeatherMap
    🔵 Exchange Rates API
    🔵 Sweet animal
    🔵 polls
    ------------------------------------------------------------------------------------------
    ✅
    🔴
    🔵
    ⚫️
    ⚪️
'''
about='taska_v0.1'
branch='main'
code='test_for_hh.ru'

from multiprocessing.connection import answer_challenge
from requests import delete
from base_manager import Bm, Column, log_time
from try_manager import User_try_aiogram as Uta
from aiogram import Bot, Dispatcher, types
import time
from config import TOKEN, CAT, HOME_CAT, LIST_ADMIN, CHANEL_ID, CHANEL_CHAT_ID
import sqlite3
import subprocess
from io import BytesIO
import random
import asyncio
import keyboard
# from handlers import bot

bot =   Bot(token=TOKEN, parse_mode=types.ParseMode.HTML)
dp  =   Dispatcher(bot)

# __________________________________GLOBAL VARIABLES____________________________________
base=f"{CAT}base.sqlite"             #actual database

# ______________________________________CLASSES________________________________________
class Links(Bm):
    _base=base
    _table='links'
    _foreign_mode=True
    _foreign_key='id'
    _foreign_table='users'

    def __init__(self, obj):
        self.find_id_in_obj(obj)
        _c1 = Column(table=self._table, name='id', type='integer', primary_key=True, meaning=self.id)
        _c2 = Column(table=self._table, name='last_invite')
        _c3 = Column(table=self._table, name='source_link')
        self._list_columns=[_c1, _c2, _c3]
        super().__init__(obj)

class Route(Bm):
    _base=base
    _table='route'
    _foreign_mode=True
    _foreign_key='id'
    _foreign_table='users'

    def __init__(self, obj):
        self.find_id_in_obj(obj)
        _c1 = Column(table=self._table, name='id', type='integer', primary_key=True, meaning=self.id)
        _c2 = Column(table=self._table, name='process')
        _c3 = Column(table=self._table, name='proc_arg')
        _c4 = Column(table=self._table, name='type_obj')
        _c5 = Column(table=self._table, name='_call_id', type='integer', meaning=0)
        _c6 = Column(table=self._table, name='_message_id', type='integer', meaning=0)
        _c7 = Column(table=self._table, name='_chat_id', type='integer', meaning=0)
        _c8 = Column(table=self._table, name='content_type')
        _c9 = Column(table=self._table, name='text')
        self._list_columns=[_c1, _c2, _c3, _c4, _c5, _c6, _c7, _c8, _c9]
        super().__init__(obj)

    def update(self, obj, process='none', proc_arg='none'):
        self.process=process
        self.proc_arg=proc_arg
        if isinstance(obj, types.CallbackQuery):
            self.type_obj='call'
            self.call_id=obj.id
            self.message_id=obj.message.message_id
            self.chat_id=obj.message.chat.id
            self.content_type=obj.message.content_type
            self.text=obj.message.text
        elif isinstance(obj, types.Message):
            self.type_obj='message'
            self.call_id='none'
            self.message_id=obj.message_id
            self.chat_id=obj.chat.id
            self.content_type=obj.content_type
            self.text=obj.text
        else: print('update_Route_obj_error!!!!!!!!!!!!!')
# __________________________________________PROPERTY____________________________________________

    @property
    def call_id(self):
        if self._call_id==0:
            answer='none'
        else:
            answer = str(self._call_id)
        return answer

    @call_id.setter
    def call_id(self, input):
        if input=='none':
            self._call_id=0
        else:
            self._call_id=int(input)

    @property
    def message_id(self):
        if self._message_id==0:
            answer='none'
        else:
            answer = str(self._message_id)
        return answer

    @message_id.setter
    def message_id(self, input):
        if input=='none':
            self._message_id=0
        else:
            self._message_id=int(input)

    @property
    def chat_id(self):
        if self._chat_id==0:
            answer='none'
        else:
            answer = str(self._chat_id)
        return answer

    @chat_id.setter
    def chat_id(self, input):
        if input=='none':
            self._chat_id=0
        else:
            self._chat_id=int(input)

class User(Bm, Uta):
    _base=base
    _table='users'
    _foreign_mode=False

    def __init__(self, obj):
        if isinstance(obj, types.CallbackQuery):
            self.id=obj.message.chat.id
            self.first_name=obj.message.chat.first_name
            self.last_name=obj.message.chat.last_name
        elif isinstance(obj, types.Message):
            self.id=obj.chat.id
            self.first_name=obj.chat.first_name
            self.last_name=obj.chat.last_name
        elif isinstance(obj, int):
            self.id=obj
            self.first_name=self.last_name='none'
        else: 
            self.id=int(obj)
            self.first_name=self.last_name='none'
        self.date_start=int(time.time())
        self.__time__last_active=int(time.time())
        _c1 = Column(table=self._table, name='id', type='integer', primary_key=True, meaning=self.id)
        _c2 = Column(table=self._table, name='contact')
        _c3 = Column(table=self._table, name='_rang', type='integer', meaning=5)
        _c4 = Column(table=self._table, name='_file1', type='BLOB NOT NULL')
        _c5 = Column(table=self._table, name='_file2', type='BLOB NOT NULL')
        _c6 = Column(table=self._table, name='_file3', type='BLOB NOT NULL')
        _c7 = Column(table=self._table, name='first_name', meaning=self.first_name)
        _c8 = Column(table=self._table, name='last_name', meaning=self.last_name)
        _c9 = Column(table=self._table, name='date_start', type='integer', meaning=self.date_start)
        _c10 = Column(table=self._table, name='_time_last_active', type='integer', meaning=self.__time__last_active)
        _c11 = Column(table=self._table, name='_list_friend', type='text', meaning='[]')
        _c12 = Column(table=self._table, name='source_friend', type='integer', meaning=0)
        self._list_columns=[_c1, _c2, _c3, _c4, _c5, _c6, _c7, _c8, _c9, _c10, _c11, _c12]
        super().__init__(obj)
        if self.first_name and self.last_name == 'none':
            if isinstance(obj, types.CallbackQuery):
                self.first_name=obj.message.chat.first_name
                self.last_name=obj.message.chat.last_name
                self.post
            elif isinstance(obj, types.Message):
                self.first_name=obj.chat.first_name
                self.last_name=obj.chat.last_name
                self.post
        self.route=Route(self.id)
        self.links=Links(self.id)
    
    def post(self):
        super().post()
        self.route.post()
        self.links.post()
# ________________________________________OPERATION__________________________________________

    async def start(self, message):
        # await message.answer(f"👋 Hi {user.first_name}!!! \nWhat do you want❓", reply_markup=keyboard.k_functions)
        await message.answer(f"👋 Hi {self.first_name}!!! \nWhat do you want❓", reply_markup=keyboard.k_functions)
        # await self.try_answer(message, f"👋 Hi {self.first_name}!!! \nWhat do you want❓", reply_markup=keyboard.k_functions)

    async def rank(self):
        answer = await bot.get_chat_member(chat_id=CHANEL_ID, user_id=self.id)
        if self.id in LIST_ADMIN:
            self._rang=0
        elif self.id in LIST_VIP or self._rang==2:
            self._rang=2
        elif answer.status=='member':
            self._rang=4
            if self.contact!='none':
                self._rang=3
        elif answer.status=='kicked':
            self._rang=6
        else: self._rang=5
        self.post()
    
    async def cancel(self, obj):
        self.route.update(obj)
        self.post()
        await self.try_call_answer(obj=obj, text="💤", show_alert=False)
        await self.try_answer(obj=obj, text='💤 Действие отменено', reply_markup=keyboard.k_help_friendly)
        await self.try_delete_message(obj=obj)

    async def registration(self):
        text='Добро пожаловать, в целях противодействия мошенничеству предоставьте контактные данные.'
        await self.try_send_message(text=text, reply_markup=keyboard.k_contact)

    async def friendly_help(self, obj):
        file=open((f"{CAT}01_info/text_02_help_03_friendly.txt"),'r', encoding='utf-8')
        text=file.read()
        file.close()
        await self.try_answer(obj, text=text, reply_markup=keyboard.k_only_man)

    async def start_friendly(self, keyboard=keyboard.k_start_friendly, obj=None):
        text='Выберите действие.'
        await self.try_send_message(text=text, reply_markup=keyboard)
        if obj!=None:
            await self.try_delete_message(obj)

    async def start_admin(self, keyboard=keyboard.k_start_admin):
        text_about=f"Версия: {about}\nВетка: {branch}\nКод: {code}"
        await self.try_send_message(text=text_about, reply_markup=keyboard)

    async def get_config(self, obj):
        await self.rank()
        if 0<=self._rang<=3:
            if self._file1=='none':
                self._file1=self.generate_file()
                self.post()
            await self.try_delete_message(obj)
            text='🔥Ваш личный файл-конфигурация.\n\n⚠️Дисклеймер⚠️\nВы несете персональную ответственность за любую деятельность осуществляемую посредством данного файла.\n📌/start'
            await self.try_send_document(document=self.file1, caption=text, reply_markup=keyboard.k_only_man)
        elif self._rang==4:
            await self.registration(obj)
        elif self._rang>4:
            await self.duragon(obj)
    
    def generate_file(self):
        client=f"{self.id}"
        command=[f"sudo bash {CAT}gen_client.sh"]
        pr1=subprocess.Popen(command, stdout=subprocess.PIPE, stdin=subprocess.PIPE, stderr=subprocess.STDOUT, universal_newlines=True, shell=True)
        out1=pr1.communicate(f"{client}\n")[0]
        print(out1)
        command=[f"mkdir -p {CAT}02_ovpn_files"]
        pr2=subprocess.Popen(command, stdout=subprocess.PIPE, stdin=subprocess.PIPE, stderr=subprocess.STDOUT, universal_newlines=True, shell=True)
        pr2.communicate()[0]
        command=[f"sudo cp /root/{client}.ovpn {CAT}02_ovpn_files"]
        pr3=subprocess.Popen(command, stdout=subprocess.PIPE, stdin=subprocess.PIPE, stderr=subprocess.STDOUT, universal_newlines=True, shell=True)
        pr3.communicate()[0]
        command=[f"sudo chown elm:elm {CAT}02_ovpn_files/{client}.ovpn"]
        pr4=subprocess.Popen(command, stdout=subprocess.PIPE, stdin=subprocess.PIPE, stderr=subprocess.STDOUT, universal_newlines=True, shell=True)
        pr4.communicate()[0]
        command=[f"sudo chmod -c 0664 {CAT}02_ovpn_files/{client}.ovpn"]
        pr5=subprocess.Popen(command, stdout=subprocess.PIPE, stdin=subprocess.PIPE, stderr=subprocess.STDOUT, universal_newlines=True, shell=True)
        pr5.communicate()[0]
        file=open(f"{CAT}02_ovpn_files/{client}.ovpn",'rb')
        file_byte=file.read()
        file.close()
        return file_byte

    async def manage(self, obj):
        con = sqlite3.connect(base)
        cursorObj = con.cursor()
        query='SELECT id, contact, _rang, first_name, last_name FROM users WHERE _rang <7 ORDER BY _rang DESC'
        cursorObj.execute(query)
        tuple_answer=(cursorObj.fetchall())
        con.commit()
        list_users=[]
        for x in tuple_answer:
            some_user=User(x[0])
            list_users.append('id')
            list_users.append(str(some_user.id))
            list_users.append('\n')
            list_users.append('contact')
            list_users.append(str(some_user.contact))
            list_users.append('\n')
            list_users.append('_rang')
            list_users.append(str(some_user._rang))
            list_users.append('\n')
            list_users.append('first_name')
            list_users.append(str(some_user.first_name))
            list_users.append('\n')
            list_users.append('last_name')
            list_users.append(str(some_user.last_name))
            list_users.append('\n')
            list_users.append('\n')
        text=' '.join(list_users)
        file=open(f"{CAT}01_info/99_actual_users.txt", 'w')
        file.write(text)
        file.close()
        text_caption='Жду id пользователя'
        file=open(f"{CAT}01_info/99_actual_users.txt", 'r')
        send_doc = await self.try_send_document(document=file, caption=text_caption, reply_markup=keyboard.k_cancel)
        await self.try_delete_message(obj=obj)
        file.close()
        self.route.update(obj=send_doc, process='/wait_id_user_for_manager')
        self.post()

    async def manage_user(self, obj, keyboard=keyboard.k_manage_user):
        '''
        obj - is a document-message (99_actual_users) to admin 
        '''
        su=User(int(obj.text))
        text=f"id: {su.id}\ntel: {su.contact}\nrang: {su._rang}({su.rang})\nf_name: {su.first_name}\nl_name: {su.last_name}"
        if su._rang==6:
            keyboard=keyboard.k_manage_user_unban
        send_mes = await self.try_send_message(text=text, reply_markup=keyboard)
        self.route.update(obj=send_mes, process='/manage_user', proc_arg=str(su.id))
        self.post()
        self.try_delete_message(obj)
    
    async def deactivate(self, obj):
        '''
        obj - is a call object from admin
        '''
        su=User(int(self.route.proc_arg))
        client=f"{su.id}"
        su._file1='none'
        su._rang=6
        su.post()
        command=[f"sudo bash {HOME_CAT}openvpn-install.sh"]
        pr=subprocess.Popen(command, stdout=subprocess.PIPE, stdin=subprocess.PIPE, stderr=subprocess.STDOUT, universal_newlines=True, shell=True)
        x=''
        while x != '   4) Exit\n':
            x=pr.stdout.readline()
        pr.stdin.write('2\n')
        pr.stdin.flush()
        str_out=''
        while client not in str_out:
            str_out=pr.stdout.readline()
        num=[]
        i=0
        while str_out[i]!=')':
            if str_out[i]!=' ':
                num.append(str_out[i])
            i+=1
        num=int(' '.join(num))
        pr.stdin.write(str(num)+'\n')
        pr.stdin.flush()
        pr.stdin.write('y\n')
        pr.stdin.flush()
        pr.terminate()
        command=[f"sudo rm /root/{client}.ovpn"]
        pr=subprocess.Popen(command, stdout=subprocess.PIPE, stdin=subprocess.PIPE, stderr=subprocess.STDOUT, universal_newlines=True, shell=True)
        pr.terminate()
        command=[f"sudo rm {CAT}02_ovpn_files/{client}.ovpn"]
        pr=subprocess.Popen(command, stdout=subprocess.PIPE, stdin=subprocess.PIPE, stderr=subprocess.STDOUT, universal_newlines=True, shell=True)
        pr.terminate()
        await bot.kick_chat_member(chat_id=CHANEL_ID, user_id=su.id, revoke_messages=True)
        await bot.kick_chat_member(chat_id=CHANEL_CHAT_ID, user_id=su.id, revoke_messages=True)
        await self.try_delete_message(obj)
        await self.try_send_message(text='⚙️ Success deactivation', reply_markup=keyboard.k_help_friendly)

    async def change_rang(self, call):
        await self.try_delete_message(call)
        message = await self.try_answer(obj=call, text='Жду число от 1 до 6\n\n1-admin\n2-vip\n3-friendly\n4-guest\n5-alien\n6-ban', reply_markup=keyboard.k_cancel)
        self.route.update(obj=message, process='/change_rang_arg', proc_arg=self.route.proc_arg)
        self.post()

    async def unban(self, obj):
        su=User(int(self.route.proc_arg))
        await bot.unban_chat_member(chat_id=CHANEL_ID, user_id=su.id, only_if_banned=True)
        await bot.unban_chat_member(chat_id=CHANEL_CHAT_ID, user_id=su.id, only_if_banned=True)
        su._rang=5
        su.post()
        await self.try_delete_message(obj)
        await self.try_send_message(text='⚙️ Success unban', reply_markup=keyboard.k_help_friendly)
    
    async def duragon(self):
        con = sqlite3.connect(base_questions)
        cursorObj = con.cursor()
        sql_select_table = "SELECT id FROM questions"
        cursorObj.execute(sql_select_table)
        list_tuple_table=cursorObj.fetchall() #list of tuple
        con.commit()
        num=random.randint(1, len(list_tuple_table))
        q=Question(num)
        text=q.question
        keyboard.k_duragon = types.InlineKeyboardMarkup()
        b1 = types.InlineKeyboardButton(text='1️⃣'+q.answer1, callback_data='/duragon_answer')
        b2 = types.InlineKeyboardButton(text='2️⃣'+q.answer2, callback_data='/duragon_answer')
        b3 = types.InlineKeyboardButton(text='3️⃣'+q.answer3, callback_data='/duragon_answer')
        b4 = types.InlineKeyboardButton(text='4️⃣'+q.answer4, callback_data='/duragon_answer')
        keyboard.k_duragon.add(b1, b2)
        keyboard.k_duragon.add(b3, b4)
        await self.try_send_message(text=text, reply_markup=keyboard.k_duragon)
        keyboard.k_duragon.clean()
    
    async def duragon_answer(self, call):
        con = sqlite3.connect(base_questions)
        cursorObj = con.cursor()
        sql_select_table = "SELECT id FROM answers"
        cursorObj.execute(sql_select_table)
        list_tuple_table=cursorObj.fetchall() #list of tuple
        con.commit()
        num=random.randint(1, len(list_tuple_table))
        a=Answer(num)
        text=a.answer
        await self.try_call_answer(obj=call, text=text, show_alert=True)

    async def get_link(self, call):
        expire_date=int(time.time())+86400
        link = await bot.create_chat_invite_link(chat_id=CHANEL_ID, expire_date=expire_date, creates_join_request=True)
        invite = Invite(link.invite_link)
        invite.author=self.id
        invite.expire_date=expire_date
        invite.mode='wait'
        invite.post()
        self.links.last_invite=link.invite_link
        self.post()
        text='Отправь это приглашение будущему бойцу.\n❗️Помни правила бойцовского клуба.\n⚠️Эта ссылка будет активна 1 день для 1 гостя'
        await self.try_call_answer(obj=call, text=text, show_alert=True)
        await self.try_delete_message(call)
        text=f"🤫 Бойцовский клуб ждёт тебя!\n\n🌐{link.invite_link}"
        await self.try_send_message(text=text, reply_markup=keyboard.k_help_friendly, disable_web_page_preview=True)

    def find_source_id(self, link):
        now_time=int(time.time())
        con = sqlite3.connect(self._base)
        cursorObj = con.cursor()
        sql_select_links = "SELECT link from invites WHERE mode='wait'"
        cursorObj.execute(sql_select_links)
        tuple_invites=cursorObj.fetchall() #list of tuple
        con.commit()
        for x in tuple_invites:
            some_invite=Invite(x[0])
            if some_invite.expire_date<now_time:
                some_invite.mode='bad'
                some_invite.post()
            elif link==some_invite.link:
                self.source_friend=some_invite.author
                su=User(some_invite.author)
                su._list_friend.append(self.id)
                su.post()
                some_invite.mode='used'
                some_invite.for_id=self.id
                some_invite.post()

    async def add_question(self, call):
        await self.try_delete_message(obj=call)
        text='Жду тупой вопрос...'
        message = await self.try_answer(call, text=text, reply_markup=keyboard.k_cancel)
        self.route.update(obj=message, process='/question')
        self.post()

    async def add_answer(self, call):
        await self.try_delete_message(obj=call)
        text='Жду тупой ответ...'
        message = await self.try_answer(call, text=text, reply_markup=keyboard.k_cancel)
        self.route.update(obj=message, process='/answer')
        self.post()
    
    async def choice_device(self, message):
        await self.try_answer(obj=message, text='Выбери устройство:', reply_markup=keyboard.k_choice_device)
        await self.try_delete_message(obj=message)

    async def instruction(self, call):
        if call.data=='/help_apple':
            file_name='apple.mp4'
            file_id_name='log_01_file_id_apple'
            icon='🍏'
        elif call.data=='/help_android':
            file_name='android.mp4'
            file_id_name='log_02_file_id_android'
            icon='🤖'
        try:
            file=open((f"{CAT}01_info/{file_id_name}"),'r', encoding='utf-8')
        except:
            await self.try_call_answer(obj=call, text=f"{icon}\nВидео инструкция загружается - ❗️ожидайте...~20MB", show_alert=True)
            await self.try_delete_message(call.message)
            video=open(f"{CAT}01_info/{file_name}", 'rb')
            message_video = await self.try_send_video(video=video, reply_markup=keyboard.k_help_friendly)
            file=open((f"{CAT}01_info/{file_id_name}"),'w', encoding='utf-8')
            file.write(message_video.video.file_id)
            file.close()
        else:
            file_id=file.read()
            file.close()
            await self.try_call_answer(obj=call, text=f"{icon} 🎦", show_alert=False)
            await self.try_delete_message(call.message)
            await self.try_send_video(video=file_id, reply_markup=keyboard.k_help_friendly)

    async def gratitude(self, obj=None):
        file=open((f"{CAT}01_info/text_03_beer_02_first_pay.txt"),'r', encoding='utf-8')
        text=file.read()
        file.close()
        await self.try_send_message(text=text, reply_markup=keyboard.k_gratitude)
        if obj!=None:
            await self.try_delete_message(obj)

    async def qiwi_pay(self, amount):
        async with qiwi_p2p_client:
            bill = await qiwi_p2p_client.create_p2p_bill(amount=amount, comment='🔥Ледники растают...')
        keyboard.k_qiwi_pay = types.InlineKeyboardMarkup()
        b1_qiwi_pay = types.InlineKeyboardButton(text=f"💚 Перевести {amount} ₽", url=bill.pay_url)
        b2_start_friendly = types.InlineKeyboardButton(text='↩️ На главную', callback_data='/start_friendly')
        keyboard.k_qiwi_pay.add(b1_qiwi_pay)
        keyboard.k_qiwi_pay.add(keyboard.b_cancel, b2_start_friendly)
        await self.try_send_message(text='🙏Заранее спасибо', reply_markup=keyboard.k_qiwi_pay)

# __________________________________________PROPERTY____________________________________________

    @property
    def file1(self):
        if self._file1=='none':
            file1='none'
        else:
            file1 = BytesIO(self._file1)
            file1.name = "fight_club_1.ovpn"
        return file1

    @file1.setter
    def file1(self, file):
        if file=='none':
            self._file1=file
        else:
            self._file1=file.read()

    @property
    def rang(self):
        dict_rang={'0':'root', '1':'admin', '2':'vip', '3':'friendly', '4':'guest', '5':'alien', '6':'ban'}
        rang=dict_rang[str(self._rang)]
        return rang

    @rang.setter
    def rang(self, input):
        dict_rang={'root':0, 'admin':1, 'vip':2, 'friendly':3, 'guest':4, 'alien':5, 'ban':6}
        self._rang=dict_rang[input]