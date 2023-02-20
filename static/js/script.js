$(function () {
    $('.cart').on('click', function (e) {
        swal('Carrinho', 'produto adcionado', 'success');
        e.preventDefault();
        $.ajax({
            url: $(this).attr('href'),
            dataType: 'json',
            success: function (data, textStatus, jqXHR) {
                alert('adcionado ao carrinho');
            }
        });
    });
});


// set up jQuery ajax object to always send CSRF token in headers
// https://docs.djangoproject.com/en/2.2/ref/csrf/#ajax
function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}
const csrftoken = getCookie('csrftoken')


$(document).ready(function () {
    $('.form').on('click', function (e) {
        let url = this.id;


        // let postData = $('form').serialize();
        e.preventDefault();
        console.log(url)
        $.ajax({
            url: url,
            // dataType: 'html',
            type: 'GET',
            data: $('form').serialize(),
            success: function (data) {
                $('#form_update').html(data)

                // swal('Update', url, 'success');
                // addItem(response)
            },
            // error: function (xhr) {
            //     console.log('Erro');
            // },
            // complete: function () {
            //     // closeModal()
            // }
        });

    });

});



// function total() {
//     document.addEventListener("DOMContentLoaded", function () {

//         var tabela = document.body.querySelectorAll("table th:nth-child(3), table td:nth-child(3)").innerHTML;

//         for (var x = 0; x < tabela.length; x++) {
//             console.log(tabela[x]);
//         }

//     });
    // var valores = document.querySelectorAll("tr");
    // for (i = 0; i < valores.length; i++) {
    //     var name = 'form-' + i + '-quantity'
    //     // pegar a td com classe quantity pra pegar o imput com name form-0-quantity
    //     const el = document.querySelector('td.quantity input[name='+name+']').value;
        
    //     // console.log(valores[i].innerHTML);
    //     console.log(el)
    // }



// function total() {
    
//     // pegar a td com classe quantity pra pegar o imput com name form-0-quantity
//     const el = document.querySelector("td.quantity input[name='form-0-quantity']").value;
//     alert(el)   
// }

// function total() {
//     var valores = document.querySelector("#form-0-quantity");

//     var texto = valores.value;
//     console.log(texto);

// }
// $(document).ready(function () {
//     $('#tbl_3 tbody tr td .quantity').dblclick(function () {
//         var idElemento = $(this).find("input").val();
//         console.log(idElemento);
//     });
// });
