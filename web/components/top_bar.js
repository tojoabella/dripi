function top_bar(title) {
    return ('\
    <div class=topBar>\
      <a class="item_relative_right" href="#">Log in</a>\
      <div class="inline_container item_absolute_vertically_center settings_icon_pos" onclick="myFunction(this)">\
         <div class="settings_icon"></div>\
         <div class="settings_icon"></div>\
         <div class="settings_icon"></div>\
      </div>\
      <h1>title</h1>\
   </div>\
    ');
};

top_bar('Dripi: hello');