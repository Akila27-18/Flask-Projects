document.addEventListener("DOMContentLoaded", () => {
    const ctx = document.getElementById('tempChart').getContext('2d');
    new Chart(ctx, {
        type: 'line',
        data: {
            labels: ['6 AM', '8 AM', '10 AM', '12 PM', '2 PM', '4 PM', '6 PM'],
            datasets: [{
                label: 'Temperature (°C)',
                data: hourlyTemps,
                borderColor: 'orange',
                backgroundColor: 'rgba(255,165,0,0.2)',
                fill: true,
                tension: 0.3
            }]
        },
        options: {
            scales: {
                y: {
                    beginAtZero: false
                }
            }
        }
    });
});
