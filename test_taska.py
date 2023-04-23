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

    async def starts(self, message):
        await self.try_answer(message, f"👋 Hi {self.first_name}!!! \nWhat do you want❓", reply_markup=keyboard.k_functions)

    async def fun_weather(self, call):
        await self.try_call_answer(obj=call, text="🌦", show_alert=False)
        city_name = await self.try_answer(call.message, f"Okay {self.first_name}, send me your city name (Eng).\nFor example: Yekaterinburg")
        self.route.update(obj=city_name, process='/city_name')
        self.post()

    async def weather_of_city(self, message):
        city_name = message.text
        file=open((f"{CAT}city_list.json"),'r', encoding='utf-8')
        dict_city=eval(file.read())
        file.close()
        list_city= []
        for x in dict_city:
            list_city.append(x["name"])
        list_result=[]
        for x in list_city:
            if city_name.lower() in x.lower(): list_result.append(x)
        await self.try_answer(message, f"This is your country? \n{list_result[0]}")
        
            
        
