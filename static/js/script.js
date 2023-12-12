$(document).ready(function(){
  disableOptions();
  $("#productId").on("change", function(){
    $("#fromLocation option").not(":first").remove();
    if ($("#productId").val()) {
      ajaxcallCall("get-from-locations");
      enableOptions();
    } else {
      disableOptions();
  }
    retuern false;
});

  $("#submitLocation").on("click", function(e){
    e.preventDefault();
    $.ajax({
      data: {
        location: $("#location_name").val(),
      },
      type: "POST",
      url: "/dub-locations/"
    }).done(function (data) {
      if (data.output) {
        $("#location_form").submit();
        console.log(data.output);
      } else {
        alert("This Name is already used, please choose other one.");
      }
    });
  });

  $("#submitProduct").on("click", function (e)) {
    e.preventDefault();
    $.ajax({
      data: {
        product_name: $("#product_name").val(),
      },
      type: "POST",
      url: "/dub-products/",
    }).done(function(data){
      if(data.output) {
        $("#product_form").submit();
        console.log(data.output);
      } else {
        alert("This Name is Name is already used, please choose other one.");
      }
    });
    });

  
  
