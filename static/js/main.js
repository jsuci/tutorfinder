
// toggle navbar
(function () {
    var burger = document.querySelector('.navbar-burger');
    var menu = document.querySelector('#' + burger.dataset.target);
    burger.addEventListener('click', function () {
        burger.classList.toggle('is-active');
        menu.classList.toggle('is-active');
    });
})();


// form notification pop up
function showToast(text, status, icon){
    var x = document.getElementById("myNotification");
    var y = document.getElementById("myStatus");
    var z = document.getElementById("myIcon");

    x.classList.add("show");
    y.classList.add(status);
    z.classList.add(icon);
    
    document.getElementById("myText").innerHTML = text;
    
    setTimeout(function(){
      x.classList.remove("show");
      y.classList.remove(status);
      z.classList.remove(icon);
    },3000);
    
}
