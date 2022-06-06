
export function homepage_side_bar() {
    /* toggle sidebar when clicking "modes"*/
    document.getElementById('side_bar').getElementsByTagName('p')[0].addEventListener('click', () => {
        document.getElementById('side_bar').getElementsByTagName('ul')[0].classList.toggle('d-none');
    });

    /* toggle active modes */
    [...document.getElementById('side_bar').getElementsByTagName('li')].forEach((li_element) => {
        li_element.addEventListener('click', () => {
            li_element.getElementsByTagName('a')[0].classList.toggle('active_item');
        });
    });
};