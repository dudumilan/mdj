function openPortal(url, imgUrl) {
    const portal = document.getElementById("portalOverlay");
    const portalZoom = document.getElementById("portalZoom");

    if (!portal || !portalZoom) {
        window.location.href = url;
        return;
    }

    portalZoom.style.backgroundImage = `url('${imgUrl}')`;

    
    portal.classList.add("active");

    setTimeout(() => {
        window.location.href = url;
    }, 800); 
}
