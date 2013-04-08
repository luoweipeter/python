

chars='keyblock'#截取标志字符
head='<{0}>'.format(chars)#截取标志字符头
tail='/{0}'.format(chars)#截取标志字符尾

fp=open('G:\\keyblock.txt','r')#打开
keyblock=fp.read()
start=keyblock.find(head)+len(head)
end=keyblock.find(tail)-1
key=keyblock[start:end].strip()
print(key)
