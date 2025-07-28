import java.util.Scanner;

public class search_1D_array {

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        System.out.print("Enter the size of the array: ");
        int size = scanner.nextInt();

        int[] array = new int[size];
        System.out.println("Enter " + size + " elements:");
        for (int i = 0; i < size; i++) {
            array[i] = scanner.nextInt();
        }

        System.out.print("Enter the element to search: ");
        int elementToSearch = scanner.nextInt();

        boolean found = false;
        int index = -1;

        for (int i = 0; i < size; i++) {
            if (array[i] == elementToSearch) {
                found = true;
                index = i;
                break; // Element found, no need to continue searching
            }
        }

        if (found) {
            System.out.println("Element " + elementToSearch + " found at index " + index);
        } else {
            System.out.println("Element " + elementToSearch + " not found in the array.");
        }

        scanner.close();
    }

}
