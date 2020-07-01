#There are two sorted arrays nums1 and nums2. Write a method to find and return the median of the two sorted arrays. (The median is the middle element of an odd-sized array, or the average of the middle elements of an even-sized array.) You may assume nums1 and nums2 cannot be both empty.
 #Example 1:	Example 2:
 #nums1 = [1, 3]	nums1 = [1, 2]
 #nums2 = [2]	nums2 = [3, 4]
 #The median is 2.0	The median is (2 + 3)/2 = 2.5

def medAvg(nums1, nums2):
    total1 = 0
    total2 = 0
    for i in range(len(nums1)):
        total1 += nums1[i]
    for j in range(len(nums2)):
        total2 += nums2[j]
    avg1 = total1/len(nums1)
    avg2 = total2/len(nums2)
    
    return (avg1 + avg2)/2

nums1 = [1, 2]
nums2 = [3, 4]
print(medAvg(nums1, nums2))
