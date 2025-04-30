# Introduction
Source of my Battle for Wesnoth Campaign, Journey of a Frost Mage

# Dependencies
* [War of Legends era](https://github.com/knyghtmare/War_of_Legends)
* [WISh, the War of Legends Inventory System](https://github.com/babaissarkar/WISh)

# Donation
Highly appreciated and helpful to the future of this project!
[![ko-fi](https://ko-fi.com/img/githubbutton_sm.svg)](https://ko-fi.com/I2I11E85IE)

# Translation commands
From the add-ons directory :
`path/to/wmlxgettext --directory="Frost_Mage" --domain="wesnoth-Frost_Mage" -o Frost_Mage/translations/wesnoth-Frost_Mage --recursive`

Then `cd` to `Frost_Mage/translations/wesnoth-Frost_Mage` and update the po file with the new strings from the pot file :
`msgmerge -vU bn.po wesnoth-Frost_Mage.pot` (change bn.po to the correct name for your po file)
