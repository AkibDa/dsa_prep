
public class LinkedList {
  // Node head;
  // private int size;

  //   public LinkedList() {
  //     this.size = 0;
  //   }
  
  // class Node {
  //   String data;
  //   Node next;

  //   Node(String data) {
  //     this.data = data;
  //     this.next = null;
  //     size++;
  //   }

  // }

  // public void addFirst(String data) {
  //   Node newNode = new Node(data);
  //   if(head == null) {
  //     head = newNode;
  //     return;
  //   } else {
  //     newNode.next = head;
  //     head = newNode;
  //   }
  // }
  // public void addLast(String data) {
  //   Node newNode = new Node(data);
  //   if(head == null) {
  //     head = newNode;
  //     return;
  //   }
  //   Node current = head;
  //   while(current.next != null) {
  //     current = current.next;
  //   }
  //   current.next = newNode;
    
  // }
  // public void printList(){
  //   if(head == null) {
  //     System.out.println("List is empty");
  //     return;
  //   }
  //   Node current = head;
  //   while(current != null) {
  //     System.out.print(current.data + " -> ");
  //     current = current.next;
  //   }
  //   System.out.println("null");
  // }

  // public void deleteFirst() {
  //   if(head == null) {
  //     System.out.println("List is empty");
  //     return;
  //   }
  //   size--;
  //   head = head.next;
  // }
  // public void deleteLast() {
  //   if(head == null) {
  //     System.out.println("List is empty");
  //     return;
  //   }
  //   size--;
  //   if(head.next == null) {
  //     head = null;
  //     return;
  //   }
  //   Node current = head;
  //   while(current.next.next != null) {
  //     current = current.next;
  //   }
  //   current.next = null;
  // }

  // public int getSize() {
  //   return size;
  // }

  public static void main(String[] args) {
    java.util.LinkedList<String> list = new java.util.LinkedList<>();
    list.addFirst("A");
    list.addFirst("B");
    list.addLast("C");
    list.addLast("D");
    System.out.println(list);
    list.removeFirst();
    System.out.println(list);
    list.removeLast();
    System.out.println(list);
    System.out.println(list.size());

    for(int i=0; i<list.size(); i++) {
      System.out.print(list.get(i) + " -> ");
    }
    System.out.println("null");

  }

}
