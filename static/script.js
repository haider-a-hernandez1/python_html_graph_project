// Example script to highlight rows when clicked
document.querySelectorAll('tr').forEach(row => {
    row.addEventListener('click', () => {
        row.style.backgroundColor = '#f0f0f0';
    });
});
