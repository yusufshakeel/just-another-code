/*
Question: Given a deeply nested array, create a function on the array,
namely flatten, that when invoked returns a flat version of the original
array. Function should be defined in a way that it can be invoked on
existing and future arrays.

Ref: https://www.linkedin.com/posts/yomeshgupta_javascript-interviewquestion-frontend-activity-6752479508416249856-wLPU
*/

const flattenRecursive = arr => arr.reduce((flatten, el) => Array.isArray(el) ? [...flatten, ...flattenRecursive(el)] : [...flatten, el], []);

Array.prototype.flatten = function() {
    return flattenRecursive(this);
};


// input
const input = [
1,
2,
3,
[4],
[5, 6, [7], [8, [9, [10]]]],
11,
12,
13,
[14, [[[[[15, [16]]]]]]],
17,
18,
[19, [20, [21, [22, [23, [24, [[[[[25]]]]]]]]]]]
];

const flatArray = input.flatten();

const expected = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25];

// assert
console.log(flatArray.length === expected.length && flatArray.every((el,idx) => el === expected[idx]) ? 'PASS' : 'FAIL');
