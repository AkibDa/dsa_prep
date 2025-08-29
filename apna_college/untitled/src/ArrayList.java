import java.util.Collection;

public class ArrayList {
  public static void main(String[] args) {
    java.util.ArrayList<String> list = new java.util.ArrayList<>();
    list.add("Hello");
    list.add("World");
    System.out.println(list);
    list.remove("Hello");
    System.out.println(list);
    System.out.println("Size: " + list.size());
    list.add(1, "element");
    list.set(1, "hello");
    System.out.println(list);
    System.out.println("Contains 'World': " + list.contains("World"));
    list.clear();
    System.out.println("Is empty: " + list.isEmpty());
    System.out.println("Final list: " + list);
    Collection.sort(list);
    System.out.println("Sorted list: " + list);
  }
}
