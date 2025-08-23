import java.util.*;

public class Patterns {

    public static void solid_rectangle(int n, int m) {
        for (int i = 1; i <= n; i++) {
            for (int j = 1; j <= m; j++) {
                System.out.print("*");
            }
            System.out.println();
        }
    }

    public static void hollow_rectangle(int n, int m) {
        for (int i = 1; i <= n; i++) {
            for (int j = 1; j <= m; j++) {
                if (i == 1 || j == 1 || j == m || i == n) {
                    System.out.print("*");
                }
                else {
                    System.out.print(" ");
                }
            }
            System.out.println();
        }
    }

    public static void half_pyramid(int n) {
        for (int i = 1; i <= n; i++) {
            for (int j = 1; j <= i; j++) {
                System.out.print("* ");
            }
            System.out.println();
        }
    }

    public static void inverted_half_pyramid(int n) {
        for (int i = n; i >= 1; i--) {
            for (int j = 1; j <= i; j++) {
                System.out.print("* ");
            }
            System.out.println();
        }
    }

    public static void inverted_half_pyramid_rotated_by_180_deg(int n) {
        for (int i = 1; i <= n; i++) {
            for(int k = 1; k <= n-i; k++) {
                System.out.print(" ");
            }
            for (int j = 1; j <= i; j++) {
                System.out.print("*");
            }
            System.out.println();
        }
    }

    public static void full_pyramid(int n) {
        for(int i = 1; i <= n; i++) {
            for(int k = 1; k <= n - i; k++) {
                System.out.print(" ");
            }
            for (int j = 1; j <= i; j++) {
                System.out.print("* ");
            }
            System.out.println();
        }
    }

    public static void half_pyramid_with_numbers(int n) {
        for (int i = 1; i <= n; i++) {
            for (int j = 1; j <= i; j++) {
                System.out.print(j+" ");
            }
            System.out.println();
        }
    }

    public static void half_inverted_pyramid_with_numbers(int n) {
        for (int i = 1; i <= n; i++) {
            for (int j = 1; j <= n-i+1; j++) {
                System.out.print(j+" ");
            }
            System.out.println();
        }
    }

    public static void floyd_triangle(int n) {
        int k = 1;
        for (int i = 1; i <= n; i++) {
            for (int j = 1; j <= i; j++) {
                System.out.print(k+" ");
                k++;
            }
            System.out.println();
        }
    }

    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);
        System.out.print("Enter the number of rows of a rectangle: ");
        int n = input.nextInt();
        System.out.print("Enter the number of columns of a rectangle: ");
        int m = input.nextInt();
        solid_rectangle(n,m);
        System.out.println();
        hollow_rectangle(n,m);
        System.out.print("Enter the number of rows of a pyramid: ");
        int a = input.nextInt();
        half_pyramid(a);
        System.out.println();
        inverted_half_pyramid(a);
        System.out.println();
        full_pyramid(a);
        System.out.println();
        inverted_half_pyramid_rotated_by_180_deg(a);
        System.out.println();
        half_pyramid_with_numbers(a);
        System.out.println();
        half_inverted_pyramid_with_numbers(a);
        System.out.println();
        floyd_triangle(a);
        System.out.println();
    }
}