// Implement a class named Airport

export default class Aireport {
    constructor(name, code) {
        this._name = name
        this._code = code
    }

    get [Symbol.toStringTag]() {
        return `${this._code}`;
    };
}