import random

# Generate a random number between 1 and 100
def random_number():
    return random.randint(1, 100)

# Main function to print a random number
def main():
    print(f"Here's your random number: {random_number()}")

# Only run main() if this script is executed directly
if __name__ == "__main__":
    print("Running directly! Let's get a random number...")
    main()


