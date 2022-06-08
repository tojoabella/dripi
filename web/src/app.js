import {homepage_side_bar} from './components/side_bar/side_bar.js';
import {homepage_top_bar} from './components/top_bar/top_bar.js';
import {theme_toggler} from './components/theme_toggler.js';
import {toggle_modes} from './modes/modes.js';

toggle_modes();
homepage_side_bar();
homepage_top_bar();
theme_toggler();

/*
document.getElementById('start').addEventListener('click', () => {
    var modes = document.getElementsByClassName('mode');
    for (let i = 0; i < modes.length; i++) {
        mode = modes[i];
        if (mode.classList.contains('active')) {
            mode.classList.remove('show');
        }
    }
});
*/

document.getElementById('start').addEventListener('click', () => {
    var modes = document.getElementsByClassName('mode');
    for (let i = 0; i < modes.length; i++) {
        mode = modes[i];
        if (mode.classList.contains('active')) {
            mode.classList.remove('show');
        }
    }
});