import java.util.Arrays;
import java.util.Scanner;

public class insert_2D_array {

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        System.out.print("Enter the number of rows: ");
        int rows = scanner.nextInt();
        System.out.print("Enter the number of columns: ");
        int cols = scanner.nextInt();

        int[][] originalArray = new int[rows][cols];
        System.out.println("Enter " + (rows * cols) + " elements for the 2D array:");
        for (int i = 0; i < rows; i++) {
            for (int j = 0; j < cols; j++) {
                originalArray[i][j] = scanner.nextInt();
            }
        }

        System.out.print("Enter the row index (0-indexed) to insert the new row at: ");
        int insertRowIndex = scanner.nextInt();

        if (insertRowIndex < 0 || insertRowIndex > rows) {
            System.out.println("Invalid row index. Must be between 0 and " + rows);
        } else {
            // Create a new 2D array with one more row
            int[][] newArray = new int[rows + 1][cols];

            // Copy rows before the insertion point
            for (int i = 0; i < insertRowIndex; i++) {
                System.arraycopy(originalArray[i], 0, newArray[i], 0, cols);
            }

            // Get the elements for the new row
            System.out.println("Enter " + cols + " elements for the new row:");
            for (int j = 0; j < cols; j++) {
                newArray[insertRowIndex][j] = scanner.nextInt();
            }

            // Copy rows after the insertion point, shifted down by one
            for (int i = insertRowIndex; i < rows; i++) {
                System.arraycopy(originalArray[i], 0, newArray[i + 1], 0, cols);
            }

            System.out.println("Original 2D Array:");
            print2DArray(originalArray);
            System.out.println("\n2D Array after row insertion:");
            print2DArray(newArray);
        }

        scanner.close();
    }

    public static void print2DArray(int[][] array) {
        for (int[] row : array) {
            System.out.println(Arrays.toString(row));
        }
    }

}
