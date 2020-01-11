# Active swap

Iterate active object/bones/vertexgroups in selection with shortcuts
<!--may behave unexpectedly in armature edit/pose mode -->

# Version 2.80

[**Download (qwerty)**](https://raw.githubusercontent.com/Pullusb/SB_ActiveSwap/master/SB_Active_swap.py) (right click, "save Target As")
(use combination with \` key)

[**Download (azerty Fr)**](https://raw.githubusercontent.com/Pullusb/SB_ActiveSwap/master/SB_Active_swap_azerty_Fr_PC.py) (right click, "save Target As")
(use combination with ² key)  

## [Demo Youtube](https://www.youtube.com/watch?v=43v5kxFkcZk)

---

### Description

The shortcuts use the key directly below escape (the left-most from the number top row). This key changes accoding to keyboard layouts...  
use \` for qwerty  
use ² for azerty Fr PC  


**press ctrl+shift+key**  next object in selection become active  
**press ctrl+shift+alt+key**  previous object in selection become active
**press alt+shift+key**  deselect active object (then next object in selection become active)

(shortcut are more complicated than the 2.79 version because \` key is already used a lot in 2.8 !)
/!\ Seems to have bugs in armature mode for now...

In vertex paint mode : iterate active group

---

# Version 2.79

[**Download 2.79 (qwerty)**](https://raw.githubusercontent.com/Pullusb/SB_ActiveSwap/master/SB_Active_swap_279.py) (right click, "save Target As")
(use combination with \` key)

[**Download 2.79 (azerty Fr)**](https://raw.githubusercontent.com/Pullusb/SB_ActiveSwap/master/SB_Active_swap_azerty_Fr_PC_279.py) (right click, "save Target As")
(use combination with ² key)  

---

### Description 2.79

The shortcuts use the key directly below escape (the left-most from the number top row). This key changes accoding to keyboard layouts...  
use \` for qwerty  
use ² for azerty Fr PC  
  
**press shift+key**  next object in selection become active  
**press ctrl+shift+key**  previous object in selection become active
**press alt+shift+key**  deselect active object (then next object in selection become active)

In vertex paint mode : iterate active group  
  
<!--Note for french:
Shortcut are for qwerty layout (since the '\`' key is easily accessible to the left hand with modifier pressed)
You must change it in source code if you are on azerty.
Someday I'll post a version with valid shortcut for french keyboard too... But what key to take ?! -->


### TODO:
- Active vertex/edge/face swapping in Edit mode

### Update:

16/11/2017
- Shortcuts are enabled all over editors (not just 3D-view) imply far less mouse trajectory ;)
for exemple : allow to let the cursor in properties (over constraints or modifiers...) and quickly iterate to change parameter.

21/12/2016

- In vertex paint mode, iterate active vertex group
- Active bone swapping in Armature mode
- add a deselect shortcut to deselect active
