const showStatus = document.getElementById('show_status');

window.addEventListener('online', (e) => {
    // User is online  https://github.com/sanchezzzhak/node-device-detector
    showStatus.innerText = 'You are online';
});

window.addEventListener('offline', (e) => {
    // User is offline https://github.com/MuminjonGuru/UserStackAPIDemoNodeJS
    showStatus.innerText = 'You are offline';
});
