import os
# print(os.name) #used to get the name of the operating system dependent module imported. The following names have currently been registered: 'posix', 'nt', 'os2', 'ce', 'java', 'riscos'.
# print(os.environ) #used to get a mapping object representing the string environment. For example, os.environ['HOME'] returns the user's home directory.
# print(os.listdir()) #used to get a list containing the names of the entries in the directory given by path. The list is in arbitrary order, and does not include the special entries '.' and '..' even if they are present in the directory.

# folder = os.path.join(os.getcwd(), "new_directory") #used to get the current working directory
# os.mkdir(folder,exist_ok=True) #used to create a directory named path with numeric mode mode. If the directory already exists, FileExistsError is raised. If exist_ok is true, FileExistsError exceptions will be ignored (same behavior as mkdir() in Python 2).
# file_path = os.path.join(folder, "new_file.txt") #used to get the current working directory
# with open(file_path, "w") as f: #used to open a file, returning a file object. It is recommended to use the with keyword when dealing with file objects, as it ensures that the file is properly closed after its suite finishes, even if an exception is raised on the way.
#     f.write("Hello, this is a new file!") #used to write a string to the file. If the file already exists, it will be overwritten.
#Purpose of OS module is to interact with the underlying operating system. 
# It provides a way to use operating system dependent functionality 
# like reading or writing to the file system, managing directories, 
# and executing system commands.

print(os.getenv("PATH")) #used to get the value of the environment variable named key. If the environment variable is not found, it returns None.