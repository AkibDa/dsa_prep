import java.util.ArrayList;
import java.util.List;

public class FinDupArr {
  public static List<Integer> findDuplicates(int[] nums) {
    List<Integer> list=new ArrayList<>();
    int[] count=new int[nums.length+1];
    for(int num:nums){
      count[num]++;
      if(count[num]==2){
        list.add(num);
      }
    }
    return list;
      
  }

  public static void main(String[] args) {
    int[] nums = {4, 3, 2, 7, 8, 2, 3, 1};
    List<Integer> result = findDuplicates(nums);
    System.out.println(result); // Output: [2, 3]
  }

}
