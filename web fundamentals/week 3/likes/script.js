var count_arr = [10,23,5,33];

function submitCurrentLikes(page) {
    if (page == 'index') {
        document.getElementById("countofLikes").innerText = count_arr[0] + " like(s)";
    } else {
        document.getElementById("countofLikes1").innerText = count_arr[1] + " like(s)";
        document.getElementById("countofLikes2").innerText = count_arr[2] + " like(s)";
        document.getElementById("countofLikes3").innerText = count_arr[3] + " likes(s)";
    }
}

function likes_btn(num) {
    count_arr[num] = Number(count_arr[num])+1;
    if (num == 0) {
        document.getElementById("countofLikes").innerText = count_arr[num] + " like(s)"
        count_arr[num] = Number(count_arr[num])+1;
    } else if (num == 1) {
        document.getElementById("countofLikes1").innerText = count_arr[num] + " like(s)"
        count_arr[num] = Number(count_arr[num])+1;
    } else if (num == 2) {
        document.getElementById("countofLikes2").innerText = count_arr[num] + " like(s)"
        count_arr[num] = Number(count_arr[num])+1;
    } else if (num == 3) {
        document.getElementById("countofLikes3").innerText = count_arr[num] + " like(s)"
        count_arr[num] = Number(count_arr[num])+1;
    }
    
}