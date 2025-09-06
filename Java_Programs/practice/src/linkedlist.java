public class linkedlist {
  public static void main(String[] args) {
    java.util.LinkedList<Integer> list = new java.util.LinkedList<>();
    java.util.LinkedList<Integer> newlist;
    list.add(1);
    list.add(2);
    list.add(3);
    for (int i : list) {
      System.out.print(i+"->");
    }
    System.out.println("null");
    newlist = list.reversed();
    for (int i : newlist) {
      System.out.print(i+"->");
    }
    System.out.println("null");
  }
}
