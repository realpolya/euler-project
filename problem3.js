/*
Largest Prime Factor

The prime factors of 13195 are 5, 7, 13 and 29.
What is the largest prime factor of the number 600851475143?

*/

const isPrime = (number) => {

      const greaterOne = number > 1 ? true : false;
      if (!greaterOne) return false;

      let divisorFound = false;
      for (let i = 2; i <= Math.sqrt(number); i++) {
            if (number % i === 0) {
                  divisorFound = true;
                  break;
            }
      }

      if (divisorFound) {
            
            // not a prime number
            return false;

      }

      return true;
  
}

/* ascending order function */
const largestPrimeAsc = (number) => {

      // prime numbers are divisible by 1 and themselves ONLY
      const primes = []

      // find ALL prime numbers up to the number
      let i = 0;
      while (i <= number) {

            // see which ones are divisible without remainder
            if (i && isPrime(i) && number % i === 0) {
                  primes.push(i)
            }

            i++; 

      }

      // establish the largest one
      return primes[primes.length - 1]

}


const largestPrimeDesc = (number) => {

      let largest;

      // find the first prime number in descending order
      let i = number;
      if (i % 2 === 0) i--;
      while (i >= 1) {

            // see which ones are divisible without remainder
            if (isPrime(i) && number % i === 0) {
                  largest = i;
                  break;
            }
            
           i -= 2

      }

      if (largest) {
            return largest
      }
      return "Unable to find"

}

console.log(largestPrimeDesc(13195))
console.log(largestPrimeDesc(600851475143))
