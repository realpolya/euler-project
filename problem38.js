/*

Pandigital Multiples

Take the number 192 and multiply it by each of 1, 2, and 3:

192 * 1 = 192
192 * 2 = 384
192 * 3 = 576

By concatenating each product we get the 1 to 9 pandigital, 192384576. We will call 192384576 the concatenated product of 192 and (1,2,3).

The same can be achieved by starting with 9 and multiplying by 1, 2, 3, 4, and 5,
giving the pandigital, 918273645, which is the concatenated product of 9 and (1,2,3,4,5).

What is the largest 1 to 9 pandigital 9-digit number that can be formed as the concatenated product of an integer with (1,2, ..., n) where n > 1?

*/
const isPandigital = (n) => {
    let unique = [];
    let notPanny = n.toString().split('').some(digit => {
        let num = Number(digit);
        if (unique.includes(num) || num === 0)
            return true;
        unique.push(num);
        return false;
    });
    return !notPanny;
};
const findLargest = (n, limit) => {
    const iArray = [1];
    let largest = 0;
    for (let i = 2; i <= 9; i++) {
        iArray.push(i);
        let products = iArray.map(member => {
            return member * n;
        }).join('');
        if (products.length > limit) {
            break;
        }
        if (Number(products) > largest) {
            largest = Number(products);
        }
    }
    return largest;
};
const panMultiples = (limit = 9) => {
    const oLimit = Math.floor((limit / 3)); // number of 0s
    const str = "1" + Array(oLimit + 2).join("0");
    const nLimit = Number(str);
    let largest = 0;
    for (let n = 1; n < nLimit; n++) {
        let current = findLargest(n, limit);
        if (current === 0) {
            break;
        }
        if (current > largest && isPandigital(current)) {
            largest = current;
        }
    }
    return largest;
};
console.log("Answer to problem 38: ", panMultiples());
