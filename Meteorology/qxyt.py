#encoding=utf-8
import os,os.path
import re
import Queue
import urllib


def CreateDir():
	u"""
        *   功能
            *   创建所需的工作目录
        *   输入
            *   无
        *   返回
            *   无
    """
    	pathZero=u"气象云图"
	pathOne=u"FY2D云图"
	pathTwo=u"地面图"
	pathThree=u"925Hpa高空图"
	pathFour=u"850Hpa高空图"
	pathFive=u"700Hpa高空图"
	pathSix=u"500Hpa高空图"
	pathSeven=u"200Hpa高空图"
	pathEight=u"100Hpa高空图"
	pathList=[]
	pathList.append(pathZero)
	pathList.append(pathOne)
	pathList.append(pathTwo)
	pathList.append(pathThree)
	pathList.append(pathFour)
	pathList.append(pathFive)
	pathList.append(pathSix)
	pathList.append(pathSeven)
	pathList.append(pathEight)
	


	if not os.path.exists(pathZero):
		os.mkdir(pathZero)
	 	print u"气象图 文件夹不存在，即将创建"

	pathOne=os.path.join(pathZero,pathOne)
	if not os.path.exists(pathOne):
		os.mkdir(pathOne)
	 	print u"FY2D云图 文件夹不存在，即将创建"

	pathTwo=os.path.join(pathZero,pathTwo)
	if not os.path.exists(pathTwo):
		os.mkdir(pathTwo)
	 	print u"地面图 文件夹不存在，即将创建"

	pathThree=os.path.join(pathZero,pathThree)
	if not os.path.exists(pathThree):
		os.mkdir(pathThree)
	 	print u"925Hpa高空图 文件夹不存在，即将创建"

	pathFour=os.path.join(pathZero,pathFour)
	if not os.path.exists(pathFour):
		os.mkdir(pathFour)
	 	print u"850Hpa高空图 文件夹不存在，即将创建"

	pathFive=os.path.join(pathZero,pathFive)
	if not os.path.exists(pathFive):
		os.mkdir(pathFive)
	 	print u"700Hpa高空图 文件夹不存在，即将创建"

	pathSix=os.path.join(pathZero,pathSix)
	if not os.path.exists(pathSix):
		os.mkdir(pathSix)
	 	print u"500Hpa高空图 文件夹不存在，即将创建"

	pathSeven=os.path.join(pathZero,pathSeven)
	if not os.path.exists(pathSeven):
		os.mkdir(pathSeven)
	 	print u"200Hpa高空图 文件夹不存在，即将创建"

	pathEight=os.path.join(pathZero,pathEight)
	if not os.path.exists(pathEight):
		os.mkdir(pathEight)
	 	print u"100Hpa高空图 文件夹不存在，即将创建"

