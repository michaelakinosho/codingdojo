function checkValues() {
  var nCount = document.getElementById("your_guess").value;
  num = (Number(nCount));
  if (Object.is(num,NaN)) {
      alert("Value is not a number")
      document.getElementById("your_guess").value = 0
  }
}