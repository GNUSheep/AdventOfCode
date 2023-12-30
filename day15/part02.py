sequences = input()
sequences = sequences.split(",")

def hash_algorith(label):
    cur_value = 0
    for c in label:
        cur_value += ord(c)
        cur_value *= 17
        cur_value %= 256
    return cur_value

boxes = {}
for i in range(256):
    boxes[i] = {}

for seq in sequences:
    if "=" in seq:
        box_label, focus_len = seq.split("=")
        box_label_hash = hash_algorith(box_label)
        boxes[box_label_hash][box_label] = focus_len
    if "-" in seq:
        box_label = seq.split("-")[0]
        box_label_hash = hash_algorith(box_label)
        if box_label in boxes[box_label_hash]:
            del boxes[box_label_hash][box_label]

total = 0
for box_value, box in boxes.items():
    if len(box) > 0:
        slot_num = 1
        for index, len_ in box.items():
            total += (int(box_value)+1)*slot_num*int(len_)
            slot_num += 1
print(total)