// Get the dialog
var dialog = document.getElementById("dialog");

// Get the buttons that open the dialog
var buttons = document.querySelectorAll(".book-btn");

// Get the <span> element that closes the dialog
var span = document.getElementsByClassName("close")[0];

// When the user clicks on any button, open the dialog
buttons.forEach(function(button) {
    button.onclick = function() {
        dialog.style.display = "block";
    };
});

// When the user clicks on <span> (x), close the dialog
span.onclick = function() {
    dialog.style.display = "none";
};

// When the user clicks anywhere outside of the dialog, close it
window.onclick = function(event) {
    if (event.target == dialog) {
        dialog.style.display = "none";
    }
};
const toggleBtn = document.getElementById('nav-toggle');
  const navLinks = document.getElementById('nav-links');

  toggleBtn.addEventListener('click', () => {
    navLinks.classList.toggle('hidden');
    navLinks.classList.toggle('flex');
  });
