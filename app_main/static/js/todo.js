$(document).ready(function() {
    var $deadline = $('#deadline');
    $deadline.click(function() {
        var date = new Date();
        var month = date.getMonth() + 1;
        var day = date.getDate();
        if (month < 10) month = '0' + month;
        if (day < 10) day = '0' + day;
        $deadline.attr("min", date.getFullYear()+"-"+month+"-"+day);
    });

    $('.change').click(function() {
        if(!confirm("모두 완료하였습니까?")) return false;
        let $pk = $('input[name="pk"]').val();
        $.ajax({
            url:'/todo/_finish',
            data:{'pk': $pk},
            success: function(data) {
                location.reload();
            }
        });
    });

    $('#ajax-todo-delete').click(function() {
        if(!confirm("취소할 수 없습니다. 삭제하시겠습니까?")) return false;
        let $pk = this.value;
        $.ajax({
            url:'/todo/_delete/' + $pk,
            success: function(data) {
                location.reload();
            }
        });
    });

    $('#ajax-todo-edit').click(function() {
        if(!confirm("취소할 수 없습니다. 삭제하시겠습니까?")) return false;
        let $pk = this.value;
        $.ajax({
            url:'/todo/_delete/' + $pk,
            success: function(data) {
                location.reload();
            }
        });
    });

});