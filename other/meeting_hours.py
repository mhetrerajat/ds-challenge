"""
Maximize meeting hours

input : hours = [1, 2, 3, 6] | target = 10
output : [1,3,6]
"""

def get_value(memo, arr):
    key = hash(arr)
    _sum = memo.get(key)
    if _sum is None:
        _sum = sum(arr)
        memo[key] = _sum

    return memo[key]


def _maximize(idx, length, hours, target, current, answer, memo):
    #if target == sum(current) and current:
     #   answer.append(current)
      #  return
 
    current_sum = get_value(memo, current)
    if idx == length and current_sum <= target and current:
        if len(answer) == 0:
            answer.append(current)
        else:
            answer_sum = get_value(memo, answer[0])
            if answer_sum < current_sum:
                answer[0] = current
        return  
    elif idx == length or current_sum > target:
        return


    _maximize(idx+1, length, hours, target, current + (hours[idx],), answer, memo)
    _maximize(idx+1, length, hours, target, current, answer, memo)

def maximize(hours, target):
    length = len(hours)
    answer = []
    current = ()
    memo = {}
    _maximize(0, length, hours, target, current, answer, memo)

    return answer[0] if answer else ()


if __name__ == "__main__":
    assert maximize([1,2,3,6], 10) == (1,3,6)
    assert maximize([5,4,3], 6) == (5,)
    assert maximize([], 4) == ()
