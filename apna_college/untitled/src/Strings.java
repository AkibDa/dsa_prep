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

    // Comparison
    String name1 = "Alice";
    String name2 = "Alice";
    if(name1.compareTo(name2) == 0) {
      System.out.println(name1 + " is equal to " + name2);
    } else {
      System.out.println(name1 + " is not equal to " + name2);
    }

    // Substring
    String str = "Hello, World!";
    String substr = str.substring(7);
    System.out.println("Substring: " + substr);

    // String builder
    StringBuilder sb = new StringBuilder("Hello");
    System.out.println(sb);
    System.out.println(sb.charAt(0));
    sb.setCharAt(0, 'h');
    System.out.println(sb);
    sb.insert(0, 'n');
    System.out.println(sb);
    sb.deleteCharAt(0);
    System.out.println(sb);

    StringBuilder sb2 = new StringBuilder("h");
    sb2.append("e");
    sb2.append("l");
    sb2.append("l");
    sb2.append("o");
    System.out.println(sb2);
    sb2.reverse();
    System.out.println(sb2);

  }

}