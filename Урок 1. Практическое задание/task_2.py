def get_min(num_list):               # O(N)
  min = num_list[0]                  # O(1)
  for i in range(len(num_list) - 1): # O(N)
    if min > num_list[i+1]:          # O(1) 
      min = num_list[i+1]            # O(1)
  return(min)

def get_min_O2(num_list):              # O(N^2)
  min = num_list[0]                    # O(1)
  for i in range(len(num_list) - 1):   # O(N)
    for j in range(len(num_list) - 1): # O(N)
      if (num_list[j] < num_list[i]):  # O(1)
        min = num_list[j]              # O(1)
    return(min)                        # O(1)

#get_min([-20,3,5,9,1,-55,5])
#get_min_O2([-200,3,5,9,1,-55,5])