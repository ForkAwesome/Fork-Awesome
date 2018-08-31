# Contributing to Fork Awesome

Looking to contribute something to Fork Awesome? **Here's how you can help.**

## Requesting new icons

New icons mostly start as requests by the [Fork Awesome community on GitHub](../../issues). Want to request a new icon? Here are some things to keep in mind:

1. Please be nice. Fork Awesome is a happy place.
2. Please [search](../../search?type=Issues) to see if your icon request already exists. If a request is found, please add a 👍 reaction to that one.
4. Please make requests for single icons, unless you are requesting a couple of strictly related icons (e.g., thumbs-up/thumbs-down).
5. Please and thank you if you include the following:
  - Title your [new issue](../../issues/new?title=Icon%20Request:%20icon-) `Icon request: icon-name` (e.g., `Icon request: icon-car`).
  - Include a few use cases for your requested icon. How do you plan on using it?
  - Attach or link to a single color image or two that represent the idea you're going for.
  - Request concrete objects: it's harder to make an icon to represent happiness, it's easier to make a smiley face. ☺


## Adding a new icon

Adding a new icon is a couple steps process that will require your attention and eyes for details. It might be a bit intimidating at the beginning, but should be easy to repeat once you've gone through it once or twice.

0. Follow the [README.md](README.md#building-fork-awesome) to install the necessary tools.
1. All icons are originally designed in SVG and fit in a grid (see `src/icons/icon-template-inkscape.svg` for a template for Inkscape).
2. Most icons should fit a square that is centered vertically and aligned left in that template. (Try importing existing icons in that template to understand how they fit.)
3. Design your icon in black only. No transparency. No gradient. Use simple shapes and forms. Note that it will be automatically transformed into a glyph. So if the design is complex, it might not show in the font as expected. Change a few things and try again if that happens.
4. From the `src/icons` folder, use the `make` command to build the icon font. It will also generate a file called `src/icons/forkawesome/forkawesome-preview.html`. Open it with a browser and search your icon on the test page. This preview file will show you how your design behaves after conversion. It will also automatically associate a unicode code point for it. Be sure remember it.
5. Once you are satisfied with your design and the preview of it. Add the icon name, unicode point and icon information at the bottom of the `src/icons/icons.yml` file. Look at other entries to see how it's done and to give it a proper classification.
6. Once all this is done, commit your changes and make a pull request.


## Suggesting icon keyword addition/removal

Icon filters are maintained by the [Fork Awesome community on GitHub](../../pulls?q=is%3Apr+label%3Adoc).

If you feel that an icon

* is missing keyword(s)
* contains invalid keyword(s)

please send a [PR](https://help.github.com/articles/using-pull-requests/) to the `master` branch.


## Reporting issues

We only accept issues that are icon requests, bug reports, or feature requests. Bugs must be isolated and reproducible problems that we can fix within the Fork Awesome core. Please read the following guidelines to ensure you are the paragon of bug reporting.

1. **Search for existing issues.** We get a lot of duplicate issues, and you'd help us out a lot by first checking if someone else has reported the same issue. Moreover, the issue may have already been resolved with a fix available.
2. **Create an isolated and reproducible test case.** Be sure the problem exists in Fork Awesome's code with a [reduced test case](http://css-tricks.com/reduced-test-cases/) that should be included in each bug report.
3. **Include a live example.** Make use of jsFiddle, jsBin, or Codepen to share your isolated test cases.
4. **Share as much information as possible.** Include operating system and version, browser and version, version of Fork Awesome, etc. where appropriate. Also include steps to reproduce the bug.


## Key branches

- `master` is the latest, deployed version
- `gh-pages` is the hosted docs (not to be used for pull requests)

## Notes on the repo

Fork Awesome's CSS, LESS, SCSS, and documentation are all powered by Jekyll templates and built before each commit and release.
- `_config.yml` - much of the site is driven off variables from this file, including Font Awesome and Bootstrap versions
- `src/doc/` - All edits to documentation, LESS, SCSS, and CSS should be made to files and templates in this directory
- `src/icons/icons.yml` - all LESS, SCSS, and CSS icon definitions are driven off this single file


## Pull requests

- Any changes to the docs must be made to the Liquid templates in the `src/doc` directory
- Any changes to the styles must be made to the .less and .scss files in the `src/doc` directory
- If modifying the .less and .scss files, always recompile and commit the compiled files
- Try to share which browsers your code has been tested in before submitting a pull request


## Coding standards: HTML

- Two spaces for indentation, never tabs
- Double quotes only, never single quotes
- Always use proper indentation
- Use tags and elements appropriate for an HTML5 doctype (e.g., self-closing tags)


## Coding standards: CSS

- Adhere to the [Recess CSS property order](http://markdotto.com/2011/11/29/css-property-order/)
- Multiple-line approach (one property and value per line)
- Always a space after a property's colon (e.g., `display: block;` and not `display:block;`)
- End all lines with a semi-colon
- For multiple, comma-separated selectors, place each selector on its own line
- Attribute selectors, like `input[type="text"]` should always wrap the attribute's value in double quotes, for consistency and safety (see this [blog post on unquoted attribute values](http://mathiasbynens.be/notes/unquoted-attribute-values) that can lead to XSS attacks)


## License

By contributing your code, you agree to license your contribution under the terms of the MIT License:
- http://opensource.org/licenses/mit-license.html


## Thanks

Thanks to Bootstrap for their wonderful CONTRIBUTING.MD doc. It was modified to create this one.
