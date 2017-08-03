#!/usr/bin/python
print "Content-Type: text/html"
print

import cgi


print "hi"

data= cgi.FormContent()
print data

print ((data['nn'][0]))
print ((data['jt'][0]))
print((data['dn'][0]))
print ((data['dn'][1]))

commands.getstatusoutput("sshpass -p a ssh -l root "+(data['nn'][0])+" hostnamectl set-hostname namenode")
		
commands.getstatusoutput("sshpass -p a scp  /root/nn/hdfs-site.xml "+(data['nn'][0])+":/etc/hadoop") 
		
commands.getstatusoutput("sshpass -p a scp  /root/core-site.xml "+(data['nn'][0])+":/etc/hadoop")
commands.getstatusoutput("sshpass -p a ssh -l root "+(data['nn'][0])+" hadoop namenode -format")
		
commands.getstatusoutput("sshpass -p a ssh -l root "+(data['nn'][0])+" hadoop-daemon.sh start namenode")


commands.getstatusoutput("sshpass -p a scp  /root/mapred-site.xml "+(data['jt'][0])+":/etc/hadoop")
		
commands.getstatusoutput("sshpass -p a scp  /root/core-site.xml "+(data['jt'][0])+":/etc/hadoop")
commands.getstatusoutput("sshpass -p a ssh -l root "+(data['jt'][0])+" hadoop-daemon.sh start jobtracker")
	

commands.getstatusoutput("sshpass -p a scp  /root/dn/hdfs-site.xml "+(data['dn'][0])+":/etc/hadoop")
commands.getstatusoutput("sshpass -p a scp  /root/core-site.xml "+(data['dn'][0])+":/etc/hadoop")
commands.getstatusoutput("sshpass -p a scp  /root/mapred-site.xml "+(data['dn'][0])+":/etc/hadoop")
commands.getstatusoutput("sshpass -p a ssh -l root "+(data['dn'][0])+" hadoop-daemon.sh start datanode")
commands.getstatusoutput("sshpass -p a ssh -l root "+(data['dn'][0])+" hadoop-daemon.sh start tasktracker")

commands.getstatusoutput("sshpass -p a scp  /root/dn/hdfs-site.xml "+(data['dn'][1])+":/etc/hadoop")
commands.getstatusoutput("sshpass -p a scp  /root/core-site.xml "+(data['dn'][1])+":/etc/hadoop")
commands.getstatusoutput("sshpass -p a scp  /root/mapred-site.xml "+(data['dn'][1])+":/etc/hadoop")
commands.getstatusoutput("sshpass -p a ssh -l root "+(data['dn'][1])+" hadoop-daemon.sh start datanode")
commands.getstatusoutput("sshpass -p a ssh -l root "+(data['dn'][1])+" hadoop-daemon.sh start tasktracker")



print "done"
