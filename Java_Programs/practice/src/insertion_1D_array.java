import java.util.Arrays;
import java.util.Scanner;

public class insertion_1D_array {

    public static void main(String[] args) {

        Scanner scanner = new Scanner(System.in);

        System.out.print("Enter the size of the array: ");
        int size = scanner.nextInt();

        int[] originalArray = new int[size];
        System.out.println("Enter " + size + " elements:");
        for (int i = 0; i < size; i++) {
            originalArray[i] = scanner.nextInt();
        }

        System.out.print("Enter the element to insert: ");
        int elementToInsert = scanner.nextInt();

        System.out.print("Enter the position (0-indexed) to insert at: ");
        int position = scanner.nextInt();

        if (position < 0 || position > size) {
            System.out.println("Invalid position. Position must be between 0 and " + size);
        } else {
            // Create a new array with increased size
            int[] newArray = new int[size + 1];

            // Copy elements before the insertion point
            for (int i = 0; i < position; i++) {
                newArray[i] = originalArray[i];
            }

            // Insert the new element
            newArray[position] = elementToInsert;

            // Copy elements after the insertion point
            for (int i = position; i < size; i++) {
                newArray[i + 1] = originalArray[i];
            }

            System.out.println("Original Array: " + Arrays.toString(originalArray));
            System.out.println("Array after insertion: " + Arrays.toString(newArray));
        }

        scanner.close();
    }
}
