// function sendToastMessage(title,message,time) {
//     let toast_html = "<div class='toast ml-auto' role='alert' data-delay='700' data-autohide='false'>";
//     toast_html += "<div class='toast-header'>";
//     toast_html += "<strong class='mr-auto text-primary'>"+title+"</strong>";
//     toast_html += "<small class='text-muted'>"+time+"</small>";
//     toast_html += "<button type=button class='ml-2 mb-1 close' data-dismiss='toast' aria-label='Close'>";
//     toast_html += "<span aria-hidden='true'>×</span></button></div><div class='toast-body'>";
//     toast_html += message;
//     toast_html += "</div></div>";
//     let toast = $(toast_html);
//     $("#toastdiv").prepend(toast);
//     console.log(toast);
//     $(toast).toast({delay:1500});
// }