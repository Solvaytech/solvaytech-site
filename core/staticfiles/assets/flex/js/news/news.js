(function () {
    "use strict";
    let news_container = document.getElementById('news-container');
    newsRequest('/news-api', news_container);

    function createNews(container, key, src_img, desc, news_link) {
        let col = document.createElement('div');
        col.className = 'col news-col';
        container.appendChild(col);
        let card = document.createElement('div');
        card.className = 'card shadow-sm'
        col.appendChild(card);
        let img = document.createElement('img');
        img.setAttribute('src', src_img);
        img.className= 'news-img';
        card.appendChild(img);
        let card_body = document.createElement('div');
        card_body.className = 'card-body';
        card.appendChild(card_body);
        let key_text = document.createElement('p');
        key_text.className = "h5 text-muted";
        key_text.innerText = key;
        card_body.appendChild(key_text);
        let card_text = document.createElement('p');
        card_text.className = "card-text";
        card_text.innerText = desc;
        card_body.appendChild(card_text);
        let button_div = document.createElement('div');
        button_div.className = "d-flex justify-content-end align-items-center";
        card_body.appendChild(button_div);
        let btn_group = document.createElement('div');
        btn_group.className = "btn-group";
        button_div.appendChild(btn_group);
        let link = document.createElement('a');
        link.setAttribute('href', news_link);
        btn_group.appendChild(link);
        let button = document.createElement('button');
        button.setAttribute('type', 'button');
        button.className = "btn btn-sm btn-outline-secondary";
        button.innerText = "Haberin devamı için tıklayınız.!";
        link.appendChild(button);
    }

    
    async function newsRequest(url, container) {
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
                throw new Error(`${response.status} ${response.statusText} ${response.url}`); 
            }
        })
        .then(data => {
            if (data['response']) {
                for (let key in data){
                    if (key == 'response') {
                        continue;
                    }
                    createNews(container, key, data[key].img_jpg, data[key].desc, data[key].link)
                }
            }
        })
        .catch((error) => {
            console.log(error)
        })
    }
})();