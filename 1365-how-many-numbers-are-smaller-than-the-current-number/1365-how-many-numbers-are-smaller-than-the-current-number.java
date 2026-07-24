import java.util.*;

class Solution {
    public int[] smallerNumbersThanCurrent(int[] nums) {

        ArrayList<Integer> list = new ArrayList<>();

        for (int num : nums) {
            list.add(num);
        }

        Collections.sort(list);

        int[] ans = new int[nums.length];

        for (int i = 0; i < nums.length; i++) {
            ans[i] = list.indexOf(nums[i]);
        }

        return ans;
    }
}