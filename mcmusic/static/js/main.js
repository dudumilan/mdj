window.addEventListener("load", function() {
const games = [
    {
      title: "Super Mario Bros",
      image: "{% static 'img/mario.png' %}"
    },
    {
      title: "The Legend of Zelda",
      image: "{% static 'img/zelda.png' %}"
    },
    {
      title: "Street fighters II",
      image: "{% static 'img/street fighter.png' %}"
    },
    {
      title: "Sonic the Hedgehog",
      image: "{% static 'img/sonic.jpg' %}"
    },
    {
      title: "Donkey Kong Country",
      image: "{% static 'img/kong.png' %}"
    },
    {
      title: "Mortal Kombat",
      image: "{% static 'img/mk.jpg' %}"
    },
    {
      title: "Mega Man 2",
      image: "{% static 'img/megaman.jpg' %}"
    },
    {
      title: "Castlevania",
      image: "{% static 'img/castel.png' %}"
    },
  ];

  let currentIndex = 0;

  function renderGames() {
    const display = document.getElementById("gameDisplay");
    display.innerHTML = '';

    const prevIndex = (currentIndex - 1 + games.length) % games.length;
    const nextIndex = (currentIndex + 1) % games.length;

    const prevGame = games[prevIndex];
    const mainGame = games[currentIndex];
    const nextGame = games[nextIndex];

    const prevDiv = document.createElement("div");
    prevDiv.className = "game side-game";
    prevDiv.style.backgroundImage = `url('${prevGame.image}')`;
    display.appendChild(prevDiv);

    const mainDiv = document.createElement("div");
    mainDiv.className = "game main-game";
    mainDiv.style.backgroundImage = `url('${mainGame.image}')`;
    display.appendChild(mainDiv);

    const nextDiv = document.createElement("div");
    nextDiv.className = "game side-game";
    nextDiv.style.backgroundImage = `url('${nextGame.image}')`;
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

  renderGames();

});