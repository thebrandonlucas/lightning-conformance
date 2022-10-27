import os 
from flask import Flask, jsonify

from graph_server.lnd import describe_graph, get_info

app = Flask(__name__, static_folder='../static', static_url_path='/')

@app.route('/')
def index():
    return app.send_static_file('index.html')

@app.route("/health")
def hello_world():
    return "<p>Yep, I'm here!</p>"

@app.route("/info/<string:node>")
def lnd_info(node):
    return get_info(node)

@app.route("/graph/<string:node>")
def lnd_graph(node):
    return describe_graph(node) 

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
    
