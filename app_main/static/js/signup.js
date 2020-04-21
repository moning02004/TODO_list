$(document).ready(function() {

    $('input[name="username"]').keyup(function() {
        var $userCheck = $('.user-check > i');
        $userCheck.removeClass("fa-check")
            .addClass("fa-user")
            .addClass("text-dark");
    });

    var $userCheckButton = $('.user-check');
    $userCheckButton.click(function() {
        let $username = $('input[name="username"]').val();
        if ($username === "") return;
        $.ajax({
            url: 'user/_check/',
            data: {username: $username},
            success: function(data) {
                var $userCheck = $('.user-check > i');
                if (data.message === "good"){
                    $userCheck.removeClass("fa-user")
                        .removeClass("text-danger")
                        .removeClass("text-dark")
                        .removeClass("fa-exclamation")
                        .addClass("fa-check")
                        .addClass("text-success");
                } else {
                    $userCheck.removeClass("fa-user")
                        .removeClass("text-dark")
                        .removeClass("text-dark")
                        .removeClass("fa-check")
                        .addClass("fa-exclamation")
                        .addClass("text-danger");
                }
            }
        })
    });

    $('input[id="password"]').keyup(function() {
        var $passwordField = $('.password1 > i');
        var $passwordField2 = $('.password2 > i');
        if (this.value.length >= 6) {
            $passwordField.removeClass("text-danger");
            $passwordField.removeClass("fa-exclamation");
            $passwordField.addClass("fa-check");
            $passwordField.addClass("text-success");
        } else {
            $passwordField.removeClass("fa-check");
            $passwordField.removeClass("text-success");
            $passwordField.addClass("fa-exclamation");
            $passwordField.addClass("text-danger");
        }
        if($('#password1').val() !== $('#password2').val()){
            $passwordField2.removeClass("fa-check");
            $passwordField2.removeClass("text-success");
            $passwordField2.addClass("fa-exclamation");
            $passwordField2.addClass("text-danger");
        } else {
            $passwordField2.removeClass("text-danger");
            $passwordField2.removeClass("fa-exclamation");
            $passwordField2.addClass("fa-check");
            $passwordField2.addClass("text-success");
        }
    });
    $('input[id="password2"]').keyup(function() {
        var $passwordField = $('.password2 > i');
        if (this.value === $('input[id="password"]').val()) {
            $passwordField.removeClass("text-danger");
            $passwordField.removeClass("fa-exclamation");
            $passwordField.addClass("fa-check");
            $passwordField.addClass("text-success");
        } else {
            $passwordField.removeClass("fa-check");
            $passwordField.removeClass("text-success");
            $passwordField.addClass("fa-exclamation");
            $passwordField.addClass("text-danger");
        }
    });
});