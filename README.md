# Cloud-computing-AWS-project

* This application determines the cost of using AWS services to estimate the value of Pi - accurate to a specifiable number of digits using the Monte Carlo method.
* We achieve this using a website hosted using Google App Engine
* We also use AWS services such as Lambda and EC2 which we connect to using HTTP client

## Previously (2021) I deployed a site using Google App Engine using the following files:
* index.py
* templates/all.htm
* templates/message.htm
* random.htm
<br/>
The site also allows the user to alter specific parameters to change the Monte Carlo calculation

## Previously (2021) I setup up an AWS Lambda and EC2 service to be able to run the Monte Carlo simulation:

* Note: Currently the EC2 service only works on the localhost site not Google App Engine

### When running the EC2 service locally you'll need to use the following files:
* Config/commands2.py
* Config/commands3.py
### When running the EC2 service locally remember to do the following:

The user will need to remember to update the cred file everytime they want to launch EC2 within my system.

The user will need to have a AWS account with the same "keyname" and "SecurityGroupID" mentioned in the code where the Security Group also has port 80 enabled.

After EC2 is run on my system the user has 20 minutes to do the following:

On a seperate terminal set the current working directory to the "Config" file.

Edit the "commands2.py" Python file so that it has the new instance public DNS web address, which can be viewed on the AWS website after the instance is launched automatically using Boto3.

Run "python3 commands2.py" on the terminal and enter "yes".

Run the "ssh -i "KeyPair6.pem" ubuntu@(DNS link))" on the terminal with the specific DNS link

Run "sudo python3 commands3.py" on the terminal.

After a few minutes this should work.

