str = input('Enter any string: ').upper()

if str == str[::-1]:
    print('This is Palindrome.')
else:
    print('This is not Palindrome.')
