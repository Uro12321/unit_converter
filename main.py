print("Hello, this program converts kilometers into miles!")

while True:
    km = float(input("Please enter number in km: "))

    ratio = 0.621

    mile = km * ratio

    print("In miles this is: ", mile)

    choice = input("Want another conversion (yes/no): ")

    if choice != "yes":
        break

print("Goodbye!")