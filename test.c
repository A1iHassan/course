#include <stdio.h>


int main() {

    char x[50];
    int i;

    printf("enter your name :\n");

    fgets(x, sizeof(x), stdin);

    for (i = 0; i < 50; i++) {
        if (x[i] >= '0' && x[i] <= '9') {
            printf("wrong value, please enter a character\n");
            break;
        }
    }

    if (i > 49) {
        printf("%s\n", x);
    }


    return 0;

}
