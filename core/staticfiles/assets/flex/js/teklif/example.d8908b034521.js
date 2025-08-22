(function() {
    "use strict";
    
    let step = 0;
    const fieldset = document.querySelectorAll('fieldset');
    const next = document.querySelector('.next');
    const prev = document.querySelector('.prev');
    const refresh = document.querySelector('.refresh');
    const form = document.querySelector('.product-form');
    const publish = document.querySelector('.publish');
    const progress = document.querySelector('#progress-bar');
    const tel = document.querySelector('.telephone');
    const loading_message = document.querySelector('.loading');
    const error_message = document.querySelector('.error-message');
    const succ_message = document.querySelector('.sent-message');

    buttonActivation();

    function validate() {
        if (step == 0) {
            nextPage();
            return allCheck;
        }
        clearInput();
        var allCheck = true;
        const inputs = document.querySelectorAll('fieldset.fieldset-animation input');
        for (let i = 0; i < inputs.length; i++) {
            if (step == 1) {
                if (i == 2) {
                    if (!inputs[i].value.match(/\S+@\S+\.\S+/)) {
                        inputFail(inputs[i]);
                        allCheck = false;
                        continue;
                    }
                } else if (i == 3) {
                    if (inputs[i].value.length != 14 || !inputs[i].value.match(/.+/)) {
                        inputFail(inputs[i]);
                        allCheck = false;
                        continue;
                    }
                }
            }
            if (!inputs[i].value.match(/.+/)) {
                inputFail(inputs[i]);
                allCheck = false;
                continue;
            }
            inputPass(inputs[i]);
        }
        if (allCheck) {
            nextPage();
        }
        return allCheck;
    }

    function nextPage() {
        if (step < fieldset.length - 1) {
            togglePage();
            step++;
            getPage();
        } else {
            handle
        }
    }

    function getPage() {
        togglePage();
        setButtonsAndProgressBar();
    }

    function setButtonsAndProgressBar() {
        progress.style.width = (step * 100) / (fieldset.length - 1) + '%';
        prev.className = step ? "btn mb-2 mb-md-0 btn-tertiary prev" : "btn mb-2 mb-md-0 btn-tertiary prev button-opacity";
        next.className = step < fieldset.length-1 ? "btn mb-2 mb-md-0 btn-primary next" : "btn mb-2 mb-md-0 btn-primary next button-opacity";
        publish.className = step == fieldset.length-1 ? "btn mb-2 mb-md-0 btn-primary publish" : "btn mb-2 mb-md-0 btn-primary publish button-dn";
        refresh.className = step == fieldset.length-1 ? "btn mb-2 mb-md-0 btn-tertiary refresh" : "btn mb-2 mb-md-0 btn-tertiary refresh button-dn";
    }

    function prevPage() {
        if (step > 0) {
            togglePage();
            step--;
            getPage();
        }
    }

    function togglePage() {
        fieldset[step].classList.toggle('fieldset-none');
        fieldset[step].classList.toggle('fieldset-animation');
    }

    function cardBlockEventListener() {
        const card = document.querySelectorAll('.card-block');
        const total = document.querySelector('#total-product');
        for (let i = 0; i < card.length; i++) {
            card[i].addEventListener('click', function(e) {
                this.classList.toggle('selected');
                total.classList.toggle('product-'+[i]);
            })
        }
    }

    function buttonActivation() {
        next.addEventListener('click', validate);
        prev.addEventListener('click', prevPage);
        cardBlockEventListener();
    }

    function clearInput() {
        const pass = document.querySelectorAll("input.pass");
        const error = document.querySelectorAll("input.error");
        for (let i = 0; i < pass.length; i++) {
            pass[i].classList.remove("pass");
        }
        for (let i = 0; i < error.length; i++) {
            error[i].classList.remove("error");
        }
    }

    function inputFail(input) {
        input.classList.add('error');
    }

    function inputPass(input) {
        input.classList.add('pass');
    }

    function displayError(error) {
        loading_message.classList.remove('d-block');
        succ_message.classList.remove('d-block');
        error_message.innerHTML = error;
        error_message.classList.add('d-block');
    }

    function displaySuccess(success) {
        loading_message.classList.remove('d-block');
        error_message.classList.remove('d-block');
        succ_message.innerHTML = success
        succ_message.classList.add('d-block');
        hideButton();
    }

    function hideButton() {
        document.querySelector('button[type=submit]').classList.add('d-none');
        document.querySelector('button[id=prev]').classList.add('d-none');
    }

    function handleAllInput() {
        loading_message.classList.add('d-block')
        let data = {
            userInformation: {
                'name' : findValue('#isim'),
                'surname' : findValue('#soyisim'),
                'email' : findValue('#email'),
                'tel' : findValue('#tel'),
                'sirket' : findValue('#sirket'),
                'posta' : findValue('#posta'),
                'sehir' : findValue('#sehir'),
                'ilce' : findValue('#ilce'),
                'message' : findValue('#message')
            },
            product: {
                'hizmet' : findProduct()
            }
        }
        return JSON.stringify(data)
    }

    async function makeRequest(url) {
        await fetch(url, {
            method: 'post',
            headers: setHeader(),
            body: handleAllInput()
        })
        .then(response => {
            if(response.ok) {
                return response.json();
            } else {
                throw new Error(` ${response.status} ${response.statusText}`);
            }
        })
        .then(data => {
            if(data['response']) {
                console.log(data);
                formReset();
                displaySuccess(data['msg']);
            } else {
                throw new Error (data['msg'])
            }
        })
        .catch((error) => {
            console.log(error);
            displayError(error);
        })
    }

    function setHeader() {
        const csrf = document.querySelector('input[name="csrfmiddlewaretoken"]').value;
        let headers = {
            'X-Requested-With': 'XMLHttpRequest',
            'Content-Type': 'application/json',
            'X-CSRFToken': csrf
        }
        return headers
    }

    function formReset(){
        form.reset();
        const pass = document.querySelectorAll('.pass');
        const error = document.querySelectorAll('.error');
        const selected = document.querySelectorAll('.selected');
        if(pass.length){
            pass.forEach((e) => {
                e.classList.remove('pass');
            });
        }
        if (error.length) {
            error.forEach((e) => {
                e.classList.remove('error');
            })
        }
        if (selected.length) {
            selected.forEach((e) => {
                e.classList.remove('selected');
            })
        }
    }

    function resetPages() {
        togglePage();
        step = 0;
        setButtonsAndProgressBar();
        getPage();
    }

    function findValue(value) {
        return document.querySelector(value).value
    }

    function findProduct() {
        return document.querySelector('#total-product').getAttribute('class')
    }

    function phoneMask (phone) {
        return phone.replace(/\D/g, '')
                    .replace(/^(\d)/, '($1')
                    .replace(/^(\(\d{3})(\d)/, '$1) $2')
                    .replace(/(\d{3})(\d{1,3})/, '$1-$2')
                    .replace(/(-\d{4})\d+?$/, '$1');
    }

    function handleInput (e) {
        e.target.value = phoneMask(e.target.value)
    }

    function beginPage() {
        togglePage();
        tel.addEventListener('input', handleInput, false)
        form.addEventListener('submit', (e) => {
            e.preventDefault();
            makeRequest('/teklif-api');
        })
        refresh.addEventListener('click', resetPages);
    }

    document.addEventListener("DOMContentLoaded", beginPage);
})();