/* toggle sidebar */
document.getElementById('modes').addEventListener('click', () => {
    document.getElementById('side_bar').getElementsByTagName('ul')[0].classList.toggle('d-none');
});

/* toggle active modes */
[...document.getElementById('side_bar').getElementsByTagName('li')].forEach((li_element) => {
    li_element.addEventListener('click', () => {
        li_element.getElementsByTagName('a')[0].classList.toggle('active_item');
    });
})