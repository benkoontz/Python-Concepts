# unpacking a list into variables makes it so you can give varibales to each value in the list
# when you unpack a list make sure your number of variables equals the number in your list

date, name, price = ['December 23, 2015', 'Bread Gloves', 8.51]

print(name)


def drop_first_last(grades):
    first, *middle, last = grades
    avg = sum(middle) / len(middle)
    print(avg)

drop_first_last([65, 76, 98, 54, 21])
