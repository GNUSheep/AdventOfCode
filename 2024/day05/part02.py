from sys import stdin

ord_rules = {}
for line in stdin:
    if line == "\n":
        break

    page_nums = line.split("|")

    l = int(page_nums[0])
    r = int(page_nums[1])

    if not (r in ord_rules):
        ord_rules[r] = [l]
    else:
        ord_rules[r].append(l)

pages_to_produce = []
for line in stdin:
    pages_to_produce.append([int(n) for n in line.split(",")])

result = 0
for page in pages_to_produce:
    n = len(page)

    ordered_page = page.copy()
    for i in range(0, n):
        swapped = False

        for j in range(0, n-i-1):
            if not (ordered_page[j+1] in ord_rules):
                ordered_page[j], ordered_page[j+1] = ordered_page[j+1], ordered_page[j]
                swapped = True
            elif not (ordered_page[j] in ord_rules[ordered_page[j+1]]):
                ordered_page[j], ordered_page[j+1] = ordered_page[j+1], ordered_page[j]
                swapped = True

        if (swapped == False):
            break

    if ordered_page != page:
        middle_index = (len(ordered_page) - 1) // 2
        result += ordered_page[middle_index]
print(result)
