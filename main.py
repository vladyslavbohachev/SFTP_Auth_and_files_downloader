import os
import paramiko

def con():
	host = 'your_hostname'
	username = 'your_username'
	password = 'your_password'
	try:
		ssh = paramiko.SSHClient()
		ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
		ssh.connect(hostname=host,username=username,password=password)
		sftp = ssh.open_sftp()
		print('Connection succesfully stablished')
	except:
		print('failed to establish connection to targeted server')
	remotepath = '/'
	localpath = 'your_local_path_for_store'
	data = []
	for filename in sftp.listdir(remotepath):
		if filename.__contains__('Lösch'):
			sftp.remove(os.path.join(remotepath,filename))
		if filename.endswith('.xml') and not filename.__contains__('Lösch'):
			data.append(filename)
			sftp.get(os.path.join(remotepath,filename), os.path.join(localpath,filename))
			sftp.remove(os.path.join(remotepath,filename))
	sftp.close()
	ssh.close()

def main():
	con()

if __name__ == '__main__':
	main()