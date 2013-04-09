import os
fileslist=[]
cfileslist=[]
file=''
for root,dirs,files in os.walk('D:\\codebook'):
    for file in files:
        if(file.endswith('.c')):
            cfileslist.append(files)
    open('D:\\develop.txt','a+').write('%s'%('\n'.join(files)))

print(cfileslist)
