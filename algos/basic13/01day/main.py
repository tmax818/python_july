
## TODO: Print all the integers from 1 to 255.
# def print1to255():
#     for i in range(1, 256):
#         print(i)

# print1to255()
## TODO: Print integers from 0 to 255, and with each integer print the sum so far.
# def printIntsAndSum0To255():
#     sum = 0
#     for i in range(256):
#         sum += i
#         print(sum)

# printIntsAndSum0To255()


## TODO: Given an array, find and print its largest element.
# def printMaxOfArray(arr):
#     # print(max(arr))
#     max = arr[0]
#     for num in arr:
#         if max < num:
#             max = num
#     print(max)

# printMaxOfArray([1,3,5, 78, 4, 2])

## TODO: Create an array with all the odd integers between 1 and 255 (inclusive).
# def returnOddsArray1to255():
#     for i in range(1, 256):
#         if i % 2 == 1:
#             print(i)

# returnOddsArray1to255()

## TODO: Given an array and a value Y, count and print the number of array values greater than Y.
def returnArrayCountGreaterThanY(arr, y):
    count = 0
    for num in arr:
        if num > y:
            print(num)
            count += 1
    print(count)

returnArrayCountGreaterThanY([1,2,3,4,5,6], 3)

## TODO: Given an array, print the max, min and average values for that array.
def printMaxMinAverageArrayVals(arr):
    pass


## TODO: Replace any negative array values with 'Dojo'.
def swapStringForArrayNegativeVals(arr):
    pass

## TODO: Print all odd integers from 1 to 255.
def printOdds1to255():
    pass

## TODO: Iterate through a given array, printing each value.
def printArrayVals(arr):
    pass

## TODO: Analyze an array’s values and print the average
def printAverageOfArray(arr):
    pass

## TODO: Square each value in a given array, returning that same array with changed values
def squareArrayVals(arr):
    pass

## TODO: Return the given array, after setting any negative values to zero.
def zeroOutArrayNegativeVals(arr):
    pass

## TODO: Given an array, move all values forward by one index, dropping the first and leaving a '0' value at the end.
def shiftArrayValsLeft(arr):
    pass


