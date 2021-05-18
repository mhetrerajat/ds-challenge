# n = 3
# choice  1,2,3


from flask import Flask
import json
from flask import jsonify

app = Flask(__name__)

@app.route("/<int:n>")
def get_combinations(n):
    return jsonify(combinations=calculate_combinations(n))
    


def _combinations(n, choices, current_sum, count):
    if current_sum == n:
        count[0] += 1
    elif current_sum > n:
        return
    else:
        # current_sum < n
        # search combinations

        _combinations(n, choices, current_sum + 1, count)
        _combinations(n, choices, current_sum + 2, count)
        _combinations(n, choices, current_sum + 3, count)


def calculate_combinations(n):
    choices = (1,2,3) 
    count = [0]
    _combinations(n, choices, 0, count)
    print(count[0], choices, n)
    return count[0]



#if __name__ == "__main__":
    #assert get_combinations(3) == 4
    #for i in [5, 10, 20]:
     #   get_combinations(i)
