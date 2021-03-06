/*
 * @lc app=leetcode id=1 lang=java
 *
 * [1] Two Sum
 *
 * https://leetcode.com/problems/two-sum/description/
 *
 * algorithms
 * Easy (40.11%)
 * Total Accepted:    1.4M
 * Total Submissions: 3.4M
 * Testcase Example:  '[2,7,11,15]\n9'
 *
 * Given an array of integers, return indices of the two numbers such that they
 * add up to a specific target.
 * 
 * You may assume that each input would have exactly one solution, and you may
 * not use the same element twice.
 * 
 * Example:
 * 
 * 
 * Given nums = [2, 7, 11, 15], target = 9,
 * 
 * Because nums[0] + nums[1] = 2 + 7 = 9,
 * return [0, 1].
 * 
 * 
 * 
 * 
 */
class Solution {
    public int[] twoSum(int[] nums, int target) {
        if(nums == null || nums.length < 2)
        return new int[] {0, 0};

        HashMap<Integer, Integer> hashmap = new HashMap<Integer, Integer>();
        for(int i = 0; i < nums.length; i++) {
            if(hashmap.containsKey(nums[i])) {
                return new int[] {hashmap.get(nums[i]), i};
            } else {
                hashmap.put(target-nums[i], i);
            }
        }
        return new int[] {0, 0};
    }
}
