$(function() {
    $(".create-modal").each(function() {
        $(this).modalForm({
            formURL: $(this).data('url'),
        });
    });

    $(".read-modal").each(function() {
        $(this).modalForm({
            formURL: $(this).data('url'),
            modalContent: ".modal-dialog",
            modalForm: ".modal-dialog form",
        });
    });

    $(".update-modal").each(function () {
        $(this).modalForm({
            formURL: $(this).data('url'),
            modalContent: ".modal-dialog",
            modalForm: ".modal-dialog form",
        });
    });

    $(".delete-modal").each(function () {
        $(this).modalForm({
            formURL: $(this).data('url'),
        });
    });

    // hide message
    $(".alert").fadeTo(2000, 500).slideUp(500, function() {
        $(".alert").slideUp(500);
    });

    // autofocus to first input field of a modal
    $('.modal').on('shown.bs.modal', function() {
        $('form').find('input[type=text]').filter(':visible:first').focus();
    });
});
