import requests
import json
import os
serverURL = 'https://petros.onrender.com'
KEY = "ABC"

def test ():
    res =  requests.get(serverURL+"/test").json()
    return res
def mkdir (path):
    body = {
        "URI": path,
        "key":KEY
    }
    res = requests.post(serverURL+"/dir", json=body).json()
    return res
def touch (path,data):
    body = {
        "URI": path,
        "data": data,
        "key":KEY
    }
    res = requests.post(serverURL+"/file", json=body).json()
    return res
def tree (path):
    res = requests.get(serverURL+"/tree"+"?URI="+path+"&key="+KEY).json()
    return res
def list (path):
    res = requests.get(serverURL+"/list"+"?URI="+path+"&key="+KEY).json()
    return res
def rmdir (path):
    body = {
        "URI": path,
        "key":KEY
    }
    res = requests.post(serverURL+"/rmdir", json=body).json()
    return res
def rm (path):
    body = {
        "URI": path,
        "key":KEY
    }
    res = requests.post(serverURL+"/rm", json=body).json()
    return res
def cat (path):
    res = requests.get(serverURL+"/cat"+"?URI="+path+"&key="+KEY).json()
    return res

def execCmd (cmd):
    body = {
        "command": cmd,
        "key":KEY
    }
    res = requests.post(serverURL+"/exec", json=body).json()
    return res

def upload(path):
    directory = "test"
    struct =  []
    def recSearch(directory) :
        for file in os.listdir(directory):
            f = os.path.join(directory, file)
            if (os.path.isfile(f)):
                with open(f) as ff:
                    lines = ff.readlines()
                    struct.append([f,lines])
            if (os.path.isdir(f)):
                recSearch(f)

    for file in struct:
        print(touch(file[0],file[1][0]))

def console():
    while True:
        print((execCmd(input("$: ")).get("message")))

console()

# print(list("testDir3"))
# print(mkdir("testDir2/hello"))
# print(touch("testDir3/txt1.txt","asdf"))
# print(list("testDir2"))
# print(mkdir("testDir"))