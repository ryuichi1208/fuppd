from flask import Flask, request, jsonify, render_template
import psutil
import os
import re

app = Flask(__name__)


@app.route('/')
def hello():
    return f"Hello, World!\nIP:{request.remote_addr}\nPID:{os.getpid()}\n"


@app.route('/__test')
def test():
    agent = request.headers.get('User-Agent')

    # ホストのリソース使用料を取得する
    cpu_per = psutil.cpu_percent(interval=1)
    mem_per = psutil.virtual_memory().percent
    ldg_per = os.getloadavg()[0]

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


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
