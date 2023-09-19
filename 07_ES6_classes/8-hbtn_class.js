// Task 8: Implement a class named HolbertonClass

export default class HolbertonClass {
  constructor(size, location) {
    this._size = size;
    this._location = location;
  }

  [Symbol.toPrimitive](input) {
    if (input === 'number') {
      return this._size;
    }
    return this._location;
  }
}
