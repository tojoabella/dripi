export default function top_bar(title) {
   let topBar = document.getElementById("top_bar");
   topBar.innerHTML = ('\
   <div class=top_bar>\
      <a class="item_relative_right" href="#">Log in</a>\
      \
      <div class="item_relative_right">\
         <button class="dropdown-btn" onclick="dropDown()">Settings</button>\
         <div class="dropdown-content" id="top_bar_dropdown">\
            <a href="#">Profile</a>\
            <a href="#" class="btn2">Theme</a>\
         </div>\
      </div>\
      <h1 class="item_absolute_center">' + title + '</h1>\
   </div>\
   ');
};