console.log('test')

let data = fetch('https://intense-retreat-39884.herokuapp.com/api/quotes')
.then(res => res.json())
.then(data => document.write(data[11].quote))



function func(){ return 2 + 2}

// const func = () => 2 + 2

func()

console.log(data)