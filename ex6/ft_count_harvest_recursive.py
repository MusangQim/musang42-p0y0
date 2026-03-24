def ft_count_harvest_recursive():
    days = int(input('Days until harvest: '))
    helper(days, 1)


def helper(days, current=1):
    if current > days:
        print('Harvest time!')
    else:
        print('Day ', current)
        helper(days, current + 1)
