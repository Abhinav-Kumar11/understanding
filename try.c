#include <stdio.h>
int main() {
    push(10);
    push(20);
    push(30);
    push(40);

    display();

    printf("Top element: %d\n", peek());

    pop();
    display();

    return 0;
}