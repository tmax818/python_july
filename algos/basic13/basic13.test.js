
const {print1to255, printOdds1to255, printIntsAndSum0To255, printArrayVals, printMaxOfArray, printAverageOfArray, returnArrayCountGreaterThanY, returnOddsArray1to255, squareArrayVals, zeroOutArrayNegativeVals, printMaxMinAverageArrayVals, shiftArrayValsLeft, swapStringForArrayNegativeVals} = require('.')


describe('Basic 13', () => {
    
    beforeEach(()=> {
        // create a function into global context for Jest
        global.console = {
            log: jest.fn()
          }
    })

    describe("print1to255", () => {
        it('should print all the integers from 1 to 255.', () => {
            print1to255()
            number = Math.floor(Math.random() * 255)
            expect(global.console.log).toHaveBeenCalledWith(number)
        })
        it('should not print zero', () => {
            print1to255()
            expect(global.console.log).not.toHaveBeenCalledWith(0)
        })
        it('should not print 256', () => {
            print1to255()
            expect(global.console.log).not.toHaveBeenCalledWith(256)

        })
    })
    
    describe("printIntsAndSum0To255", () => {
        it('should print the numbers', () => {
            printIntsAndSum0To255()
            let number = Math.floor(Math.random() * 255)
            expect(global.console.log).toHaveBeenCalledWith(number)
        })
        it('should print zero', () => {
            printIntsAndSum0To255()
            expect(global.console.log).toHaveBeenCalledWith(0)

        })
        it('should print the final sum', () => {
            printIntsAndSum0To255()
            expect(global.console.log).toHaveBeenCalledWith(32640)
        })
    })

    describe("printMaxOfArray", () => {
        it("prints the largest element of a given array", () => {
            const arr1 = [4, 5, 65, 42, 2]
            printMaxOfArray(arr1)
            expect(global.console.log).toHaveBeenCalledWith(65)
        })
    })

    describe("returnOddsArray1to255", () => {
        it("returns an array of the odd integers between 1 and 255", () => {
            const arr1 = [13,23,36,44,57]
            expect(returnOddsArray1to255()).toContain(253)
            expect(returnOddsArray1to255()).not.toContain(252)
        })
    })

    describe("returnArrayCountGreaterThanY", () => {
        it("prints and counts of the values of an array greater than a given number", () => {
            const arr1 = [13,23,36,44,57]
            returnArrayCountGreaterThanY(arr1, 13)
            expect(global.console.log).toHaveBeenCalledWith(57)
            expect(global.console.log).toHaveBeenCalledWith(4)
        })
    })

    describe("printMaxMinAverageArrayVals", () => {
        it('should print the max, min and average values for a given array', () => {
            const arr1 = [13,23,36,44,57]
            printMaxMinAverageArrayVals(arr1)
            expect(global.console.log).toHaveBeenCalledWith(13)
            expect(global.console.log).toHaveBeenCalledWith(57)
            expect(global.console.log).toHaveBeenCalledWith(34.6)
        })
    })

    describe("swapStringForArrayNegativeVals", () => {
        it("Swaps negative values in an array for the string 'Dojo'.", () => {
            const arr1 = [13,23,-36,44,-57]
            swapStringForArrayNegativeVals(arr1)
            expect(swapStringForArrayNegativeVals(arr1)).toContain('Dojo')
            expect(swapStringForArrayNegativeVals(arr1)).not.toContain(-36)
            expect(swapStringForArrayNegativeVals(arr1)).toBe(arr1)
        })
    })

    describe("printOdds1to255", () => {
        it('should print the odd numbers', () => {
            printOdds1to255()
            let number = Math.floor(Math.random() * 255)
            number % 2 === 0 ? number+=1 : number
            expect(global.console.log).toHaveBeenCalledWith(number)
            expect(global.console.log).not.toHaveBeenCalledWith(number + 1)
            expect(global.console.log).not.toHaveBeenCalledWith(256)
            expect(global.console.log).not.toHaveBeenCalledWith(0)
        })
    })

    describe("printArrayVals", () => {
        it("prints each element of a given array", () => {
            const arr1 = [4, 5, 65, 42, 2]
            printArrayVals(arr1)
            expect(global.console.log).toHaveBeenCalledTimes(arr1.length)
            expect(global.console.log).toHaveBeenCalledWith(arr1[arr1.length - 1])
            expect(global.console.log).toHaveBeenCalledWith(65)
        })
    })

    describe("printAverageOfArray", () => {
        it("prints the average of a given array of numbers", () => {
            const arr1 = [13,23,36,44,57]
            printAverageOfArray(arr1)
            expect(global.console.log).toHaveBeenCalledWith(34.6)
        })
    })
    
    describe("squareArrayVals", () => {
        it("returns an array with each value squared", () => {
            const arr1 = [4,23,36,44,57]
            expect(squareArrayVals(arr1)).toContain(16)
            expect(squareArrayVals(arr1)).toBe(arr1)
        })
    })
    
    describe("zeroOutArrayNegativeVals", () => {
        it("Swaps negative values with zero.", () => {
            const arr1 = [13,23,-36,44,-57]
            zeroOutArrayNegativeVals(arr1)
            expect(zeroOutArrayNegativeVals(arr1)).toContainEqual(13,23,0,44,0)
            expect(zeroOutArrayNegativeVals(arr1)).not.toContain(-36)
            expect(zeroOutArrayNegativeVals(arr1)).toBe(arr1)
        })
    })

    describe("shiftArrayValsLeft", () => {
        it("Shifts values in a given array to the left", () => {
            const arr1 = [1,2,3,4,5]
            expect(shiftArrayValsLeft(arr1)).toContainEqual(2,3,4,5,0)
        })
    })
  })