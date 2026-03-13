def ft_count_harvest_recursive(days, current=1):
    if current > days:
        print('Harvest time!')
    else:
        print('Day ', current)
        ft_count_harvest_recursive(days, current + 1)


days = int(input('Days until harvest: '))
