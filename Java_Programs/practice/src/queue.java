import java.util.Scanner;

public class queue {

    int MAX_SIZE;
    int[] queue;
    int front, rear;

    public queue() {
        MAX_SIZE = 10;
        queue = new int[MAX_SIZE];
        front = rear = -1;
    }

    public void enqueue(int item) {
        if (rear == MAX_SIZE - 1) {
            System.out.println("Queue is full. Please try again.");
        }  else {
            if (front == -1) {
                front++;
            }
            rear++;
            queue[rear] = item;
        }
    }

    public void dequeue() {
        if (front == -1) {
            System.out.println("Queue is empty. Please try again.");
        }
        else {
            int item = queue[front];
            if (front == rear) {
                front = rear = -1;
            }
            else  {
                front = front + 1;
            }
            System.out.println("Dequeued item: " + item);
        }
    }

    public static void  main(String[] args) {
        queue obj = new queue();
        Scanner sc = new Scanner(System.in);
        System.out.println("Enter the size of the queue:\n");
        int size = sc.nextInt();
        int choice;

        while (true) {
            System.out.println("\nEnter your choice:");
            System.out.println("1. Enqueue");
            System.out.println("2. Dequeue");
            System.out.println("3. Display");
            System.out.println("4. Exit");
            choice = sc.nextInt();

            switch (choice) {
                case 1:
                    System.out.println("Enter the number to push:");
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
                    System.exit(0);
                    break;
                default:
                    System.out.println("Invalid choice. Please try again.");
            }
        }
    }

}
