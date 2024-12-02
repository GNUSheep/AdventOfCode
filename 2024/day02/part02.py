from sys import stdin

def solve(levels):
    is_desc = False
    if levels[0] > levels[1]:
        is_desc = True

    is_unsafe = False   
    for i in range(0, len(levels) - 1):
        if abs(levels[i] - levels[i + 1]) > 3:
            is_unsafe = True
            break

        if not is_desc and levels[i] >= levels[i + 1]:
            is_unsafe = True
            break
        
        if is_desc and levels[i] <= levels[i + 1]:
            is_unsafe = True
            break

    if not is_unsafe:
        return 1
    return 0
    
safe_reports_count = 0
for line in stdin:
    line_int = [int(n) for n in line.split()]

    if solve(line_int) == 0:
        for i in range(0, len(line_int)):
            new_list = line_int.copy()

            del new_list[i]

            if solve(new_list) == 1:
                safe_reports_count += 1
                break
    else:
        safe_reports_count += 1

    

print(safe_reports_count)
