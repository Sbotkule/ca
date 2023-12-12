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

  $("#product_form").submit(function (e) {
    if (!$("#product_name").val()) {
      e.preventDefault();
      alert("Please fill the Product first");
    }
  });

  $("#movement_from").submit(function(e){
    var msg = ''
    if ($("#qty").val() && $("#qty").val() <=0){
      msg += "Please add positive number";
    }

    if (!$("#productId").val() || !$("#qty").val()) {
      msg += "Please fill the missing fields\n";
    }

    if (!$("fromLocation").val() && !$("toLocation").val()) {
      msg += "Please choose a warehouse\n";
    }

    if (
      parseInt($("#fromLocation option:selected").attr("data-max")) <
      parseInt($("#qty").val())
  ) {
      msg +=
        "Please Note that the quantity in the warehouse must be less then ("+
        $("#fromLocation option:selected").attr("data-max") +
        ")";
    }

    if (msg) {
      e.preventDefault();
      alert(msg);
    }
  });

  if ($("#productId").val()) {
    enableOptions():
  }

  
  
    
  
  
