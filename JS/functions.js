//well done video about an arrow functions https://www.youtube.com/watch?v=5vgzCnqxRso

let square = x => x * x;//arrow function with one parametor x.
console.log(square(5));//returns 25

//multiline arrow function with two parametors
let multiply = (x, y) => {
    let result = x * y;
    return result;
};

let add = (x, y) => x + y; //arrow function add with x and y parametors
console.log(add(5, 5)); //returns 10

let giveMeAnswer = () => 42;//arrowfunction, that always returns 42

(() => console.log("IIFE"))(); //one row arrow IIFE


(() => {
alert ("IIFE");
console.log("IIFE")
})(); //multirow arrow IIFE



// using function as a parameter for another function

const chk2p2 = () => { //declaring an inner function
    for(let i = 1; i <= 1000000; i++) {
      if ( (2 + 2) != 4) {
        console.log('Something has gone very wrong :( ');
      }
    }
  };
  
  const timeFunc = funcParameter => { // declaring an outer function, which will accept and call another funct. as a parameter
    let t1 = Date.now();
    funcParameter();
    let t2 = Date.now();
    return t2 - t1;
  };
  
  console.log(timeFunc(chk2p2)); // shoing - how many time processing of inner function is taken
  
  