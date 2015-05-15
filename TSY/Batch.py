#encoding=utf-8


#版本1.0
#2015-4-17
#作者：Patrickuo
import sys
reload( sys )
sys.setdefaultencoding("utf-8")
import os,os.path
fileList=[]
cwd=os.getcwd()
def walk_dir(dir,fileinfo,topdown=True):
    for root, dirs, files in os.walk(dir, topdown):
        for name in files:
        	item=os.path.join(cwd,root)
        	item=os.path.join(item,name)
        	fileList.append(item)
    #遍历得到目录结构
    for root, dirs, files in os.walk(dir, topdown):
        for name in files:
            fileinfo.write(os.path.join(root,name) + '\n')
        for name in dirs:
            fileinfo.write(os.path.join(root,name) + '\n')

def sy_rename(filepath,fileinfo):
    file_size=os.path.getsize(filepath)
    dirname=os.path.dirname(filepath)
    basename=os.path.basename(filepath)
    filename=os.path.splitext(basename)[0]
    ext=os.path.splitext(basename)[1]
    filename_without_ext=os.path.join(dirname,filename)

    if file_size>50485760:
        print u"以下文件大于50M，将不进行拖水印:"
        print basename
        fileinfo.write(filepath+"\n")
        return
    # print filename_without_ext
    try:
        os.rename(filepath,filename_without_ext)
    except:
        print filepath
        fileinfo.write(filepath+"\n")
        return 
    filename_jpg=filename_without_ext+".jpg"
    os.rename(filename_without_ext,filename_jpg)
    fp=open(filename_jpg,"rb")
    item=fp.read()
    fp.close()
    filename_dst=os.path.join(dirname,"dst")
    fp=open(filename_dst,"wb")
    fp.write(item)
    fp.close()
    filename_old=os.path.join(dirname,filename_without_ext)
    filename_old=filename_old+"(old)"+ext
    os.rename(filename_jpg,filename_old)
    # 删除文件
    os.remove(filename_old)

    temp=u"人家才不是水印"
    temp=basename
    try:
        filename_dst_ori=os.path.join(dirname,temp)
    except:
        fileinfo.write(filepath+"\n")
        print u"错误："
        print filepath
        print u"dirname:"+dirname
        print u"basename："+basename
        return
    os.rename(filename_dst,filename_dst_ori)
    

dir='test'
fileinfo_no = open(u'未脱.txt','w')
fileinfo=open(u"目录结构.txt","w")
walk_dir(dir,fileinfo)
file_total=len(fileList)
print u"总共有%d个文件进行处理" %file_total
i=1
for item in fileList:
    print u"正在处理第%d个文件,还有%d个文件" %(i,file_total-i)
    i=i+1
    sy_rename(item,fileinfo_no)
print u"处理完成"
	# print item