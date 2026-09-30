class Solution {
   public:
    int removeElement(vector<int>& nums, int val) {
        int fast = 0;
        int slow = 0;
        while (fast < nums.size()) {
            if (nums[fast] == val) {
                fast++;
                continue;
            }
            if (nums[slow] == val) {
                int temp = nums[fast];
                nums[fast] = nums[slow];
                nums[slow] = temp;
            }
            slow++;
            fast++;
        }
        return slow;
    }
};