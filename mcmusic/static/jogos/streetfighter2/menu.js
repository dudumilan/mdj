const items = document.querySelectorAll('.sf2-item');
let selectedIndex = 0;


function playSound(id) {
    const audio = document.getElementById(id);
    if(audio) {
        audio.currentTime = 0.1;
        audio.play();
    }
}

window.addEventListener('load', () => {
    playSound('ready');
});


items.forEach((item, index) => {
    setTimeout(() => {
        item.style.opacity = '1';
        item.style.transform = 'scale(1)';
        playSound(item.dataset.sound);
    }, index * 200); 
});


items[selectedIndex].classList.add('selected');


items.forEach((item, index) => {
    item.addEventListener('mouseenter', () => {
        items[selectedIndex].classList.remove('selected');
        selectedIndex = index;
        item.classList.add('selected');
        playSound(item.dataset.sound);
    });

    item.addEventListener('click', () => {
        confirmSelection();
    });
});


document.addEventListener('keydown', e => {
    items[selectedIndex].classList.remove('selected');
    const rowLength = 4;

    switch(e.key) {
        case 'ArrowRight':
            selectedIndex = (selectedIndex + 1) % items.length;
            break;
        case 'ArrowLeft':
            selectedIndex = (selectedIndex - 1 + items.length) % items.length;
            break;
        case 'ArrowDown':
            selectedIndex = (selectedIndex + rowLength) % items.length;
            break;
        case 'ArrowUp':
            selectedIndex = (selectedIndex - rowLength + items.length) % items.length;
            break;
        case 'Enter':
            confirmSelection();
            break;
    }

    items[selectedIndex].classList.add('selected');
    playSound(items[selectedIndex].dataset.sound);
});


function confirmSelection() {
    playSound('confirm');
    vsZoom();
    setTimeout(() => {
       
        window.location.href = "/jogo/streetfighter2/historia/";
    }, 3100);
}



function vsZoom() {
    const vs = document.querySelector('.vs-animation');
    vs.style.transform = 'translate(-50%, -50%) scale(1.5)';
    setTimeout(() => {
        vs.style.transform = 'translate(-50%, -50%) scale(1)';
    }, 300);
}
const previewImage = document.getElementById('previewImage');

function updatePreview() {
    const currentItem = items[selectedIndex];
    const character = currentItem.dataset.character;
    previewImage.src = `/static/jogos/streetfighter2/imagens/preview/${character}.png`;
}


items.forEach((item, index) => {
    item.addEventListener('mouseenter', () => {
        items[selectedIndex].classList.remove('selected');
        selectedIndex = index;
        item.classList.add('selected');
        playSound(item.dataset.sound);
        updatePreview();
    });
});

document.addEventListener('keydown', e => {
    items[selectedIndex].classList.remove('selected');
    const rowLength = 6; 

    let moved = false;

    switch(e.key) {
        case 'ArrowRight':
            if ((selectedIndex + 1) % rowLength !== 0 && selectedIndex < items.length-1) {
                selectedIndex++;
                moved = true;
            }
            break;
        case 'ArrowLeft':
            if (selectedIndex % rowLength !== 0) {
                selectedIndex--;
                moved = true;
            }
            break;
        case 'ArrowDown':
            if (selectedIndex + rowLength < items.length) {
                selectedIndex += rowLength;
                moved = true;
            }
            break;
        case 'ArrowUp':
            if (selectedIndex - rowLength >= 0) {
                selectedIndex -= rowLength;
                moved = true;
            }
            break;
        case 'Enter':
            confirmSelection();
            break;
    }

    items[selectedIndex].classList.add('selected');
    playSound(items[selectedIndex].dataset.sound);

    if(moved) updatePreview();
});

updatePreview();
