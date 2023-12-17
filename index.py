#the code below contains modified code from page 18 from the Cloud Computing Lab 1 sheet produced by Lee Gillam

import os
import logging

from flask import Flask, request, render_template

app = Flask(__name__)

def doRender(tname, values={}):
	if not os.path.isfile(os.path.join(os.getcwd(), 'templates/'+tname)):
		return render_template('message.htm')
	return render_template(tname, **values)

@app.route('/random', methods=['POST'])
def RandomHandler():
        import http.client
        import time
        import queue
        import threading
        import math
        import urllib.request
        import pkgutil
        from time import sleep
        import os
        import urllib.request
        import pkgutil
        from time import sleep
        import boto3

        if request.method == 'POST':
        
                #the code below contains modified code from page 26 from the Cloud Computing Lab 1 sheet produced by Lee Gillam
                
                choice = request.form.get('choice')
                shots_total = request.form.get('shots')
                q_value = request.form.get('q_value')
                runs = request.form.get('runs')
                d_value = request.form.get('d_value')
                
                if choice == "LAMBDA":
                
                    runs = int(runs)
                    shots_total = int(shots_total)
                    d_value = int(d_value)
                
                    shots = int(shots_total/runs)
                    
                    #the code below contains modified code from page 13 from the Cloud Computing Lab 3 sheet produced by Lee Gillam
                
                    queue1 = queue.Queue()
                    queue2 = queue.Queue()
                
                    class ThreadUrl(threading.Thread):
                        def __init__(self, queue1, queue2, task_id):
                            threading.Thread.__init__(self)
                            self.queue1 = queue1
                            self.queue2 = queue2
                            self.task_id = task_id
                            self.data = None

                        def run(self):
                        
                            shots = self.queue1.get()
                            q_value = self.queue2.get()
                            host = "zfis95cmm5.execute-api.us-east-1.amazonaws.com"
                            try:
                                c = http.client.HTTPSConnection(host)
                                json= '{ "shots": ' + str(shots) + ', "q_value":' + str(q_value) + '}'
                                c.request("POST", "/default/function_one", json)
 
                                response = c.getresponse()
                                self.data = response.read().decode('utf-8')
                            
                            except IOError:
                                print( 'Failed to open ' , host ) 

                            self.queue1.task_done()
                            self.queue2.task_done()

                    def parallel_run():
                        threads=[]
                    
                        for i in range(0, runs):
                            t = ThreadUrl(queue1, queue2, i)
                            threads.append(t)
                            t.setDaemon(True)
                            t.start()

                        for x in range(0, runs):
                            queue1.put(shots)
                            queue2.put(q_value)
    
                        queue1.join()
                        queue2.join()

                        results = [t.data for t in threads]

                        return(results)
                
                    time_list = []
                    start = time.time()
                
                    data = parallel_run()
                
                    time_resource = time.time()-start
                    time_list.append(time_resource)
                
                    def format_list(data):
                
                        all_elements = []
                        incircle_list = []
                        shots_list = []
                        
                        #the code below contains modified code from the source:
                        #https://stackoverflow.com/questions/1894269/how-to-convert-string-representation-of-list-to-a-list
                
                        import ast
                        for vector in data:
                            vector = ast.literal_eval(vector)
                            for element in vector:
                                all_elements.append(element)
                        
                        incircle_list = all_elements[0::2]
                        
                        #the code below contains modified code from the source:
                        #https://stackoverflow.com/questions/28883769/remove-odd-indexed-elements-from-list-in-python 
                          
                        del all_elements[0::2]
                
                        shots_list = all_elements
                
                        resource_ID = []
                
                        shots2 = int(shots)
                        q_value2 = int(q_value)
                
                        number = int((shots2/q_value2))
                
                        for i in range(1,runs+1):
                            for j in range(0,number):
                                resource_ID.append(i)
                            
                        return incircle_list, shots_list, resource_ID, number
                    
                    count = 1
                    
                    def pi_calculation(shots_list,incircle_list):
                
                        shots_total = sum(shots_list)
                        incircle_total = sum(incircle_list)
                        pi_estimate = (incircle_total/shots_total)*4
                        pi_estimate = str(pi_estimate)
                        return(pi_estimate)   
                
                    pi_actual = str(math.pi)
                
                    d = 1 + d_value
                
                    def pi_check(pi_estimate):
                        pi_estimate = str(pi_estimate)                           
                        if pi_estimate[0:d] == pi_actual[0:d]:
                            return ('yes')
                        else:
                            return('no')    
                 
                    incircle_list, shots_list, resource_ID, number = format_list(data)
                
                    pi_estimate = pi_calculation(shots_list,incircle_list)
                
                    pi_estimate = str(pi_estimate)
                
                    while True and count<100:
                    
                        if pi_check(pi_estimate) == 'yes':
                            break
                        
                        else:
                            start = time.time()
                        
                            data = parallel_run()
                        
                            time_resource = time.time()-start
                            time_list.append(time_resource)
                        
                            incircle_list2, shots_list2, resource_ID2, number = format_list(data)
                            incircle_list = incircle_list + incircle_list2
                            shots_list = shots_list + shots_list2
                            resource_ID = resource_ID + resource_ID2
                            count +=1
                            pi_estimate = pi_calculation(shots_list,incircle_list)
                        
                            continue
                    
                    #the code below contains modified code from the source:
                    #https://stackoverflow.com/questions/20639180/explanation-of-how-nested-list-comprehension-works  
                      
                    shots_increasing = [sum(shots_list[0:n+1]) for n in range(len(shots_list))]
                    incircle_increasing = [sum(incircle_list[0:n+1]) for n in range(len(incircle_list))]
                
                    pi_list = []
                
                    for i in range(0,len(shots_increasing)):
                        value = (incircle_increasing[i]/shots_increasing[i])*4
                        pi_list.append(value)
                
                    listB = []
                
                    for k in range(0,len(shots_list)):
                        listA = []
                        listA.append(incircle_list[k])
                        listA.append(shots_list[k])
                        listA.append(resource_ID[k])
                        listC = tuple(listA)
                        listB.append(listC)
                    data = tuple(listB)
                
                    headings = ("Incircle","Shots","Resource ID")
   
                    data2 = pi_list
                    data2 = data2[0::20]
                    str1 = str(data2[0])
                    for i in data2[1:]:
                        str1 = str1 + ',' + str(i)
                    
                    time_final = sum(time_list)
                    time_final = str(time_final)
                    pi_estimate = str(pi_estimate)
                    
                    cost = (3.5/(1000000))*count*runs
                    cost = str(cost)
                    
                    pi_estimate = "|" + pi_estimate + "|"
                    time_final = "|" + time_final + "|"
                    cost = "|" + cost + "|"
                    
                    #the code below contains modified code from the source:
                    #https://stackoverflow.com/questions/46725789/flask-render-template
                    
                    return render_template('all.htm', headings=headings, data=data, data2=str1, pi_estimate=pi_estimate, time_final=time_final,cost=cost)
                      
                
                elif choice == "EC2":
                
                    runs = int(runs)
                    shots_total = int(shots_total)
                    d_value = int(d_value)
                
                    shots = int(shots_total/runs)
                    
                    #the user will need to remember to update the cred file everytime they want to launch EC2 within my system
                    #the user will need to have a AWS account with the same "keyname" and "SecurityGroupID" mentioned below where the Security Group also has port 80 enabled
                    
                    #the code below contains modified code from the sources:
                    #Cloud computing lab 5 page 22 produced by Lee Gillam
                    #https://boto3.amazonaws.com/v1/documentation/api/latest/guide/migrationec2.html
                
                    os.environ['AWS_SHARED_CREDENTIALS_FILE']='./cred' 

                    ec2 = boto3.resource('ec2',region_name='us-east-1')

                    image = "ami-09e67e426f25ce0d7"
                    keyname = "KeyPair6"

                    instances = ec2.create_instances(ImageId=image, MinCount=1, MaxCount=1, InstanceType ='t2.micro', KeyName=keyname, SecurityGroupIds=['sg-09203c7f3f0599b55',])
                    
                    #the code below contains modified code from the source:
                    #https://stackoverflow.com/questions/34728477/retrieving-public-dns-of-ec2-instance-with-boto3

                    instance = instances[0]

                    instance.wait_until_running()
                
                    start = time.time()

                    instance.load()
                    link = str(instance.public_dns_name)
                    
                    #the for loop below gives the user around 20 minutes to configure the launched instance on a seperate terminal. Within this time limit user must:
                    
                    #On a seperate terminal set the current working directory to the "Config" file
                    #edit the "commands2.py" Python file so that it has the new instance public DNS web address, which can be viewed on the AWS website after the instance is launched automatically above.
                    #run "python3 commands2.py" on the terminal and enter "yes"
                    #run the "ssh -i "KeyPair6.pem" ubuntu@(DNS link)" on the terminal with the specific DNS link (e.g. ssh -i "KeyPair6.pem" ubuntu@ec2-50-17-7-227.compute-1.amazonaws.com)
                    #run "sudo python3 commands3.py" on the terminal
                    #after a few minutes this should work

                    for x in range(0, 120):
                        try:
                            link2 = 'http://' + link + '/form.py?shots=200000&q_value=10000'
                            urllib.request.urlopen(link2).read().decode('utf-8').replace('\n', '')
                            break
                        except:
                            sleep(10)
                            continue
                            
                    #the code below contains modified code from page 13 from the Cloud Computing Lab 3 sheet produced by Lee Gillam
                        
                    queue1 = queue.Queue()
                    queue2 = queue.Queue()
                
                    class ThreadUrl(threading.Thread):
                        def __init__(self, queue1, queue2, task_id):
                            threading.Thread.__init__(self)
                            self.queue1 = queue1
                            self.queue2 = queue2
                            self.task_id = task_id
                            self.data = None

                        def run(self):
                       
                            shots = self.queue1.get()
                            q_value = self.queue2.get()
                            host = "http://" + link
                            try:
                                host2 = host + "/form.py?shots=" + str(shots) + "&q_value=" + str(q_value)
                                f = urllib.request.urlopen(host2)
                                data = f.read().decode('utf-8')
                                data = data.replace('\n', '')
                                self.data = data
                            
                            except IOError:
                                print( 'Failed to open ' , host )

                            self.queue1.task_done()
                            self.queue2.task_done()


                    def parallel_run():
                
                        threads=[]
                    
                        for i in range(0, runs):
                            t = ThreadUrl(queue1, queue2, i)
                            threads.append(t)
                            t.setDaemon(True)
                            t.start()

                        for x in range(0, runs):
                            queue1.put(shots)
                            queue2.put(q_value)
    
                        queue1.join()
                        queue2.join()

                        results = [t.data for t in threads]

                        return(results)

                    time_list = []
                    start2 = time.time()
                
                    data = parallel_run()
                
                    time_resource = time.time()-start2
                    time_list.append(time_resource)
                
                    def format_list(data):
                
                        all_elements = []
                        incircle_list = []
                        shots_list = []
                
                        import ast
                        for vector in data:
                            vector = ast.literal_eval(vector)
                            for element in vector:
                                all_elements.append(element)
                        
                        incircle_list = all_elements[0::2]
                  
                        del all_elements[0::2]
                
                        shots_list = all_elements
                
                        resource_ID = []
                
                        shots2 = int(shots)
                        q_value2 = int(q_value)
                
                        number = int((shots2/q_value2))
                
                        for i in range(1,runs+1):
                            for j in range(0,number):
                                resource_ID.append(i)
                            
                        return incircle_list, shots_list, resource_ID, number
                    
                    count = 1
                    
                    def pi_calculation(shots_list,incircle_list):
                
                        shots_total = sum(shots_list)
                        incircle_total = sum(incircle_list)
                        pi_estimate = (incircle_total/shots_total)*4
                        pi_estimate = str(pi_estimate)
                        return(pi_estimate)  
                    
                    pi_actual = str(math.pi)
                
                    d = 1 + d_value
                
                    def pi_check(pi_estimate):
                        pi_estimate = str(pi_estimate)                           
                        if pi_estimate[0:d] == pi_actual[0:d]:
                            return ('yes')
                        else:
                            return('no')    
                
                    incircle_list, shots_list, resource_ID, number = format_list(data)
                
                    pi_estimate = pi_calculation(shots_list,incircle_list)
                
                    pi_estimate = str(pi_estimate)
                
                    while True and count<100:
                    
                        if pi_check(pi_estimate) == 'yes':
                            break
                        
                        else:
                            start2 = time.time()
                            data = parallel_run()
                        
                            time_resource = time.time()-start2
                            time_list.append(time_resource)
                            
                            
                            incircle_list2, shots_list2, resource_ID2, number = format_list(data)
                            incircle_list = incircle_list + incircle_list2
                            shots_list = shots_list + shots_list2
                            resource_ID = resource_ID + resource_ID2
                            count +=1
                            pi_estimate = pi_calculation(shots_list,incircle_list)
                        
                            continue
                        
                    shots_increasing = [sum(shots_list[0:n+1]) for n in range(len(shots_list))]
                    incircle_increasing = [sum(incircle_list[0:n+1]) for n in range(len(incircle_list))]
                
                    pi_list = []
                
                    for i in range(0,len(shots_increasing)):
                        value = (incircle_increasing[i]/shots_increasing[i])*4
                        pi_list.append(value)
                
                    listB = []
                
                    for k in range(0,len(shots_list)):
                        listA = []
                        listA.append(incircle_list[k])
                        listA.append(shots_list[k])
                        listA.append(resource_ID[k])
                        listC = tuple(listA)
                        listB.append(listC)
                    data = tuple(listB)
                
                    headings = ("Incircle","Shots","Resource ID")
                
                    data2 = pi_list
                    data2 = data2[0::10]
                    str1 = str(data2[0])
                    for i in data2[1:]:
                        str1 = str1 + ',' + str(i)
                    

                    os.environ['AWS_SHARED_CREDENTIALS_FILE']='./cred'

                    ec2 = boto3.resource('ec2',region_name='us-east-1')
                    
                    #the code below contains modified code from the source:
                    #https://www.edureka.co/community/31996/how-print-all-the-instance-instance-state-using-python-boto3

                    for instance in ec2.instances.all():
                        ID = instance.id

                    ID_list = []
                    ID_list.append(ID)

                    ec2.instances.filter(InstanceIds=ID_list).terminate()
                    
                    time_final2 = time.time()-start
                    
                    time_rounded = round(time_final2)
           
                    cost = time_rounded*((0.0116)/(60*60))
                    
                    cost = str(cost)
                    
                    time_final = sum(time_list)
                    time_final = str(time_final)
                    
                    pi_estimate = "|" + pi_estimate + "|"
                    time_final = "|" + time_final + "|"
                    cost = "|" + cost + "|"
             
                    return render_template('all.htm', headings=headings, data=data, data2=str1, pi_estimate=pi_estimate, time_final=time_final, cost=cost)
                    
                else:
                
                    return('Please click the back button to return to the first page')
               
#the code below contains code from page 18 from the Cloud Computing Lab 1 sheet produced by Lee Gillam
              
@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def mainPage(path):
	return doRender(path)

@app.errorhandler(500)
def server_error(e):
    logging.exception('ERROR!')
    return """
    An  error occurred: <pre>{}</pre>
    """.format(e), 500

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8080, debug=True)
