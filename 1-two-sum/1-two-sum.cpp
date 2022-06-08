class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        map<int, int> data;
        data[nums[0]] = 0;
        vector<int> output;
        for (int i = 1; i < nums.size(); i++) {
            if (data.find(target - nums[i]) != data.end()) {
                output.push_back(data[target - nums[i]]);
                output.push_back(i);
                break;
            }
            data[nums[i]] = i;
        }
        return output;
    }
};