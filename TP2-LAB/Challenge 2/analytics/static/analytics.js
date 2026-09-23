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
    //generate a random id
    // crypto.randomUUID() only exists in secure contexts (HTTPS/localhost); *.test over HTTP is not one
    analyticsId = Array.from(crypto.getRandomValues(new Uint8Array(16)), b => b.toString(16).padStart(2, "0")).join("");
    //store it 
    document.cookie = `analytics_id=${analyticsId}; Path=/`;

    console.log("New analytics ID created:", analyticsId);
} else {
    console.log("Existing analytics ID:", analyticsId);
}