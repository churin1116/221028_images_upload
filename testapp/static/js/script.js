// load : ページ全体が、スタイルシートや画像などのすべての依存するリソースを含めて読み込まれたときに発生
window.addEventListener("load", function () {

    $(document).on("click", ".trash", function(){ trash(this); });

    // 新たな画像input箇所を作成
    $(document).on("input", ".image_input", function(){ 
        $("#image_input_area").append('<input class="image_input" type="file" name="image">');    
    })

});



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
