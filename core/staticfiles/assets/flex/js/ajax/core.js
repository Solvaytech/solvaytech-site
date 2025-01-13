async function makeRequest(url, method, body) {
    let headers = {
        'X-Requested-With': 'XMLHttpRequest',
        'Content-Type': 'application/json'
    };

    if (method == 'post') {
        const csrf = document.querySelector('[name=csrfmiddlewaretoken]').value
        headers['X-CSRFToken'] = csrf
    };

    let response = await fetch(url, {
        method: method,
        headers: headers,
        body: body
    });

    return await response.json();
}

async function download(token, fileID) {
    let headers = {
        'X-Requested-With': 'XMLHttpRequest',
        'Content-Type': 'application/json',
        'Autherization' : token
    };

    let url = "/get_file"

    await fetch(url, {
        method : 'get',
        headers : headers,
        })
        .then(response => 
            response.blob())
        .then(blob => {
            var url = window.URL.createObjectURL(blob);
            var a = document.createElement('a');
            a.href = url;
            a.download = "excel.xlsx";
            a.stlye = 'display:none;'
            document.querySelector('body').appendChild(a);
            a.click();
            a.remove();
        })
}