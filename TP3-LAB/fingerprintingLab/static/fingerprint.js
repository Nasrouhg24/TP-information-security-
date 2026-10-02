// Ask the navigator object for the browser’s preferred language
const browserLanguage = navigator.language;

// Display the collected value in the Developer Tools console
console.log("Browser language:", browserLanguage);

// Find the HTML element whose identifier is "feature-output"
const outputElement = document.getElementById("feature-output");

// Display the collected value inside the webpage
outputElement.textContent = "Browser language: " + browserLanguage;

// Resolution
const resolution = {x: screen.width,y: screen.height};
outputElement.textContent +="\n Resolution: " + resolution.x + "x" + resolution.y;


// Device pixel ratio
const devicePixelRatio = window.devicePixelRatio;
outputElement.textContent +="\n Pixel Resolution: " + devicePixelRatio;

// CPU cores
const CPUcores = navigator.hardwareConcurrency;
outputElement.textContent +="\n CPU cores: " + CPUcores;
// Device memory
const memory = navigator.deviceMemory;
outputElement.textContent +="\n Device Memory: " + memory;

// Timezone
const Timezone = Intl.DateTimeFormat().resolvedOptions().timeZone;
outputElement.textContent +="\n Time Zone: " + Timezone;



const fingerprint = {
    browserLanguage: browserLanguage,
    Resolution: resolution.x + "x" + resolution.y,
    DevicePixelResolution: devicePixelRatio,
    CPUcores: CPUcores,
    deviceMemory: memory,
    Timezone: Timezone
};

fetch("/fingerprint", {
    method: "POST",
    headers: {
        "Content-Type": "application/json"
    },
    body: JSON.stringify(fingerprint)
});



//TAsk 3 
const input = document.getElementById("typing-input");
const target = document.getElementById("target-sentence");
const resetButton = document.getElementById("reset-button");
const typingTime = document.getElementById("typing-time");
const typingSpeed = document.getElementById("typing-speed");
const typingCorrections = document.getElementById("typing-corrections");
let startTime = null;
let corrections = 0;



// Start the timer when Alice starts typing
input.addEventListener("input", function () {
    console.log("Current input:", input.value);
    console.log("Target:", target.textContent.trim());
    if (startTime === null && input.value.length > 0) {
        startTime = Date.now();
    }

    // Check whether the sentence has been reproduced
    if (input.value === target.textContent.trim()) {
        const endTime = Date.now();
        const totalTime = (endTime - startTime) / 1000;
        // # of words in the sentence target 
        const wordCount = target.textContent.trim().split(/\s+/).length;
        // Words per minute
        const speed = (wordCount / totalTime) * 60;
        typingTime.textContent ="Total typing time: " + totalTime.toFixed(2) + " seconds";
        typingSpeed.textContent ="Typing speed: " + speed.toFixed(2) + " words/minute";
        typingCorrections.textContent ="Number of corrections: " + corrections;

        // Sending to flask 
        fetch("/typing-results", {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify({
                typing_time: totalTime,
                typing_speed: speed,
                corrections: corrections
            })
        })
        .then(response => response.json())
        .then(data => {
            console.log("Server response:", data);
        })
        .catch(error => {
            console.error("Error sending typing results:", error);
        });
    
   
    }
});


// Count Backspace and Delete as corrections
input.addEventListener("keydown", function (event) {
    if (event.key === "Backspace" || event.key === "Delete") {
        corrections++;
    }
});


// Reset 
resetButton.addEventListener("click", function () {
    input.value = "";
    startTime = null;
    corrections = 0;
    typingTime.textContent = "";
    typingSpeed.textContent = "";
    typingCorrections.textContent = "";
    input.focus();
});




// Last Part : producing the hash 
const combinedFeatures = browserLanguage + "|" +resolution + "|" +devicePixelRatio + "|" +CPUcores + "|" +memory+ "|" +Timezone;
console.log("Combined features:", combinedFeatures);


// now to sha 
async function generateFingerprint() {

    // string -> bytes
    const encoder = new TextEncoder();
    const data = encoder.encode(combinedFeatures);

    // sha-256
    const hashBuffer = await crypto.subtle.digest("SHA-256",data);

    //  hash bytes -> hexadecimal
    const hashArray = Array.from(new Uint8Array(hashBuffer));

    const fingerprint = hashArray.map(byte => byte.toString(16).padStart(2, "0")).join("");

    // Display fingerprint
    document.getElementById("fingerprint-hash").textContent =fingerprint;

    console.log("SHA-256 fingerprint:", fingerprint);


   

    fetch("/fingerprint-hash", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({
            fingerprint: fingerprint
        })
    })
    .then(response => response.json())
    .then(data => {
        console.log("Server response:", data);
    })
    .catch(error => {
        console.error("Error sending fingerprint:", error);
    });
}


// Calling the funct
generateFingerprint();