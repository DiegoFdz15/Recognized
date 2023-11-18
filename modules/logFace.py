import os

def logFace(texto, name):
    folder = os.getcwd().replace("\\",'/') + '/logs'
    if not os.path.exists(folder):
        os.makedirs(folder)
    file = folder + f'/{name}_log.txt'

    if os.path.exists(file):
        f = open(file, "a")
    else:
        f = open(file, "x")
    f.write(texto)
    f.close()