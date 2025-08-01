import os
# Custom pseudorandom number generator with a random initial seed
class PRNG:
    def __init__(self, seed=None):
        # Use a truly random seed if no seed is provided
        if seed is None:
            seed = int.from_bytes(os.urandom(4), 'big')  # Generate a random 32-bit integer
        self.state = seed

    def randint(self, low, high):
        # Simple linear congruential generator (LCG)
        self.state = (1103515245 * self.state + 12345) % (2**31)
        return low + (self.state % (high - low + 1))
#####

# Generate logistics dataset
def generate_logistics_dataset(num_warehouses=100, max_packages=1000, seed=None):
    """Generates a logistics dataset with a random or specified seed."""
    prng = PRNG(seed)  # Initialize PRNG with the seed or a random one
    data = []
    for i in range(1, num_warehouses + 1):
        warehouse_id = f"WH-{str(i).zfill(3)}"
        priority_level = prng.randint(1, 5)
        package_count = prng.randint(0, max_packages)
        data.append([warehouse_id, priority_level, package_count])
    return data

# Save dataset to a CSV file
def save_to_csv(data, file_name):
    """Saves the dataset to a CSV file."""
    with open(file_name, "w") as file:
        # Write the header
        file.write("Warehouse_ID,Priority_Level,Package_Count\n")
        # Write each row
        for row in data:
            file.write(",".join(map(str, row)) + "\n")


######### YOUR CODE GOES HERE ---  You should define here two_level_sorting and the 3 sorting functions

### Your three sorting functions should have global variable named as counter. So do not return it.
# Bubble Sort function
# It sorts an array by repeatedly swapping adjacent elements if they are in the wrong order
def bubble_sort(array):
    global counter
    if len(array) == 1:  # Base case: if the array has only one element, return it
        return array
    for pass_num in range(len(array) - 1, 0, -1):  # Iterate through the array for each pass
        for i in range(pass_num):  # Compare adjacent elements
            counter += 1  # Increment comparison counter
            if array[i] > array[i + 1]:  # Swap if elements are in the wrong order
                temp = array[i]
                array[i] = array[i + 1]
                array[i + 1] = temp
    return array

