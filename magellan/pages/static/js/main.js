// Browser frame

$(document).ready(function () {
    $(".browser-frame-it").wrap("<div class='browser-frame'></div>").parent().prepend("<div class='bf-browser-controls'><div class='bf-window-controls'><span class='bf-close'></span> <span class='bf-minimise'></span> <span class='bf-maximise'></span></div><span class='bf-url-bar bf-white-container'>https://www.magellan.com/</span></div>");
})

