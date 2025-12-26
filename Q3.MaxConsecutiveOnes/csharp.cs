public class Solution {
    public int FindMaxConsecutiveOnes(int[] nums) {
        int c = 0;
        int c_aux = 0;
        foreach(var i in nums){
            if(i == 1){
                c++;
            } else {
                c = 0;
            }
            if (c_aux < c) c_aux = c; 
        }
        return c_aux;
    }
}