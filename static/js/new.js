$(document).ready(function() {
    let newContent = $('textarea#content');
    let num = 1;
    newContent.val(newContent.val() + (num) + '.  ');
    newContent.keyup(function(e) {
        if (e.keyCode === 13) { // enter 키를 입력했다면
            newContent.val(newContent.val() + (++num) + '.  ');
        }
    });
});