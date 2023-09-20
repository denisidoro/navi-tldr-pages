# navi-tldr-pages
Cheatsheets for [navi][navi], extracted from [tldr][tldr].

The original files and translated into a format compatible with [navi][navi].

Please don't edit the `.cheat` files by hand.

### Usage
- install [navi][navi]
- run `navi repo add denisidoro/navi-tldr-pages`
- select the `.cheat` files you are interested in
- run `navi` again

### Updating using this repo
- go to the project root
- clone [tldr][tldr]
- Alternatively, if you already have tldr cloned (to tldr folder, for example), pull changes ("cd tldr; git pull") 
- run `./scripts/translate`
- git commit -m "Updates pages" && git push
- run `navi repo add Coqueiro/navi-tldr-pages`

### Creating personal cheatsheets
- Edit pages under `personal_pages`
- Use supported syntax: https://github.com/denisidoro/navi/blob/master/docs/cheatsheet_syntax.md

### Alternative

You can run `navi --tldr <query>`.

More info [here](https://github.com/denisidoro/navi/blob/master/docs/cheatsheet_repositories.md#using-cheatsheets-from-other-tools).

[tldr]: https://github.com/tldr-pages/tldr
[navi]: https://github.com/denisidoro/navi
