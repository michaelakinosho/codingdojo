function onClickAccept(id1, id2, id3) {
    var num1 = document.getElementById(id1).innerText;
    document.getElementById(id1).innerText = Number(num1) - 1;
    
    var num2 = document.getElementById(id2).innerText;
    document.getElementById(id2).innerText = Number(num2) + 1

    document.getElementById(id3).remove();
}

function onClickClose(id1,id3) {
    var num1 = document.getElementById(id1).innerText;
    document.getElementById(id1).innerText = Number(num1) - 1;

    document.getElementById(id3).remove();
}

function onClickChangeName (name_id) {

    let prompt_text = prompt("Please enter your profile name","Jane Doe");
    prompt_text = prompt_text.trim();
    if (prompt_text != null && prompt_text != "") {
        document.getElementById(name_id).innerText = prompt_text;
    }
    
}