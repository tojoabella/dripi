import {homepage_side_bar} from './components/side_bar/side_bar.js';
import {homepage_top_bar} from './components/top_bar/top_bar.js';
import {theme_toggler} from './components/theme_toggler.js';
import {mode_1} from "./modes/mode1.js"

homepage_side_bar();
homepage_top_bar();
theme_toggler();
mode_1();
document.getElementById('start').addEventListener('click', () => {
    var modes = document.getElementsByClassName('mode');
    for (let i = 0; i < modes.length; i++) {
        mode = modes[i];
        if (mode.classList.contains('active')) {
            mode.classList.remove('show');
        }
    }
});