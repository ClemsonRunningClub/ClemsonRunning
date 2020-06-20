/* Toggle between adding and removing the "responsive" class to topnav when the user clicks on the icon */
/* In order to change /routes, must change assets/script.js (this code)
   and /pages/templates/info/routes.html */
function myFunction() {
    var x = document.getElementById("myTopnav");
    if (x.className === "topnav") {
        x.className += " responsive";
    } else {
        x.className = "topnav";
    }
}

document.addEventListener("touchstart", function(){}, true)

var routes = ["https://bit.ly/2LGL9XJ","https://bit.ly/2t2kE81", "https://bit.ly/2LVUAT4",
  "https://bit.ly/2LSMOcM", "https://bit.ly/2LUOAKl", "https://bit.ly/2LUOXod",
  "https://bit.ly/2LTpY4x", "https://bit.ly/2LTqvDz", "https://bit.ly/2LR3txh",
  "https://bit.ly/2LVY48e", "https://bit.ly/2LVdOrV", "https://bit.ly/2LWmEG1"];

var routeNames = ["Short Perimeter ~ 3.14 Miles", "Botanical Garden ~ 3.84 Miles", "Y Beach Loop ~ 4.00 Miles",
  "Long Perimeter ~ 4.34 Miles", "Dikes Loop (Clockwise) ~ 4.78 Miles", "Dabo Loop ~ 4.83 Miles",
  "Dikes Loop (Counterclockwise) ~ 4.84 Miles", "Golf Course Neighborhoods ~ 5.12 Miles", "Old Central (Clockwise) ~ 6.27 Miles",
  "Old Central (Counterclockwise) ~ 6.27 Miles", "Full Neighborhoods ~ 5.40 Miles" , "Country Walk ~ 6.53 Miles"];

function loadMap(routeNum) {
    $("#rtmap").attr("src", routes[routeNum]);
    $("#rtmap-header").text(routeNames[routeNum]);
    var id = "#" + routeNum
    $(".rt-list .list-group-item").removeClass("active");
    $(id).addClass("active");
    $("#rt-link").attr("href", routes[routeNum]);
}

$(function () {
  $('[data-toggle="tooltip"]').tooltip()
})
