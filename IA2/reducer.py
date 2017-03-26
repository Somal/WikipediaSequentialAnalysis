import sys

THRESHOLD = 10000

current_title = None
count_by_date = {}
for line in sys.stdin:
    title, count, date = line.split('\t')

    try:
        count = int(count)
        date = int(date)
    except ValueError:
        continue

    if title == current_title:
        count_by_date[date] = count
    else:
        if current_title is not None:
            total_month_views = sum(count_by_date.values())
            # print(total_month_views)
            if total_month_views > THRESHOLD:
                print("{}\t{}\t".format(total_month_views, title) + "\t".join(
                    ["{}:{}".format(date, count_by_date[date]) for date in sorted(count_by_date.keys())]))
        current_title = title
        count_by_date = {date: count}

total_month_views = sum(count_by_date.values())
if total_month_views > THRESHOLD:
    print("{}\t{}".format(total_month_views, current_title) + "\t".join(
        ["{}:{}".format(date, count) for date, count in count_by_date.items()]))
