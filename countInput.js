// 2703. Return Length of Arguments Passed
// Easy
// Write a function argumentsLength that returns the count of arguments passed to it.

// Example 1:

// Input: args = [5]
// Output: 1
// Explanation:
// argumentsLength(5); // 1

// One value was passed to the function so it should return 1.
// Example 2:

// Input: args = [{}, null, "3"]
// Output: 3
// Explanation: 
// argumentsLength({}, null, "3"); // 3

// Three values were passed to the function so it should return 3.
 

var argumentsLength = function(args) {
    for (var i = 0; i < args.length; i++){
		console.log(args[i])
    } return i
};

console.log(argumentsLength(['1', 'r', '3as']))