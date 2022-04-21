# oresat-kicad
All things KiCAD for OreSat; libraries, tools, settings, etc.

This library is meant to be a submodule in the directory of your KiCAD project. Yes, that's terrible. No, we don't have a better solution until KiCAD implements the idea of multiple library paths.

If your folder already has the `oresat-kicad` as a submodule, you just have to run:

{{{
git submodule init
git submodule update
}}}

If you want to add this as a submodule inside your shiny new KiCAD project folder, type:

`git submodule add git@github.com:oresat/oresat-kicad.git`

(If you don't have github org access, you can do:

`git submodule add https://github.com/oresat/oresat-kicad.git`

... but that will make the rest of us with github org access cry when we try to push changes from the local repo, so try to avoid that :)

Ping the #git-halp channel on Slack if you need more help!


# LICENSE

Copyright the Portland State Aerospace Society 2021.

This source describes Open Hardware and is licensed under CERN-OHL-S v2 or any later version.

You may redistribute and modify this source and make products using it under the terms of the CERN-OHL-S v2 (https://ohwr.org/cern_ohl_s_v2.txt).

This source is distributed WITHOUT ANY EXPRESS OR IMPLIED WARRANTY, INCLUDING OF MERCHANTABILITY, SATISFACTORY QUALITY AND FITNESS FOR A PARTICULAR PURPOSE. Please see the CERN-OHL-S v2 for applicable conditions.

Source location: https://github.com/oresat

As per CERN-OHL-S v2 section 4, should You produce hardware based on this source, You must where practicable maintain the Source Location visible on the external case of the Gizmo or other products you make using this source.
