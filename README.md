# SFTP authentication and files downloader
Using SSH paramiko to auth on an SFTP Server without any security certificate to download, filter and delete files.   

```python
import os
import paramiko
```
***import os*** - for the folder declaration  
***import paramiko*** - for ssh auth

```python
def con():
  host = 'your_hostname'
  username = 'your_username'
  password = 'your_password'
```
***enter auth credentials*** - hostname of the server or ip address and username, password

```python
try:
  ssh = paramiko.SSHClient()
  ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
  ssh.connect(hostname=host,username=username,password=password)
  sftp = ssh.open_sftp()
  print('Connection succesfully stablished')
except:
  print('failed to establish connection to targeted server')
```
Try to establish connection to the server if connection is ok the code will print out:  
> Connection succesfully stablished  

***otherwise:***  

> failed to establish connection to targeted server  

```python 
remotepath = '/'
localpath = 'your_local_path_for_store'
```

specify remote and local path for the data transaction.  

```python
data = []
  for filename in sftp.listdir(remotepath):
    if filename.__contains__('Lösch'):
      sftp.remove(os.path.join(remotepath,filename))
    if filename.endswith('.xml') and not filename.__contains__('Lösch'):
      data.append(filename)
      sftp.get(os.path.join(remotepath,filename), os.path.join(localpath,filename))
      sftp.remove(os.path.join(remotepath,filename))
```
catch the data on the server to an array and filter it with some creteria that you need.  
with the block ```python sftp.get ``` you can download the date form the server to your local folder.  
With ```python sftp.remove ``` you delete the data on the server. 

As last thing that you dont have to forget ist to close the connection to the server.

```python

sftp.close()
ssh.close()
```

# Authentication methods
username and password
private-key not supported

# Features 
get file
list directory
test connection
remove file
filter files

# Usage 

> $root> python main.py
