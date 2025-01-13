function getCookie(cookie_name) {
    const value = "; " + document.cookie;
    const parts = value.split("; " + cookie_name + "=");
    if (parts.length === 2) return parts.pop().split(";").shift();
}

function setCookie(cookie_name, cookie_value) {
    document.cookie = cookie_name + "=" + cookie_value + ";" + "path=/";
}

function deleteCookie(cookie_name) {
    document.cookie = cookie_name + "= ; expires=Thu, 01 Jan 1970 00:00:00 GMT; path=/";
}
