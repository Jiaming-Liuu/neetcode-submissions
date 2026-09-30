class Solution {
public:
    int maxArea(vector<int>& heights) {
        int left = 0, right = heights.size() - 1, res = 0;
        while (left < right) {
            res = std::max(res, std::min(heights[left], heights[right]) * (right - left));
            if (heights[left] > heights[right]) {
                right--;
            } else {
                left++;
            }
        }
        return res;
    }
};
