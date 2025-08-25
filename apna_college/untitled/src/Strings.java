

public class Strings {

  public static void main(String[] args) {

    // Concatination
    String firstName = "John";
    String lastName = "Doe";
    String fullName = firstName + " " + lastName;
    System.out.println("Full Name: " + fullName); 
    System.out.println("Length of Full Name: " + fullName.length());
    System.out.println("Uppercase Full Name: " + fullName.toUpperCase());
    System.out.println("Lowercase Full Name: " + fullName.toLowerCase());

    String name1 = "Alice";
    String name2 = "Alice";

    if(name1.compareTo(name2) == 0) {
      System.out.println(name1 + " is equal to " + name2);
    } else {
      System.out.println(name1 + " is not equal to " + name2);
    }

  }

}