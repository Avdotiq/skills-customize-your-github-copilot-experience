from helpers import greet_user, calculate_rectangle_area, is_prime


def main():
    name = "Alex"
    print(greet_user(name))

    width = 5
    height = 3
    area = calculate_rectangle_area(width, height)
    print(f"A {width} x {height} rectangle has area {area}.")

    number = 17
    prime_result = is_prime(number)
    print(f"Is {number} a prime number? {prime_result}")


if __name__ == "__main__":
    main()
