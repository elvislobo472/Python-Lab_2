
from module_ListFunc import max_1, min_1, calc_sum, comp_avg, med

int_list = [x for x in range(1, 21)]  

float_list = [x * 0.5 for x in range(1, 16)] 


neg_list = [x for x in range(-8, 6)]


empty_list = []



print("Integer List:", int_list)
print("Max:", max_1(int_list))
print("Min:", min_1(int_list))
print("Sum:", calc_sum(int_list))
print("Average:", comp_avg(int_list))
print("Median:", med(int_list))


print("\nFloating-point List:", float_list)
print("Max:", max_1(float_list))
print("Min:", min_1(float_list))
print("Sum:", calc_sum(float_list))
print("Average:", comp_avg(float_list))
print("Median:", med(float_list))


print("\nNegative Numbers List:", neg_list)
print("Max:", max_1(neg_list))
print("Min:", min_1(neg_list))
print("Sum:", calc_sum(neg_list))
print("Average:", comp_avg(neg_list))
print("Median:", med(neg_list))


print("\nEmpty List:", empty_list)
try:
    print("Max:", max_1(empty_list))
except ValueError as e:
    print("Error:", e)

try:
    print("Min:", min_1(empty_list))
except ValueError as e:
    print("Error:", e)

print("Sum:", calc_sum(empty_list)) 
try:
    print("Average:", comp_avg(empty_list))
except ValueError as e:
    print("Error:", e)

try:
    print("Median:", med(empty_list))
except ValueError as e:
    print("Error:", e)
