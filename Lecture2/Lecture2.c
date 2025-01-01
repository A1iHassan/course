
#include <stdio.h>
#include <stdlib.h>

int compare(int x, int y);
void set(int* x, int y);
void display(int x);


int main() {

    int ratings[7] = {147, 30, 50, 98, 195, 22, 70};
    int reference = 110;
    int current, winner, i;
    int *x = &winner;

    winner = ratings[0];

    for (i = 1; i < 7; i++) {
        current = compare(reference, ratings[i]);
        if (current < compare(reference, winner)) {
            set(x, ratings[i]);
        }
    }

    display(winner);

    return(0);
}

int compare(int x, int y) {
    int z = x - y;
    z = abs(z);
    return(z);
}

void set(int* x, int y) {
    *x = y;
}
void display(int winner) {
    printf("\n");
    printf("the winner is %d\n", winner);
    printf("\n");
}