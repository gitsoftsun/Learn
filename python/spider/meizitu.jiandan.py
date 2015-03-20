# -*- coding: utf-8 -*-

# every day scraw  beautiful girl from jiandan.net

# 将妹子图专栏下载的信息存入输入库
# 所存字段： 上传者， 图片地址， 圈圈/支持， 叉叉/反对， 吐曹（暂时不收集 -不好收集）
# update time :20150320 - pageNum: 1354
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
sys.setrecursionlimit(100000)
from pyquery import PyQuery
import urllib2, urllib
import chardet
import time
import socket
import mysql.connector
girls_url = r'http://jandan.net/ooxx'


def process_info(url, endPageNum):
    """
    抓取信息
    :return:信息（图片信息）
    """
    url_request = urllib2.Request(url, headers={'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/38.0.2125.122 Safari/537.36'})
    try:
        socket.setdefaulttimeout(20)  # 这里对整个socket层设置超时时间。后续文件中如果再使用到socket，不必再设置 
        page = urllib2.urlopen(url_request)
        page_obj = page.read()
        page.close()
    except socket.error:
        print 'socket timeout ', url
        try:
            time.sleep(5)
            # page = urllib2.urlopen(url_request)
            # page_obj = page.read()
            # page.close()
            process_info(True, url)
            return
        except socket.timeout, e:
            print 'socket timeout , url failed : %' % url
        except urllib2.URLError, e:
            print e.reason
            print 'urlopen error : url %s' % url
            time.sleep(4)
            page = urllib2.urlopen(url_request)
            page_obj = page.read()
            page.close()
        except urllib2.HTTPError, e:
            print e.reason
            print 'http error url :%s' % url
            time.sleep(4)
            page = urllib2.urlopen(url_request)
            page_obj = page.read()
            page.close()
    except urllib2.HTTPError, e:
        print e.reason
        print 'http error url :%s' % url
        time.sleep(4)
        page = urllib2.urlopen(url_request)
        page_obj = page.read()
        page.close()

    except urllib2.URLError, e:
        print e.reason
        time.sleep(4)
        page = urllib2.urlopen(url_request)
        page_obj = page.read()
        page.close()
    if isinstance(page_obj, str):
        page_obj = unicode(page_obj, chardet.detect(page_obj)['encoding'])
    html_pq = PyQuery(page_obj)('.commentlist li')
    # 获取下一页URL
    next_url = PyQuery(page_obj)('.previous-comment-page').attr['href']
    # 处理页面内容
    print "the picture nums: ", len(html_pq)
    if len(html_pq) <= 1:
        print 'This is last page'
        return
    for i in range(len(html_pq)):
        uploader = html_pq.eq(i)('.author strong').text()
        if not uploader:
            continue
        upload_time = html_pq.eq(i)('.author small').text()
        img_url = html_pq.eq(i)('.text p img').attr['src']
        vote_support = '#cos_support-'
        vote_unsupport = '#cos_unsupport-'
        vote = html_pq.eq(i)('.vote').attr['id']
        vote_id = str(vote)[5:].strip()
        # print "vote id ", vote_id
        vote_support_id = vote_support+vote_id
        vote_unsupport_id = vote_unsupport + vote_id
        # print "vote support %s un_support %s", (vote_support_id, vote_unsupport_id)
        vote_support_num = html_pq.eq(i)('.vote ')(vote_support_id).text()
        vote_unsupport_num = html_pq.eq(i)('.vote ')(vote_unsupport_id).text()
        # 判断图片是否存在
        has_img = is_existed(str(img_url).split())
        print 'has image %s' % has_img
        # 存储信息
        out_info = '%s, %s, %s, %s, %s' % ("'"+uploader+"'", "'"+upload_time+"'", "'"+img_url+"'", vote_support_num, vote_unsupport_num)
        print out_info
        if not has_img:
            save2db(out_info)

        # fw.write(out_info+"\n")
    # 是否要递归

    if next_url and int(next_url[next_url.index('-')+1:next_url.index('#')]) > int(endPageNum):
        time.sleep(1)
        print "next url is : ", next_url
        process_info(next_url, endPageNum)


def is_existed(img_url):
    """
    img 在mysql中是否存在
    :param img:
    :return:
    """
    config = {
        'user': 'root',
        'password': 'root',
        'host': '127.0.0.1',
        'port': 3306,
        'database': 'spider'
    }
    try:
        # print img_url[0]
        cnx = mysql.connector.connect(**config)
        cursor = cnx.cursor()
        select_sql = ("SELECT id FROM xxoo_jiandan WHERE img_url =%s")
        cursor.execute(select_sql % str("'"+img_url[0]+"'"))
        if len(cursor.fetchall()):
            return True
        else:
            return False
    except mysql.connector.Error, e:
        print e
        return False


def save2db(img_info):
    """
    save to mysql
    :return:
    """
    config = {
        'user': 'root',
        'password': 'root',
        'host': '127.0.0.1',
        'port': 3306,
        'database': 'spider'
    }
    if not img_info:
        return
    try:
        add_xxoo = "insert into xxoo_jiandan (uploader, uploader_time, img_url, support_num, un_support_num) VALUES (%s, %s, %s, %s, %s)"
        insert_sql = add_xxoo % tuple(img_info.split(','))
        print insert_sql
    #   persistence data
        cnx = mysql.connector.connect(**config)
        cursor = cnx.cursor()
        cursor.execute(insert_sql)
        cnx.commit()
    except mysql.connector.Error, e:
        print e
    finally:
        # cnx.close()
        return


def save_info_by_db():
    """
    保存至美女图表
    :return:
    """
    fr = open('../result/comment_meizhitu.txt', 'r')
    config = {
        'user': 'root',
        'password': 'root',
        'host': '127.0.0.1',
        'port': '3306',
        'database': 'spider'
    }
    # try:
    cnx = mysql.connector.connect(**config)
    cursor = cnx.cursor()
    for line in fr:
        line = line.rstrip('\n')
        line = unicode(line, chardet.detect(line)['encoding']).encode('utf-8')
        add_xxoo = 'insert into xxoo_jiandan (uploader, uploader_time, img_url, support_num, un_support_num) VALUES (%s, %s, %s, %s, %s)'
        print (add_xxoo, line.split(','))
        cursor.execute(add_xxoo, line.split(','))
    cnx.commit()
    cursor.close()
    # except mysql.connector.Error as err:
    #     print err.message
    fr.close()


def main():
    """
    控制
    :return:
    """
    next_url = r'http://jandan.net/ooxx/page-1350#comments'
    # global fw
    # fw = open("../result/comment_meizhitu_1.txt", 'w+')
    process_info(next_url, 1354)
    # fw.close()
    # save_info_by_db()

    # print is_existed(r' http://ww3.sinaimg.cn/mw600/005UDDlRjw1eq25qzjhyuj30zk0nnmzo.jpg')
if __name__ == '__main__':
    main()