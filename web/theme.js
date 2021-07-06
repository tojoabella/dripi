function themeToggler() {
    const theme = document.querySelector('.btn2');
    theme.addEventListener('click', function(){
        let bodyClassName = document.body.className;
        if (bodyClassName == "light-theme") {
            this.textContent = "Dark";
            document.body.classList.add('dark-theme');
            document.body.classList.remove('light-theme');
        }
        else{
            this.textContent = "Light";
            document.body.classList.add('light-theme');
            document.body.classList.remove('dark-theme');
        }
    });
};

themeToggler();