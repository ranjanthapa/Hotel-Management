document.addEventListener("DOMContentLoaded", function() {
    const nextButtons = document.querySelectorAll('.carousel-control-next');
    const prevButtons = document.querySelectorAll('.carousel-control-prev');

    nextButtons.forEach(button => {
        button.addEventListener('click', function(e) {
            e.preventDefault();
            const carousel = this.closest('.carousel');
            const activeItem = carousel.querySelector('.carousel-item.active');
            let nextItem = activeItem.nextElementSibling;
            if (!nextItem) {
                nextItem = carousel.querySelector('.carousel-item:first-child');
            }
            activeItem.classList.remove('active');
            nextItem.classList.add('active');
        });
    });

    prevButtons.forEach(button => {
        button.addEventListener('click', function(e) {
            e.preventDefault();
            const carousel = this.closest('.carousel');
            const activeItem = carousel.querySelector('.carousel-item.active');
            let prevItem = activeItem.previousElementSibling;
            if (!prevItem) {
                prevItem = carousel.querySelector('.carousel-item:last-child');
            }
            activeItem.classList.remove('active');
            prevItem.classList.add('active');
        });
    });
});
