/*
Sum Square Difference

The sum of the squares of the first ten natural numbers is,

      1^2 + 2^2 + ... + 10^2 = 385.

The square of the sum of the first ten natural numbers is,

      (1 + 2 + ... + 10)^2 = 55^2 = 3025.

Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is 

      3025 - 385 = 2640.

Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.

*/

const sumSquareDiff = limit => {

      // create an array of natural numbers up to limit
      const array = []
      for (let i = 1; i <= limit; i++) {
            array.push(+i)
      }

      // calculate sum of the squares 
      const sumOfSquares = array.reduce((arg, num) => {
            return arg += num * num
      }, 0)

      // calculate square of the sum
      const sum = array.reduce((arg, num) => {
            return arg += num
      }, 0)

      const squareOfSum = sum * sum

      // calculate difference
      const difference = squareOfSum - sumOfSquares
      
      // return difference
      return difference

}

console.log("Answer to problem 6: ", sumSquareDiff(100))