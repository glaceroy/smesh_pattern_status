import os, http.client, json
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')

def dashboard():
    
    a = {}  

    f = open("static/endpoints.json", "r")
    eps = json.load(f)

    for key, value in eps.items():
        connection = http.client.HTTPSConnection(value, timeout=10)
        connection.request("GET", "/")
        response = connection.getresponse()
        scode = response.status
        sreason = response.reason
        a.setdefault(key, [])
        a[key].append(value)
        a[key].append(scode)
        a[key].append(sreason)
        
        connection.close()

    return render_template('index.html', urls=a)

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, use_reloader=True, debug=True)