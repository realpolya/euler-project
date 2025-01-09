/*

Truncatable Primes

The number 3797 has an interesting property. Being prime itself, it is possible to continuously remove digits from left to right,
and remain prime at each stage: 3797, 797, 97, and 7. Similarly we can work from right to left: 3797, 379, 37, and 3.
Find the sum of the only eleven primes that are both truncatable from left to right and right to left.

NOTE: 2, 3, 5, and 7 are not considered to be truncatable primes.

*/
var isPrimeNum = function (num) {
    var greaterOne = num > 1 ? true : false;
    if (!greaterOne)
        return false;
    var divisorFound = false;
    for (var i = 2; i <= Math.sqrt(num); i++) {
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
};
var findTruncatables = function () {
    var sum = 0;
    var limit = 11;
    var currentFinds = 0;
    var n = 11;
    // create a while loop iterating over numbers
    // while (n < 4000) {
    while (currentFinds < limit) {
        if (isPrimeNum(n)) {
            var isTruncatable = true;
            var nArr = n.toString().split('').map(Number);
            var arr = n.toString().split('').map(Number);
            var reverseArr = n.toString().split('').map(Number);
            for (var i = 0; i < nArr.length - 1; i++) {
                arr.pop();
                reverseArr.shift();
                if (!isPrimeNum(Number(arr.join(''))) || !isPrimeNum(Number(reverseArr.join('')))) {
                    isTruncatable = false;
                    break;
                }
            }
            if (isTruncatable) {
                console.log("n is truncatable prime ", n);
                sum += n;
                currentFinds += 1;
            }
        }
        n += 2;
    }
    return sum;
};
console.log(findTruncatables());
