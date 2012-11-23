(function($) {
    $(function() {
        
        $("#slides").cycle({timeout: 20000});

        var $info = $("#infobox");
        var slug = "main";

        var last_body = "";
        var update_state = function(text) {
            if (text != last_body) {
                last_body = text;
                if (text) {
                    $info.html(text);
                    $info.fadeIn("slow");
                }
                else {
                    $info.fadeOut(
                        "slow",
                        function() {
                            $info.html(text);
                        });
                }
            }
        };
        
        var state_url = '/i/' + slug + '/state/';
        var check_state = function() {
            $.ajax(state_url, {
                dataType: 'text',
                success: update_state
            });
        };

        window.setInterval(check_state, 1000);

    });
})(jQuery);
