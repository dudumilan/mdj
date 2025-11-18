window.addEventListener('load', () => {
    const video = document.getElementById('bgVideo');
    const music = document.getElementById('bgMusic');
    let clicked = false;

    document.body.addEventListener('click', () => {
        if (!clicked) {
            
            if (video) {
                video.muted = false; 
                video.play().catch(err => console.log("Erro ao tocar vídeo:", err));
            }
            if (music) {
                music.play().catch(err => console.log("Erro ao tocar música:", err));
            }
            clicked = true;
        } else {
           
            window.location.href = '/jogo/streetfighter2/menu/';
        }
    });
});
