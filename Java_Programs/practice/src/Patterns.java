public class Patterns {
  public static void main(String[] args) {
    pattern1(5);
    System.out.println();
    pattern2(5);
    System.out.println();
    pattern3(5);
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
}