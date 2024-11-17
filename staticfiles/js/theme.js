document.addEventListener('DOMContentLoaded', function() {
    const themeToggles = document.querySelectorAll('#theme-toggle');
    
    // Verifica o tema salvo
    const currentTheme = localStorage.getItem('theme') || 'light';
    document.documentElement.setAttribute('data-theme', currentTheme);
    
    themeToggles.forEach(toggle => {
        const icon = toggle.querySelector('i');
        updateIcon(icon, currentTheme);
        
        toggle.addEventListener('click', function() {
            const currentTheme = document.documentElement.getAttribute('data-theme');
            const newTheme = currentTheme === 'light' ? 'dark' : 'light';
            
            document.documentElement.setAttribute('data-theme', newTheme);
            localStorage.setItem('theme', newTheme);
            
            themeToggles.forEach(t => {
                updateIcon(t.querySelector('i'), newTheme);
            });
        });
    });
    
    function updateIcon(icon, theme) {
        if (theme === 'dark') {
            icon.classList.remove('fa-moon');
            icon.classList.add('fa-sun');
        } else {
            icon.classList.remove('fa-sun');
            icon.classList.add('fa-moon');
        }
    }
});
