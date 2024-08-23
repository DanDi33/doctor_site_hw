$(document).ready(function () {

    $('#feedbackModal').on('show.bs.modal', function (event) {
                var button = $(event.relatedTarget); // Кнопка, которая активировала модальное окно
                var img = button.data('img'); // Извлечение информации из атрибутов data-*
    
                var modal = $(this);
                modal.find('.modal-body #feedbackModalImage').attr('src', img); // Устанавливаем URL изображения в src атрибут      
            });

    $('.slider').slick(
        {
            arrows: true,
            dots: true,
            adaptiveHeight: true,
            slidesToShow: 3,
            slidesToScroll: 1,
            autoplay: true,
            autoplaySpeed: 3000,
            responsive: [
                {
                    breakpoint: 1024,
                    settings: {
                        slidesToShow: 2,
                        slidesToScroll: 1,
                        infinite: true,
                        dots: true
                    }
                },
                {
                    breakpoint: 600,
                    settings: {
                        slidesToShow: 1,
                        slidesToScroll: 1
                    }
                }
            ]
        }
    );
})