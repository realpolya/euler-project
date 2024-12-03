/*
Special Pythagorean Triplet

A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,
      a^2 + b^2 = c^2.

For example, 3^2 + 4^2 = 9 + 16 = 25 = 5^2.

There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc.

*/

/*
let a;
let b;
let c;

a < b < c;
(a + b + c) = 1000;
(a^2 + b^2) = c^2;

c = 1000 - a - b
c = Math.sqrt(a^2 + b^2)
Math.sqrt(a^2 + b^2) = 1000 - a - b
Math.sqrt(a^2 + b^2) + a = 1000 - b
a = 1000 - b - Math.sqrt(a^2 + b^2)
*/

const findTriplet = (sum) => {

      let a;
      let b;
      let c;

      // outer loop b
      bLoop: for (let i = 2; i < +sum/2; i++) {

            // inner loop a
            for (let j = 1; j < i; j++) {

                  // if the equation above is satisfied and a smaller than b
                  if (j === (+sum - i - Math.sqrt((j ** 2) + (i ** 2)))) {
                        
                        // assign a and b
                        a = j
                        b = i
            
                        // the same solution with break out of both loops
                        break bLoop
                  }

            }
            
      }

      
      // assign c
      if (a) {

            c = +sum - a - b

            if (a ** 2 + b ** 2 === c ** 2) {
                  return (a * b * c)
            }

      }

      return "Solution not found"

}

console.log("Answer to problem 9: ", findTriplet(1000))