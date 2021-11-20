function checkValues() {
    var nCount = document.getElementById("count_num").value;
    num = (Number(nCount));
    if (Object.is(num,NaN)) {
        alert("Value is not a number")
        document.getElementById("count_num").value = 0
    }


}