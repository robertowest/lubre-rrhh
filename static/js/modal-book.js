$(function () {
    // Create book button
    $(".create-book").modalForm({formURL: "{% url 'rrhh:art_create' %}"});

    // Update book buttons
    $(".update-book").each(function () {
        $(this).modalForm({formURL: $(this).data('id')});
    });

    // Read book buttons
    $(".read-book").each(function () {
        $(this).modalForm({formURL: $(this).data('id')});
    });

    // Delete book buttons
    $(".delete-book").each(function () {
        $(this).modalForm({formURL: $(this).data('id')});
    })

    // info de activo
    $(".read-activo").each(function () {$(this).modalForm({formURL: $(this).data('id')});});

    // Hide message
    $(".alert").fadeTo(2000, 500).slideUp(500, function(){
        $(".alert").slideUp(500);
    });
});