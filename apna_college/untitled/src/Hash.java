import java.util.HashSet;
import java.util.Iterator;

public class Hash {
  
  public static void main(String[] args) {
    //Creating a HashSet
    HashSet<Integer> set = new HashSet<>();

    //Adding elements to the HashSet
    set.add(1);
    set.add(2);
    set.add(3);
    set.add(1);

    //Size
    System.out.println("Size of HashSet: " + set.size());

    //Search - contains
    // if(set.contains(1)) {
    //   System.out.println("Set contains 1");
    // } else {
    //   System.out.println("Set does not contain 1");
    // }

    //Remove an element
    set.remove(2);
    if(!set.contains(2)) {
      System.out.println("Set does not contain 2");
    }

    //Print the HashSet
    System.out.println("HashSet: " + set);

    //Iterate over the HashSet
    Iterator it = set.iterator();
    while(it.hasNext()) {
      System.out.println(it.next());
    }
  }

}
