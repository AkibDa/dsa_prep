public class searchInStrings {
    public static void main(String[] args) {
        String name = "Akib";
        char target = 'u';
        System.out.println(search(name, target));
        System.out.println(search2(name, target));
        searchInRange(name, target, 1, 3);

    }

    static void searchInRange(String str, char target, int start, int end){
      if(str.length() == 0){
        System.out.println("String is empty");
        return;
      }
      for(int i=start; i<=end; i++){
        if(str.charAt(i) == target){
          System.out.println("Found " + target + " at index " + i);
          return;
        }
      }
      System.out.println(target + " not found in the given range");

    }

    static  boolean search2(String str, char target){
      if(str.length() == 0){
        return false;
      }
      for(char ch : str.toCharArray()){
        if(ch == target){
          return true;
        }
      }
      return false;
    }

    static boolean search(String str, char target){
      if(str.length() == 0){
        return false;
      }
      for(int i=0;i<str.length();i++){
        if(target == str.charAt(i)){
          return true;
        }
      }
      return false;
    }
}