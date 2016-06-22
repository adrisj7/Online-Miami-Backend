#from flask import jsonify
from json import dumps, loads
def read(directory):
    try:
        f = open(directory,'r')
        string = f.read()
        f.close()
    except:
        print 'FILE ' + directory + ' NOT FOUND'
        string = ''
    return string

def readJSON(directory):
    text = read(directory)
    return convert(loads(text))

def write(text,directory):
    f = open(directory,'w')
    f.write(text)
    f.close()

def writeJSON(dictionary,directory):
    write(dumps(dictionary),directory)
    


def convert(input):
    if isinstance(input, dict):
        return {convert(key): convert(value) for key, value in input.iteritems()}
    elif isinstance(input, list):
        return [convert(element) for element in input]
    elif isinstance(input, unicode):
        return input.encode('utf-8')
    else:
        return input
