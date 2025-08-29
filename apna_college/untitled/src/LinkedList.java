public class LinkedList {
  Node head;
  
  class Node {
    String data;
    Node next;

    Node(String data) {
      this.data = data;
      this.next = null;
    }

  }

  //add - first, last, at index

  public void addFirst(String data) {
    Node newNode = new Node(data);
    if(head == null) {
      head = newNode;
      return;
    } else {
      newNode.next = head;
      head = newNode;
    }
  }
  public void addLast(String data) {
    Node newNode = new Node(data);
    if(head == null) {
      head = newNode;
      return;
    }
    Node current = head;
    while(current.next != null) {
      current = current.next;
    }
    current.next = newNode;
    
  }
  public void printList(){
    if(head == null) {
      System.out.println("List is empty");
      return;
    }
    Node current = head;
    while(current != null) {
      System.out.print(current.data + " -> ");
      current = current.next;
    }
    System.out.println("null");
  }

  public static void main(String[] args) {
    LinkedList list = new LinkedList();
    list.addFirst("A");
    list.addFirst("B");
    list.printList();
    list.addLast("C");
    list.printList();
  }

}
