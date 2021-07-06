import {themeToggler} from './theme.js';

function visitPageNewWindow(link){
    window.open(link);
};

function scrollTo(id){
    document.getElementById('led').scrollIntoView();
};

/*light and dark theme*/
themeToggler();