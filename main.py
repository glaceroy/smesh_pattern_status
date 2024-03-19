"""This is the main module of the smesh dashboard application"""
import http.client
import json
from flask import Flask, render_template


app = Flask(__name__)

@app.route('/')

def dashboard():
    """This function reads the static endpoints and gets the http connection status"""
    eps_dict = {}
    with open("static/endpoints.json", encoding="utf-8") as file:
        eps = json.load(file)

    for key, value in eps.items():
        connection = http.client.HTTPSConnection(value, timeout=10)
        connection.request("GET", "/")
        response = connection.getresponse()
        stat_code = response.status
        stat_reason = response.reason
        eps_dict.setdefault(key, [])
        eps_dict[key].append(value)
        eps_dict[key].append(stat_code)
        eps_dict[key].append(stat_reason)
        connection.close()
    return render_template('index.html', urls=eps_dict)

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=7000, use_reloader=True, debug=True)
