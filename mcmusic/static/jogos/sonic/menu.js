const options = document.querySelectorAll('.option');
let currentIndex = 0;

const menuMusic = document.getElementById('menu-music');
const selectSound = document.getElementById('select-sound');
selectSound.volume = 0.3


menuMusic.volume = 0.1;
menuMusic.pause();


document.body.addEventListener('click', () => {
    menuMusic.play();
}, { once: true });

function updateSelection() {
    options.forEach((opt, i) => {
        opt.classList.toggle('selected', i === currentIndex);
    });
    if(document.getElementById('nav-sound')) {
        const navSound = document.getElementById('nav-sound');
        navSound.currentTime = 0;
        navSound.play();
    }
}

document.addEventListener('keydown', (e) => {
    if(e.key === 'ArrowDown') {
        currentIndex = (currentIndex + 1) % options.length;
        updateSelection();
    } else if(e.key === 'ArrowUp') {
        currentIndex = (currentIndex - 1 + options.length) % options.length;
        updateSelection();
    } else if(e.key === 'Enter') {
        const action = options[currentIndex].dataset.action;
        const url = options[currentIndex].dataset.url;

        selectSound.currentTime = 0;
        selectSound.play();

        if(action === 'start') {
            document.querySelector('.menu-container').classList.add('fade-out');
            document.querySelector('.menu-bg').classList.add('fade-out');

            setTimeout(() => {
                window.location.href = url;
            }, 800);
        }
    }
});
