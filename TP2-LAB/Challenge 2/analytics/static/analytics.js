function getCookie(name) {
    const cookies = document.cookie.split(";");

    for (let cookie of cookies) {
        cookie = cookie.trim();

        if (cookie.startsWith(name + "=")) {
            return cookie.substring(name.length + 1);
        }
    }

    return null;
}


let analyticsId = getCookie("analytics_id");

if (!analyticsId) {
    //Generating rand ID
    analyticsId = Array.from(crypto.getRandomValues(new Uint8Array(16)), b => b.toString(16).padStart(2, "0")).join("");

    //store 
    document.cookie = `analytics_id=${analyticsId}; Path=/`;

    console.log("New analytics ID created:", analyticsId);
} else {
    console.log("Existing analytics ID:", analyticsId);
}


// Send browsing activity to the analytics server
const page = window.location.href;

const analyticsUrl =
    "http://analytics.test:9100/collect" +
    "?id=" + encodeURIComponent(analyticsId) +
    "&page=" + encodeURIComponent(page);

fetch(analyticsUrl)//send the data 
    .then(response => response.text())
    .then(data => {
        console.log("Analytics server response:", data);
    })
    .catch(error => {
        console.error("Analytics request failed:", error);
    });