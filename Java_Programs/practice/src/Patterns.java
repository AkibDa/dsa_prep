public class Patterns {
  public static void main(String[] args) {
    pattern1();
  }

  static void pattern1(){
    for(int i=1; i<=4; i++){  // Number of lines in the pattern = outer loop
      for(int j=1; j<=i; j++){  // For every row number , how many columns are there and what type of elemens are there in the columns
        System.out.print("* "); // What to print in the columns
      }
      System.out.println();
    }
  }
}
// Output:
// *
// * *
// * * *
// * * * *