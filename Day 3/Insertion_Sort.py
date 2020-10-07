class insertion_sort():
    def __init__(self,arr):
        self.arr = arr
    def sort(self):
        for i in range(1,len(self.arr)):
            j = i
            while j > 0:
                if self.arr[j] < self.arr[j-1]:
                    self.arr[j], self.arr[j-1] = self.arr[j-1], self.arr[j]
                    j -= 1
                else:
                    break
        return self.arr
        
print('Enter a array:')
arr = list(map(int,input().split()))
sorter = insertion_sort(arr)
arr = sorter.sort()
print('\nSorted array:')
for i in arr: print(i,end = ' ')
