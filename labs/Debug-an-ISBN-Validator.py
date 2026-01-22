def validate_isbn(isbn, length):
    # Check if the length matches what the user specified
    if len(isbn) != length:
        print(f'ISBN-{length} code should be {length} digits long.')
        return
    
    try:
        # The check digit is the last character, the main digits are everything before it
        # Fix: off-by-one error. main_digits should be all except the last one.
        main_digits = isbn[:-1]
        given_check_digit = isbn[-1]
        
        # Convert the main digits to integers to verify they are numeric
        main_digits_list = [int(digit) for digit in main_digits]
        
        # Calculate the check digit from other digits
        if length == 10:
            expected_check_digit = calculate_check_digit_10(main_digits_list)
        else:
            expected_check_digit = calculate_check_digit_13(main_digits_list)
        
        # Check if the given check digit matches with the calculated check digit
        if given_check_digit == expected_check_digit:
            print('Valid ISBN Code.')
        else:
            print('Invalid ISBN Code.')
            
    except ValueError:
        # This catches cases where non-numeric characters are in main_digits
        print('Invalid character was found.')

def calculate_check_digit_10(main_digits_list):
    digits_sum = 0
    for index, digit in enumerate(main_digits_list):
        digits_sum += digit * (10 - index)
    result = 11 - digits_sum % 11
    if result == 11:
        expected_check_digit = '0'
    elif result == 10:
        expected_check_digit = 'X'
    else:
        expected_check_digit = str(result)
    return expected_check_digit

def calculate_check_digit_13(main_digits_list):
    digits_sum = 0
    for index, digit in enumerate(main_digits_list):
        if index % 2 == 0:
            digits_sum += digit * 1
        else:
            digits_sum += digit * 3
    result = 10 - digits_sum % 10
    if result == 10:
        expected_check_digit = '0'
    else:
        expected_check_digit = str(result)
    return expected_check_digit

def main():
    user_input = input('Enter ISBN and length: ')
    
    # Handle missing comma (IndexError)
    try:
        values = user_input.split(',')
        if len(values) < 2:
            raise IndexError
        
        isbn = values[0]
        
        # Handle non-numeric length (ValueError)
        try:
            length = int(values[1])
        except ValueError:
            print('Length must be a number.')
            return

        if length == 10 or length == 13:
            validate_isbn(isbn, length)
        else:
            print('Length should be 10 or 13.')
            
    except IndexError:
        print('Enter comma-separated values.')

# Important: main() is commented out for the tests to run properly
# main()