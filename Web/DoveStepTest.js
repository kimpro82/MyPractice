// Rounding off in JavaScript

console.log(Math.floor(0.7))                // 0
console.log(Math.ceil(1.3))                 // 2
console.log(Math.round(2.3))                // 2
console.log(Math.round(2.7))                // 3


// Trigonometric Function in JavaScript

console.log(Math.PI);                       // 3.141592653589793
console.log(Math.PI / 180)                  // 0.017453292519943295

console.log(Math.sin(Math.PI / 180))        // 0.01745240643728351
console.log(Math.cos(Math.PI / 180))        // 0.9998476951563913

console.log(Math.sin(Math.PI *   0 / 180))  // 0
console.log(Math.sin(Math.PI *  30 / 180))  // 0.49999999999999994
console.log(Math.sin(Math.PI *  45 / 180))  // 0.7071067811865475
console.log(Math.sin(Math.PI *  60 / 180))  // 0.8660254037844386
console.log(Math.sin(Math.PI *  90 / 180))  // 1
console.log(Math.sin(Math.PI * 180 / 180))  // 1.2246467991473532e-16 ≒ 0
console.log(Math.sin(Math.PI * 270 / 180))  // -1
console.log(Math.sin(Math.PI * 360 / 180))  // -2.4492935982947064e-16 ≒ 0

console.log(Math.cos(Math.PI *   0 / 180))  // 1
console.log(Math.cos(Math.PI *  30 / 180))  // 0.8660254037844387
console.log(Math.cos(Math.PI *  45 / 180))  // 0.7071067811865476
console.log(Math.cos(Math.PI *  60 / 180))  // 0.5000000000000001
console.log(Math.cos(Math.PI *  90 / 180))  // 6.123233995736766e-17 ≒ 0
console.log(Math.cos(Math.PI * 180 / 180))  // -1
console.log(Math.cos(Math.PI * 270 / 180))  // -1.8369701987210297e-16 ≒ 0
console.log(Math.cos(Math.PI * 360 / 180))  // 1