var cards = {
    card1: {
        pic: "https://fakeimg.pl/700x250",
        title: "This is our first title",
        desc: "this is a wider card with supporting text below as a natural lead-in to additional content. This content is a little bit longer.",
        date: "1 / March"
    },
    card2: {
        pic: "https://fakeimg.pl/700x250",
        title: "Second Title",
        desc: "Second description",
        date: "28 / February"

    },
    card3: {
        pic: "https://fakeimg.pl/700x250",
        title: "Third",
        desc: "this is a wider card with supporting text below as a natural lead-in to additional content. This content is a little bit longer.",
        date: "27 / February"
    },
    card4: {
        pic: "https://fakeimg.pl/700x250",
        title: "Fourth Card",
        desc: "Fourth description",
        date: "22 / February"
    },
    card5: {
        pic: "https://fakeimg.pl/700x250",
        title: "Game news network",
        desc: "our news",
        date: "21 / February"
    },
    card6: {
        pic: "https://fakeimg.pl/700x250",
        title: "out of ideas",
        desc: "sixth description",
        date: "20 / February"
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
