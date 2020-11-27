// There is a intentional mixture of pure JavaScript and jQuery to demonstrate understanding of both
// There are uncompleted sections because of time constraints.

window.addEventListener('load', (event) => {
    registerDelegatedEventListener();
    toggleRegisterButton();
});

function registerDelegatedEventListener() {
    var registerForm = document.getElementById('registrationForm');
    if(registerForm.addEventListener){
        registerForm.addEventListener('focusout', onRegistrationInputChange);  //Modern browsers
    }else if(registerForm.attachEvent){
        registerForm.attachEvent('focusout', onRegistrationInputChange); //IE
    }
}

function onRegistrationInputChange(event) {
    let valid = true;

    const targetElem = event.target;
    
    if (targetElem.nodeName === 'INPUT') {
        const targetJqElem = $(targetElem);
        const value = targetJqElem.val();
        targetJqElem.removeClass('is-invalid');

        
        if (value.trim() === '') {
            flagFieldAsInvalid(targetElem);
            targetJqElem.addClass('is-invalid');
            valid = false;
        }

        if (targetElem.id === 'passwordConfirmation') {
            const passwordElem = $('#password');
            const passwordValue = passwordElem.val();
            passwordElem.removeClass('is-invalid');
            targetJqElem.removeClass('is-invalid');

            if (passwordValue != value) {
                flagFieldAsInvalid(targetElem);
                passwordElem.addClass('is-invalid');
                targetJqElem.addClass('is-invalid');
                valid = false;
            }
        }
    }

    // Needs to work at form level not field level
    if(valid) {
        toggleRegisterButton();
    }
}

function flagFieldAsInvalid(fieldElem){
    // display validation error elem for field
}

function flagFieldAsValid(fieldElem){
    // remove validation error elem for field
}

function toggleRegisterButton() {
    const registerElem = $('#register');
    if (registerElem.prop('disabled')){
        registerElem.prop('disabled', false);
    } else {
        registerElem.prop('disabled', true);
    }
}



