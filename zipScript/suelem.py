def subelem(chars,path,subkey):
    head='<{0}>'.format(chars)#截取标志字符头
    tail='/{0}'.format(chars)#截取标志字符尾

    fp=open(path,'r',encoding='utf-8')#打开处理的文件
    keyblock=fp.read()
    start=keyblock.find(head)+len(head)
    end=keyblock.find(tail)-1
    key=keyblock[start:end].strip()

    elem=[]
    keylist=key.split('\n')
    for keyelem in keylist:
        keyelems=keyelem.split(subkey)
        elem.append(keyelems[1])
    
    return(elem)

print(subelem('key','G:\\2013年数学文都高数基础班第二部分_汤家凤.txt','：'))



