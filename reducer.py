import sys

current_title = None
current_count = 0
for line in sys.stdin:
    title, count = line.split('\t')

    try:
        count = int(count)
    except ValueError:
        continue

    if title == current_title:
        current_count += count
    else:
        if current_title is not None:
            print("{}\t{}".format(current_title, current_count))
        current_title, current_count = title, count

if current_title == title:
    print("{}\t{}".format(current_title, current_count))
