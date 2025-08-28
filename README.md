# Introduction
Source of my Battle for Wesnoth Campaign, Journey of a Frost Mage

# Dependencies
* [War of Legends era](https://github.com/knyghtmare/War_of_Legends)
* [WISh, the War of Legends Inventory System](https://github.com/babaissarkar/WISh)

# Donation
Highly appreciated and helpful to the future of this project!<br/>
[![ko-fi](https://ko-fi.com/img/githubbutton_sm.svg)](https://ko-fi.com/I2I11E85IE)

## Weird WML Syntax

Some files in this repository use a **sugared WML syntax** for brevity.

* **Self-closing tags** like `[tag ... /]` or `[tag {payload} /]` are allowed.
* Before Wesnoth can read them, these files must be **syntax-expanded** to standard WML.
* This repository includes a **expander tool** (`wml_expand.py`) that handles this conversion.

### For Contributors

* If you see `.cwml` files or unusual `/]` syntax, the **expander is involved**.
* Run the expander tool to generate valid WML:

```bash
python wml_expand.py path/to/file.cwml
```

* **Original `.cwml` files are preserved**; output is written as `.cfg`.
* Always backup before testing or editing `.cwml` files.

This ensures that **Wesnoth-ready WML** is generated from the concise, wacky syntax used for development.


# Translation commands
From the add-ons directory :
`path/to/wmlxgettext --directory="Frost_Mage" --domain="wesnoth-Frost_Mage" -o Frost_Mage/translations/wesnoth-Frost_Mage --recursive`

Then `cd` to `Frost_Mage/translations/wesnoth-Frost_Mage` and update the po file with the new strings from the pot file :
`msgmerge -vU bn.po wesnoth-Frost_Mage.pot` (change bn.po to the correct name for your po file)
