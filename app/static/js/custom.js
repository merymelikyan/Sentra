
// // Function to get the CSRF token from the cookies
// function getCSRFToken() {
//     var csrfToken = null;
//     if (document.cookie && document.cookie !== '') {
//         var cookies = document.cookie.split(';');
//         for (var i = 0; i < cookies.length; i++) {
//             var cookie = cookies[i].trim();
//             if (cookie.substring(0, 10) === 'csrftoken=') {
//                 csrfToken = decodeURIComponent(cookie.substring(10));
//                 break;
//             }
//         }
//     }
//     return csrfToken;
// }

// $('#submit-button').on('click', function() {
//     $.ajax({
//         url: '/receive-message/',  // URL to your Django view
//         type: 'POST',
//         data: {
//             'name': $('input[name=name]').val(),
//             'email': $('input[name=email]').val(),
//             'subject': $('input[name=subject]').val(),
//             'content': $('textarea[name=content]').val(),
//         },
//         beforeSend: function(xhr) {
//             xhr.setRequestHeader("X-CSRFToken", getCSRFToken());  // Set the CSRF token header
//         },
//         success: function(response) {
//             if (response.status === 'success') {
//                 alert('Message sent successfully!');
//             } else {
//                 alert(response.message || 'An error occurred.');
//             }
//         },
//         error: function(xhr, status, error) {
//             console.error('An error occurred:', error);
//         }
//     });
// });





// (function ($) {
    
// Hide Header on on scroll down
var didScroll;
var lastScrollTop = 0;
var delta = 5;
var navbarHeight = $('header').outerHeight();

$(window).scroll(function(event){
    didScroll = true;
});

setInterval(function() {
    if (didScroll) {
        hasScrolled();
        didScroll = false;
    }
}, 250);

function hasScrolled() {
    var st = $(this).scrollTop();
    
    // Make sure they scroll more than delta
    if(Math.abs(lastScrollTop - st) <= delta)
        return;
    
    // If they scrolled down and are past the navbar, add class .nav-up.
    // This is necessary so you never see what is "behind" the navbar.
    if (st > lastScrollTop && st > navbarHeight){
        // Scroll Down
        $('header').removeClass('nav-down').addClass('nav-up');
    } else {
        // Scroll Up
        if(st + $(window).height() < $(document).height()) {
            $('header').removeClass('nav-up').addClass('nav-down');
        }
    }
    
    lastScrollTop = st;
}

$("#contact").on("submit", (e) => {
    e.preventDefault();
    const data = {
        'name': $('input[name=name]').val(),
        'email': $('input[name=email]').val(),
        'sumbit': $('input[name=sumbit]').val(),
        'content': $('textarea[name=content]').val(),
        'csrfmiddlewaretoken': '{{ csrf_token }}'
    };
    $.post("http://127.0.0.1:8000/messages/receive_message/", data, () => {
        console.log("all is okay");
    });

    e.target.reset();
    });
            

(window.jQuery);