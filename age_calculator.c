#include <stdio.h>

int main() {
    int birthYear, currentYear;
    printf("Enter your birth year: ");
    scanf("%d", &birthYear);
    printf("Enter the current year: ");
    scanf("%d", &currentYear);

    int age = currentYear - birthYear;
    printf("You are %d years old.\n", age);
    return 0;
}
