// ************************************************************************* 

history.navigationMode = 'compatible';

var CardsInRowCounter = 0;
var rowID = 0;
var row = "";


$(document).ready(function() {
    $.ajax({
        url: "https://undocuscholar.herokuapp.com/api/scholarships"
    }).then(function(data) {                
        // Add all the returned scholarships from the JSON 
        //    onto the list of scholarships on the Website
        
        console.log(data.scholarships.length);
        $.each(data.scholarships, function(key, value){

            
            
            if(CardsInRowCounter%4 == 0){
                // open a row          
                console.log("openROw" + CardsInRowCounter);
                $(".scolarships-row").append("<div class="+'"row row'+rowID+'">');
                row = "row"+rowID;
                rowID++;
            }
                        
            
            
//            <div class="card small teal">                
//                <div class="card-image waves-effect waves-block waves-light">
//                  <img class="activator" src="https://cdn4.iconfinder.com/data/icons/flat-business-icon-set/450/dollar-128.png">
//                </div>
//                  
//                <div class="card-content">
//                  <span class="card-title activator grey-text text-darken-4">Scholarship Name<i class="material-icons right">more_vert</i></span>
//                  <p>Amount</p>
//                  <p><a href="#">URL</a></p>
//                </div> 
//                  
//                <div class="card-reveal">
//                  <span class="card-title grey-text text-darken-4">Scholarship Name<i class="material-icons right">close</i></span>
//                  <p>Scholarship Description</p>
//                  <button>Apply_URL</button>
//                
//                </div>                
//            </div>
            
            
            
            
            var col= "<div class="+'"col s12 m6 l3"'+">";
            var card="<div class="+'"card small teal"'+">";
            
             var cardContent="<div class="+'"card-content"'+">";
             var cardNAme="<span class="+'"card-title activator grey-text text-darken-4"'+">"+value.name+"<i class="+'"material-icons right"'+">more_vert</i></span>";
             var cardAmount="<p>"+value.amount+"</p>";
             var cardURL="<p><a href="+'"'+value.url+'"'+">URL</a></p></div>";
            
             var cardReveal="<div class="+'"card-reveal"'+">";
             var cardName="<span class="+'"card-title grey-text text-darken-4"'+">"+value.name+"<i class="+'"material-icons right"'+">close</i></span>";
             var cardDescription="<p>Scholarship Description</p>";
             var cardButton="<a href="+value.url+" class="+'"waves-effect waves-light btn"'+">Apply</button>";
            
            
            var span="<span class="+'"white-text"'+">Small Card</span>";
            var div="</div></div>";
            $('.scolarships-row .'+row).append(col+card+cardContent+cardNAme+cardAmount+cardURL+cardReveal+cardName+cardDescription+cardButton+span+div);
            
//                var li="<li>";
//                var si="<strong>Scholarship Info:</strong>";
//                var p0="<p>ID:"+ value.id +"</p>";
//                var p1="<p>Name:"+ value.name + "</p>";
//                var p2="<p>deadline:"+ value.deadline + "</p>";
//                var p3="<p>amount:"+ value.amount + "</p>";
//                var p4="<button><a href=" +'"'+value.url+'"'+">Apply</a></button></li>";
//                $(".scolarships-list ol").append(li+si+p0+p1+p2+p3+p4);
            
            
            CardsInRowCounter++;
            
            if(CardsInRowCounter == 4 || CardsInRowCounter == data.scholarships.length  ){
                //close row
                console.log("closeRow" + CardsInRowCounter);   
                $(".scolarships-row").append("</div>"); 
            }
        });
    });     
});
   
// ************************************************************************* 

//// Temp String 
////     that will represent the future JSON result that will be 
////     Returned to us when a call is made to the Backend API 
//var tempJSONStr = '{"code":0,"message":"List of Scholarships","results":[{"name":"Frank F. Conlon Fellowship","deadline":"1/15/2016","amount":8000},{"name":"WAVA Phyllis Lawson Scholarship Award","deadline":"1/31/2016","amount":800},{"name":"WAVA Phyllis Lawson Scholarship Award","deadline":"1/31/2016","amount":100},{"name":"WAVA Phyllis Lawson Scholarship Award","deadline":"1/31/2016","amount":1050},{"name":"WAVA Phyllis Lawson Scholarship Award","deadline":"1/31/2016","amount":5000},{"name":"WAVA Phyllis Lawson Scholarship Award","deadline":"1/31/2016","amount":400},{"name":"WAVA Phyllis Lawson Scholarship Award","deadline":"1/31/2016","amount":375}]}';
//obj = JSON.parse(tempJSONStr);
//
//$(document).ready(function() {    
//   
//
//    // **********************************************  
//    // Add all the returned scholarships from the JSON 
//    //    onto the list of scholarships on the Website
//    $.each(obj.results, function(key, value){
//
//                var li="<li>";
//                var si="<strong>Scholarship Info:</strong>";
//                var p1="<p>Name:"+ value.name + "</p>";
//                var p2="<p>deadline:"+ value.deadline + "</p>";
//                var p3="<p>amount:"+ value.amount + "</p></li>";
//                $(".scolarships-list ol").append(li+si+p1+p2+p3);
//
//    });
//
//    // **********************************************  
//    // Respond to a button
//    $("#btn1").click(function(){         
//    
//    });    
//       
//});










