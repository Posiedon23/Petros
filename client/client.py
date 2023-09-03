import requests
import json

serverURL = 'https://petros.onrender.com'


def test ():
    res =  requests.get(serverURL+"/test").json()
    return res
def mkdir (path):
    body = {
        "URI": path
    }
    res = requests.post(serverURL+"/dir", json=body).json()
    return res
def touch (path,data):
    body = {
        "URI": path,
        "data": data
    }
    res = requests.post(serverURL+"/file", json=body).json()
    return res
def tree (path):
    res = requests.get(serverURL+"/tree"+"?URI="+path).json()
    return res
def list (path):
    res = requests.get(serverURL+"/list"+"?URI="+path).json()
    return res
def rmdir (path):
    body = {
        "URI": path
    }
    res = requests.post(serverURL+"/rmdir", json=body).json()
    return res
def rm (path):
    body = {
        "URI": path
    }
    res = requests.post(serverURL+"/rm", json=body).json()
    return res
def cat (path):
    res = requests.get(serverURL+"/cat"+"?URI="+path).json()
    return res

def execCmd (cmd):
    body = {
        "key": "exec",
        "command": cmd,
    }
    res = requests.post(serverURL+"/exec", json=body).json()
    return res

# while  True:
#     print((execCmd(input("$: ")).get("message")))
print(list(""))
print(touch("testDir2/hello4.txt","hleo"))
print(list(""))
# print(mkdir("testDir"))