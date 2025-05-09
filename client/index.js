function onClickedEstimatePrice() {
    const sqft = parseFloat(document.getElementById("uiSqft").value);
    const bhk = parseInt(document.getElementById("uiBHK").value);
    const bath = parseInt(document.getElementById("uiBathrooms").value);
    const floor = parseInt(document.getElementById("uiFloor").value);
    const location = document.getElementById("uiLocations").value;
    const estPrice = document.getElementById("uiEstimatedPrice");

    $.post("http://127.0.0.1:5000/predict_home_price", {
        land_area: sqft,
        location: location,
        floor: floor,
        bhk: bhk,
        bathroom: bath
    }, function(data) {
        estPrice.innerHTML = "<h2>Estimated Price: " + data.estimated_price;
    });
}

function onPageLoad() {
    $.get("http://127.0.0.1:5000/get_location_names", function(data) {
        const locations = data.locations;
        const uiLocations = document.getElementById("uiLocations");
        $('#uiLocations').empty();
        $('#uiLocations').append(new Option("Choose a Location", ""));
        for (let i in locations) {
            const opt = new Option(locations[i]);
            $('#uiLocations').append(opt);
        }
    });
}

window.onload = onPageLoad;
