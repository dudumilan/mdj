const titleText = "HISTORIA";
const storyText = `No vibrante mundo de Green Hill, o malvado Dr. Robotnik captura animais inocentes, 
transformando-os em máquinas cruéis. Apenas Sonic, o ouriço mais rápido do planeta, pode detê-lo. 
Corra através de colinas, coletando anéis e enfrentando perigos, enquanto embarca em uma aventura épica 
para salvar seus amigos e restaurar a paz em seu mundo.`;

const creditsText = `Criadores: Yuji Naka e Naoto Ohshima
Empresa: SEGA
Console de Lançamento: SEGA Mega Drive (1991)`;

const faseBg = document.querySelector('.fase-bg');
let clickCount = 0;

const storyMusic = document.createElement('audio');
storyMusic.src = '/static/jogos/sonic/musicas/green_hill.mp3';
storyMusic.loop = true;
storyMusic.volume = 0.1;
storyMusic.pause();

const backButton = document.createElement('img');
backButton.id = 'backButton';
backButton.src = '/static/jogos/sonic/imagens/moeda.png'; 
backButton.style.height = '100px';
backButton.style.display = 'none';
backButton.style.position = 'absolute';
backButton.style.bottom = '20px';
backButton.style.right = '20px';
backButton.style.cursor = 'pointer';
faseBg.appendChild(backButton);

backButton.addEventListener('click', () => {
    window.location.href = "/"; 
});



function startAnimation() {
    storyMusic.play();

    const title = document.createElement('div');
    title.classList.add('fase-title');
    title.textContent = titleText;
    faseBg.appendChild(title);

    setTimeout(() => {
        title.classList.add('fade-out');
        setTimeout(() => {
            title.style.display = 'none';
            faseBg.style.background = "url('/static/jogos/sonic/imagens/green_hill.gif') no-repeat center center";
            faseBg.style.backgroundSize = "cover";

            const storyDiv = document.createElement('div');
            storyDiv.classList.add('story-text');
            storyDiv.textContent = storyText;
            faseBg.appendChild(storyDiv);

            faseBg.addEventListener('click', () => {
                clickCount++;
                if(clickCount === 1){
                    storyDiv.classList.add('fade-out-text');
                    setTimeout(() => {
                        storyDiv.style.display = 'none';
                        const creditsDiv = document.createElement('div');
                        creditsDiv.classList.add('story-text');
                        creditsDiv.textContent = creditsText;
                        faseBg.appendChild(creditsDiv);
                    }, 800);
                } else if(clickCount === 2){
                    backButton.style.display = 'block'; 
                }
            });
        }, 1200);
    }, 2000);
}

faseBg.addEventListener('click', startAnimation, { once: true });
