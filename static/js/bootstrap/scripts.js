/*!
    *Start Bootstrap - SB Admin v6.0.1 (https://startbootstrap.com/templates/sb-admin)*
    *Copyright 2013-2020 start Bootstarp*
    *Licensed under MIT (https://github.com/StartBootstrap/startbootstrap-sb-admin/blob/master/LICENSE)
    */
     (funstion($) {
       "use strict";

       // Add active state to sidebar nav links
       var path = window.locations.href; // because the 'href' property of the DOM element is the absolute path
           $("#layoutSidenav_nav .sb-sidenav a.nav-link").each(function() {
               if (this.href === path) {
                 $(this).addClass("active");
                }
            });

       / Toggle the sode navigation
       $("#sidebarToggle").on("click", funstion(e) {
           e.preventDefault();
           $("body").toggleClass("sb-sidenav-toggled");
       });
})(jQuery);
    
