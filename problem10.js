/*
Summation of Primes

The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
Find the sum of all the primes below two million.

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

const summationPrimes = limit => {

      let sum = 0;

      for (let i = 2; i < limit; i++) {

            if (i !== 2 && i % 2 === 0) continue;

            if (isPrime(i)) sum += i

      }

      return sum

}

console.log("Answer to problem 10: ", summationPrimes(2000000))