# damaltor1 THANKS U https://www.reddit.com/r/adventofcode/comments/18ghux0/comment/kd0npmi/
from sys import stdin

cache = {}
def get_num_of_solutions(record, criteria):
    if len(record) == 0:
        if len(criteria) == 0:
            return 1
        return 0

    if len(criteria) == 0:
        if "#" not in record:
            return 1
        return 0

    key = (record, criteria)
    if key in cache:
        return cache[key]

    result = 0

    if record[0] in ".?":
        result += get_num_of_solutions(record[1:], criteria)

    if record[0] in "#?":
        if len(record) >= criteria[0] and "." not in record[:criteria[0]] and (len(record) == criteria[0] or record[criteria[0]] != "#"):
            result += get_num_of_solutions(record[criteria[0] + 1:], criteria[1:])
    cache[key] = result
    return result

sum_of_solutions = 0
for line in stdin:
    record = line.split()[0]
    criteria = line.split()[1].split(',')
    criteria = tuple(eval(i) for i in criteria)

    record = "?".join([record] * 5)
    criteria *= 5

    sum_of_solutions += get_num_of_solutions(record, criteria)
print(sum_of_solutions)