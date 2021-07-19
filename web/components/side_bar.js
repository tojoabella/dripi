/*
sideBarCategories = {"continuous": list of cont. objects, "noncontinuous": list of noncont. objects}
((non)cont object) = {"title": , "elements": list of modes}
*/
export default function side_bar(sideBarCategories) {
    let sideBar = document.getElementById("side_bar");

    if (sideBarCategories.hasOwnProperty('continuous')){
        let continuous = sideBarCategories.continuous;
        for (const continuousGroup of continuous) {
            sideBar.innerHTML += '<p class="item_relative_horizontally_center">' + continuousGroup.title + '</p>';
            let ul_elem = document.createElement("ul");
            for (const element of continuousGroup.elements) {
                ul_elem.innerHTML += '<li><a class="side_bar_element constant" onclick="activationToggler(this)">' + element + '</a></li>';
            }
            sideBar.appendChild(ul_elem);
            sideBar.innerHTML += '<hr style="margin:0">';
        }
    }
    if (sideBarCategories.hasOwnProperty('noncontinuous')){
        let noncontinuous = sideBarCategories.noncontinuous;
        for (const noncontinuousGroup of noncontinuous) {
            sideBar.innerHTML += '<p class="item_relative_horizontally_center">' + noncontinuousGroup.title + '</p>';
            let ul_elem = document.createElement("ul");
            for (const element of noncontinuousGroup.elements) {
                ul_elem.innerHTML += '<li><a class="side_bar_element one_time" onmousedown="colorChanger(this,\'#889bac\')" onmouseup="colorChanger(this, \'#dddddd\')">' + element + '</a></li>';
            }
            sideBar.appendChild(ul_elem);
        }
    }
}

/*homapage example
<label class="sticky side_bar" id="side_bar">
      <p class="item_relative_horizontally_center">CONTINUOUS MODES</p>
      <ul>
         <li><a class="side_bar_element constant" onclick="activationToggler(this)">street change alerter</a></li>
         <li><a class="side_bar_element constant"  onclick="activationToggler(this)">city change alerter</a></li>
         <li><a class="side_bar_element constant"  onclick="activationToggler(this)">street length</a></li>
         <li><a class="side_bar_element constant" onclick="activationToggler(this)">offramp major dest</a></li>
         <li><a class="side_bar_element constant" onclick="activationToggler(this)">ahapua'a and moku</a></li>
         <li><a class="side_bar_element constant" onclick="activationToggler(this)">cameras</a></li>
         <li><a class="side_bar_element constant" onclick="activationToggler(this)">driving history</a></li>
      </ul>
      <hr style="margin:0">
      <p class="item_relative_horizontally_center">AT-CALL-TIME MODES</p>
      <ul>
         <li><a class="side_bar_element one_time" onmousedown="colorChanger(this,'#889bac')" onmouseup="colorChanger(this, '#dddddd')">beach and surf</a></li>
         <li><a class="side_bar_element one_time" onmousedown="colorChanger(this,'#889bac')" onmouseup="colorChanger(this, '#dddddd')">speed limit</a></li>
         <li><a class="side_bar_element one_time" onmousedown="colorChanger(this,'#889bac')" onmouseup="colorChanger(this, '#dddddd')">quota</a></li>
         <li><a class="side_bar_element one_time" onmousedown="colorChanger(this,'#889bac')" onmouseup="colorChanger(this, '#dddddd')">current location</a></li>
      </ul>
   </label>
*/