def WebRe(que):
	u"""
       	*   功能
            *   正则匹配网页里面需要下载的元素
        *   输入
            *   que作业队列
        *   返回
            *   无
     """

	#FY2D云图匹配
	# webContent=open(url,'r')
	webContent=urllib.urlopen('http://www.nmc.cn/publish/satellite.html')
	webContent=webContent.read()
	reReg=r'<p class="time">(.*)</p>'
	reg=re.compile(reReg)
	itemNameList=reg.findall(webContent)
	reReg=r'data-original=\"([^\"]*)\?v=\d*\"'
	reg=re.compile(reReg)
	itemLinkList=reg.findall(webContent)

	if len(itemLinkList)==len(itemNameList):
		print u"已经匹配完所有卫星云图，总计%d张图" %len(itemNameList)
	for item in range(len(itemNameList)):
		itemName=itemNameList[item]
		itemLink=itemLinkList[item]
		item=(itemName,itemLink,1)
		que.put(item)

	#地面图匹配
	# webContent=open("2.html",'r')
	webContent=urllib.urlopen('http://www.nmc.cn/publish/observations/china/index.html')
	webContent=webContent.read()
	reReg=r'<p class="time">(.*)</p>'
	reg=re.compile(reReg)
	itemNameList=reg.findall(webContent)
	reReg=r'data-original=\"([^\"]*)\?v=\d*\"'
	reg=re.compile(reReg)
	itemLinkList=reg.findall(webContent)
	# print itemLinkList
	if len(itemLinkList)==len(itemNameList):
		print u"已经匹配完所有地面图，总计%d张图" %len(itemNameList)
	for item in range(len(itemNameList)):
		itemName=itemNameList[item]
		itemLink=itemLinkList[item]
		item=(itemName,itemLink,2)
		que.put(item)

	#925Hpa高空图
	# webContent=open("3.html",'r')
	webContent=urllib.urlopen('http://www.nmc.cn/publish/observations/china/weatherchart_925hpa.html')
	webContent=webContent.read()
	reReg=r'<p class="time">(.*)</p>'
	reg=re.compile(reReg)
	itemNameList=reg.findall(webContent)
	reReg=r'data-original=\"([^\"]*)\?v=\d*\"'
	reg=re.compile(reReg)
	itemLinkList=reg.findall(webContent)
	# print itemLinkList
	if len(itemLinkList)==len(itemNameList):
		print u"已经匹配完所有925Hpa高空图，总计%d张图" %len(itemNameList)
	for item in range(len(itemNameList)):
		itemName=itemNameList[item]
		itemLink=itemLinkList[item]
		item=(itemName,itemLink,3)
		que.put(item)
		# print que.qsize()

	#850Hpa高空图
	# webContent=open("4.html",'r')
	webContent=urllib.urlopen('http://www.nmc.cn/publish/observations/china/weatherchart-h850.html')
	webContent=webContent.read()
	reReg=r'<p class="time">(.*)</p>'
	reg=re.compile(reReg)
	itemNameList=reg.findall(webContent)
	reReg=r'data-original=\"([^\"]*)\?v=\d*\"'
	reg=re.compile(reReg)
	itemLinkList=reg.findall(webContent)

	if len(itemLinkList)==len(itemNameList):
		print u"已经匹配完所有850Hpa高空图，总计%d张图" %len(itemNameList)
	for item in range(len(itemNameList)):
		itemName=itemNameList[item]
		itemLink=itemLinkList[item]
		item=(itemName,itemLink,4)
		que.put(item)

	#700Hpa高空图
	# webContent=open("5.html",'r')
	webContent=urllib.urlopen('http://www.nmc.cn/publish/observations/china/weatherchart-h700.html')
	webContent=webContent.read()
	reReg=r'<p class="time">(.*)</p>'
	reg=re.compile(reReg)
	itemNameList=reg.findall(webContent)
	reReg=r'data-original=\"([^\"]*)\?v=\d*\"'
	reg=re.compile(reReg)
	itemLinkList=reg.findall(webContent)

	if len(itemLinkList)==len(itemNameList):
		print u"已经匹配完所有700Hpa高空图，总计%d张图" %len(itemNameList)
	for item in range(len(itemNameList)):
		itemName=itemNameList[item]
		itemLink=itemLinkList[item]
		item=(itemName,itemLink,5)
		que.put(item)

	#500Hpa高空图
	# webContent=open("6.html",'r')
	webContent=urllib.urlopen('http://www.nmc.cn/publish/observations/china/weatherchart-h500.html')
	webContent=webContent.read()
	reReg=r'<p class="time">(.*)</p>'
	reg=re.compile(reReg)
	itemNameList=reg.findall(webContent)
	reReg=r'data-original=\"([^\"]*)\?v=\d*\"'
	reg=re.compile(reReg)
	itemLinkList=reg.findall(webContent)

	if len(itemLinkList)==len(itemNameList):
		print u"已经匹配完所有500Hpa高空图，总计%d张图" %len(itemNameList)
	for item in range(len(itemNameList)):
		itemName=itemNameList[item]
		itemLink=itemLinkList[item]
		item=(itemName,itemLink,6)
		que.put(item)


	#200Hpa高空图
	# webContent=open("7.html",'r')
 	webContent=urllib.urlopen('http://www.nmc.cn/publish/observations/china/weatherchart_200hpa.html')
	webContent=webContent.read()
	reReg=r'<p class="time">(.*)</p>'
	reg=re.compile(reReg)
	itemNameList=reg.findall(webContent)
	reReg=r'data-original=\"([^\"]*)\?v=\d*\"'
	reg=re.compile(reReg)
	itemLinkList=reg.findall(webContent)

	if len(itemLinkList)==len(itemNameList):
		print u"已经匹配完所有200Hpa高空图，总计%d张图" %len(itemNameList)
	for item in range(len(itemNameList)):
		itemName=itemNameList[item]
		itemLink=itemLinkList[item]
		item=(itemName,itemLink,7)
		que.put(item)

	#100Hpa高空图
	# webContent=open("8.html",'r')
	webContent=urllib.urlopen('http://www.nmc.cn/publish/observations/china/weatherchart_100hpa.html')
	webContent=webContent.read()
	reReg=r'<p class="time">(.*)</p>'
	reg=re.compile(reReg)
	itemNameList=reg.findall(webContent)
	reReg=r'data-original=\"([^\"]*)\?v=\d*\"'
	reg=re.compile(reReg)
	itemLinkList=reg.findall(webContent)

	if len(itemLinkList)==len(itemNameList):
		print u"已经匹配完所有100Hpa高空图，总计%d张图" %len(itemNameList)
	for item in range(len(itemNameList)):
		itemName=itemNameList[item]
		itemLink=itemLinkList[item]
		item=(itemName,itemLink,7)
		que.put(item)


