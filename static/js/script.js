var create_btn = document.getElementById('open');

var model = document.getElementById('model');
var close_btn = document.getElementById('close_btn');
var closeBtn = document.getElementById('close');

create_btn.addEventListener('click', openModel);
close_btn.addEventListener('click', closeModel);
window.addEventListener('click', clickOutside);
closeBtn.addEventListener('click', closeModel)

function openModel() {
    model.style.display = 'block'
}
function closeModel() {
    model.style.display = 'none'
}
function clickOutside(e) {
    if (e.target == model) {
        model.style.display = 'none'
    }

}
