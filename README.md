here is some code:

  {
  ssh_client=paramiko.SSHClient()
  ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
  password=getpass.getpass('Please enter the password: ')
  }


![Screenshot 2025-05-07 143757](https://github.com/user-attachments/assets/b40bf119-832d-4165-bbbc-c82ae4891eb3)
