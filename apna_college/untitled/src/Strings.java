
import java.util.Scanner;

public class Strings {

  public static void main(String[] args) {

    Scanner sc = new Scanner(System.in);
    String fullName;
    System.out.print("Enter your full name: ");
    fullName = sc.nextLine();
    String sentence = "Welcome, " + fullName + ".";
    System.out.println(sentence);
    sc.close();
  }

}