/*
Largest Palindrome Product

A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 times 99.
Find the largest palindrome made from the product of two 3-digit numbers.

*/

const largestPalindrome = digits => {

      let largestMultiplierArr = []
      let smallestMultiplierArr = [1]

      for (let i = 0; i < digits; i++) {
            largestMultiplierArr.push(9)
            if (i < digits - 1) {
                  smallestMultiplierArr.push(0)
            }
      }

      let largestMultiplier = +largestMultiplierArr.join('')
      let smallestMultiplier = +smallestMultiplierArr.join('')

      let product;
      let allPalindromes = []

      outerLoop: for (let i = largestMultiplier; i >= smallestMultiplier; i--) {

            innerLoop: for (let j = largestMultiplier; j >= smallestMultiplier; j--) {

                  // multiply
                  product = +j * +i
            
                  // convert number into a string
                  let string = product.toString().split('')

                  let y = string.length - 1
                  let half = Math.floor(string.length / 2)
                  let palindrome = true;

                  // and see if exterior digits match
                  miniLoop: for (let z = 0; z < half; z++) {

                        // if exterior digits match continue checking the digits
                        if (string[z] != string[y]) {
                              palindrome = false
                              break miniLoop
                        }
                        y--

                  }

                  if (palindrome) {
                        allPalindromes.push(product)
                  }


            }
      }

      return Math.max(...allPalindromes)

}

console.log("Answer to problem 4: ", largestPalindrome(3))


/* TODO:

create a faster solution by introducing stepwise motion and better loop architecture

*/