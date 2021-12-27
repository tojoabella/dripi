
export function homepage_top_bar() {
    /* When the user clicks on the button, toggle between hiding and showing the dropdown content */
    document.getElementById('dropdown-btn').addEventListener('click', () => {
        document.getElementById("top_bar_dropdown").classList.toggle("show");
    });

    // Close the dropdown menu if the user clicks outside of it
    window.onclick = function(event) {
        if (!event.target.matches('#dropdown-btn')) {
            var dropdowns = document.getElementsByClassName("dropdown-content");
            for (let i = 0; i < dropdowns.length; i++) {
                var openDropdown = dropdowns[i];
                if (openDropdown.classList.contains('show')) {
                    openDropdown.classList.remove('show');
                }
            }
        }
    };
};