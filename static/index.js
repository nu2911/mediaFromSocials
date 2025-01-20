function showSpinner() {
  document.getElementById("spinner-container").style.display = "block";
}
function hideSpinner() {
  document.getElementById("spinner-container").style.display = "none";
}
window.onload = function () {
  hideSpinner();
};
function hideDownloadBtn() {
  document.getElementById("fbtns").style.display = "none";
}

