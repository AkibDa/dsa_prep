class Solution {
    public int[] Two_sum(int[] nums, int target) {
        int i=0;
        int j=nums.length-1;
        while(i<j){
            int sum=nums[i]+nums[j];
            if(sum==target){
                return new int[]{i+1,j+1};
            } else {
                i++;
                j--;
            }
        }
        return null;

    }
}