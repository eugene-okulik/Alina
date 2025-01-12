from statistics import mean

temperatures = [20, 15, 32, 34, 21, 19, 25, 27, 30, 32, 34, 30, 29, 25, 27, 22,
                22, 23, 25, 29, 29, 31, 33, 31, 30, 32, 30, 28, 24, 23]

new_temperature = list(filter(lambda x: x > 28, temperatures))
print(new_temperature)

max_value = max(new_temperature)
min_value = min(new_temperature)
average_value = round(mean(new_temperature), 1)
print(f'Some statistics: MAX t is "{max_value}",'
      f' MIN t is "{min_value}" and Average t is "{average_value}"')
