// Create an Object to Represent a Person
// Create an object person that represents a person with properties: firstName, lastName, and age. Then, log the full name of the person (combine firstName and lastName).
const person = {
    firstName: "John",
    lastName: "Doe",
    age: 30
}
console.log(person.firstName + " " + person.lastName);

// Add and Access Properties Dynamically
// Add a new property email to the person object dynamically, and then log it.
person.email = "johndoe@gmail.com";
console.log(person.email);

// Modify Object Properties
// Modify the age property of the person object to 35. Then, log the updated object.
person.age = 35;
console.log(person.age);

// Check if Property Exists in an Object
// Check if the age property exists in the person object. If it exists, log the age; otherwise, log a message that the property does not exist.
console.log(person.hasOwnProperty("age") ? person.age : "The property age doesn't exist");

// Delete a Property from an Object
// Delete the age property from the person object and then log the object.
delete person.age;
console.log(person);

// Object Method Example
// Create an object car with properties make, model, and year. Add a method getCarInfo() that returns the car's information as a string, and log the result.
car = {
    make: "ford",
    model: "mustang",
    year: 1997,
    getCarInfo : function () {
        return this.make + " " + this.model + " " + this.year;
    }
}
console.log(car.getCarInfo());

// Object Destructuring
// Using object destructuring, extract the properties firstName and lastName from the person object and log them.
let {firstName, lastName} = person;
console.log(firstName + " " + lastName);

// Object Spread Operator
// Create a new object updatedPerson by copying all properties from person, but change the age to 40. Log both person and updatedPerson.
const updatedPerson = {...person};
updatedPerson.age = 40;
console.log(updatedPerson);
console.log(person);

// Loop Through Object Properties
// Write a function that loops through the properties of the person object and logs both the key and the value.
for (let key in person) {
        console.log(key + ": " + person[key]);
}
// console.log(Object.keys(person));
// console.log(Object.values(person));
// console.log(Object.entries(person));

// Nested Object Access
// Access the city property from the address object inside person and log it.
person.address = {city: "Gurugram"};
console.log(person.address.city);

// Object Method Returning Another Object
// Write a method createEmployee() inside an object that returns another object with name and position properties.
const employees = {

    createEmployee: function () {
        return {
            name: "Jane Doe",
            position: "Applications Developer"
        };
    }
}
console.log(employees.createEmployee());

// Object Freezing
// Freeze the person object to prevent adding new properties, and attempt to add a new property. Check if it is added.
// Object.freeze(person);
person.phoneNumber = "+9121345678";
console.log(person);

// Object Merging
// Merge two objects person and address into one new object fullInfo. Log the merged object.
const address = { city: "Gurugram", country: "India" };
const fullInfo = { ...person, ...address };
console.log(fullInfo);

// Object Property Short-Hand
// Refactor the following code using shorthand property names:

// const firstName = 'John';
// const lastName = 'Doe';
// const person = { firstName: firstName, lastName: lastName };
const person = new Object();
person.firstName = "John";
person.lastName = "Doe";
