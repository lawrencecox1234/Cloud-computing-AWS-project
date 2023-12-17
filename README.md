# Cloud-computing-AWS-project

Remember to only use the EC2 service on a localhost site not Google App Engine, if possible.

The user will need to remember to update the cred file everytime they want to launch EC2 within my system.

The user will need to have a AWS account with the same "keyname" and "SecurityGroupID" mentioned in the code where the Security Group also has port 80 enabled.

After EC2 is run on my system the user has 20 minutes to do the following:

On a seperate terminal set the current working directory to the "Config" file.

Edit the "commands2.py" Python file so that it has the new instance public DNS web address, which can be viewed on the AWS website after the instance is launched automatically using Boto3.

Run "python3 commands2.py" on the terminal and enter "yes".

Run the "ssh -i "KeyPair6.pem" ubuntu@(DNS link))" on the terminal with the specific DNS link

Run "sudo python3 commands3.py" on the terminal.

After a few minutes this should work.

