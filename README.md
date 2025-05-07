here is some code:

  {
  ssh_client=paramiko.SSHClient()
  ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
  password=getpass.getpass('Please enter the password: ')
  }



![Screenshot 2025-05-04 203030](https://github.com/user-attachments/assets/ed97046a-d68d-414a-9d96-8dfc1fc9a175)
