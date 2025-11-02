public class Patterns {
  public static void main(String[] args) {
    pattern1(4);
    System.out.println();
    pattern2(5);
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
  
  static void pattern2(int n){
    for(int i=1;i<=n;i++){
      for(int j=n;j>=i;j--){
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
}