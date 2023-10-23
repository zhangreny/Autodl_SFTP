import paramiko
import time
import os

def sftp_transfer(hostname, port, username, password, source_path, destination_path):
    transport = paramiko.Transport((hostname, port))

    try:
        transport.connect(username=username, password=password)
        sftp = paramiko.SFTPClient.from_transport(transport)

        try:
            print(f"Transferring file from {source_path} to {destination_path}")
            sftp.put(source_path, destination_path)
            print("File transferred successfully!")
        except Exception as e:
            print(f"Error: {e}")
            print("Retrying in 1 second...")
            time.sleep(1)
            # 递归调用自身进行重试
            sftp_transfer(hostname, port, username, password, source_path, destination_path)
        finally:
            sftp.close()
    except Exception as e:
        print(f"Error connecting to SFTP server: {e}")
    finally:
        transport.close()

hostname = 'xxx.com'  # SFTP服务器的主机名或IP地址
port = 43071  # SFTP服务器的端口号，默认是22
username = 'xxx'  # SFTP服务器的用户名
password = 'xxx'  # SFTP服务器的密码


'''
    这个函数的功能是
    把一个文件夹里面的所有文件都sftp上传到远端服务器的某个路径下面
    因此需要把某个文件夹中放满要上传的文件
    然后修改 source_path 和 destination_path 的值
'''

source_path = 'C:/xxx/xxx/'  # 本地文件的路径
destination_path = '/xxx/xxx/xxx/'

for filename in os.listdir(source_path):
    print("============="+filename+"=============")
    filepath = source_path + filename
    sftp_transfer(hostname, port, username, password, filepath, destination_path+filename)
