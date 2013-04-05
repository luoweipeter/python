import os

cmd=["echo IGD>/sys/kernel/debug/vgaswitcheroo/switch",
     "echo OFF>/sys/kernel/debug/vgaswitcheroo/switch",
     "cat /sys/kernel/debug/vgaswitcheroo/switch"]

fp=open('/etc/rc.local','a+')
for i in range(0,2):
	fp.writelines("\n"+cmd[i]+"\n")
fp.close()


os.system("gedit /etc/rc.local")
os.system("cat /sys/kernel/debug/vgaswitcheroo/switch")

