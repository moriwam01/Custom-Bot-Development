$(document).ready(function() {
    $("#sendButton").click(function() {
        let message = $("#messageInput").val();
        if(message) {
            appendMessage(message, 'user-message');
            $("#messageInput").val('');
            $.ajax({
                type: "POST",
                url: "/api",
                data: JSON.stringify({message: message}),
                contentType: "application/json; charset=utf-8",
                dataType: "json",
                success: function(response) {
                    appendMessage(response.message, 'response-message');
                },
                error: function(errMsg) {
                    console.error("Error sending message", errMsg);
                }
            });
        }
    });

    function appendMessage(message, className) {
        let messageDiv = $("<div>").addClass("chat-message " + className).text(message);
        $("#chatContainer").append(messageDiv).scrollTop($("#chatContainer")[0].scrollHeight);
    }
});