// Task 10: Rewrite the function appendToEachArrayValue to use ES6’s for...of operator.
// And don’t forget that var is not ES6-friendly.

const newarray = [];
export default function appendToEachArrayValue(array, appendString) {
  for (const idx of array) {
    newarray.push(appendString + idx);
  }

  return newarray;
}
