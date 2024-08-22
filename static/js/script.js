// Mobile Navbar
const hamMenu = document.querySelector('.ham-menu');
const navbar = document.querySelector('.navbar');

hamMenu.addEventListener('click', () => {
    hamMenu.classList.toggle('active');
    navbar.classList.toggle('active');
});