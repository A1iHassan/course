
#include <stdio.h>

int main() {
    int num = 10; // Declaration of an integer variable
    float pi = 3.14; // Declaration of a float variable


    printf("Number: %d, Pi: %.2f\n", num, pi);

    num = "Ali"; // this will give a Type-mismatch error when trying to compile this code


    int num = 10;
    char A = "A";
    char text[] = "20";

    // Here the A will be converted to its ASCII form,
    // which is equal to 65, and then it will be treated as an interger
    printf("Result: %d\n", num + A);

    // Implicit conversion happens here: string "20" is interpreted as its pointer,
    // since there is no currosponding value to it as what we saw in the previous example
    printf("Result: %d\n", num + text);  // Undefined behavior

    // Explicit conversion fixes the issue
    int converted = atoi(text);  // Convert string to integer
    printf("Result: %d\n", num + converted);  // Output: 30
    
    return 0;
}
