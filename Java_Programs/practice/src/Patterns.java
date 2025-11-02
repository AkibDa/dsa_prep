public class Patterns {
  public static void main(String[] args) {
    pattern1(5);
    System.out.println();
    pattern2(5);
    System.out.println();
    pattern3(5);
    System.out.println();
    pattern4(5);
    System.out.println();
    pattern5(5);
    System.out.println();
    pattern6(5);
    System.out.println();
    pattern7(4);
  }

  static void pattern1(int n){
    for(int i=1; i<=n; i++){  // Number of lines in the pattern = outer loop
      for(int j=1; j<=i; j++){  // For every row number , how many columns are there and what type of elemens are there in the columns
        System.out.print("* "); // What to print in the columns
      }
      System.out.println();
    }
  }
  // Output:
  // *
  // * *
  // * * *
  // * * * *
  // * * * * *

  static void pattern2(int n){
    for(int i=1;i<=n;i++){
      for(int j=1;j<=n-i+1;j++){
        System.out.print("* ");
      }
      System.out.println();
    }
  }
  // Output:
  // * * * * *
  // * * * *
  // * * *
  // * *
  // *

  static void pattern3(int n){
    for(int i=0;i<=2*n;i++){
      int totalColsInRow = i>n ? 2*n-i : i;
      for(int j=0;j<totalColsInRow;j++){
        System.out.print("* ");
      }
      System.out.println();
    }
  }
  // Output:
  // *
  // * *
  // * * *
  // * * * *
  // * * * * *
  // * * * *
  // * * *
  // * *
  // *

  static void pattern4(int n){
    for(int i=0;i<2*n;i++){
      int totalColsInRow = i>n ? 2*n-i : i;
      int noOfSpaces = n - totalColsInRow;
      for(int s=0;s<noOfSpaces;s++){
        System.out.print(" ");
      }
      for(int j=0;j<totalColsInRow;j++){
        System.out.print("* ");
      }
      System.out.println();
    }
  }
  // Output:
  //      *
  //     * *
  //    * * *
  //   * * * *
  //  * * * * *
  //   * * * *
  //    * * *
  //     * *
  //      *

  static void pattern5(int n){
    for(int i=1;i<=n;i++){
      for(int j=0;j<n-i;j++){
        System.out.print("  ");
      }
      for(int j=i;j>=1;j--){
        System.out.print(j+" ");
      }
      for(int j=2;j<=i;j++){
        System.out.print(j+" ");
      }
      System.out.println();
    }
  }
  // Output:
  //         1
  //       2 1 2
  //     3 2 1 2 3
  //   4 3 2 1 2 3 4
  // 5 4 3 2 1 2 3 4 5

  static void pattern6(int n){
    for(int i=1;i<=2*n;i++){
      int totalColsInRow = i>n ? 2*n-i : i;
      int noOfSpaces = n - totalColsInRow;
      for(int s=0;s<noOfSpaces;s++){
        System.out.print("  ");
      }
      for(int j=totalColsInRow;j>=1;j--){
        System.out.print(j+" ");
      }
      for(int j=2;j<=totalColsInRow;j++){
        System.out.print(j+" ");
      }
      System.out.println();
    }
  }
  // Output:
  //         1
  //       2 1 2
  //     3 2 1 2 3
  //   4 3 2 1 2 3 4
  // 5 4 3 2 1 2 3 4 5
  //   4 3 2 1 2 3 4
  //     3 2 1 2 3
  //       2 1 2
  //         1

  static void pattern7(int n){
    for(int i=1;i<=2*n;i++){
      for(int j=1;j<=2*n;j++){
        int atEveryIndex = Math.min(Math.min(i,j),Math.min(2*n-i,2*n-j));
        System.out.print(atEveryIndex+" ");
      }
      System.out.println();
    }
  }
  // Output for n=4:
  // 1 1 1 1 1 1 1 1
  // 1 2 2 2 2 2 2 1
  // 1 2 3 3 3 3 2 1
  // 1 2 3 4 4 3 2 1
  // 1 2 3 4 4 3 2 1
  // 1 2 3 3 3 3 2 1
  // 1 2 2 2 2 2 2 1
  // 1 1 1 1 1 1 1 1
}