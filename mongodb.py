#!/usr/bin/env python
# -*- coding:utf-8 -*-

import pymongo
import traceback
from pymongo import Connection
from random import randrange

connection = Connection()

class MongoDB:
    def __init__(self):
        db = connection.message
        self.coll = db.message
        self.coll.ensure_index('messsage')

    def get_data(self):
        count = self.coll.find().count()
        offset = randrange(1,count)
        a = self.coll.find().skip(offset).limit(1)[0]
        return a["message"]

