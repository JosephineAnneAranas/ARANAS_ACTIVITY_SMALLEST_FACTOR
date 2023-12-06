while True: #Create an infinite loop to get the right input required
    number = int(input("Enter a positive integer: ")) #Let user input a positive integer

    if number <= 2: #Create a condition for inputs of <=2
        print("Invalid number! Choose a number greater than 2")

    else:
        for i in range(2, int(number**0.5) + 1): # Iterate from 2 onwards and find the smallest factor
            if number % i == 0:
                print(f"The smallest factor of {number} is {i}")
                break

        else:
            print(f"{number} is a prime number.")   # Determining if it is a prime number if there are no other factors
            break
