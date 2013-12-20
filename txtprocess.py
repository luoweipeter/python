# -*- coding: cp936 -*-
'''
一个处理TXT文件的文本
能够处理有如下行：
文件名 密码是：密码 
的文件。
'''
fp=open("*.txt","r")
fop=open("j:/txt.bat","w")
#def lineProcess(lines):
def f1(lines):
    i=1
    lst=[]
    for line in lines:
        if i<10:
            sStr=line[1:]
            fname,passwd=sStr.split("：")
            fname=fname.split(" ")[0]
            lst.append([fname,passwd])
            i=i+1
        else:
            sStr=line[2:]
            fname,passwd=sStr.split("：")
            fname=fname.split(" ")[0]
            lst.append([fname,passwd])
            i=i+1
    return lst
    

if __name__=="__main__":
    try:
        lines=[]
        i=1
        for line in fp:
            if i<=3:
                i+=1
                continue
            lines.append(line)
        
        print lines[0]
        result=f1(lines)
        for r in result:
            print>>fop,"7z e {fname}.zip -p{passwd}".format(fname=r[0],passwd=r[1])
    finally:
        fp.close()
        fop.close()
