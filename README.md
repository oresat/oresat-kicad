# oresat-kicad
All things KiCAD for OreSat; libraries, tools, settings, etc.

This library is meant to be a submodule in the directory of your KiCAD project. Yes, that's terrible. No, we don't have a better solution until KiCAD implements the idea of multiple library paths.

## If you already see a folder in the OreSat repo called "oresat-kicad"

This means someone else added the submodule to this project already. After you clone the repo, simply run:

{{{
git submodule init
git submodule update
}}}

... and that will initialize and pull the submodule so you can use it.

## If you need to add the repo to your KiCAD project folder

From within your repo, run:

`git submodule add git@github.com:oresat/oresat-kicad.git`

that's it! You should be ready to go.

## Updating the submodule

cd into `oresat-kicad` and run `git pull`. This will update the submodule to the latest bits. Then `cd ..` back into your project, and run `git add oresat-kicad`. Commit that, and now your project is committed with the latest `oresat-kicad` files.

Ping the #git-halp channel on Slack if you need more help!

# Using oresat-kicad inside KiCAD

* Open up your project.
* In the project panel, choose Preferences > Manage Symbol Libraries.
* Select the "Project Specific Libraries" tab.
* Click on the Folder icon below.
   * THIS IS IMPORTANT. DO NOT CLICK ON "+". CLICK ON THE FOLDER.
* In your project folder, navigate to `oresat-kicad/oresat-symbols` and choose the symbol(s) you want. You can all of them if you want!
* Chose Open, then OK.
* Back in the project panel, choose Preferences > Manage Footprint Libraries.
* Select the "Project Specific Libraries" tab.
* Click on the Folder icon below.
   * THIS IS IMPORTANT. DO NOT CLICK ON "+". CLICK ON THE FOLDER.
* In your project folder, navigate to `oresat-kicad/oresat-footprints`.
* Chose Open, then OK.

At this point, your project should be pointing to your oresat-kicad repository and you should be good to go!


# LICENSE

Copyright the Portland State Aerospace Society 2021.

This source describes Open Hardware and is licensed under CERN-OHL-S v2 or any later version.

You may redistribute and modify this source and make products using it under the terms of the CERN-OHL-S v2 (https://ohwr.org/cern_ohl_s_v2.txt).

This source is distributed WITHOUT ANY EXPRESS OR IMPLIED WARRANTY, INCLUDING OF MERCHANTABILITY, SATISFACTORY QUALITY AND FITNESS FOR A PARTICULAR PURPOSE. Please see the CERN-OHL-S v2 for applicable conditions.

Source location: https://github.com/oresat

As per CERN-OHL-S v2 section 4, should You produce hardware based on this source, You must where practicable maintain the Source Location visible on the external case of the Gizmo or other products you make using this source.
