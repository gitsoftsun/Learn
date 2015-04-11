# -*- coding: utf-8 -*-
__author__ = 'lzy'
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
import time
import mysql.connector
import urllib


class downloads:
    def __init__(self):
        """
        this is init method
        :return:
        """
        pass

    @classmethod
    def ooxx_jiandan(cls):
        """
        download img file
        :return:
        """
        failed_save_url =[]
        cnx = mysql.connector.connect(user='root', database='spider', password='root')
        cursor = cnx.cursor(buffered=True)
        query = ("select id, img_url from xxoo_jiandan where id > 2565")
        cursor.execute(query)
        for(id, img_url) in cursor:
            print "img_url = %s\n" % img_url
            path = '/home/lzy/Pictures/ooxx_jiandan/'+str(id)+str(img_url)[-4:]
            try:
                data = urllib.urlopen(img_url).read()
            except IOError , e:
                failed_save_url.append(img_url)
                print img_url, "failed"
                continue
            time.sleep(2)
            fw = file(path, 'wb')
            fw.write(data)
            fw.close()
        cnx.commit()
        cnx.close()

if __name__ == '__main__':
    downloads.ooxx_jiandan()