(function () {
    "use strict";

    async function adminRequest(url) {
        let response = await fetch(url, {
            method: 'get',
            headers: {
                'X-Requested-With': 'XMLHttpRequest',
                'Content-Type': 'application/json',
            }
        })
        .then(response => {
            if(response.ok) {
                return response.json();
            } else {
                console.log(`${response.status} ${response.statusText} ${response.url}`); 
            }
        })
        .then(data => {
            console.log(data);
        })
    }

    adminRequest('/et6dGgvOhHundfaDOZwJ3Uu1AYMOSN')
})();