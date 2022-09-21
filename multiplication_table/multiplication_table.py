for first_number in range(1, 11): # or range(1, 10 + 1)
    for second_number in range(1, 12): # or range(1, 11 + 1)  ## every 11 line print empty line
        result = first_number * second_number

        if second_number > 10: 
            print()
        else:
            print(f'{first_number} * {second_number} = {result}')
