from flask import Flask
hello = Flask(__name__)

@hello.route('/')
def hello_world():
    return 'Hello World!'

if __name__ == '__main__':
    hello.run()