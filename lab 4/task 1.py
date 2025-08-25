import random

def generate_indian_mobile_number():
    # Indian mobile numbers start with 6, 7, 8, or 9 and are 10 digits long
    first_digit = str(random.choice([6, 7, 8, 9]))
    remaining_digits = ''.join(str(random.randint(0, 9)) for _ in range(9))
    return first_digit + remaining_digits

def main():
    mobile_number = generate_indian_mobile_number()
    print("Generated Indian Mobile Number:", mobile_number)

if __name__ == "__main__":
    main()