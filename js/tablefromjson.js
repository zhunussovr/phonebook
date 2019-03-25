        $(document).ready(function(){
            $.getJSON("contactlist.json", function(data){
                var employers = '';
                $.each(data, function(key, value){
                    employers += '<tr>';
                    employers += '<td>'+""+'</td>';
                    employers += '<td>'+value.uname+'</td>';
                    employers += '<td>'+value.umobile+'</td>';
                    employers += '<td>'+value.uphone+'</td>';
                    employers += '<td>'+value.uemail+'</td>';
                    employers += '<td>'+value.utitle+'</td>';                    
                    employers += '<td>'+value.udepartment+'</td>';
                    employers += '</tr>';
                });
                $('#employee_table').append(employers);
            });
        });

        $(document).ready(function(){
            $("#search").keyup(function(){
            _this = this;
            
            $.each($("#employee_table tbody tr"), function() {
                if($(this).text().toLowerCase().indexOf($(_this).val().toLowerCase()) === -1) {
                    $(this).hide();
                } else {
                    $(this).show();                
                }
                });
            });
        });
