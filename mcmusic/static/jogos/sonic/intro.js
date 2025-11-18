window.addEventListener('load', () => {
    const video = document.getElementById('bgVideo');
    const music = document.getElementById('bgMusic');
    let clicked = false;

    document.body.addEventListener('click', () => {
        if (!clicked) {
            // Primeira vez: toca vídeo e música
            if (video) {
                video.muted = false; // caso queira som do vídeo também
                video.play().catch(err => console.log("Erro ao tocar vídeo:", err));
            }
            if (music) {
                music.play().catch(err => console.log("Erro ao tocar música:", err));
            }
            clicked = true;
        } else {
            // Segunda vez: troca de página
            window.location.href = '/outra-pagina/'; // substitua pela URL desejada
        }
    });
});
