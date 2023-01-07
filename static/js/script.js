$(function () {
    $('.cart').on('click', function (e) {
        swal('Carrinho', 'produto adcionado', 'success');
        e.preventDefault();
        $.ajax({
            url: $(this).attr('href'),
            dataType: 'json',
            success: function (data, textStatus, jqXHR) {
                
            }
        });
    });
});


