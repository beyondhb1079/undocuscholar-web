history.navigationMode = 'compatible';
$(document).ready(function() {
    

    $.ajax({
        url: "https://undocuscholar.herokuapp.com/api/scholarships"
    }).then(function(data) {
                
        // Add all the returned scholarships from the JSON 
        //    onto the list of scholarships on the Website
        $.each(data.results, function(key, value){

                var li="<li>";
                var si="<strong>Scholarship Info:</strong>";
                var p1="<p>Name:"+ value.name + "</p>";
                var p2="<p>deadline:"+ value.deadline + "</p>";
                var p3="<p>amount:"+ value.amount + "</p></li>";
                $(".scolarships-list ol").append(li+si+p1+p2+p3);

        });
    });
    
    
});









