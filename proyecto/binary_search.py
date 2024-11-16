import random

def binary_search(data, target, low, high):
    if low > high:
        return False

    mid = (low + high) // 2  # mid valor del medio

    if target == data[mid]:
        return True
    elif target < data[mid]:
        return binary_search(data, target, low, mid - 1)
    else:
        return binary_search(data, target, mid + 1, high)

if __name__ == '__main__':
    data = [random.randint(0, 100) for i in range(10)]
    data.sort()
    print("Data:", data)

    target = int(input("Ingrese el número a buscar: "))
    found = binary_search(data, target, 0, len(data) - 1)
    
    if found:
        print(f"El número {target} se encuentra en la lista.")
    else:
        print(f"El número {target} no se encuentra en la lista.")


