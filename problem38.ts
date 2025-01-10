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

const findLargest = (n: number, limit: number): number => {

    let exceeded: boolean = false;
    let largest: number = 0;

    while (!exceeded) {

        let iArray: number[] = [] 

        for (let i: number = 1; i <= 9; i++) {

            iArray.push(i)

            let products: string = iArray.map(member => {
                return member * n;
            }).join('')

            if (products.length > 9) {
                exceeded = true
                break
            } else if (products.length < 9) {
                continue
            }

            if (Number(products) > largest) {
                largest = Number(products)
            }

        }

    }

    return largest

}



const panMultiples = (limit: number): number => {

    let largest: number = 0;

    // unknown n: integer
    // unknown set with unknown number of members: consecutive 1 through n
    // limit 999 999 999 - 9 digits

    

    return largest

}