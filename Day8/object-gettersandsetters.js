// Object getters and setterss
// nomal functions
let person = {
    firstName: "John",
    lastName: "Doe",
    getFullname() {
        return `${this.firstName} ${this.lastName}`;
    },
    setFullName(name) {
        let [first, last] = name.split(" ");
        this.firstName = first;
        this.lastName = last;
        return `${this.firstName} ${this.lastName}`;
    }
};

console.log(person.getFullname());
console.log(person.setFullName("Martina Alinda"));

// using get and set keywords defined in javascript
let person1 = {
    firstName: "Jane",
    lastName: "Smith",
    get fullName() {
        return `${this.firstName} ${this.lastName}`;
    },
    set fullName(name) {
        let [first, last] = name.split(" ");
        this.firstName = first;
        this.lastName = last;
    }
}
console.log(person1.fullName);
person1.fullName = "Martina Alinda"
console.log(person1.fullName);