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

}
