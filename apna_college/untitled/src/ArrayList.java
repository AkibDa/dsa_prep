public class ArrayList {
  public static void main(String[] args) {
    java.util.ArrayList<String> list = new java.util.ArrayList<>();
    list.add("Hello");
    list.add("World");
    System.out.println(list);
    list.remove("Hello");
    System.out.println(list);
    System.out.println("Size: " + list.size());
  }
}
