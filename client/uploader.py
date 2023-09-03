import os
directory = "test"
struct =  []
def recSearch(directory) :
    for file in os.listdir(directory):
        f = os.path.join(directory, file)
        print(f)
        if (os.path.isfile(f)):
            struct.append(f)
        if (os.path.isdir(f)):
            recSearch(f)

recSearch("test")
print(struct)
