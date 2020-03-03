$("#id_name").keyup(function () {
    console.log($(this).val());
    var name = $(this).val();
    $.ajax({
        url: 'checkNames/',
        data: {
            'name': name
        },
        dataType: 'json',
        success: function (data) {
            element = document.getElementById("names");
            var child = element.lastElementChild;
            while(child){
                element.removeChild(child);
                child = element.lastElementChild;
            }
            objects = data.results;
            for(var i = 0; i < objects.length; i++){
                var tagElement = document.createElement('option');
                tagElement.value = objects[i].name;
                document.getElementById("names").appendChild(tagElement);
            }
        }
    });
});