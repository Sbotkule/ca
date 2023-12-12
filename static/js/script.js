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
        loaction: $("#location_name").val(),
      },
      type: "POST",
      url: "/dub-locations/"
    }).done(function (data) {
      if (data.output) {
        $("#location_form").submit();
      } else {
        alert("This Name is already used, please choose other one.");
      }
    });
  });