# Merge Sort function
# It divides the array into two halves, sorts each half, and then merges them
def merge_sort(array):
    # Helper function to merge two sorted arrays
    def merge(array1, array2):
        global counter
        c = []  # List to store merged elements
        while len(array1) != 0 and len(array2) != 0:  # Merge while both arrays have elements
            if array1[0] > array2[0]:  # Compare the first elements
                counter += 1  # Increment comparison counter
                c.append(array2.pop(0))  # Append the smaller element
            else:
                c.append(array1.pop(0))
        while len(array1) != 0:  # Append remaining elements from array1
            c.append(array1.pop(0))
        while len(array2) != 0:  # Append remaining elements from array2
            c.append(array2.pop(0))
        return c

    n = len(array)
    if n == 1:  # Base case: if the array has only one element, return it
        return array
    array1 = []
    array2 = []
    # Split the array into two halves
    for i in range(n // 2):
        array1.append(array[i])
    for i in range(n // 2, n):
        array2.append(array[i])
    # Recursively sort both halves and merge them
    array1 = merge_sort(array1)
    array2 = merge_sort(array2)
    return merge(array1, array2)

# Quick Sort function
# It selects a pivot element, partitions the array, and recursively sorts each part
def quick_sort(array):
    global counter
    if len(array) == 1:  # Base case: if the array has only one element, return it
        return array
    counter += 1  # Increment comparison counter
    pivot = array[len(array) // 2]  # Choose the middle element as the pivot
    array.remove(pivot)  # Remove the pivot from the array
    smaller = []  # Elements smaller than the pivot
    larger = []  # Elements larger than the pivot
    pivots = [pivot]  # List to store pivot(s) (handling duplicates)

    # Partition the array into smaller, larger, and pivot lists
    for i in range(len(array)):
        if array[i] < pivot:
            smaller.append(array[i])
        elif array[i] > pivot:
            larger.append(array[i])
        else:
            pivots.append(array[i])

    # Recursively sort the smaller and larger lists
    if len(smaller) > 0:
        smaller = quick_sort(smaller)
    if len(larger) > 0:
        larger = quick_sort(larger)

    # Return the combined sorted list
    return smaller + pivots + larger

# Two-level sorting function
# It performs two-level sorting on a dataset using the given sort type
def two_level_sorting(sort_type, dataset):
    global counter
    counter = 0
    # Check if the dataset has only one element
    if len(dataset) == 1:
        print('You entered 1 element in database!')
        return dataset, 0, 0
    # Check for duplicate entries in the dataset
    elif len(dataset) != len(set(map(tuple, dataset))):
        print('There are duplicated elements in the database!')
        return dataset, 0, 0
    else:
        pl_array = []  # Array to store priority levels
        for row in dataset:
            pl_array.append(row[1])
        # Sort the priority levels using the specified sort type
        sorted_pl_array = sort_type(pl_array)
        pl_count_num = counter  # Save the counter value for priority level sorting

        pl_sorted_dataset = []  # Sorted dataset based on priority levels
        # Rebuild the dataset according to the sorted priority levels
        for pl in sorted_pl_array:
            for row in dataset:
                if row[1] == pl and row not in pl_sorted_dataset:
                    pl_sorted_dataset.append(row)

        sorted_dataset = []  # Final sorted dataset
        equal_group = []  # Group of rows with the same priority level
        pc_count_num = 0  # Counter for packet count sorting

        # Perform second-level sorting based on packet counts within each priority group
        for i in range(len(pl_sorted_dataset)):
            equal_group.append(pl_sorted_dataset[i])
            if i == len(pl_sorted_dataset) - 1 or pl_sorted_dataset[i][1] != pl_sorted_dataset[i + 1][1]:
                pc_array = []  # Array to store packet counts
                for row in equal_group:
                    pc_array.append(row[2])
                counter = 0
                # Sort the packet counts using the specified sort type
                sorted_pc_array = sort_type(pc_array)
                pc_count_num += counter  # Add the counter value for packet count sorting

                # Rebuild the dataset according to the sorted packet counts
                for pc in sorted_pc_array:
                    for row in equal_group:
                        if row[2] == pc and row not in sorted_dataset:
                            sorted_dataset.append(row)

                equal_group = []  # Reset the group for the next priority level

        # Return the fully sorted dataset and the counters for both sorting levels
        return sorted_dataset, pl_count_num, pc_count_num
#########

def write_output_file(
    bubble_sorted, merge_sorted, quick_sorted,
    bubble_sort_pl_iterations, merge_sort_pl_counter, quick_sort_pl_counter,
    bubble_sort_pc_iterations, merge_sort_pc_counter, quick_sort_pc_counter,
    merge_check, quick_check
):
    """Write sorted results and comparisons to the output file."""
    with open(OUTPUT_FILE, 'w', encoding='utf-8') as file:
        file.write("=== Bubble Sorted Results ===\n")
        # file.write(bubble_sorted.to_string() + "\n\n")
        file.write("Warehouse_ID  Priority_Level  Package_Count\n")
        file.write("-" * 40 + "\n")
        for row in bubble_sorted:
            file.write(f"{row[0]:<12}  {row[1]:<14}  {row[2]:<13}\n")
        file.write("\n")
        file.write("=== Comparison Results ===\n")
        if merge_check:
            file.write("Merge and Bubble sorts are identical.\n")
        else:
            file.write("Merge and Bubble sorts differ.\n")
        
        if quick_check:
            file.write("Quick and Bubble sorts are identical.\n")
        else:
            file.write("Quick and Bubble sorts differ.\n")
        
        file.write("\n=== Sort Performance Metrics ===\n")
        file.write(f"Bubble priority sort iteration count: {bubble_sort_pl_iterations}\n")
        file.write(f"Merge priority sort n_of right array is smaller than left: {merge_sort_pl_counter}\n")
        file.write(f"Quick priority sort recursive step count: {quick_sort_pl_counter}\n\n")
        
        file.write(f"Bubble package count sort iteration count: {bubble_sort_pc_iterations}\n")
        file.write(f"Merge package count n_of right array is smaller than left: {merge_sort_pc_counter}\n")
        file.write(f"Quick package count sort recursive step count: {quick_sort_pc_counter}\n")
    
    print(f"Results written to {OUTPUT_FILE}")
    
if __name__ == "__main__":
    # File paths and dataset size
    # Specify paths for input and output files
    INPUT_FILE = "input.csv"   # Path where the generated dataset will be saved
    OUTPUT_FILE = "output.txt"  # Path where the sorted results and metrics will be saved
    SIZE = 100  # Number of warehouses in the dataset

    # Generate the dataset
    dataset = generate_logistics_dataset(SIZE, max_packages=100)  # Generate a dataset with SIZE warehouses and max_packages packages
    
    # Save the generated dataset to the input file
    save_to_csv(dataset,INPUT_FILE)
    
    ###############################################################################################################
    # Perform sorting and counting operations
    # Sort using Bubble Sort and count iterations for Priority Level (_pl_) and Package Count (_pc_)
    bubble_sorted, bubble_sort_pl_iterations, bubble_sort_pc_iterations = two_level_sorting(bubble_sort, dataset)
    
    # Sort using Merge Sort and count recursive steps for Priority Level and Package Count
    merge_sorted, merge_sort_pl_counter, merge_sort_pc_counter = two_level_sorting(merge_sort, dataset)
    
    # Sort using Quick Sort and count recursive steps for Priority Level and Package Count
    quick_sorted, quick_sort_pl_counter, quick_sort_pc_counter = two_level_sorting(quick_sort, dataset)
    ###############################################################################################################
    
    
    # Comparisons
    # Check if Merge Sort results match Bubble Sort results
    merge_check = merge_sorted == bubble_sorted

    # Check if Quick Sort results match Bubble Sort results
    quick_check = quick_sorted == bubble_sorted

    # Write results and metrics to the output file
    write_output_file(
        bubble_sorted, merge_sorted, quick_sorted,
        bubble_sort_pl_iterations, merge_sort_pl_counter, quick_sort_pl_counter,
        bubble_sort_pc_iterations, merge_sort_pc_counter, quick_sort_pc_counter,
        merge_check, quick_check
    )
