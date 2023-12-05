#2. Given an integer array of size n, find all elements that appear more than ⌊ n/3 ⌋ times.
def findMajority(arr, n):
    # Flag to check if a majority element is found
    flag = 0

    # Outer loop to iterate through each element in the array
    for i in range(n):
        # Counter to keep track of occurrences of the current element
        count = 0

        # Inner loop to count occurrences of the current element
        for j in range(i, n):
            if arr[i] == arr[j]:
                count += 1

        # If the count is greater than n/3, the current element is a majority element
        if count > int(n / 3):
            print(arr[i], end=" ")  # Print the majority element
            flag = 1  # Set flag to indicate that a majority element is found

    # If no majority element is found, print a message
    if flag == 0:
        print("No Majority Element")

# Take input as a list of integers
arr = list(map(int, input().split()))
n = len(arr)

# Call the function to find and print majority elements
findMajority(arr, n)
