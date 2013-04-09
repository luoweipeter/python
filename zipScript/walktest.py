import os

i=1
filelist=[]
for root, dirs, files in os.walk("."):
    for file in files:
        if(file.endswith('.py')):
            filelist.append(file)
            open('newtxt.txt','a+').write("\n第%d次:  %s"%(i,file))
        i=i+1;
print(filelist)
