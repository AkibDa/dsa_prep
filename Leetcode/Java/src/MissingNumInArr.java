import java.util.List;

public class MissingNumInArr {
  public static List<Integer> findDisappearedNumbers(int[] nums) {
    int n = nums.length;
    for (int i = 0; i < n; i++) {
      int index = Math.abs(nums[i]) - 1;
      if (nums[index] > 0) {
        nums[index] = -nums[index];
      }
    }
    List<Integer> result = new java.util.ArrayList<>();
    for (int i = 0; i < n; i++) {
      if (nums[i] > 0) {
        result.add(i + 1);
      }
    }
    return result;
  }

  public static void main(String[] args) {
    int[] nums = {4, 3, 2, 7, 8, 2, 3, 1};
    List<Integer> missingNumbers = findDisappearedNumbers(nums);
    System.out.println("Missing numbers: " + missingNumbers);
  }

}
