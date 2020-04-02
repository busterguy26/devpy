
var = 1
var2 = '2'
var3 = 'Privet Vitalik'
var_list = [var, var2, {'d': 323, 1: 3424}]
var_list.append(var3)
new_list = [print, print]

new_list.append(var_list)

get_print = new_list[-1]
second_list = get_print

second_list.append('213213213123123')

var_tuple = (1, 2, 3, 3, '243234', 'a', 'a', 10, 10)

var_dict = {
    1: 'New car',
    var2: var_list,
    'Vasya': 33,

}
print(var_dict[var2])
