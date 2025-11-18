document.addEventListener("DOMContentLoaded", () => {
    const video = document.getElementById("bgVideo");
    const audio = document.getElementById("intro-music");
    
    audio.pause();

    document.body.addEventListener('click', () => {
        video.play();
        audio.play();
    }, { once: true });

    video.onended = () => {
        window.location.href = "/jogo/sonic/menu/";
    };
});
