function login(element) {
    var txt = element.innerHTML;
    console.log(txt);
    if (txt == 'Login') {
        element.innerHTML = 'Logout';
    } else {element.innerHTML = 'Login'}
}

function add_definition(element) {
    element.remove();
}

function likes_btn(element) {
    var arr = element.innerHTML.split(" ");
    var num = Number(arr[0])+1;
    element.innerHTML = (num + " likes");
    alert("Ninja was liked");
}