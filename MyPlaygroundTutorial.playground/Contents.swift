//: Playground - noun: a place where people can play

import UIKit

var str = "Hello, playground"

var optionalString: String? = "Hello"
print(optionalString == nil)

// \ to take care of optionals
var optionalName: String? = nil
var greeting = "Hello!"
if let name = optionalName {
    greeting = "Hello, \(name)"
} else {
    greeting = "Bye!"
}

// ?? to take care of optionals
let nickName: String? = nil
let fullName: String = "John Appleseed"
let informalGreeting = "Hi \(nickName ?? fullName)"

// switch cases
let vegetable = "red pepper"
switch vegetable {
case "celery":
    print("Add some raisins and make ants on a log.")
case "cucumber", "watercress":
    print("That would make a good tea sandwich.")
case let x where x.hasSuffix("pepper"):
    print("Is it a spicy \(x)?")
default:
    print("Everything tastes good in soup.")
}

//for-in
let interestingNumbers = [
    "Prime": [2, 3, 5, 7, 11, 13],
    "Fibonacci": [1, 1, 2, 3, 5, 8],
    "Square": [1, 4, 9, 16, 25],
]
var largest = 0
for (kind, numbers) in interestingNumbers {
    for thing in numbers {
        if thing > largest {
            largest = thing
        }
    }
}
print(largest)

//while
var n = 2
while n < 100 {
    n = n * 2
}
print(n)

//repeat-while
var m = 2
repeat {
    m = m * 2
} while m < 100
print(m)


//for loop
var total = 0
for i in 0..<4 {
    total += i
}
print(total)

//function (arguments) -> return type
func greet(name: String, day: String) -> String {
    return "Hello \(name), today is \(day)."
}
greet("Bob", day: "Tuesday")

//tuples

func calculateStatistics(scores: [Int]) -> (min: Int, max: Int, sum: Int) {
    var min = scores[0]
    var max = scores[0]
    var sum = 0
    
    for score in scores {
        if score > max {
            max = score
        } else if score < min {
            min = score
        }
        sum += score
    }
    
    return (min, max, sum)
}
let statistics = calculateStatistics([5, 3, 100, 3, 9])
print(statistics.sum)
print(statistics.2)
print(statistics.0)

//variable number of arguments in a func

func avgOf(numbers: Int...) -> Int {
    var sum = 0
    var count = 0
    for number in numbers {
        sum += number
        count += 1
    }
    if count > 0 {
        return (sum/count)
    } else {
        return 0
    }
}
avgOf()
avgOf(42, 597, 12)

//nested functions
func returnFifteen() -> Int {
    var y = 10
    func add() {
        y += 5
    }
    add()
    return y
}
returnFifteen()

//function returning another function
func makeIncrementer() -> ((Int) -> Int) {
    func addOne(number: Int) -> Int {
        return 1 + number
    }
    return addOne
}
var increment = makeIncrementer()
increment(7)

//function with other function as an argument
func hasAnyMatches(list: [Int], condition: (Int) -> Bool) -> Bool {
    for item in list {
        if condition(item) {
            return true
        }
    }
    return false
}
func lessThanTen(number: Int) -> Bool {
    return number < 10
}
var numbers = [20, 19, 7, 12]
hasAnyMatches(numbers, condition: lessThanTen)

//closures - don't understand this all the way

numbers.map({
    (number: Int) -> Int in
    let result = 3 * number
    return result
})

let mappedNumbers = numbers.map({ number in 3 * number })
print(mappedNumbers)

let sortedNumbers = numbers.sort { $0 > $1 }
print(sortedNumbers)


//classes
class Shape {
    var numberOfSides: Int = 0
    var name: String

    init(name: String) {
        self.name = name
    }
    func simpleDescription() -> String {
        return "A shape with \(numberOfSides) sides."
    }
    let num = 6
    func sayIt() -> Int {
        return num
    }
}

var shape = Shape(name : "Traingle")
shape.numberOfSides = 7
var shapeDescription = shape.simpleDescription()

//subclasses
class Square: NamedShape {
    var sideLength: Double
    
    init(sideLength: Double, name: String) {
        self.sideLength = sideLength
        super.init(name: name)
        numberOfSides = 4
    }
    
    func area() ->  Double {
        return sideLength * sideLength
    }
    
    override func simpleDescription() -> String {
        return "A square with sides of length \(sideLength)."
    }
}
let test = Square(sideLength: 5.2, name: "my test square")
test.area()
test.simpleDescription()

