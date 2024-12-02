/*
Smallest Multiple

2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
What is the smallest positive number that is evenly divisible (divisible with no remainder)
by all of the numbers from 1 to 20?

*/

const smallestMultiple = (range) => {

      if (!Array.isArray(range) || range.length != 2) return "Range must be an array of two integers"

      let multiple;
      const rangeArr = []
      for (let i = +range[0]; i <= +range[1]; i++) {
            rangeArr.push(i)
      }

      // start with multiplying the two largest numbers in range
      let candidate = rangeArr[rangeArr.length - 1] * rangeArr[rangeArr.length - 2]

      // check if the number is even
      if (candidate % 2 !== 0) candidate++;

      // from there go through even numbers
      while (!multiple) {

            // do range.ForEach or range.some to see if the condition is satisfied
            let notAnswer = rangeArr.some(divisor => {
                  return candidate % divisor !== 0
            })

            // if some is false
            if (!notAnswer) {

                  // assign multiple
                  multiple = candidate

            }

            candidate += 2

      }

      return multiple

}

console.log("Answer to problem 5: ", smallestMultiple([1, 20]))