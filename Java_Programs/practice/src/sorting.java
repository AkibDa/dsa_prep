import java.util.Arrays;

public class sorting {

    /**
     * Prints the elements of an array.
     * @param arr The array to be printed.
     */
    public static void printArray(int[] arr) {
        System.out.println(Arrays.toString(arr));
    }

    // --- Bubble Sort ---
    /**
     * Implements the Bubble Sort algorithm.
     * Repeatedly steps through the list, compares adjacent elements and swaps them if they are in the wrong order.
     * @param arr The array to be sorted.
     */
    public static void bubbleSort(int[] arr) {
        int n = arr.length;
        boolean swapped;
        for (int i = 0; i < n - 1; i++) {
            swapped = false;
            for (int j = 0; j < n - 1 - i; j++) {
                // Compare adjacent elements
                if (arr[j] > arr[j + 1]) {
                    // Swap arr[j] and arr[j+1]
                    int temp = arr[j];
                    arr[j] = arr[j + 1];
                    arr[j + 1] = temp;
                    swapped = true;
                }
            }
            // If no two elements were swapped by inner loop, then break
            if (!swapped) {
                break;
            }
        }
    }

    // --- Selection Sort ---
    /**
     * Implements the Selection Sort algorithm.
     * Finds the minimum element from the unsorted part and puts it at the beginning.
     * @param arr The array to be sorted.
     */
    public static void selectionSort(int[] arr) {
        int n = arr.length;
        for (int i = 0; i < n - 1; i++) {
            // Find the minimum element in unsorted array
            int min_idx = i;
            for (int j = i + 1; j < n; j++) {
                if (arr[j] < arr[min_idx]) {
                    min_idx = j;
                }
            }
            // Swap the found minimum element with the first element
            int temp = arr[min_idx];
            arr[min_idx] = arr[i];
            arr[i] = temp;
        }
    }

    // --- Insertion Sort ---
    /**
     * Implements the Insertion Sort algorithm.
     * Builds the final sorted array one item at a time.
     * @param arr The array to be sorted.
     */
    public static void insertionSort(int[] arr) {
        int n = arr.length;
        for (int i = 1; i < n; i++) {
            int key = arr[i];
            int j = i - 1;

            // Move elements of arr[0..i-1], that are greater than key,
            // to one position ahead of their current position
            while (j >= 0 && arr[j] > key) {
                arr[j + 1] = arr[j];
                j = j - 1;
            }
            arr[j + 1] = key;
        }
    }

    // --- Merge Sort ---
    /**
     * Merges two subarrays of arr[].
     * First subarray is arr[l..m]
     * Second subarray is arr[m+1..r]
     * @param arr The array containing the subarrays.
     * @param l The starting index of the first subarray.
     * @param m The middle index.
     * @param r The ending index of the second subarray.
     */
    public static void merge(int[] arr, int l, int m, int r) {
        // Find sizes of two subarrays to be merged
        int n1 = m - l + 1;
        int n2 = r - m;

        /* Create temp arrays */
        int[] L = new int[n1];
        int[] R = new int[n2];

        /* Copy data to temp arrays */
        for (int i = 0; i < n1; ++i)
            L[i] = arr[l + i];
        for (int j = 0; j < n2; ++j)
            R[j] = arr[m + 1 + j];

        /* Merge the temp arrays */

        // Initial indexes of first and second subarrays
        int i = 0, j = 0;

        // Initial index of merged subarray array
        int k = l;
        while (i < n1 && j < n2) {
            if (L[i] <= R[j]) {
                arr[k] = L[i];
                i++;
            } else {
                arr[k] = R[j];
                j++;
            }
            k++;
        }

        /* Copy remaining elements of L[] if any */
        while (i < n1) {
            arr[k] = L[i];
            i++;
            k++;
        }

        /* Copy remaining elements of R[] if any */
        while (j < n2) {
            arr[k] = R[j];
            j++;
            k++;
        }
    }

