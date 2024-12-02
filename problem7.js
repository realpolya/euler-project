/*
10 001st Prime

By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.
What is the 10,001st prime number?

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


const findPrime = orderNum => {

      // create an empty array
      const primeNumbers = []

      // create an iterable i
      let i = 2

      // create a while loop that is going until the length of the array reaches the limit
      while (+primeNumbers.length < +orderNum) {
            
            // check if the number is prime
            if (isPrime(i)) primeNumbers.push(i)
            
            // only go through odd numbers, increment by 2 after i = 2
            if (i === 2) {
                  i++
            } else {
                  i += 2
            }

      }

      // extract the last element of the array
      const answer = primeNumbers[primeNumbers.length - 1]

      // return the element
      return answer

}

console.log("Answer to problem 6: ", findPrime(10001))