function visitPageNewWindow(link){
    window.open(link);
};

function colorChanger(element, color){
        element.style.backgroundColor = color;
};

/* When the user clicks on the button, toggle between hiding and showing the dropdown content */
function dropDown() {
    document.getElementById("top_bar_dropdown").classList.toggle("show");
};
  
  // Close the dropdown menu if the user clicks outside of it
window.onclick = function(event) {
    if (!event.target.matches('.dropdown-btn')) {
        var dropdowns = document.getElementsByClassName("dropdown-content");
        var i;
        for (i = 0; i < dropdowns.length; i++) {
            var openDropdown = dropdowns[i];
            if (openDropdown.classList.contains('show')) {
                openDropdown.classList.remove('show');
            }
        }
    }
}
