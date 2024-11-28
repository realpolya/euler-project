/*
Multiples of 3 or 5

If we list all the natural numbers below $10$ that are multiples of $3$ or $5$, we get $3, 5, 6$ and $9$. The sum of these multiples is $23$.
Find the sum of all the multiples of $3$ or $5$ below $1000$.
*/

const multiples53 = (limit) => {

      const multiples = []

      for (let i = 1; i < limit; i++) {
            if (i % 3 === 0 || i % 5 === 0) {
                  multiples.push(i)
            }
      }

      return multiples.reduce((arg, i) => {

            return arg += i;

      }, 0)
      
}

console.log(multiples53(10))
console.log(multiples53(1000))