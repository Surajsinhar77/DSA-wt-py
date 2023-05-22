def merge(self,arr, f, mid, l):
        i = f
        j = mid+1
        n1 = mid
        n2 = l
        ans = []
        while(i<=n1 and j<=n2):
            if(arr[i] < arr[j]):
                ans.append(arr[i])
                i+=1
            else:
                ans.append(arr[j])
                j+=1
    
        while(i<=n1):
            ans.append(arr[i])
            i+=1
    
        while(j<=n2):
            ans.append(arr[j])
            j+=1
    
        k = 0
        for i in range(f, l+1):
            arr[i] = ans[k]
            k+=1
            
    def mergeSort(self,arr, f, l):
        if(f >= l):
            return
        
        mid = int((f+l)/2)
        self.mergeSort(arr, f ,mid)
        self.mergeSort(arr, mid+1, l)
        self.merge(arr, f , mid , l)