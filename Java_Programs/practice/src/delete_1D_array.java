import java.util.Arrays;
import java.util.Scanner;

public class delete_1D_array {

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        System.out.print("Enter the size of the array: ");
        int size = scanner.nextInt();

        int[] originalArray = new int[size];
        System.out.println("Enter " + size + " elements:");
        for (int i = 0; i < size; i++) {
            originalArray[i] = scanner.nextInt();
        }

        System.out.print("Enter the element to delete: ");
        int elementToDelete = scanner.nextInt();

        int indexToDelete = -1; // To store the index of the element to delete

        // Find the index of the element to delete
        for (int i = 0; i < size; i++) {
            if (originalArray[i] == elementToDelete) {
                indexToDelete = i;
                break; // Found the first occurrence, stop searching
            }
        }

        if (indexToDelete == -1) {
            System.out.println("Element " + elementToDelete + " not found in the array.");
        } else {
            // Create a new array with decreased size
            int[] newArray = new int[size - 1];
            int newArrayIndex = 0;

            // Copy elements, skipping the one to be deleted
            for (int i = 0; i < size; i++) {
                if (i != indexToDelete) {
                    newArray[newArrayIndex++] = originalArray[i];
                }
            }

            System.out.println("Original Array: " + Arrays.toString(originalArray));
            System.out.println("Array after deletion: " + Arrays.toString(newArray));
        }

        scanner.close();
    }

}
