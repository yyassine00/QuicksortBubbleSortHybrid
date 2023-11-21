import Sort 
import matplotlib.pyplot as plt


arr1 = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
sorted_arr2 = Sort.quick_sort(arr1)
print(sorted_arr2)

arr2 = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
sorted_arr2 = Sort.bubble_sort(arr2)
print(sorted_arr2)


with open('rand1000000.txt')as f:
    arr = [int(num) for line in f for num in line.split()]



# test different values of k
ks = [10, 30, 50, 70, 90, 110, 130, 150, 170, 190]
times = []
for k in ks:
    t = Sort.time_sort(lambda x: Sort.hybrid_sort(x, k), arr)
    times.append(t)
    print(f"k={k}: {t:.2f} seconds")

# plot the times as a function of k
plt.plot(ks, times)
plt.xlabel('k')
plt.ylabel('Time (seconds)')
plt.title('Hybrid Sort Performance')
plt.show()
