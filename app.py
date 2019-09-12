from flask import Flask, request, jsonify, render_template
import psutil
import os
import re
import sys

app = Flask(__name__)


def gen_counter():
    """
    アクセスカウンタ用の関数
    """
    access_cnt = 0

    def _count_add():
        nonlocal access_cnt
        access_cnt += 1
        return access_cnt
    return _count_add


def get_resource():
    """
    ホストのメトリクスを収集する関数
    """
    return psutil.cpu_percent(interval=1), \
        psutil.virtual_memory().percent, \
        os.getloadavg()[0],


# カウンタ用のクロージャ
gc = gen_counter()


@app.route('/')
def hello():
    return f"Hello, World!\nIP:{request.remote_addr}\nPID:{os.getpid()}\n"


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


@app.route('/__count')
def counter():
    return "ACCESS : " + str(gc()) + "\n" + "PID : " + str(os.getpid()) + "\n"


@app.errorhandler(404)
def err_404(error):
    response = jsonify({"message": "Not Found", "result": error.code})
    return response, error.code


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
