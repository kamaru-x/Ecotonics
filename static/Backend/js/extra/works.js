$(document).ready(function(){
    $('#category').on('change' , function(){
        var category_id = $('#category').val()

        $.ajax({
            url : '/dashboard/work/service/get/',
            type : 'POST',
            data : {'category_id' : category_id},

            success : function(response){
                var result = ''

                for (let i = 0; i < response.services.length; i++) {
                    result += `<option value="${ response.services[i].id }">${ response.services[i].Title }</option>`;
                }

                $('#services').html(result)
            }
        })
    })
})