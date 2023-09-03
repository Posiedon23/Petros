import requests
import json
import os

serverURL = 'https://petros.onrender.com'
KEY = "Lcml145"


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
    directory = path
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
    recSearch(directory)
    for file in struct:
        print(touch(file[0],file[1][0]))

def console():
    while True:
        print((execCmd(input("$: ")).get("message")))

def tree_display(path):
    data = tree(path)

    def display_directory_tree(node, indent="", last_sibling=True, root=True):
        if "name" in node:
            if not root:
                if last_sibling:
                    prefix = "└── "
                else:
                    prefix = "├── "
                print(indent + prefix + node["name"])
            else:
                print(node["name"])
        
        if "children" in node:
            num_children = len(node["children"])
            for i, child in enumerate(node["children"]):
                is_last = i == num_children - 1
                display_directory_tree(child, indent + ("    " if (last_sibling or i == num_children - 1) else "│   "), is_last, False)

    display_directory_tree(data["message"])