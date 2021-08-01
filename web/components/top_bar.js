export default function top_bar(title) {
   let topBar = document.getElementById("top_bar");
   topBar.innerHTML = ('\
   <div class=top_bar>\
      <a class="item_relative_right" href="#">Log in</a>\
      \
      <div class="item_relative_right">\
         <button class="dropbtn" onclick="myFunction()">Dropdown</button>\
         <div class="dropdown-content" id="myDropdown">\
            <a href="#">Link 1</a>\
            <a href="#">Link 2</a>\
         </div>\
      </div>\
      <h1>' + title + '</h1>\
   </div>\
   ');
};

//<div class="inline_container item_absolute_vertically_center">\
//</div>\
// <div class="settings_icon"></div>\
//         <div class="settings_icon"></div>\
 //        <div class="settings_icon"></div>\