import os

os.system("sudo apt-get update -y")
os.system("sudo apt-get upgrade -y")
os.system("sudo apt-get install vim apache2 libapache2-mod-php php-mysql mysql-server -y")
os.system("sudo apt-get install mysql-client-core-8.0 -y")
os.system("sudo apt-get install php-cli -y")
os.system("sudo apt-get install python3 -y")
os.system("sudo apache2ctl restart")

#the code below contains modified code from the source:
#https://stackoverflow.com/questions/123198/how-can-a-file-be-copied

import shutil
shutil.copy("/home/ubuntu/apache2.conf","/etc/apache2/apache2.conf")
shutil.copy("/home/ubuntu/cgi_python.py","/var/www/html/form.py")

os.system("sudo chmod 755 /var/www/html/form.py")
os.system("sudo a2enmod cgi")
os.system("sudo service apache2 restart")
