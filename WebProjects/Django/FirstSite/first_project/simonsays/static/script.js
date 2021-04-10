var green = document.getElementById('green')
var score = 0
const BOXES = document.querySelectorAll('.block')
let moves = []

function sleep(ms){
    return new Promise(resolve => setTimeout(resolve, ms))
}

var AddRandomMove = () => {
    let random = Math.floor(Math.random() * 4)
    moves.push(random)
}

var ToggleClass = (el) => {
    BOXES[el].classList.remove('visible')
    BOXES[el].classList.add('hide')
    setTimeout(() => {
        BOXES[el].classList.remove('hide')
        BOXES[el].classList.add('visible')
    }, 400)
    
}
var ShowOrder = () => {
    var time = 800
    moves.forEach(el =>
        {
            setTimeout(() => {ToggleClass(el)}, time)
            time+=800
        })
}
var AddFunctionToButtons = () => {
var i = 0
BOXES.forEach(el => {
    el.addEventListener('click', () => {
    console.log('Elemnet id = '+ el.id)
    console.log(i)
    console.log(moves[i])
    console.log('Correct id= '+ BOXES[moves[i]].id)
    if(el.id == BOXES[moves[i]].id && i<= moves.length)
    {
        console.log("HIT")
        i++
        console.log(i)
    }else{
        BOXES.forEach(el => {
            el.style.display = 'none'
        })
        document.getElementById('startingScreen').style.display = 'block'
        document.getElementById('startingButton').innerHTML = "Try again"
        document.getElementById('startingButton').addEventListener('click', () => {
            location.reload()
        })
    }
    if(i == moves.length)
    {
        i= 0
        score++
        document.getElementById('score').innerHTML = "Your Score: "+score
        var random = Math.floor(Math.random() * 4)
        moves.push(random)
        console.log(moves)
        setTimeout(() => {
            ShowOrder()
        }, 1000)
    }
    
    })
})
}
var StartGame = () => {
    moves = []
    score = 0
    BOXES.forEach(el => {
        el.style.display = 'inline-block'
    })
    document.getElementById('score').innerHTML = "Your Score: "+score
    AddRandomMove()
    ShowOrder()
    AddFunctionToButtons()
    document.getElementById('startingScreen').style.display = 'none'
}
startButton = document.getElementById('startingButton')
startButton.addEventListener('click', () => {StartGame()})
