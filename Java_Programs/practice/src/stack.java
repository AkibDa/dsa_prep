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

    public void push(int number) {
        if (top == maxSize - 1) {
            System.out.println("Overflow");
        } else {
            top++;
            stack[top] = number;
            System.out.println("Pushed: " + number);
        }
    }

    public void pop() {

        if (top == -1) {
            System.out.println("Underflow");
        } else {
            int popped = stack[top];
            System.out.println("Popped: " + popped);
            top--;
        }
    }

    public void peek() {

        if (top == -1) {
            System.out.println("No item present");
        } else {
            System.out.println("Item: " + stack[top]);
        }
    }

    public void display() {

        if (top == -1) {
            System.out.println("No item present");
        } else {
            for (int i = top; i >= 0; i--) {
                System.out.print(stack[i] + " ");
            }
            System.out.println();
        }
    }

    public static void main(String[] args) {

        stack obj = new stack();
        Scanner sc = new Scanner(System.in);
        int choice;

        while (true) {
            System.out.println("\nEnter your choice:");
            System.out.println("1. Push");
            System.out.println("2. Pop");
            System.out.println("3. Peek");
            System.out.println("4. Display");
            System.out.println("5. Exit");
            choice = sc.nextInt();

            switch (choice) {
                case 1:
                    System.out.println("Enter the number to push:");
                    int number = sc.nextInt();
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
                    System.out.println("Exiting program.");
                    System.exit(0);
                    break;
                default:
                    System.out.println("Invalid choice. Please try again.");
            }
        }
    }

}
