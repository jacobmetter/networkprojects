here is some code:

  {
  ssh_client=paramiko.SSHClient()
  ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
  password=getpass.getpass('Please enter the password: ')
  }



