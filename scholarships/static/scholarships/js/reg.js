 $(document).ready(function() {
    $('select').material_select();
  });

var ageVal, sidVal;

$('#age').bind('change', function (e) {
    'use strict';
//    console.log($(this).prop('checked'));
    ageVal = $(this).prop('checked');
    if (ageVal === false) {
        console.log("studetn is an adult");
    } else {
        var $toastAge = $('<span> you are underage: Would you like to procced with a parent involved?</span>').add($('<button class="btn-flat toast-action" id="btn" >Yes</button>'));
        Materialize.toast($toastAge, 10000);
        console.log("student is under age");

        if ($(document).ready(function (){
            $('#btn').click(function (){
                alert("button has been pressed!");
//                toast needs to be dismissed
                if ($('#sid').bind('change', function (e){
                                   console.log($(this).prop('checked'));
                                   }));

            })
        }));

        }

    })



//
//$(document).ready(function () {
//            $('#btn').click(function () {
////                testing new code
//                alert("btn pressed"); // code ends here!
//                if($('#sid').bind('change', function (e){
//                    console.log($(this).prop('checked'));
//                }));
//
//                })
//            })
