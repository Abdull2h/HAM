var uid = 0 //html id for user card
$(document).ready(function () {
    $("#myButton").click(function () {
        $.ajax({
            type: 'GET',
            url: 'https://reqres.in/api/users',
        }).done(function (resp) {
            if (uid <= 5) {
                for (key in resp.data) {
                    $("#users").append(`
                        <div class="col mb-4" id="`+ uid + `"style="display:none;">
                        <div class="card">
                        <img src="${resp.data[key].avatar}" class="card-img-top" alt="...">
                        <div class="card-body">
                        <h5 class="card-title">${resp.data[key].id}- ${resp.data[key].first_name} ${resp.data[key].last_name}</h5>
                        <p class="card-text">${resp.data[key].email}</p>
                        </div>
                        </div>
                        </div>`);
                    $("#" + uid).fadeIn(3000);
                    uid += 1
                }//for loop end
            } //if statement end
        });
    });
})

