class Solution {
public:
    int removeElement(vector<int>& nums, int val) {
        int size = nums.size();
        for (int i = 0; i < size; i++) {
            while (nums[i] == val) {
                nums[i] = val - 1;
                swap(nums[i], nums[size - 1]);
                size -= 1;
            }
        }
        return size;
    }
};