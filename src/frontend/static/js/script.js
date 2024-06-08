document.addEventListener("DOMContentLoaded", () => {
    const video = document.getElementById("video");

    // Access the webcam
    navigator.mediaDevices.getUserMedia({ video: true })
        .then(stream => {
            video.srcObject = stream;
        })
        .catch(err => console.error("Error accessing webcam: ", err));

    // Setup WebSocket connection
    const socket = new WebSocket("ws://localhost:5000/ws");

    socket.onopen = () => {
        console.log("WebSocket connection established.");
    };

    socket.onmessage = (event) => {
        const data = JSON.parse(event.data);
        document.getElementById("output").innerText = `Gesture: ${data.gesture}`;
    };

    // Capture video frame and send to backend for processing
    function captureFrame() {
        const canvas = document.createElement("canvas");
        canvas.width = video.videoWidth;
        canvas.height = video.videoHeight;
        const context = canvas.getContext("2d");
        context.drawImage(video, 0, 0, canvas.width, canvas.height);

        // Convert frame to base64
        const frame = canvas.toDataURL("image/jpeg");

        // Send frame to backend via WebSocket
        socket.send(JSON.stringify({ frame: frame }));
    }

    // Capture frame every second
    setInterval(captureFrame, 1000);
});
