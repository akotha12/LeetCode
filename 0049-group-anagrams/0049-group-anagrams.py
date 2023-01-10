class Solution(object):
    def groupAnagrams(self, strs):
        myMap = {}
        output = []
        for word in strs:
            var = copy.deepcopy(word)
            var = sorted(var)
            var = ''.join(var)
            if not myMap.has_key(var):
                myMap[var] = []
            myMap[var].append(word)
        for val in myMap.values():
            output.append(val)
        return output
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
          