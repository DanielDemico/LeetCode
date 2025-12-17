public class Solution {
    public int[] TwoSum(int[] nums, int target) {
        
        List<int> correct_itens = new List<int>();

        int head = 0;
        int tail = 1;
        while(true){
            if(tail >= nums.Length){
                    head++;
                    tail = head + 1;
                } 
            if(nums[head] + nums[tail] == target){
                return new int[] {head, tail};
            } 
            tail++;
        }
        return new int[0];
    }
}