    /**
     * Implements the Merge Sort algorithm.
     * Divides the array into two halves, recursively sorts them, and then merges the two sorted halves.
     * @param arr The array to be sorted.
     * @param l The starting index.
     * @param r The ending index.
     */
    public static void mergeSort(int[] arr, int l, int r) {
        if (l < r) {
            // Find the middle point
            int m = l + (r - l) / 2;

            // Sort first and second halves
            mergeSort(arr, l, m);
            mergeSort(arr, m + 1, r);

            // Merge the sorted halves
            merge(arr, l, m, r);
        }
    }

    // --- Quick Sort ---
    /**
     * Takes last element as pivot, places the pivot element at its correct position
     * in sorted array, and places all smaller (than pivot) to left of pivot and
     * all greater elements to right of pivot.
     * @param arr The array to be partitioned.
     * @param low The starting index.
     * @param high The ending index.
     * @return The partitioning index.
     */
    public static int partition(int[] arr, int low, int high) {
        int pivot = arr[high]; // Pivot
        int i = (low - 1); // Index of smaller element

        for (int j = low; j < high; j++) {
            // If current element is smaller than or equal to pivot
            if (arr[j] <= pivot) {
                i++;

                // Swap arr[i] and arr[j]
                int temp = arr[i];
                arr[i] = arr[j];
                arr[j] = temp;
            }
        }

        // Swap arr[i+1] and arr[high] (or pivot)
        int temp = arr[i + 1];
        arr[i + 1] = arr[high];
        arr[high] = temp;

        return i + 1;
    }

    /**
     * Implements the Quick Sort algorithm.
     * Uses a divide and conquer approach, picking an element as pivot and partitioning the array around the picked pivot.
     * @param arr The array to be sorted.
     * @param low The starting index.
     * @param high The ending index.
     */
    public static void quickSort(int[] arr, int low, int high) {
        if (low < high) {
            // pi is partitioning index, arr[pi] is now at right place
            int pi = partition(arr, low, high);

            // Recursively sort elements before partition and after partition
            quickSort(arr, low, pi - 1);
            quickSort(arr, pi + 1, high);
        }
    }

    public static void main(String[] args) {
        // Test Bubble Sort
        int[] arr1 = {64, 34, 25, 12, 22, 11, 90};
        System.out.println("Original array (Bubble Sort):");
        printArray(arr1);
        bubbleSort(arr1);
        System.out.println("Sorted array (Bubble Sort):");
        printArray(arr1);
        System.out.println("------------------------------------");

        // Test Selection Sort
        int[] arr2 = {64, 25, 12, 22, 11};
        System.out.println("Original array (Selection Sort):");
        printArray(arr2);
        selectionSort(arr2);
        System.out.println("Sorted array (Selection Sort):");
        printArray(arr2);
        System.out.println("------------------------------------");

        // Test Insertion Sort
        int[] arr3 = {12, 11, 13, 5, 6};
        System.out.println("Original array (Insertion Sort):");
        printArray(arr3);
        insertionSort(arr3);
        System.out.println("Sorted array (Insertion Sort):");
        printArray(arr3);
        System.out.println("------------------------------------");

        // Test Merge Sort
        int[] arr4 = {38, 27, 43, 3, 9, 82, 10};
        System.out.println("Original array (Merge Sort):");
        printArray(arr4);
        mergeSort(arr4, 0, arr4.length - 1);
        System.out.println("Sorted array (Merge Sort):");
        printArray(arr4);
        System.out.println("------------------------------------");

        // Test Quick Sort
        int[] arr5 = {10, 7, 8, 9, 1, 5};
        System.out.println("Original array (Quick Sort):");
        printArray(arr5);
        quickSort(arr5, 0, arr5.length - 1);
        System.out.println("Sorted array (Quick Sort):");
        printArray(arr5);
        System.out.println("------------------------------------");
    }

}
