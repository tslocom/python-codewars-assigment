# Solution: Even or Odd
def even_or_odd(number):
    if number % 2 == 0:
        return "Even"
    else:
        return "Odd"
    
# Solution: Convert a Number to a String
def number_to_string(num):
    string = str(num)
    return string

# Solution: Remove String Spaces
def no_space(x):
    x_no_space = x.replace(" ", "")
    return x_no_space

# Solution: Vowel Count
def get_count(sentence):
    vowels = "aeiou"
    return sum(1 for char in sentence.lower() if char in vowels)