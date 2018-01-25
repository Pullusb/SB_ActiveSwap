# SB_ActiveSwap

right click, "save Target As"
## [Download (qwerty)](https://raw.githubusercontent.com/Pullusb/SB_ActiveSwap/master/SB_Active_swap.py)
(use combination with \` key)
## [Download (azerty Fr)](https://raw.githubusercontent.com/Pullusb/SB_ActiveSwap/master/SB_Active_swap_azerty_Fr_PC.py)
(use combination with ² key)  


Allow to iterate active object/bones/vertexgroups in selectionselected with shortcuts (shift+\`: next, ctrl+shift+\` : prev)
<!--may behave unexpectedly in armature edit/pose mode -->

---

### Description

azerty : for Fr version use ² instead of \`  
**press shift+\`**  next object in selection become active  
**press ctrl+shift+\`**  previous object in selection become active
**press alt+shift+\`**  deselect active object (then next object in selection become active)

In vertex paint mode : iterate active group

Note for french:
Shortcut are for qwerty layout (since the '\`' key is easily accessible to the left hand with modifier pressed)
You must change it in source code if you are on azerty.
Someday I'll post a version with valid shortcut for french keyboard too... But what key to take ?!


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
