export function mode_1() {
    document.getElementById('mode1').addEventListener('click', () => {
        document.getElementById('side_bar').getElementsByTagName('ul')[0].classList.toggle('d-none');
    });
};
