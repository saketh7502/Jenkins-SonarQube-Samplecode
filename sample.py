def main():
    # Creating an array
    my_array = [1, 2, 3, 4, 5]

    # Accessing elements of the array
    print("Array elements:")
    for element in my_array:
        print(element)

    # Modifying elements of the array
    my_array[2] = 10
    print("\nModified array:")
    print(my_array)

    # Appending elements to the array
    my_array.append(6)
    print("\nArray after appending an element:")
    print(my_array)

    # Removing elements from the array
    removed_element = my_array.pop(1)
    print(f"\nRemoved element: {removed_element}")
    print("Array after removing an element:")
    print(my_array)

    # Slicing arrays
    sliced_array = my_array[1:4]
    print("\nSliced array:")
    print(sliced_array)

if __name__ == "__main__":
    main()
