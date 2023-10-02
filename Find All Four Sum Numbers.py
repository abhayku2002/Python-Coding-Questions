'''
Given an array A of integers and another number K. Find all the unique quadruple from the given array that sums up to K.

Also note that all the quadruples which you return should be internally sorted, ie for any quadruple [q1, q2, q3, q4] the following should follow: q1 <= q2 <= q3 <= q4.
'''

#Python solution

        arr.sort()
        s=[]
        n=len(arr)
        for i in range(n-3):
            if i>0 and arr[i]==arr[i-1]:
                continue
            for j in range(i+1,n-2):
               if j>i+1 and arr[j]==arr[j-1]:
                   continue
               start=j+1;
               end=n-1;
               while(start<end):
                    newtarget=arr[i]+arr[j]+arr[start]+arr[end]
                    if newtarget==k:
                        s.append([arr[i],arr[j],arr[start],arr[end]])
                        while start<end and arr[start]==arr[start+1]:
                            start+=1
                        while start<end and arr[end]==arr[end-1]:
                            end-=1
                        start+=1
                        end-=1
                       elif newtarget<k:
                        start+=1
                    else:
                        end-=1
                
        return s
