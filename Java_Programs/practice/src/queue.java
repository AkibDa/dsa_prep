import java.util.Scanner;

public class queue {

    int MAX_SIZE = 10;
    int[] queueArray;
    int front, rear;

    public queue() {
        queueArray = new int[MAX_SIZE];
        front = -1;
        rear = -1;
    }

    public boolean isEmpty() {
        return front == -1;
    }

    public boolean isFull() {
        return rear == MAX_SIZE - 1;
    }

    public void enqueue(int item) {
        if (isFull()) {
            System.out.println("Queue is full. Cannot enqueue.");
            return;
        }

        if (isEmpty()) {
            front = 0;
        }

        rear++;
        queueArray[rear] = item;
        System.out.println("Enqueued item: " + item);
    }

    public void dequeue() {
        if (isEmpty()) {
            System.out.println("Queue is empty. Cannot dequeue.");
            return;
        }

        int item = queueArray[front];
        System.out.println("Dequeued item: " + item);

        for (int i = front; i < rear; i++) {
            queueArray[i] = queueArray[i + 1];
        }

        rear--;
        if (rear == -1) {
            front = -1;
        }
    }

    public void display() {
        if (isEmpty()) {
            System.out.println("Queue is empty.");
            return;
        }

        System.out.print("Elements in the queue are: ");
        for (int i = front; i <= rear; i++) {
            System.out.print(queueArray[i] + " ");
        }
        System.out.println();
    }

    public static void main(String[] args) {
        queue obj = new queue();
        Scanner sc = new Scanner(System.in);
        int choice;

        while (true) {
            System.out.println("\n--- Linear Queue Operations ---");
            System.out.println("1. Enqueue");
            System.out.println("2. Dequeue");
            System.out.println("3. Display");
            System.out.println("4. Exit\n");
            System.out.print("Enter your choice: ");
            choice = sc.nextInt();

            switch (choice) {
                case 1:
                    System.out.print("Enter the number to insert: ");
                    int number = sc.nextInt();
                    obj.enqueue(number);
                    break;
                case 2:
                    obj.dequeue();
                    break;
                case 3:
                    obj.display();
                    break;
                case 4:
                    System.out.println("Exiting program.");
                    sc.close();
                    System.exit(0);
                    break;
                default:
                    System.out.println("Invalid choice. Please try again.");
            }
        }
    }
}