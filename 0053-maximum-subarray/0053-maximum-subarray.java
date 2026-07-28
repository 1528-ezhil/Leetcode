class Solution {
    public int maxSubArray(int[] nums){

        int currentSum=0;
        int currentMax=nums[0];

        for(int i=0;i<nums.length;i++){
            currentSum=currentSum+nums[i];
        

        if(currentSum>currentMax){
            currentMax=currentSum;
        }

        if(currentSum<0){
            currentSum=0;
        }
        }

        return currentMax;
        
    }
}