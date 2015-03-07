#  -*- coding: utf-8 -*-

import MYSQLdb

conn = MYSQLdb.connect('localhost', 'root', 'root', 'test', charset='utf-8')
cur  = conn.cursor()