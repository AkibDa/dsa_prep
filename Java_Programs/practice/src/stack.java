import java.util.*;

public class stack {

    int maxSize;
    int[] stack;
    int top;

    public stack() {
        maxSize = 5;
        stack = new int[maxSize];
        top = -1;
    }

    public void push(int data) {

        if (top == maxSize - 1) {
            System.out.println("Overflow");
        }
        else {
            top++;
            stack[top] = data;
            System.out.println("Pushed: " + data);
        }

        return;
    }

    public void pop() {

        if (top == -1) {
            System.out.println("Underflow");
        }
        else {
            int popped = stack[top];
            System.out.println("Popped: " + popped);
            top--;
        }

        return;

    }

    public void peek() {

        if (top == -1) {
            System.out.println("No item present");
        }
        else {
            System.out.println("Item: " + stack[top]);
        }

        return;

    }

    public void display() {

        if (top == -1) {
            System.out.println("No item present");
        }
        else {
            for (int i = top; i >= 0; i--) {
                System.out.print(stack[i] + " ");
            }
            System.out.println();
        }

        return;
    }

    public static void main(String[] args) {

        stack obj = new stack();
        Scanner sc = new Scanner(System.in);
        int choice;
        int number;
        System.out.println("Enter your choice:\n");
        System.out.println("1. Push\n2. Pop\n3. Peek\n4. Display\n5. Exit");
        choice = sc.nextInt();
       while(true){
            switch (choice) {
                case 1:
                    System.out.println("Enter the number to push\n");
                    number = sc.nextInt();
                    obj.push(number);
                    break;
                case 2:
                    obj.pop();
                    break;
                case 3:
                    obj.peek();
                    break;
                case 4:
                    obj.display();
                    break;
                case 5:
                    System.exit(0);
                    break;
                default:
                    System.out.println("Invalid choice");
            }
        }
    }

}
