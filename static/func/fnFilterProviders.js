function filterProviders() {
    const input = document.getElementById('searchInput');
    const filter = input.value.toLowerCase();
    const grid = document.getElementById('providerGrid');
    const cards = grid.getElementsByClassName('provider-card');

    for (let i = 0; i < cards.length; i++) {
        const name = cards[i].getAttribute('data-name').toLowerCase();
        const trade = cards[i].getAttribute('data-trade').toLowerCase();
        
        if (name.includes(filter) || trade.includes(filter)) {
            cards[i].style.display = "";
        } else {
            cards[i].style.display = "none";
        }
    }
}
