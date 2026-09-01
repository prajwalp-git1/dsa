import array

# Static array
static_arr =[0] * 3
static_arr[0] = 10
static_arr[1] = 20
static_arr[2] = 30
print("Static array:", static_arr)
try:
    static_arr[3] = 40  # This will raise an IndexError
except IndexError as e:
    print("Error:", e, "Cannot add more elements to a static array.")

# Dynamic array (list)
dynamic_arr = []
dynamic_arr.append(10)  
dynamic_arr.append(20)
dynamic_arr.append(30)
print("Dynamic array:", dynamic_arr)
dynamic_arr.append(40)  # This works fine
print("Dynamic array after adding an element:", dynamic_arr)
print("Length of dynamic array:", len(dynamic_arr))
