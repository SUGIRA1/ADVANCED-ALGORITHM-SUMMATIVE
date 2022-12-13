def countPairsWithsamediff(arr, n, k):
	count = 0

	for i in range(0, n):
		
		# See if there is a pair of this picked element
    
		for j in range(i+1, n) :
      
			#int k: an integer, the target difference
			#int arr[n]: an array of integers

			if arr[i] - arr[j] == k or arr[j] - arr[i] == k:
				count += 1
				
	return count
arr = [1, 2, 3, 4]
n = len(arr)
k = 1
print (f"Count of  pairs of array {arr} that have a difference equal to the target value of {k} is ",
       countPairsWithsamediff(arr, n, k))
