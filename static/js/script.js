// Mobile Navbar
const hamMenu = document.querySelector('.ham-menu');
const navbar = document.querySelector('.navbar');

hamMenu.addEventListener('click', () => {
    hamMenu.classList.toggle('active');
    navbar.classList.toggle('active');
});

const submitBtn = document.querySelector('.contact-btn')

if (submitBtn != null) {
    submitBtn.addEventListener('click', () => {
        const first = document.querySelector('#first').value;
        const last = document.querySelector('#last').value;
        const email = document.querySelector('#email').value;
        const phone = document.querySelector('#phone').value;
        const address = document.querySelector('#address').value;
        const subject = document.querySelector('#subject').value;
        const message = document.querySelector('#message').value;

        fetch('https://api.pixel-master.com/sendemail/construction1', {
            method: 'POST',
            mode: 'no-cors',
            body: JSON.stringify({
                name: first + " " + last,
                email: email,
                phone: phone,
                address: address,
                subject: subject,
                message: message,
                to_email: 'homerevivecontracting@gmail.com'
            })
        })  
        .then((response) => {
            const status = response.status;
            if (status == 0) {
                fetch('thank-you', {
                    method: 'GET'
                })
                .then((response) => {
                    window.location.href = response.url;
                })
            } else {
                alert("Something went wrong on our end. Please call us and we will get this resolved as quickly as possible")
            }
        })
        
    })
}