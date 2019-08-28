//$('#modal').on('show.bs.modal', function (event) {
//    var modal = $(this)
//    $.ajax({
//        url: "{% url 'news-create' %}",
//        context: document.body
//    }).done(function(response) {
//        modal.html(response);
//    });
//})

//$(document).ready(function() { alert('se cargó el script para ventanas modal'); });

var modal;
function abrir_modal(url, titulo)
{
    alert('modal');
    modal = $('#modal').dialog(
    {
        title: titulo,
        modal: true,
        width: 500,
        resizable: false
    }).dialog('open').load(url)
}

function cerrar_modal()
{
    modal.dialog("close");
}
