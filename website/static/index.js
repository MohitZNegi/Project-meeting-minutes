function deleteNote(noteId) {
    fetch("/delete-note", {
      method: "POST",
      body: JSON.stringify({ minuteId: minuteId }),
    }).then((_res) => {
      window.location.href = "/";
    });
  }
// form pop up
  function openForm() {
    document.getElementById("newMinutes").style.display = "block";
  }
  
  function closeForm() {
    document.getElementById("newMinutes").style.display = "none";
  }

  function openTable() {
    document.getElementById("table").style.display = "block";
  }
  
  function closeTable() {
    document.getElementById("table").style.display = "none";
  }

// Buttons to hide a particular table

var btn_click_S1 = 0;
function hide() {
  
    if (0 == btn_click_S1 % 2){
    data = document.getElementById("form").style.display="none"
    btn_click_S1++;}
    else if (0 != btn_click_S1 % 2){
      data =  document.getElementById("form").style.display= "block";
    btn_click_S1++;}
   
 
}

var btn_click_S2 = 0;
function S2() {
  if (0 == btn_click_S2 % 2){
  document.getElementById("S2I").style.display= "none";
  document.getElementById("S2D").style.display= "none";
btn_click_S2++;}
else if (0 != btn_click_S2 % 2){
  document.getElementById("S2I").style.display= "block";
  document.getElementById("S2D").style.display= "block";
btn_click_S2++;}
}

var btn_click_S3 = 0;
function S3() {
  if (0 == btn_click_S3 % 2){
  document.getElementById("S3I").style.display= "none";
  document.getElementById("S3D").style.display= "none";
btn_click_S3++;}
else if (0 != btn_click_S3 % 2){
  document.getElementById("S3I").style.display= "block";
  document.getElementById("S3D").style.display= "block";
btn_click_S3++;}
}

var btn_click_S4 = 0;
function S4() {
  if (0 == btn_click_S4 % 2){
  document.getElementById("S4I").style.display= "none";
  document.getElementById("S4D").style.display= "none";
btn_click_S4++;}
else if (0 != btn_click_S4 % 2){
  document.getElementById("S4I").style.display= "block";
  document.getElementById("S4D").style.display= "block";
btn_click_S4++;}
}

var btn_click_S5 = 0;
function S5() {
  if (0 == btn_click_S5 % 2){
  document.getElementById("S5I").style.display= "none";
  document.getElementById("S5D").style.display= "none";
btn_click_S5++;}
else if (0 != btn_click_S5 % 2){
  document.getElementById("S5I").style.display= "block";
  document.getElementById("S5D").style.display= "block";
btn_click_S5++;}
}




