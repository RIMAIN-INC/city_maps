
import random

#function to partition a list
def partition(the_list,p,r,compare_func):

    i = random.randint(p,r) #random index between first and last index of a list
    the_list[i],the_list[r] = the_list[r], the_list[i] #swap item at random index with last item in the list

    pivot = the_list[r] # assigns pivot to the last index item of sublist

    i = p - 1
    j = p
    while j < r: #loop function to compare all items to pivot
        if compare_func(the_list[j], pivot):
            i += 1
            the_list[i], the_list[j] = the_list[j], the_list[i] #swaps items in the sublist
            j += 1
        else:
            j += 1

    the_list[i+1], the_list[r] = the_list[r], the_list[i+1] #swaps the pivot to it intend position
    return i + 1 #returns the pivot index


#quicksort function
def quicksort(the_list,p,r,compare_func):

    if p < r: #base case when left > right or left == right
        q = partition(the_list,p,r,compare_func) #partition and get index
        quicksort(the_list,p,q-1,compare_func)
        quicksort(the_list,q+1,r,compare_func)


def sort(the_list,compare_func):
    left = 0
    right = len(the_list) - 1
    quicksort(the_list,left,right,compare_func)
    return the_list
