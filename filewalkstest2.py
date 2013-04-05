import os
for root,dirs,files in os.walk('/home/lw/develop/'):
    open('/home/lw/develop.txt','a+').write('%s,%s,%s,'%(''.join(root),''.join(dirs),''.join(files)))
    
