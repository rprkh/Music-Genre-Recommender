$('.form2').on('submit', function() {
    $.ajax({
        beforeSend: function() {
            $('.loader #spinner').show();
        }
    })
});

$('.form3').on('submit', function() {
    $('#spinner').show();
});
