$(document).ready(function() {

    let date = new Date();
    let month = date.getMonth() + 1;
    let day = date.getDate();
    if (month < 10) month = '0' + month;
    if (day < 10) day = '0' + day;

    var $deadline = $('#deadline');
    $deadline.click(function() {
        $deadline.attr("min", date.getFullYear()+"-"+month+"-"+day);
    });

    $('button[name="save"]').click(function(){
        if ($('input[name="title"]').val() !== "" && $('textarea[name="content"]').val() !== ""){
            return (confirm("저장하시겠습니까?"));
        }
        alert("입력 정보를 다시 한 번 확인하십시오.");
        return false;
    });

    let $editButton = $('button[name="edit-button"]');
    $editButton.click(function() {
        if ($editButton.html() !== "확인") {
            $('.edit-field').attr('hidden', false);
            $('button[name="edit-button"]').html("확인");
        } else {
            $('.edit-field').attr('hidden', true);
            $('button[name="edit-button"]').html("수정");
        }
    });

    $('.change').click(function() {
        let $pk = $('input[name="pk"]').val();
        $.ajax({
            url:'/todo/_finish',
            data:{'pk': $pk},
            success: function(data) {
                location.reload();
            }
        });
    });

    $('.delete-todo').click(function() {
        if(confirm("취소할 수 없습니다. 삭제하시겠습니까?")) {
            let $pk = this.value;
            $.ajax({
                url:'/todo/_delete/' + $pk,
                success: function(data) {
                    location.reload();
                }
            });
        }
    });

    $('.pri').click(function() {
        let $pk = this.value;
        let arrow = this.name;

        $.ajax({
            url:'/todo/_change/'+$pk,
            data: {'arrow': arrow},
            success: function(data){
                location.reload();
            }
        });
    });
});