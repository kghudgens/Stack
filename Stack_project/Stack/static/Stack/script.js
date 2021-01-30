// Create overlay variable 
const overlay = document.querySelector('.overlay')

// hide the overlay container
overlay.classList.add('hidden')

// create function that will remove the hidden class
function showOverlay(){
    overlay.classList.remove('hidden')
}
// Set timer for window pop
window.setTimeout(showOverlay, 10000)

// Takes the user input
document.querySelector('.save').addEventListener('click', function(){
    let formInput = document.querySelector('.formInput').value;
}
)

