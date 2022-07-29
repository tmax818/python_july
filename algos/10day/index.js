// countdown

// write a function that counts down from a given number

function countdown(num){
  for(let i = num; i >= 0; i--){
    console.log(i)
  }
}

// countdown(5)

function rcountdown(num){
  // print that number
  console.log(num)
  // call the fuction again until n = 0
  // everytime function is called, call with n - 1
  if (num > 0){
    rcountdown(num - 1)
  }

}


rcountdown(5)