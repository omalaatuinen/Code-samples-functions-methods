// перебор массивов

for (let i = 0; i < arr.length; i++) {
  alert( arr[i] );
}

//или 

for (let fruit of fruits) {
  alert( fruit );
}


let numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10];// array numbers
let sum = 0;//variable sum
numbers.forEach(function num(){//loop through array numbers
sum += num;
});
console.log(sum);//returns 55

//arrow function for an array
numbers.forEach(num => sum += num);
console.log(sum);//returns 55
