// Task 11: Write a function named createEmployeesObject that will receive two arguments

export default function createEmployeesObject(departmentName, employees) {
  const employeesArray = {
    [departmentName]: employees,
  };

  return employeesArray;
}
