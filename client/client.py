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

# mkdir("Test")
print(test())
# print(rm("../ta.js"))
print(list("../../server/data"))
# print(touch("t2.txt","lorem"))
# print(list(""))
# print(rm("*"))
# print(rmdir("../../server"))
# print(cat("../../../../.ssh_env"))
# print(mkdir("tst"))