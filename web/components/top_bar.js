export default function top_bar(title) {
   let topBar = document.getElementById("top_bar");
   topBar.innerHTML = ('\
   <div class=top_bar>\
     <a class="item_relative_right" href="#">Log in</a>\
     <div class="inline_container item_absolute_vertically_center settings_icon_pos" onclick="myFunction(this)">\
        <div class="settings_icon"></div>\
        <div class="settings_icon"></div>\
        <div class="settings_icon"></div>\
     </div>\
     <h1>' + title + '</h1>\
  </div>\
   ');
};