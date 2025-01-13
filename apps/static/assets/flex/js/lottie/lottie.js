function startAnimation() {
    var animation = bodymovin.loadAnimation({
        container : document.getElementById('target'),
        path : "static/assets/flex/js/lottie/json/left-confeti.json",
        render : "html",
        width : "auto",
        height : "auto",
        loop : true,
        autoplay : true,
    });
};

document.addEventListener("DOMContentLoaded", function() {
    startAnimation();
});