
# Logistics Dataset Sorter

This project generates a random logistics dataset and performs two-level sorting using three different sorting algorithms: **Bubble Sort**, **Merge Sort**, and **Quick Sort**. It compares their performance in terms of sorting operations.

## Features

- Random logistics dataset generation
- Two-level sorting:
  - **Level 1:** Priority Level
  - **Level 2:** Package Count
- Sorting algorithm implementations:
  - Bubble Sort
  - Merge Sort
  - Quick Sort
- Performance comparison via iteration and recursion counts
- Outputs written to file

## Requirements

- Python 3.x
- No additional libraries required

## How to Run

1. Run the script `477dd2da-979d-489a-943c-16d63b1374d0.py`:

```bash
python 477dd2da-979d-489a-943c-16d63b1374d0.py
```

2. The script will generate the following files:
   - `hw05_input.csv`: The generated logistics dataset.
   - `hw05_output.txt`: Sorted results and performance metrics for each algorithm.

## Key Components

### `generate_logistics_dataset`
Generates a list of warehouses with random:
- `Warehouse_ID` (e.g., WH-001)
- `Priority_Level` (1 to 5)
- `Package_Count` (0 to 1000)

### `two_level_sorting(sort_type, dataset)`
Sorts the dataset using a two-level approach:
1. By `Priority_Level`
2. Then by `Package_Count` within the same priority group

The sorting algorithm is passed as a parameter and the number of operations is counted using a global `counter`.

### Sorting Functions
- `bubble_sort(array)`
- `merge_sort(array)`
- `quick_sort(array)`

Each function tracks the number of operations (`counter`) for performance comparison.

### `write_output_file(...)`
Writes:
- Bubble Sorted result
- Comparison results with Merge and Quick Sort
- Performance metrics of all sorting methods

## Output Example

The `hw05_output.txt` file includes:
- Formatted sorted results (by Bubble Sort)
- Checks if Merge/Quick Sorts produced identical results
- Comparison counts for each sorting level and algorithm

## License

This project is provided for educational purposes and is not licensed under any particular terms.
