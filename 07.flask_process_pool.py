import json
import math
from concurrent.futures import ProcessPoolExecutor
import flask

app = flask.Flask(__name__)


def is_prime(number):
    # 是否是素数  cpu密集型
    if number < 2:
        return False
    if number == 2:
        return True
    if number % 2 == 0:
        return False
    sqrt_n = int(math.floor(math.sqrt(number)))
    for i in range(3, sqrt_n + 1, 2):
        if number % i == 0:
            return False
    return True


@app.route("/is_prime/<numbers>")
def api_is_prime(numbers):
    number_list = [int(x) for x in numbers.split(",")]
    results = process_pool.map(is_prime, number_list)
    return json.dumps(dict(zip(number_list, results)))


if __name__ == "__main__":
    process_pool = ProcessPoolExecutor()
    app.run()
    '''
    在地址栏输入  http://127.0.0.1:5000/is_prime/1,2,3,4,5
    {"1": false, "2": true, "3": true, "4": false, "5": true}   
    '''


