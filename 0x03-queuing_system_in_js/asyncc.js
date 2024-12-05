function fun1() {
    return new Promise((resolve, reject) => {
        setTimeout(() => {
            reject('404')
        }, 100)

    })
}


function fun2() {
    return new Promise((resolve, reject) => {
        setTimeout(() => {
            resolve(':)')
        }, 100)
    })
}


function onSuccess(data) {
    console.log(data)
}


function onError(data){
    console.log(data)
}


fun1()
    .then(fun2, onError)
    .then(onSuccess, onError)