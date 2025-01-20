let lastScroll = 0;
const navbar = document.querySelector('.navbar');

window.addEventListener('scroll', () => {
    const currentScroll = window.pageYOffset;
    if (currentScroll > lastScroll && currentScroll > 60) {
        // Скролл вниз — скрыть навбар
        navbar.classList.add('hidden');
    } else {
        // Скролл вверх — показать навбар
        navbar.classList.remove('hidden');
    }
    lastScroll = currentScroll;
});


const video = document.getElementById('myVideo');

function playVideo() {
    video.play();
}

function pauseVideo() {
    video.pause();
}