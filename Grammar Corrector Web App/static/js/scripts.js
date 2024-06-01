$(document).ready(function() {
    $('#checkButton').click(function() {
        var inputText = $('#inputText').val();
        $.ajax({
            url: '/check_grammar',
            type: 'POST',
            data: { text: inputText },
            success: function(response) {
                $('#outputText').val(response.corrected_text);
            }
        });
    });
});
