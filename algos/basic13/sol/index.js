// Print all the integers from 1 to 255
function print1to255(){
    for(let i = 1; i < 256; i++){
        console.log(i)
    }
}
// print1to255()

// Print all odd integers from 1 to 255
function printOdds1to255(){
    for(let i = 1; i < 256; i++){
        if(i % 2 != 0){            
            console.log(i)
        }
    }
}
// printOdds1to255()

// Print integers from 0 to 255 and with each integer print the sum so far
function printIntsAndSum0To255(){
    let sum = 0;
    for(let i = 0; i < 256; i++){
        sum += i
        console.log(i)
        console.log(sum)
    }
}

// Given an array, find and print its largest element
function printArrayVals(arr){
    for(let i = 0; i < arr.length; i++){
        console.log(arr[i])
    }
}

function printMaxOfArray(arr){
    let largest = 0;
    for(let i = 0; i < arr.length; i++){
        if(arr[i] > largest){
            largest = arr[i]
        }
    }
    console.log(largest)
}

function printAverageOfArray(arr){
    let sum = 0;
    for(let i = 0; i < arr.length; i++){
        sum += arr[i]
    }
    console.log(sum/arr.length)
}

printAverageOfArray([13,23,36,44,57])

function returnOddsArray1to255(){
    const newArr = []
    for(let i = 1; i < 256; i++){
        if(i % 2 != 0){            
            newArr.push(i)
        }
    }
    return newArr
}

function squareArrayVals(arr){
    for(let i = 0; i < arr.length; i++){
        arr[i] = arr[i] * arr[i]
    }
    return arr
}


function returnArrayCountGreaterThanY(arr, y){
    let count = 0
    for(let i = 0; i < arr.length; i++){
        if(arr[i] > y){
            count += 1
            console.log(arr[i])
        }
    }
    console.log(count)
}

function zeroOutArrayNegativeVals(arr){
    for(let i = 0; i < arr.length; i++){
        if(arr[i] < 0){
            arr[i] = 0
        }
    }
    return arr
}

function printMaxMinAverageArrayVals(arr){
    printAverageOfArray(arr)
    printMaxOfArray(arr)
    let min = arr[0];
    for(let i = 0; i < arr.length; i++){
        if(arr[i] < min){
            min = arr[i]
        }
    }
    console.log(min)
}

function shiftArrayValsLeft(arr){
    for(let i = 0; i < arr.length; i++){
        arr[i] = arr[i + 1]
    }
    arr[arr.length -1] = 0
    return arr
}
console.log(shiftArrayValsLeft([1,2,3,4,5]))

function swapStringForArrayNegativeVals(arr){
    for(let i = 0; i < arr.length; i++){
        if(arr[i] < 0){
            arr[i] = 'Dojo'
        }
    }
    return arr
}



// printIntsAndSum0To255()
module.exports = {print1to255, printOdds1to255, printIntsAndSum0To255, printArrayVals, printMaxOfArray, printAverageOfArray, returnArrayCountGreaterThanY, returnOddsArray1to255, squareArrayVals, zeroOutArrayNegativeVals, printMaxMinAverageArrayVals, shiftArrayValsLeft, swapStringForArrayNegativeVals}