// Implement a class named HolbertonCourse:

// Make sure to verify the type of attributes during object creation
// Each attribute must be stored in an “underscore” attribute version (ex: name is stored in _name)
// Implement a getter and setter for each attribute.

export default class HolbertonCourse {
    constructor(name, length, students) {
        this.name = name;
        this.length = length;
        this.students = students;
    }

    get name() {
        return this._name;
    }

    get length() {
        return this._length;
    }

    get students() {
        return this._students;
    }

    set name(newName) {
        if (typeof newName !== 'string') {
            throw new TypeError('Name must be a string');
        }
        this._name = newName;
    }

    set length(newlength) {
        if (typeof newlength !== 'number') {
            throw new TypeError('Length must be a number');
        }
        this._length = newlength;
    }

    set students(newStudents) {
        if (!Array.isArray(newStudents)) {
            throw new TypeError('Students must be an array');
        }
        this._students = newStudents;
    }
}
