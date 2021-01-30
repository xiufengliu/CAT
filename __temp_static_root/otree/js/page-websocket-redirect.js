$(document).ready(function () {

    // i also considered using document.currentScript.getAttribute()
    // as described here: https://stackoverflow.com/a/32589923/38146
    // but PyCharm doesn't like that the script has non data- params
    // maybe non-standard?
    var $currentScript = $('#websocket-redirect');

    var socketUrl = $currentScript.data('socketUrl');
    var isBrowserBot = $currentScript.data('isBrowserBot');
    var redirectUrl = $currentScript.data('redirectUrl');
    var isDebug = $currentScript.data('isDebug');

    /*
    One user reported that with a 588 bot session,
    web socket for auto-advance adds 4s to each page load.
    */
    var socket;

    function initWebSocket() {
        socket = makeReconnectingWebSocket(socketUrl);
        socket.onmessage = function (e) {
            var data = JSON.parse(e.data);

            if (data.error) {
                console.log('Error receiving websocket message. Maybe the server was stopped.')
            }

            if (data.auto_advanced) {
                console.log('Received redirect message', e.data);
                window.location.href = redirectUrl;
            }
        };

    }

    initWebSocket();
});
