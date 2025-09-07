import java.util.HashMap;
import java.util.Map.Entry;
import java.util.Set;

public class Hashmap {
  public static void main(String[] args) {
    //Creation
    //country(key), population(value)
    HashMap<String, Integer> map = new HashMap<>();

    //Insertion
    map.put("India", 120);
    map.put("USA", 30);
    map.put("China", 150);
    map.put("Russia", 20);

    //Print
    System.out.println(map);

    map.put("India", 125); //update
    System.out.println(map);

    //Search
    if(map.containsKey("India")) {
      System.out.println("Key is present");
    } else {
      System.out.println("Key is absent");
    }

    System.out.println(map.get("India")); //125
    System.out.println(map.get("Indonesia")); //null

    int arr[] = {1,2,3,4,5,6};
    for(int i=0;i<6;i++) {
      System.out.print(arr[i]+ " ");
    }
    System.out.println();
    for(int value : arr) {
      System.out.print(value+" ");
    }
    System.out.println();

    for(Entry<String, Integer> e : map.entrySet()) {
      System.out.println(e.getKey() + " : " + e.getValue());
    }

    Set<String> keys = map.keySet();
    for(String key : keys) {
      System.out.println(key + " : " + map.get(key));
    }
  }
}
