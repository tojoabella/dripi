import themeToggler from './components/theme_toggler.js';

themeToggler();

function visitPageNewWindow(link){
    window.open(link);
};

function scrollTo(id){
    document.getElementById(id).scrollIntoView();
};

function activationToggler(element){
    element.classList.toggle('active_item');
};

function colorChanger(element, color){
        element.style.backgroundColor = color;
};
