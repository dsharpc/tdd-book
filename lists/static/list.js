window.Superlists = {};
window.Superslists.initialise = function() {
    $('input[name="text"]').on('keypress', function () {
        $('.has-error').hide();
    });
};
