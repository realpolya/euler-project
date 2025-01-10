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
var findLargest = function (n, limit) {
    var exceeded = false;
    var largest = 0;
    console.log("current n is ", n);
    var iArray = [1, 2];
    for (var i = 3; i <= 9; i++) {
        iArray.push(i);
        console.log("current iArray is ", iArray);
        var products = iArray.map(function (member) {
            return member * n;
        }).join('');
        console.log("current product is ", products);
        if (products.length > limit) {
            console.log("EXCEEDED");
            break;
        }
        console.log("products made it through barrier ", products);
        if (Number(products) > largest) {
            largest = Number(products);
        }
    }
    console.log("largest is ", largest);
    return largest;
};
var panMultiples = function (limit) {
    if (limit === void 0) { limit = 9; }
    var oLimit = Math.floor((limit / 3)); // number of 0s
    var str = "1" + Array(oLimit + 2).join("0");
    var nLimit = Number(str);
    console.log(nLimit);
    var largest = 0;
    // unknown n: integer
    // unknown set with unknown number of members: consecutive 1 through n
    // limit 999 999 999 - 9 digits
    for (var n = 1; n < nLimit; n++) {
        var current = findLargest(n, limit);
        if (current === 0) {
            break;
        }
        if (current > largest) {
            largest = current;
        }
    }
    return largest;
};
console.log(panMultiples(9));
