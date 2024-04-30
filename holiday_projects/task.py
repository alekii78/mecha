COOKIES = 48
BUTTER = 1
SUGAR = 1.5 * BUTTER
FLOOR = 2.7 * BUTTER
formular = (SUGAR + BUTTER + FLOOR) / 48
sugar = (48 * formular - FLOOR - BUTTER) / 1.5
butter = (48 * formular - sugar - FLOOR)
floor = (48 * formular - (1.5 * sugar) - butter) / 2.7
no_of_cookies = int(input('enter the number of cookies you want to bake  '))
amount_of_sugar = no_of_cookies * sugar
amount_of_butter = no_of_cookies * butter
amount_of_floor = no_of_cookies * floor
print('sugar needed', amount_of_sugar * 0.03125)
print('butter needed ', amount_of_butter * 0.0208)
print('floor needed  ', amount_of_floor * 0.05625)
