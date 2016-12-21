# SB_ActiveSwap

Allow to iterate active object over selected with shortcuts (shift+\`: next, ctrl+shift+\` : prev)

> /!\ may behave unexpectedly in armature edit/pose mode

---

### Description

**press shift+\`**  next object in selection become active  
**press ctrl+shift+\`**  previous object in selection become active
**press alt+shift+\`**  deselect active object (then next object in selection become active)

In vertex paint mode : iterate over active group

Shortcut are for qwerty layout (since the '\`' key is easily accessible to the left hand with modifier pressed)
You must change it in source code if you are on azerty.
If I finish it someday I'll post a version with valid shortcut for french keyboard too.


### TODO:
- Active vertex/edge/face swapping in Edit mode

### Update:

21/12/2016

- In vertex paint mode, iterate active vertex group
- Active bone swapping in Armature mode
- add a deselect shortcut to deselect active