def imgDownload(queDownload):
	u"""
       	*   功能
            *   下载队列里面的图片
        *   输入
            *   作业队列
        *   返回
            *   无
     """
	count=1
	total=queDownload.qsize()
	while True:
		# print queDownload.qsize()
		try:
			item=queDownload.get(block=False)
		except:
			print u"所有图片已下载完成"
			break
		itemName=item[0]
		itemLink=item[1]
		type=item[2]
		pathZero=u"气象云图"
		pathOne=u"FY2D云图"
		pathItem=os.path.join(pathZero,pathList[type])
		itemName=itemName.replace(':',"")
		#大图-小图
		itemLink=itemLink.replace('small','medium')
		target=itemName+u".jpg"
		target=os.path.join(pathItem,target)
		# print target
		url=itemLink
		try:
			print url 
			print target
			print u"正在下载第%d张图，还有%d张图,共%d张图"%(count,queDownload.qsize(),total)
			if os.path.exists(target):
				print u"文件已经存在"
			else:
				urllib.urlretrieve(url,target)
		except:
			print u"%s下载失败" %itemName
	print u"所有任务已经完成"
if __name__=="__main__":
	pathZero=u"气象云图"
	pathOne=u"FY2D云图"
	pathTwo=u"地面图"
	pathThree=u"925Hpa高空图"
	pathFour=u"850Hpa高空图"
	pathFive=u"700Hpa高空图"
	pathSix=u"500Hpa高空图"
	pathSeven=u"200Hpa高空图"
	pathEight=u"100Hpa高空图"
	pathList=[]
	pathList.append(pathZero)
	pathList.append(pathOne)
	pathList.append(pathTwo)
	pathList.append(pathThree)
	pathList.append(pathFour)
	pathList.append(pathFive)
	pathList.append(pathSix)
	pathList.append(pathSeven)
	pathList.append(pathEight)

	queDownload=Queue.Queue()
	CreateDir()
	WebRe(queDownload)
	imgDownload(queDownload)
