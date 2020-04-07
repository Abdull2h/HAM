var cards = {
    card1: {
        pic: "https://psmedia.playstation.com/is/image/psmedia/ps.com-listing-thumb-01-eu-09may18?$Icon$",
        title: "Sony Launches $100 Million COVID-19 Relief Fund",
        desc: "Sony is seeking ways to support creative communities and help with lost education opportunities by using its technological expertise.",
        date: "April 4, 2020"

    },
    card2: {
        pic: "https://specials-images.forbesimg.com/imageserve/5e84dce0a1a0ef0006051022/960x0.jpg?fit=scale",
        title: "Call of Duty: Modern Warfare 2 Campaign Remastered Is Official and Out Now",
        desc: "Modern Warfare 2 Campaign Remastered has officially launched on PS4.",
        date: "April 1, 2020"
    },
    card3: {
        pic: "https://onlysp.escapistmagazine.com/wp-content/uploads/2020/03/Rockstar-Games-logo-expanded-v2-800x400.png",
        title: "Rockstar Games Will Donate 5% Of In-Game Revenue To COVID-19 Relief",
        desc: "The money will go towards small businesses and communities struggling due to the effects of COVID-19.",
        date: "March 30, 2020"
    },
    card4: {
        pic: "https://images.pushsquare.com/f3c617d139561/cyberpunk-2077-delay-ps4-xbox-one.900x.jpg",
        title: "Cyberpunk 2077's Updated Female Protagonist Is Now an Incredible Figurine",
        desc: "Pure Arts is releasing a new figurine of Cyberpunk 2077's updated female protagonist.",
        date: "March 28, 2020"
    },
    card5: {
        pic: "https://static-ca.ebgames.ca/images/products/729000/3max.jpg",
        title: "Nintendo of America Temporarily Shuts Down Repair Facilities",
        desc: "The closures are a response to governmental guidelines regarding COVID-19",
        date: "March 27, 2020"
    }

}

$(document).ready(function () {
    for (var key in cards) {
        $("#cardGet").append(
            `<div class="card border-info rounded mb-3">
        <img src="`+ cards[key].pic + `" class="card-img-top" alt="..."></img>
        <div class="card-body">
        <h5 class="card-title text-info text-center">`+ cards[key].title + `</h5>
        <p class="card-text text-justify">`+ cards[key].desc + `</p>
        <p class="card-text"><small class="text-muted">`+ cards[key].date + `</small></p></div></div>`);
    }
});
