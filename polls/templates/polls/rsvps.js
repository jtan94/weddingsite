var e = document.getElementById("currentRSVPS");
system.out.println(currentRSVPS);
var rsvpName = e.options[e.selectedIndex].text;
system.out.println(rsvpName);

document.getElementById("demo").innerHTML = rsvpName;