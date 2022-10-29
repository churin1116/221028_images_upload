// load : ページ全体が、スタイルシートや画像などのすべての依存するリソースを含めて読み込まれたときに発生
window.addEventListener("load", function () {

    $(document).on("click", "#submit", function(){ submit(); });
    $(document).on("click", ".trash", function(){ trash(this); });

    // 新たな画像input箇所を作成
    $(document).on("input", ".image_input", function(){ 
        $("#image_input_area").append('<input class="image_input" type="file" name="image">');    
    })

});


function submit(){

    let form_elem   = "#form_area";

    let data    = new FormData( $(form_elem).get(0) );
    let url     = $(form_elem).prop("action");
    let method  = $(form_elem).prop("method");

    for (let v of data) { console.log(v); }
    // 画像2枚アップロード時
    // ['csrfmiddlewaretoken', '7sIQRFMiOQ5ALrnqgjfpoqA4yHWfBlNviDAzIo7LVrU5RBTvmKibI7QiFhNOYXEq']
    // ['comment', 'test']
    // ['image', File]
    // ['image', File]
    // ['image', File]

    $.ajax({
        url: url,
        type: method,
        data: data,
        processData: false,
        contentType: false,
        dataType: 'json'
    }).done( function(data, status, xhr ) { 

        if (data.error){
            console.log("ERROR");
        }
        else{
            $("#content_area").html(data.content);
            $("#textarea").val("");
        }

    }).fail( function(xhr, status, error) {
        console.log(status + ":" + error );
    }); 

}

function trash(elem){

    let form_elem   = $(elem).parent("form");
    let url         = $(form_elem).prop("action");

    $.ajax({
        url: url,
        type: "DELETE",
        dataType: 'json'
    }).done( function(data, status, xhr ) { 

        if (data.error){
            console.log("ERROR");
        }
        else{
            $("#content_area").html(data.content);
        }

    }).fail( function(xhr, status, error) {
        console.log(status + ":" + error );
    }); 

}
