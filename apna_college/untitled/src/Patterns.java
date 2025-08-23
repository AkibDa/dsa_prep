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

    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);

        System.out.print("Enter the number of rows of a rectangle: ");
        int n = input.nextInt();
        System.out.print("Enter the number of columns of a rectangle: ");
        int m = input.nextInt();
        solid_rectangle(n,m);
        hollow_rectangle(n,m);

        System.out.print("Enter the number of rows of a pyramid: ");
        int a = input.nextInt();
        half_pyramid(a);

    }
}