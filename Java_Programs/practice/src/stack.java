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

    }

    public void peek() {

        if (top == -1) {
            System.out.println("No item present");
        }
        else {
            System.out.println("Item: " + stack[top]);
        }

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
    }

    public static void main(String[] args) {}

}
