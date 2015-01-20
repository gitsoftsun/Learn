#coding=utf-8
# http://s.dianping.com/event/shanghai
#定位城市：北京，上海，广州，深圳，南京，杭州，苏州，成都，重庆，青岛，厦门，武汉
#首页抓取，抓取所有活动数量，报名人数，活动地点
#详细信息抓取：点进banner,抓取活动具体地点，活动时间，活动名额，评论数量

import urllib2
import time
import json
import sys
reload(sys)
sys.setdefaultencoding('utf8')

from pyquery import PyQuery as pq
dict_citys = {'beijing':'北京', 'shanghai':'上海', 'guangzhou':'广州', 'shenzhen':'深圳', 'nanjing':'南京', 'hangzhou':'杭州', 'suzhou':'苏州', 'chengdu':'成都', 'chongqing':'重庆', 'qingdao':'青岛', 'xiamen':'厦门', 'wuhan':'武汉'};
URL = 'http://s.dianping.com/event/';
# 字典: beijing:'北京'
def get_homepageInfo(citys):
	fw = open('homePageInfo.txt', 'w+');
	for city in citys:
		html = urllib2.urlopen(URL + city).read();
		htmlPq = pq(html)(".free-activity p strong"); #获取标签中的内容
		numEvent = htmlPq.text(); #活动数量
		htmlPq1 = pq(html)(".apply-activ p strong");
		totalpeople = htmlPq1.text(); # 报名人数
		info = dict_citys.get(city) +", 活动数量: "+numEvent+", 报名人数: "+totalpeople+" \n";
		info = info.encode('utf-8');
		fw.write(info);
	fw.close();

#获取单个城市的每个活动的url
def get_subHref(city):	
	#获取所有活动的url 存到list中
	urlList =[];
	html = urllib2.urlopen(URL+city).read();
	

	htmlPq = pq(html)(".monad-default");
	m_url = 'http://s.dianping.com';
	for i in range(0, len(htmlPq)):
		purl = htmlPq.eq(i)('.tit a').attr['href'];
		urlList.append(m_url+purl);

	return urlList;

#抓取活动具体地点，活动时间，活动名额，评论数量
def get_subPageInfo(citys):
	fw = open("subpageinfo.txt", "w+");
	for city in citys:
		urls = get_subHref(city);
		fw.write(dict_citys.get(city)+"\n");
		for x in urls:
			html = urllib2.urlopen(x).read();
			entity = ""; 
			address = pq(html)(".address").text(); #活动地址
			entity = entity+address+", ";
			#活动时间
			tpq = pq(html)(".activity-list li");
			for t in range(2, 4):
				var = tpq.eq(t).text();
				entity = entity + var;
			recordCount = pq(html)("#J_recordCount").text(); #评论数量
			entity = entity+", 评论数量: "+recordCount+"\n";
			fw.write(entity);
		fw.write("\n");
	fw.close();

def main():
	# get_homepageInfo(dict_citys.keys());
	get_subPageInfo(dict_citys.keys());
if __name__ == "__main__":
    main()

				

