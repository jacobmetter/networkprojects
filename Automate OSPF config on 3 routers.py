import paramiko
import time

ssh_client=paramiko.SSHClient()
ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())  #these commands are necessary for paramiko to work

router1 = {'hostname':'10.1.2.10','port': '22','username':'u1','password':'cisco'}
router2= {'hostname':'10.1.2.20','port': '22','username':'u1','password':'cisco'}
router3= {'hostname':'10.1.2.30','port': '22','username':'u1','password':'cisco'}

routers=[router1,router2,router3] #the list of routers we are iterating over

for router in routers:

    print(f'Connecting to {router["hostname"]}')
    ssh_client.connect(**router, look_for_keys=False, allow_agent=False) #**router unpacks the dictionary router and puts it in this command

    shell=ssh_client.invoke_shell()

    shell.send('enable\n')
    shell.send('cisco\n') #this is the enable password
    shell.send('config t\n')
    shell.send('router ospf 1\n')
    shell.send('network 0.0.0.0 0.0.0.0 area 0\n')
    shell.send('end\n')
    shell.send('terminal length 0\n')
    shell.send('sh ip protocols\n')
    shell.send('wr\n')
    time.sleep(2)

    output=shell.recv(10000).decode() #takes everything that was run as bytes and decodes it to human readable format
    print(output)

    if ssh_client.get_transport().is_active()==True: #if the connection is active, then close connection
        print('Closing connection')
        ssh_client.close()