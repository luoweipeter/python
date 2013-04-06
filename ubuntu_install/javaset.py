import os
os.system("mkdir /usr/bin/java")

os.system("cp -ri /home/lw/develop/jdk1.7 /usr/bin/java")

pathlis=["export JAVA_HOME=/usr/lib/java/jdk1.7",
         "export JRE_HOME=$JAVA_HOME/jre",
         "export CLASSPATH=.:$JAVA_HOME/lib:$JRE_HOME/lib:$CLASSPATH",
         "export PATH=$JAVA_HOME/bin:JRE_HOME/bin:$PATH"
     ]

fp=open('/etc/profile','a+')
for i in range(0,4):
	fp.writelines("\n"+pathlis[i]+"\n")

fp.close()

os.system("update-alternatives --install /usr/bin/java java /usr/lib/java/jdk1.7/bin/java 300")

os.system("update-alternatives --install /usr/bin/javac javac /usr/lib/java/jdk1.7/bin/javac 300")

os.system("update-alternatives --config java") 

os.system("update-alternatives --config javac")

os.system("java -version")


