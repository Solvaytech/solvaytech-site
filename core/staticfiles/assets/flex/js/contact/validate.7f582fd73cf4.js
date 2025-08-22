(function () {
    "use strict";
    let forms = document.querySelectorAll('.contact-form');
    forms.forEach( function(e) {
        e.addEventListener('submit', function(event) {
            event.preventDefault();
            let thisForm = this;
            thisForm.querySelector('.loading').classList.add('d-block');
            thisForm.querySelector('.error-message').classList.remove('d-block');
            thisForm.querySelector('.sent-message').classList.remove('d-block');
            makeRequest("/contact-api", thisForm)
        });
    });

    async function makeRequest(url, form) {
        let response = await fetch(url, {
            method: 'post',
            headers: setHeader(form),
            body: setFormData(form)
        })
        .then(response => {
            if(response.ok) {
                return response.json();
            } else {
                throw new Error(`${response.status} ${response.statusText} ${response.url}`); 
            }
        })
        .then(data => {
            form.querySelector('.loading').classList.remove('d-block');
            if(data['response']) {
                form.querySelector('.sent-message').classList.add('d-block');
                form.reset()
            } else {
                throw new Error('Form gönderme başarısız: ' + data['reason']);
            }
        })
        .catch((error) => {
            displayError(form, error)
        })
    }

    function setHeader(thisForm) {
        const csrf = thisForm.querySelector('input[name="csrfmiddlewaretoken"]').value
        let headers = {
            'X-Requested-With': 'XMLHttpRequest',
            'Content-Type': 'application/json',
            'X-CSRFToken': csrf
        }
        return headers
    }

    function setFormData(thisForm) {
        const name = thisForm.querySelector('input[name="name"]').value
        const email = thisForm.querySelector('input[name="email"]').value
        const subject = thisForm.querySelector('input[name="subject"]').value
        const message = thisForm.querySelector('textarea[name="message"]').value
        let body = JSON.stringify({
            name: name,
            email: email,
            subject: subject,
            message: message
        })
        return body
    }

    function displayError(thisForm, error) {
        thisForm.querySelector('.loading').classList.remove('d-block');
        thisForm.querySelector('.error-message').innerHTML = error;
        thisForm.querySelector('.error-message').classList.add('d-block');
    }
})();