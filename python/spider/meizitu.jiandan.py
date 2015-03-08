# -*- coding: utf-8 -*-

# every day scraw  beautiful girl from jiandan.net

# 将妹子图专栏下载的信息存入输入库
# 所存字段： 上传者， 图片地址， 圈圈/支持， 叉叉/反对， 吐曹（暂时不收集 -不好收集）
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
from pyquery import PyQuery
import urllib2
import chardet
girls_url = r'http://jandan.net/ooxx'


def process_info(all_pic):
    """
    抓取信息
    :return:信息（图片信息）
    """
    url_request = urllib2.Request(girls_url, headers={'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/40.0.2214.111 Chrome/40.0.2214.111 Safari/537.36'})
    page = urllib2.urlopen(url_request, timeout=10)
    if page.getcode() != 200:
        print 'url : %s;  status code: %d' % (girls_url, page.getcode())
    page_obj = page.read()
    if isinstance(page_obj, str):
        page_obj = unicode(page_obj, chardet.detect(page_obj)['encoding'])
    html_pq = PyQuery(page_obj)('.commentlist li')
    # 处理页面内容
    if len(html_pq) <= 1:
        print 'This is last page'
        return
    for i in range(len(html_pq)):
        uploader = PyQuery.eq(i)('.author strong').text()
        upload_time = PyQuery.eq(i)('.author small').text()
        img_url = PyQuery.eq(i)('.text p img').attr['src']
        vote_support = 'cos_support-'
        vote_unsupport = 'cos_unsupport'
        vote = PyQuery.eq(i)('.vote').attr['id']
        vote_id = str(vote)[5:].strip()
        vote_support_id = vote_support+vote_id
        vote_support_num = PyQuery.eq(i)('.vote')(vote_support_id).text()
        vote_unsupport_id = vote_unsupport + vote_id
        vote_unsupport_num = PyQuery.eq(i)('.vote')(vote_unsupport_id).text()
        # 判断时间是否合理
        is_today = False
        # 存储信息
    #是否要递归



def save_info():
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
    pass
if __name__ == '__main__':
    main()