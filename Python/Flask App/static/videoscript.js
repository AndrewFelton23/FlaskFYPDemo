// JavaScript code to display the video stream using the video element
const video = document.getElementById('video-stream');

function startVideoStream() {
    navigator.mediaDevices.getUserMedia({ video: true })
        .then(stream => {
            video.srcObject = stream;
        })
        .catch(error => {
            console.error('Error accessing the camera:', error);
        });
}

startVideoStream();