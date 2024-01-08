from pyftpdlib.authorizers import DummyAuthorizer
from pyftpdlib.handlers import FTPHandler
from pyftpdlib.servers import FTPServer
import os

# Set local path
local_file_path = os.getcwd().replace("\\", "/")

# Set up authorizer
authorizer = DummyAuthorizer()
authorizer.add_user("admin", "admin", local_file_path+"/files", perm="elradfmw")

# Create FTP handler
handler = FTPHandler
handler.authorizer = authorizer

# Create FTP server
server = FTPServer(("127.0.0.1", 21), handler)

print("FTP server started. Listening on 127.0.0.1:21")

# Start the server
server.serve_forever()
