let currentIndex = 0;

window.addEventListener("load", function () {
    renderGames();
});

function renderGames() {
    const display = document.getElementById("gameDisplay");
    display.innerHTML = '';

    if (!games || games.length === 0) {
        display.innerHTML = "<p>Nenhum jogo encontrado.</p>";
        return;
    }

    const prevIndex = (currentIndex - 1 + games.length) % games.length;
    const nextIndex = (currentIndex + 1) % games.length;

    const prevGame = games[prevIndex];
    const mainGame = games[currentIndex];
    const nextGameObj = games[nextIndex];

    const prevDiv = document.createElement("div");
    prevDiv.className = "game side-game";
    prevDiv.style.backgroundImage = `url('${prevGame.image}')`;
    prevDiv.onclick = () => prevGameClick();
    display.appendChild(prevDiv);

    const mainDiv = document.createElement("div");
    mainDiv.className = "game main-game";
    mainDiv.style.backgroundImage = `url('${mainGame.image}')`;
    mainDiv.onclick = () => openPortal(`/jogo/${mainGame.id}/`);
    display.appendChild(mainDiv);

    const nextDiv = document.createElement("div");
    nextDiv.className = "game side-game";
    nextDiv.style.backgroundImage = `url('${nextGameObj.image}')`;
    nextDiv.onclick = () => nextGame();
    display.appendChild(nextDiv);
}

function nextGame() {
    currentIndex = (currentIndex + 1) % games.length;
    renderGames();
}

function prevGame() {
    currentIndex = (currentIndex - 1 + games.length) % games.length;
    renderGames();
}

function prevGameClick() {
    prevGame();
}

function openPortal(url) {
    const portal = document.getElementById("portalOverlay");

    if (!portal) {
        window.location.href = url;
        return;
    }

    portal.classList.add("portal-active");

    setTimeout(() => {
        window.location.href = url;
    }, 900);
}
