def total_values():
    total_value = 0
    while True:
        value = input('Please enter the value: ')
        if value != '':
            try:
                float_value = float(value)
                if value != '':
                    total_value += float_value
            except Exception as e:
                print('\nThe entered value is not of number type, more details mentioned below:\n')
                print(e)
        else:
            print('\nYou have pressed enter key.\nThank you')
            break
    print(f'\nTotal value is {total_value}')


total_values()
