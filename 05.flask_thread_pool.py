import time

import flask
import json

from concurrent.futures import ThreadPoolExecutor

app = flask.Flask(__name__)
pool = ThreadPoolExecutor()


def read_file():
    time.sleep(0.1)
    return "file result"


def read_db():
    time.sleep(0.2)
    return "db result"

def read_api():
    time.sleep(0.3)
    return "api result"

@app.route("/")
def index():
    '''
    不用线程池，一定是600ms+
    ➜  ~ time curl http://127.0.0.1:5000/
    {"result_file": "file result",
     "result_db": "db result",
     "result_api": "api result"
     }
     curl http://127.0.0.1:5000/  0.00s user 0.02s system 3% cpu 0.643 total
    '''

    # result_file = read_file()
    # result_db = read_db()
    # result_api = read_api()
    # return json.dumps({
    #     "result_file": result_file,
    #     "result_db": result_db,
    #     "result_api": result_api,
    # })

    # 使用了线程池
    '''
    使用了线程池，耗时在300ms+
    ➜  ~ time curl http://127.0.0.1:5000/
    {
      "result_file": "file result", 
      "result_db": "db result", 
      "result_api": "api result"
    }
    curl http://127.0.0.1:5000/  0.00s user 0.01s system 2% cpu 0.323 total
    '''
    result_file =pool.submit(read_file)
    result_db = pool.submit(read_db)
    result_api = pool.submit(read_api)
    return json.dumps({
        "result_file": result_file.result(),
        "result_db": result_db.result(),
        "result_api": result_api.result(),
    })

if __name__ == "__main__":
    app.run()