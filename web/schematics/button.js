<p>
      <b>mode button</b> 
      <br>
      <ul>
      <li>not pressed: 3.3v -> power button</li>
      <li>pressed: 3.3v -> power button -> resistor -> led parallel gpio24
         <ul>
            <li>led -> ground</li>
         </ul>
      </li>
      </ul>
      <br>
      <b>power button</b><br>
      <ul>
         <li>not pressed: 3.3v -> mode button</li>
         <li>pressed: 3.3v -> mode button -> resistor -> gpio23</li>
      </ul>
   </p>