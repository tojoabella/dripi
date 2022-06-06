export function mode_1() {
    document.getElementById('mode1').addEventListener('click', () => {
        document.getElementById('side_bar').getElementsByTagName('li')[0].getElementsByTagName('a')[0].classList.toggle('active_item');
    });
};
