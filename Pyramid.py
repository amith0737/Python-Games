def number_pattern_pyramid():
    print("Number Pattern: Pyramid")
    try:
        # Ask the user for the number of rows
        rows = int(input("Enter the number of rows for the pyramid: "))
        
        print("\nGenerated Pattern:\n")
        for i in range(1, rows + 1):
            # Print leading spaces
            print(" " * (rows - i), end="")
            # Print numbers in ascending order
            for j in range(1, i + 1):
                print(j, end=" ")
            print()  # Move to the next line
    except ValueError:
        print("⚠️ Invalid input! Please enter a valid number.")

# Run the function
number_pattern_pyramid()
