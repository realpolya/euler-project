/*

Truncatable Primes

The number 3797 has an interesting property. Being prime itself, it is possible to continuously remove digits from left to right, 
and remain prime at each stage: 3797, 797, 97, and 7. Similarly we can work from right to left: 3797, 379, 37, and 3.
Find the sum of the only eleven primes that are both truncatable from left to right and right to left.

NOTE: 2, 3, 5, and 7 are not considered to be truncatable primes.

*/

const isPrimeNum = (num: number): boolean => {

    const greaterOne: boolean = num > 1 ? true : false;
    if (!greaterOne) return false;

    let divisorFound: boolean = false;
    for (let i = 2; i <= Math.sqrt(num); i++) {
          if (num % i === 0) {
                divisorFound = true;
                break;
          }
    }

    if (divisorFound) {
          
          // not a prime num
          return false;

    }

    return true;

}


const findTruncatables = (): number => {

    let sum: number = 0;

    return sum

}