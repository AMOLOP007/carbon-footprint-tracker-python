// script.js - basic client side stuff for aetherra

// login form check
function validateLogin() {
    var email = document.getElementById('email').value;
    var pass = document.getElementById('password').value;

    if (!email || !pass) {
        alert('Please fill in all fields.');
        return false;
    }

    // basic email check
    if (!email.includes('@')) {
        alert('Please enter a valid email.');
        return false;
    }

    return true;
}

// register form check
function validateRegister() {
    var name = document.getElementById('name').value;
    var email = document.getElementById('email').value;
    var pass = document.getElementById('password').value;

    if (!name || !email || !pass) {
        alert('Please fill in all fields.');
        return false;
    }

    if (!email.includes('@')) {
        alert('Please enter a valid email.');
        return false;
    }

    // minimum password length
    if (pass.length < 4) {
        alert('Password must be at least 4 characters.');
        return false;
    }

    return true;
}

// hide flash messages after a few seconds
window.onload = function () {
    var msgs = document.querySelectorAll('.flash-msg');
    msgs.forEach(function (msg) {
        setTimeout(function () {
            msg.style.opacity = '0';
            msg.style.transition = 'opacity 0.5s';
            setTimeout(function () { msg.remove(); }, 500);
        }, 4000);
    });
};
