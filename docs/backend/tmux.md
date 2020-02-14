# Tmux
## Requirements
- tmux > 3.0

## Commands
```bash
tmux new -s ${session}
tmux ls
tmux lsc
tmux a -t ${session}
tmux kill-session -t ${session}
tmux kill-server
```

## Prefix
Prefix is ==++ctrl+++b== command.
Controll tmux, type prefix and any following key.

### Session
|  Key  |  Action  |
| ---- | ---- |
|  :  |  prompt  |
|  ?  |  show list of key bind  |
|  s  |  select session  |
|  d  |  detatche session  |
|  $  |  rename current session  |

### Window
|  Key  |  Action  |
| ---- | ---- |
|  c  |  create new window  |
|  w  |  show window list  |
|  n  |  move next window  |
|  p  |  move previous window  |

### Pane
|  Key  |  Action  |
| ---- | ---- |
|  %  |  split pane horizontally  |
|  "  |  split pane vertically  |
|  o  |  move next pane  |
|  ;  |  move previous pane  |
|  ++space++  |  change layout  |

## Config
put file ==~/.tmux.conf== or ==/etc/tmux.conf==

sample
```
set -g mouse off
bind-key -n WheelUpPane if-shell -F -t = "#{mouse_any_flag}" "send-keys -M" "if -Ft= '#{pane_in_mode}' 'send-keys -M' 'select-pane -t=; copy-mode -e; send
-keys -M'"
bind-key -n WheelDownPane select-pane -t= \; send-keys -M
setw -g mode-keys vi

```