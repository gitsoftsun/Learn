# -*- coding: utf-8 -*-

# every day scraw  beautiful girl from jiandan.net

# 将妹子图专栏下载的信息存入输入库
# 所存字段： 上传者， 图片地址， 圈圈/支持， 叉叉/反对， 吐曹（暂时不收集 -不好收集）
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
sys.setrecursionlimit(100000)
from pyquery import PyQuery
import urllib2, urllib
import chardet
import time
import socket
girls_url = r'http://jandan.net/ooxx'


def process_info(all_pic, url):
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
            print 'socket timeout last'
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
        # 判断时间是否合理
        is_today = False
        # 存储信息
        out_info = '%s, %s, %s, %s, %s' % (uploader, upload_time, img_url, vote_support_num, vote_unsupport_num)
        fw.write(out_info+"\n")
        print out_info
    #是否要递归
    if all_pic and next_url:
        time.sleep(1)
        print "next url is : ", next_url
        process_info(True, next_url)


def save_info_by_db():
    """
    保存至美女图表
    :return:
    """
    pass


def main():
    """
    控制
    :return:
    """
    global fw
    fw = open("../result/comment_meizhitu.txt", 'w+')
    process_info(True, girls_url)
    fw.close()
if __name__ == '__main__':
    main()