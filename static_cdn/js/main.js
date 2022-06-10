console.log("hello world");

var form = document.getElementById('profileForm')
form.addEventListener('submit', function(e){
    e.preventDefault()
    console.log('Form submitted')
})