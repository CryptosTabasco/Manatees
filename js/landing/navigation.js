(function ($) {
    // Menu Functions
    $(document).ready(function () {
        $('#menuToggle').click(function (e) {
            var $parent = $(this).parent('.menu');
            $parent.toggleClass("open");
            var navState = $parent.hasClass('open') ? "hide" : "show";
            $(this).attr("title", navState + " navigation");
            // Set the timeout to the animation length in the CSS.
            setTimeout(function () {
                console.log("timeout set");
                $('#menuToggle > span').toggleClass("navClosed").toggleClass("navOpen");
            }, 200);
            e.preventDefault();
        });
    });
})(jQuery);