/*
Largest Product in a Series 

The four adjacent digits in the 1000-digit number that have the greatest product are 9 * 9 * 8 * 9 = 5832.

73167176531330624919225119674426574742355349194934
96983520312774506326239578318016984801869478851843
85861560789112949495459501737958331952853208805511
12540698747158523863050715693290963295227443043557
66896648950445244523161731856403098711121722383113
62229893423380308135336276614282806444486645238749
30358907296290491560440772390713810515859307960866
70172427121883998797908792274921901699720888093776
65727333001053367881220235421809751254540594752243
52584907711670556013604839586446706324415722155397
53697817977846174064955149290862569321978468622482
83972241375657056057490261407972968652414535100474
82166370484403199890008895243450658541227588666881
16427171479924442928230863465674813919123162824586
17866458359124566529476545682848912883142607690042
24219022671055626321111109370544217506941658960408
07198403850962455444362981230987879927244284909188
84580156166097919133875499200524063689912560717606
05886116467109405077541002256983155200055935729725
71636269561882670428252483600823257530420752963450

Find the thirteen adjacent digits in the 1000-digit number that have the greatest product. What is the value of this product?

*/

const given = `
73167176531330624919225119674426574742355349194934
96983520312774506326239578318016984801869478851843
85861560789112949495459501737958331952853208805511
12540698747158523863050715693290963295227443043557
66896648950445244523161731856403098711121722383113
62229893423380308135336276614282806444486645238749
30358907296290491560440772390713810515859307960866
70172427121883998797908792274921901699720888093776
65727333001053367881220235421809751254540594752243
52584907711670556013604839586446706324415722155397
53697817977846174064955149290862569321978468622482
83972241375657056057490261407972968652414535100474
82166370484403199890008895243450658541227588666881
16427171479924442928230863465674813919123162824586
17866458359124566529476545682848912883142607690042
24219022671055626321111109370544217506941658960408
07198403850962455444362981230987879927244284909188
84580156166097919133875499200524063689912560717606
05886116467109405077541002256983155200055935729725
71636269561882670428252483600823257530420752963450`.replace(/\n/g, '')


const largestProduct = (length, number=given) => {

      const array = number.split('')
      const products = []
      
      for (let i = 0; i < (+number.length - +length); i++) {

            let product = 1;

            for (let j = i; j < (length + i); j++) {

                  product *= array[j]
                  if (!product) break

            }

            if (product) {
                  products.push(product)
            }
      }

      return Math.max(...products)

}

console.log("Answer to problem 8: ", largestProduct(13))


// the solution below calculates adjacent numbers within the number 
// (aka 1, 2, 3 is acceptable, 4, 7, 9 is not as a sequence)
const oldSolution = (length, number=given) => {

      const array = number.split('')

      // 2d array of sequences
      const sequences = []
      
      // find all possible sequences of "length" adjacent numbers
      // create a loop to start with all the digits minus the last ones
      for (let i = 0; i < (+number.length - +length); i++) {

            let adjSequence = true
            let currentSequence = []
            let beforeLast = false;

            // nested loop to count for the requested sequence length
            for (let j = i; j < (length + i); j++) {

                  if (beforeLast) {

                        currentSequence.push(array[j])
                        continue;

                  } else if (+array[j] === +array[j+1] || 
                        (+array[j] - +array[j+1] === 1) ||
                        (+array[j] - +array[j+1] === -1)
                  ) {

                        // special case for the last member
                        if ((j + 2 === length + i)) {
                              // console.log("turning before last true")
                              beforeLast = true
                        } 
                        
                        currentSequence.push(array[j])
                        continue;
                  } 

                  adjSequence = false
                  break;

            }

            if (adjSequence) sequences.push(currentSequence)

      }
      
      console.log('sequences are ', sequences)

      // calculate their products
      const products = []
      sequences.forEach(sequence => {
            let product = sequence.reduce((arg, digit) => {
                  return arg *= digit
            }, 1)
            products.push(product)
      })

      console.log(products)

      // choose the largest product
      const largest = Math.max(...products)
      return largest

}