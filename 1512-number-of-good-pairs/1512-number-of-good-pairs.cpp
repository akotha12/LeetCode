class Solution {
public:
    int numIdenticalPairs(vector<int>& nums) {
        sort(nums.begin(), nums.end());
        int temp = nums[0];
        int count = 1;
        int output = 0;
        for (int i = 1; i < nums.size(); i++) {
            if (temp != nums[i]) {
                if (count >= 2) {
                    output += 0.5 * (count) * (count - 1);
                }
                temp = nums[i];
                count = 0;
            }
            count++;
        }        
        if (count >= 2) {
            output += 0.5 * (count) * (count - 1);
        }
        return output;
    }
};