#the code below contains modified code from the source:
#https://stackoverflow.com/questions/6466711/what-is-the-return-value-of-os-system-in-python

import os
os.system("scp -i KeyPair6.pem cgi_python.py ubuntu@ec2-54-242-206-216.compute-1.amazonaws.com:")
os.system("scp -i KeyPair6.pem apache2.conf ubuntu@ec2-54-242-206-216.compute-1.amazonaws.com:")
os.system("scp -i KeyPair6.pem commands3.py ubuntu@ec2-54-242-206-216.compute-1.amazonaws.com:")
