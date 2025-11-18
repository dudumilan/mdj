window.addEventListener('load', () => {
    const video = document.getElementById('bgVideo');
    if (video) {
        video.muted = true; // garante autoplay sem bloqueio
        video.play().catch(err => console.log("Autoplay do vídeo bloqueado:", err));
    }

    const music = document.getElementById('bgMusic');
    if (music) {
        let musicStarted = false;

        document.body.addEventListener('click', () => {
            if (!musicStarted) {
                music.play().catch(err => console.log("Erro ao tocar música:", err));
                musicStarted = true;
            }
        });
    }
});
