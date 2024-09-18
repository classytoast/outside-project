const forecastDivs = document.querySelectorAll('.forecast_col');

forecastDivs.forEach(div => {
    div.addEventListener("click", () => {
        const day = div.getAttribute('data-day');
        showHourlyData(day);
    });
});

function showHourlyData(day) {
    const container = document.getElementById('hourlyDataContainer');
    
    container.innerHTML = '';

    for (let hour in daily_data[day]['hours_data']) {
        const p = document.createElement('p');
        
        p.textContent = daily_data[day]['hours_data'][hour];

        p.classList.add('dynamic');
        
        container.appendChild(p);

        setTimeout(() => {
            p.classList.add('show');  // Добавляем класс, который активирует плавное появление
        }, 50);
    }

}