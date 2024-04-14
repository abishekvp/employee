function load_employee(){
    $('#employee-data').empty();
    $.ajax({
        url: '/load-employee',
        type: 'GET',
        success: function(response){
            for(i=0; i<response['employee']['employee_data'].length; i++){
                $('#employee-data').append(
                    '<tr><td>'+
                    response['employee']['employee_data'][i]['code']+
                    '</td><td>'+response['employee']['employee_data'][i]['name']+
                    '</td><td>'+response['employee']['employee_data'][i]['age']+
                    '</td><td id="operations"><button id="'+
                    response['employee']['employee_data'][i]['code']+
                    '" onclick="edit_emp(this.id)">Edit</button><button id="'+
                    response['employee']['employee_data'][i]['code']+
                    '" onclick="delete_emp(this.id)">Delete</button></td></tr>');
                $('#total-emp').html(i+1);
            }
        }
    });
}

function create(){
    $('.profile').css('display', 'block');
    $('.update_emp').css('display', 'none');
    $('.create_emp').css('display', 'block');
}

function create_emp(){
    $.ajax({
        url: '/create-employee',
        type: 'POST',
        data: {
            emp_name: $('#emp-name').val(),
            emp_age: $('#emp-age').val(),
            csrfmiddlewaretoken: $('input[name=csrfmiddlewaretoken]').val()
        },
        success: function(response){
            if (response['status'] == 200){
                alert('Employee Created Successfully')
                load_employee();
                $('#emp-name').val("");
                $('#emp-age').val("");
                $('.profile').css('display', 'none');
            } else {
                alert("Employee Can't be Created");
            }
        }
    });
}

function search_employee(valu){
    $.ajax({
        url: '/search-employee',
        type: 'POST',
        data: {
            search: valu,
            csrfmiddlewaretoken: $('input[name=csrfmiddlewaretoken]').val()
        },
        success: function(response){
            $('#employee-data').empty();

            for(i=0; i<response['employee']['employee_data'].length; i++){
                $('#employee-data').append(
                    '<tr><td>'+
                    response['employee']['employee_data'][i]['code']+
                    '</td><td>'+response['employee']['employee_data'][i]['name']+
                    '</td><td>'+response['employee']['employee_data'][i]['age']+
                    '</td><td id="operations"><button id="'+
                    response['employee']['employee_data'][i]['code']+
                    '" onclick="edit_emp(this.id)">Edit</button><button id="'+
                    response['employee']['employee_data'][i]['code']+
                    '" onclick="delete_emp(this.id)">Delete</button></td></tr>');
                $('#total-emp').html(i+1);
            }
        }
    });
}

function delete_emp(id){
    $.ajax({
        url: '/delete-employee',
        type: 'POST',
        data: {
            emp_code: id,
            csrfmiddlewaretoken: $('input[name=csrfmiddlewaretoken]').val()
        },
        success: function(result){
            load_employee();
        }
    });
}

function edit_emp(id){
    $.ajax({
        url: '/edit-employee',
        type: 'POST',
        data: {
            emp_code: id,
            csrfmiddlewaretoken: $('input[name=csrfmiddlewaretoken]').val()
        },
        success: function(response){
            $('.profile').css('display', 'block');
            $('.create_emp').css('display', 'none');
            $('.update_emp').css('display', 'block');
            $('.update_emp').attr('id',response['employee']['emp_code']);
            $('#emp-name').val(response['employee']['emp_name']);
            $('#emp-age').val(response['employee']['emp_age']);

        }
    });
}

function update_emp(id){
    $.ajax({
        url: '/update-employee',
        type: 'POST',
        data: {
            emp_code: id,
            emp_name: $('#emp-name').val(),
            emp_age: $('#emp-age').val(),
            csrfmiddlewaretoken: $('input[name=csrfmiddlewaretoken]').val()
        },
        success: function(response){
            if(response['status'] == 200){
                alert('Employee Updated Successfully');
                load_employee();
                $('.profile').css('display', 'none');
            }else{
                alert("Employee Can't be Updated");
            }
        }
    });
    load_employee();
}

function test(){
    $.ajax({
        url: '/test-net',
        type: 'POST',
        data: {
            limit: prompt('Limit'),
            csrfmiddlewaretoken: $('input[name=csrfmiddlewaretoken]').val()
        },
        success: function(response){
            load_employee();
        }
    });
}

function close_x(){
    $('.profile').css('display', 'none');
}
