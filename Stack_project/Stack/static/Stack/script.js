// Create overlay variable 
const overlay = document.querySelector('.overlay')

// hide the overlay container
try{
    overlay.classList.add('hidden')
} catch(err){
    console.error("Type Error");
}


// create function that will remove the hidden class
function showOverlay(){
    overlay.classList.remove('hidden')
}
// Set timer for window pop
window.setTimeout(showOverlay, 5000)

// Takes the user input
document.querySelector('.save').addEventListener('click', function(){
    let formInput = document.querySelector('.formInput').value;
}
)

updateForm = document.querySelector('.update')
console.log(updateForm);