// Task 6: Implement a class named SkyHighBuilding that extends from Building

import Building from './5-building';

export default class SkyHighBuilding extends Building {
  constructor(sqft, floors) {
    super(sqft);
    this._floors = floors;
  }

  evacuationWarningMessage() {
    return (`Evacuate slowly the ${this._floors} floors`);
  }

  get sqft() {
    return this._sqft;
  }

  get floors() {
    return this._floors;
  }

  set sqft(newSqft) {
    this._sqft = newSqft;
  }

  set floors(newFloors) {
    this._floors = newFloors;
  }
}
