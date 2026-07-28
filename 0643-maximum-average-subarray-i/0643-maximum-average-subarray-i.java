class Solution {
    public double findMaxAverage(int[] nums, int k) {

        int gSum = 0;
        int cSum = 0;

        for (int i = 0; i <= nums.length - k; i++) {

            cSum = 0;

            for (int j = i; j < i + k; j++) {
            	
                cSum += nums[j];
            }

            if (i == 0 || cSum > gSum) {
                gSum = cSum;
            }
        }

        return (double) gSum/k;
        
    }
}