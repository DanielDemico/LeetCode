public class Solution {
    public int[] Shuffle(int[] nums, int n) {
        
        List<int> Xs = nums.Take(n).ToList();
        List<int> Ys = nums.Skip(n).ToList(); 

        List<int> newList = new List<int>();

        for (int i = 0; i < n; i++){
            newList.Add(Xs[i]);
            newList.Add(Ys[i]);
        }
        return newList.ToArray();
        }
}