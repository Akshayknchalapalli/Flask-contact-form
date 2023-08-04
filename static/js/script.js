document.addEventListener('DOMContentLoaded', function () {
  const contactForm = document.getElementById('contact-form');
  contactForm.addEventListener('submit', function (event) {
    const nameInput = document.getElementById('name');
    const emailInput = document.getElementById('email');
    const messageInput = document.getElementById('message');
    let isValid = true;

    if (nameInput.value.trim() === '') {
      isValid = false;
      nameInput.classList.add('error');
    } else {
      nameInput.classList.remove('error');
    }

    if (emailInput.value.trim() === '' || !validateEmail(emailInput.value)) {
      isValid = false;
      emailInput.classList.add('error');
    } else {
      emailInput.classList.remove('error');
    }

    if (messageInput.value.trim() === '') {
      isValid = false;
      messageInput.classList.add('error');
    } else {
      messageInput.classList.remove('error');
    }

    if (!isValid) {
      event.preventDefault();
    }
  });

  function validateEmail(email) {
    const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
    return emailRegex.test(email);
  }
});
