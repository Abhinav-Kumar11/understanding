#include <stdio.h>
#define MAX 100
int stack[MAX];
int top = -1;

// Check if stack is full
int isFull() {
    return top == MAX - 1;
}

// Check if stack is empty
int isEmpty() {
    return top == -1;
}
// Peek operation
int peek() {
    if (isEmpty()) {
        printf("Stack is Empty\n");
        return -1;
    }
    return stack[top];
}

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