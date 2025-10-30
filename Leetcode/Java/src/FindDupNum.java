public class FindDupNum {
  public static int findDuplicate(int[] nums) {
    while(nums[0] != nums[nums[0]]) {
      int next = nums[nums[0]];
      nums[nums[0]] = nums[0];
      nums[0] = next;
    }
  return nums[0];
  }

  public static void main(String[] args) {
    int[] nums = {1, 3, 4, 2, 2};
    System.out.println("The duplicate number is: " + findDuplicate(nums)); // Output: 2
  }

}
