$(document).on('click', '#newcomment, #newcommentinner', function (e) {
    e.preventDefault();

    var button = $(this).attr("value");

    var placement = "commentform"
    if (button == "newcommentform") {
        var placement = "newcommentform"
    }

    $.ajax({
        type: 'POST',
        url: '{% url "video_id:addcomment" %}',
        data: $("#" + button).serialize(),
        cache: false,
        success: function (json) {
            console.log(json)


            $('<div id="" class="my-2 p-2" style="border: 1px solid grey"> \
          <div class="d-flex justify-content-between">By ' + json['user'] + '<div></div>Posted: Just now!</div> \
          <div>' + json['result'] + '</div> \
          <hr> \
          </div>').insertBefore('#' + placement);

            $('.commentform').trigger("reset");
            formExit()

        },
        error: function (xhr, errmsg, err) {

        }
    });
})

function formExit(e) {
    e.preventDefault();
    document.getElementById("newcommentform").remove();
    $("#newcommentform").remove();
}

function deleteComment(id) {
    console.log(id)
    $.ajax({
        type: 'POST',
        url: '{% url "video_id:addcomment" %}',
        data: {
            nodeid: id,
            action: 'delete',
            csrfmiddlewaretoken: $('input[name=csrfmiddlewaretoken]').val(),
        },
        success: function (json) {
            $("#" + json['remove']).remove();
        },
        error: function (xhr, errmsg, err) { }
    });
}

function myFunction(id) {
    if (document.contains(document.getElementById("newcommentform"))) {
        document.getElementById("newcommentform").remove();
    }
    var videoid = document.getElementById('thumbs').getAttribute('data-value');
    var imgFullURL = $('img.avatar_comment')[0].src;
    var d1 = document.getElementById(id);
    d1.insertAdjacentHTML('afterend',
        '<form id="newcommentform" class="commentform" method="post"> \
        {% csrf_token %} \
        <select name="post" class="d-none" id="id_post"> \
          <option value="' + postid + '" selected="' + postid + '"></option> \
        </select> <label class="small font-weight-bold"></label> \
        <select name="parent" class="d-none" id="id_parent"> \
          <option value="' + id + '" selected="' + id + '"></option> \
        </select> \
        <div class="d-flex"> \
          <img class="avatar_comment align-self-center" src="' + imgFullURL + '"> \
          <textarea name="content" cols="40" rows="1" class="ml-3 mb-3 form-control border-0 comment-add rounded-0" placeholder="Add a public comment" required="" id="id_content"></textarea> \
        </div> \
        <div class="d-flex flex-row-reverse"> \
        <button type="button" class="btn btn-outline-secondary" onclick="formExit()">Close</button> \
          <button value="newcommentform" id="newcommentinner" type="submit" class="mr-1 newcomment btn btn-primary ">Submit</button> \
        </div> \
      </form>'
    );
}



//Reset form on page reload

$('.commentform').trigger("reset");