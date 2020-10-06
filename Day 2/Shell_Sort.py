class shellsort():
    def __init__(self,arr):
        self.a = arr

    def sort(self):
        n = len(self.a)
        gap = n//2
        while gap>0:
            for i in range(gap,n):
                val = self.a[i]
                pos = i

                while pos>=gap and val<self.a[pos-gap]:
                    self.a[pos] = self.a[pos-gap]
                    pos -= gap
                self.a[pos] = val
            gap = gap//2
        return self.a

arr = list(map(int,input('Enter an array: ').split()))
sorter = shellsort(arr)
arr = sorter.sort()
for i in arr: print(i,end=' ')
