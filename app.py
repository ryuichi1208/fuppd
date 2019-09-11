from flask import Flask, request, jsonify, render_template
import psutil
import os
import re

app = Flask(__name__)


@app.route('/')
def hello():
    return f"Hello, World!\nIP:{request.remote_addr}\nPID:{os.getpid()}\n"


def get_resource():
    return psutil.cpu_percent(interval=1), \
            psutil.virtual_memory().percent, \
            os.getloadavg()[0],


@app.route('/__health')
def test():
    agent = request.headers.get('User-Agent')

    # ホストのリソース使用料を取得する
    cpu_per, mem_per, ldg_per = get_resource()

    if "Mozilla" in agent:
        return render_template('index.html',
                               cpu=cpu_per, mem=mem_per, ldg=ldg_per)
    else:
        return jsonify(
            {
                'CPU': cpu_per,
                'MEM': mem_per,
                'LDG': ldg_per
            }
        )


@app.errorhandler(404)
def err_404(error):
    response = jsonify({"message": "Not Found", "result": error.code})
    return response, error.code


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
