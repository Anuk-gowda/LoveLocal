//Given an integer n, count the total number of digit 1 appearing in all non-negative integers less than or equal to n.
#include <stdio.h>

// Function to count the occurrences of digit '1' in all non-negative integers
// less than or equal to the given number 'n'.
void count_ones_in(int n) {
    // Initialize a variable to keep track of the count of digit '1'.
    int count = 0;

    // Iterate through all non-negative integers less than or equal to 'n'.
    for (int i = 0; i <= n; ++i) {
        int num = i;

        // Iterate through each digit of the current number 'i'.
        while (num > 0) {
            // Check if the current digit is equal to '1'.
            if (num % 10 == 1) {
                count++;  // Increment the count if the digit is '1'.
            }
            num /= 10;  // Move to the next digit.
        }
    }

    // Print the total count of digit '1'.
    printf("%d\n", count);
}

// The main function where the program starts execution.
int main() {
    int n;

    // Prompt the user to input a value for 'n'.
    printf("Enter a non-negative integer: ");
    scanf("%d", &n);

    // Call the function to count the occurrences of digit '1' and print the result.
    count_ones_in(n);

    // Indicate that the program has successfully run.
    return 0;
}
