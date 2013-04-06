import os
import time

t=time.strftime("%Y-%m-%d %H:%S",time.localtime(time.time()))
os.system("git add .")
os.system("git commit -m '%s'"%t)
os.system("git push")
