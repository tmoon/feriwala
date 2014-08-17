from flask import Flask
from random import random
hello = Flask(__name__)

@hello.route('/')
def hello_world():
    return 'Hello World! New site!' + str( random() )

if __name__ == '__main__':
    hello.run()