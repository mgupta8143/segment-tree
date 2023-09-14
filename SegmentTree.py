class SegmentTree:
    def __init__(self, arr):
        if len(arr) <= 0:
            raise IndexError("Array has to be greater than length 0.")
        self.range = len(arr)
        self.tree = [0] * (len(arr) * 3 + 2)
        self.__construct_tree(arr, 0, len(arr))

    # L is inclusive, r is exclusive
    def __construct_tree(self, arr, l, r, i = 1):
        if r - l <= 1:
            self.tree[i] = arr[l]
            return arr[l]

        m = (l + r) // 2
        self.tree[i] = self.__construct_tree(arr, l, m, 2 * i) + \
                       self.__construct_tree(arr, m, r, 2 * i + 1)
        return self.tree[i]
    
    def update(self, j, val):
        if j < 0 or j >= self.range:
            raise IndexError("Index has to be in a valid range.")
        self.__update_helper(j, val, 0, self.range)

    def __update_helper(self, j, val, l, r, i = 1):
        if r - l <= 1:
            diff = val - self.tree[i]
            self.tree[i] = val 
            return diff
        
        m = (l + r) // 2
        if j < m:
            diff = self.__update_helper(j, val, l, m, 2 * i)
        else:
            diff = self.__update_helper(j, val, m, r, 2 * i + 1)
        
        self.tree[i] += diff
        return diff 

    # l is inclsuve, r is exclusive
    def get(self, range_l, range_r):
        if range_l < 0 or range_l >= self.range:
            raise IndexError("Index has to be in a valid range.")
        if range_r < 0 or range_r > self.range: 
            raise IndexError("Index has to be in a valid range.")
        if range_l >= range_r:
            raise IndexError("Range has to be bigger than one.")
        return self.__get_helper(range_l, range_r, 0, self.range)

    
    def __get_helper(self, range_l, range_r, l, r, i = 1):
        if l == range_l and r == range_r:
            return self.tree[i]
        
        m = (l + r) // 2
        if range_r <= m:
            return self.__get_helper(range_l, range_r, l, m, 2 * i)
        elif range_l >= m:
            return self.__get_helper(range_l, range_r, m, r, 2 * i + 1)
        else:
            return self.__get_helper(range_l, m, l, m, 2 * i) + \
                   self.__get_helper(m, range_r, m, r, 2 * i  + 1)

arr = [1, 2, 3, 4, 5, 6, 7, 8]
st = SegmentTree(arr)
print(st.tree)
print(st.get(2, 6))
st.update(0, 2)
st.update(3, 9)
print(st.get(3, 7))

print(st.tree)
