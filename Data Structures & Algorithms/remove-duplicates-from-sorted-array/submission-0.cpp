class Solution {
public:
    int removeDuplicates(vector<int>& nums) {
        int k = 0;
        for (int index = 1; index < nums.size(); index++) {
            if (nums[index] != nums[index - 1]) {
                k++;
                nums[k] = nums[index];
            }
        }
        return k + 1;
    }
};