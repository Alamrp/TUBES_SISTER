from ftplib import FTP
import os

def upload_file(ftp, local_file_path, remote_file_name):
    with open(local_file_path, "rb") as file:
        ftp.storbinary("STOR "+remote_file_name, file)
    print("File "+local_file_path+" uploaded as "+remote_file_name)

def download_file(ftp, remote_file_name, local_file_path):
    with open(local_file_path, "wb") as file:
        ftp.retrbinary("RETR "+remote_file_name, file.write)
    print("File "+remote_file_name+" downloaded as "+local_file_path)

# FTP server details
host = "127.0.0.1"
port = 21
user = "admin"
password = "admin"

# Connect to FTP server
ftp = FTP()
ftp.connect(host, port)
ftp.login(user, password)

# Set local path
local_file_path = os.getcwd().replace("\\", "/")

loop = True
while loop:
    print("what would you like to do?")
    print("1. upload")
    print("2. download")
    def upload():
        files = [f for f in os.listdir(local_file_path+"/files/")]
        if files:
            print("which file to upload?")
            i = 1
            for f in files:
                print(str(i)+" "+f)
                i+=1
            canceled = False
            while True:
                try:
                    remote_file_name_upload = files[input()-1]
                    break
                except:
                    print("upload canceled")
                    canceled = True
                    break
            if not canceled:
                local_file_path_upload = local_file_path+"/files/"+remote_file_name_upload
                upload_file(ftp, local_file_path_upload, remote_file_name_upload)
        else:
            print("no file in your directory")
    def download():
        print("insert file name to download: ")
        while True:
            try:
                remote_file_name_download = input()
                break
            except:
                print("wrap input in quotation marks!")
        local_file_path_download = local_file_path+"/download/"+remote_file_name_download
        try:
            download_file(ftp, remote_file_name_download, local_file_path_download)
        except:
            print("file not found")
    def neither():
        global loop
        loop = False
    while True:
        try:
            {1: upload, 2: download}.get(input(), neither)()
            break
        except:
            neither()
            break

# Example: Upload a file
# local_file_path_upload = "D:/College/SEM5/Distributed Systems/TUBES 2/client/files/hello world.txt"
# remote_file_name_upload = "hello world.txt"
# upload_file(ftp, local_file_path_upload, remote_file_name_upload)

# Example: Download a file
# remote_file_name_download = "hello world.txt"
# local_file_path_download = "D:/College/SEM5/Distributed Systems/TUBES 2/client/download/hello world.txt"
# download_file(ftp, remote_file_name_download, local_file_path_download)
