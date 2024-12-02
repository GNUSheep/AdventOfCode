from sys import stdin

safe_reports_count = 0
for line in stdin:
    line_int = [int(n) for n in line.split()]

    is_desc = False
    if line_int[0] > line_int[1]:
        is_desc = True

    is_unsafe = False   
    for i in range(0, len(line_int) - 1):
        if abs(line_int[i] - line_int[i + 1]) > 3:
            is_unsafe = True
            break

        if not is_desc and line_int[i] >= line_int[i + 1]:
            is_unsafe = True
            break
        
        if is_desc and line_int[i] <= line_int[i + 1]:
            is_unsafe = True
            break
        
    if not is_unsafe:
        safe_reports_count += 1

print(safe_reports_count)
