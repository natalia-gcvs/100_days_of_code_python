string = 'ryan'
def solution(string):
    a = ''
    for index, letter in enumerate(string):
        a += string[-1 - index]
    return a


print(solution(string))