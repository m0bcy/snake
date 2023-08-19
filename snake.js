// Create WebSocket connection.
const socket = new WebSocket("ws://localhost:8765");

// Listen for messages
socket.addEventListener("message", (event) => {
    console.log("Message from server ", event.data);
    document.getElementById('tx').innerHTML = event.data;
});

function foo() {
    socket.send("Hello Server!");
}
