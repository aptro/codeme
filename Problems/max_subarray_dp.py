#Dynamic programming

def max_subarray(l):
    current_sum =0
    current_index =-1
    best_sum = 0
    best_start_index =-1
    best_end_index = -1
    
    for i in xrange(len(l)):
        val = current_sum + l[i]
        if (val > 0):
            if current_sum == 0:
                current_index =i
            current_sum =val
        else:
            current_sum = 0
        if current_sum > best_sum:
            best_sum = current_sum
            best_start_index = current_index
            best_end_index = i
    return l[best_start_index:best_end_index+1]
    
print max_subarray([1, -2, 5, -3, 8, -7, -100, ])    
    
    
    
    
    
    
    
    
    
    