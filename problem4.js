/*
Largest Palindrome Product

A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 times 99.
Find the largest palindrome made from the product of two 3-digit numbers.

*/

const largestPalindrome = digits => {

      // start from the largest numbers with the requested number of digits
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

      // console.log("largest multiplier is ", largestMultiplier)
      // console.log("smallest multiplier is ", smallestMultiplier)

      let product;

      // loop within a loop
      outerLoop: for (let i = largestMultiplier; i >= smallestMultiplier; i--) {

            innerLoop: for (let j = largestMultiplier; j >= smallestMultiplier; j--) {

                  console.log("i is ", i, "j is ", j)

                  // multiply
                  product = +j * +i
            
                  // convert number into a string
                  let string = product.toString().split('')
                  console.log('string is ', string)

                  let y = string.length - 1
                  let half = Math.floor(string.length / 2)
                  let palindrome = true;

                  // and see if exterior digits match
                  miniLoop: for (let z = 0; z < half; z++) {

                        console.log("y is ", y, "z is ", z)
                        console.log("string at z is ", string[z], "string at y is ", string[y])

                        // if exterior digits match continue checking the digits
                        if (string[z] != string[y]) {
                              console.log("not a palindrome")
                              palindrome = false
                              break miniLoop
                        }
                        y--

                  }

                  if (palindrome) {
                        console.log("breaking outer loop, found the largest palindrome")
                        break outerLoop
                  }


            }
      }

      console.log("palindrome is", product)
      return product

}

// largestPalindrome(2)
largestPalindrome(3)