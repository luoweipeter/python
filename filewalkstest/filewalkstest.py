
import os

dirlis=[]
filelis=[]

for root,dirs,files in os.walk('d:\\TDDOWNLOAD'):
    for dir in dirs:
        dirlis.append(dir)
        fp=open('d:\\newpython.txt','a+').write('\n'+os.path.join(root,dir)+';\n')
    for file in files:
        filelis.append(os.path.join(root,file))
        fp=open('d:\\newpython.txt','a+').write(os.path.join(root,file)+';\n')
    
print('完成')
print(dirlis)
print(filelis)
print(open('d:\\newpython.txt','r').read())
