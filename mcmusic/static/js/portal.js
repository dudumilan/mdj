function openPortalAndGo(url) {
    const overlay = document.getElementById("portalOverlay");
    overlay.classList.add("active");

    setTimeout(() => {
        window.location.href = url;
    }, 700);
}
