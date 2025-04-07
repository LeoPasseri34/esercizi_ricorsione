def quicksort(sequenza):
    if len(sequenza) == 1:
        return sequenza
    else:
        # 1- scegliere il pivot
        pivot = sequenza[0]
        # 2 - dividere sequenza in sottosequenze
        sequenza_small = []
        sequenza_large = []
        sequenza_pivot = []
        for i in sequenza:
            if i < pivot:
                sequenza_small.append(i)
            elif i > pivot:
                sequenza_large.append(i)
            else:
                sequenza_pivot.append(i)
        return quicksort(sequenza_small) + sequenza_pivot + quicksort(sequenza_large)


if __name__ == '__main__':
    sequenza = [3, 5, 2, 9, 11, 4, 7]
    print(quicksort(sequenza))