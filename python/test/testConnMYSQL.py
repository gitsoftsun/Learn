# -*- coding: utf-8 -*-
__author__ = 'Lzy_pc'

import mysql.connector


def testSelect(imgurl):
    config = {
        'user': 'root',
        'password': 'root',
        'database': 'spider'
    }
    cnx = mysql.connector.connect(**config)
    cursor = cnx.cursor()
    select = ("select id, img_url from xxoo_jiandan WHERE img_url = %s")
    print "SQL = " + select % str("'"+imgurl+"'")
    cursor.execute(select % str("'"+imgurl+"'"))
    if len(cursor.fetchall()):
        print cursor.fetchall()[0][0]
    # for (id, img_url) in cursor:
    #     print "id = %s, img_url = %s" % (id, img_url)
    cnx.commit()
    cnx.close()


if __name__ == '__main__':
    testSelect(r' http://ww3.sinaimg.cn/mw600/005UDDlRjw1eq25qzjhyuj3k0nnmzo.jpg')