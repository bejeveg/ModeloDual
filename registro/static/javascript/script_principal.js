var optionList = document.getElementById("edad");
for(var i = 1; i < 101; i++){
  var opt = document.createElement("option");
  opt.value = i;
  opt.innerHTML = i;
  optionList.appendChild(opt);
}
