# Fork Awesome
### A fork of the iconic font and CSS toolkit

Fork Awesome is a full suite of 699 pictographic icons for easy scalable vector graphics on websites, originally created by [Dave Gandy](https://twitter.com/davegandy) and now maintained by a community.

Following concerns regarding [the development of Font Awesome](https://github.com/FortAwesome/Font-Awesome/issues/12199#issuecomment-362919956), the PR Freeze since Oct 2016 and the direction Fort Awesome is taking with the version 5.0 of their project, we are forking Font Awesome (4.7), in order to build on this incredible tool Dave Gandy has given us, while at the same time allowing this project to be run by a distributed community of contributors.

A tremendous gratitude is given to the whole team behind [Font Awesome](https://fontawesome.com), and you are encouraged to support them and buy Font Awesome Pro for your project.

Though If you believe in distributed open source design and wish to be part of this new adventure, please start submitting patches and suggestions of improvement.

## License
- The Fork Awesome font is licensed under the SIL OFL 1.1:
  - http://scripts.sil.org/OFL
- Fork Awesome CSS, LESS, and Sass files are licensed under the MIT License:
  - https://opensource.org/licenses/mit-license.html
- The Fork Awesome documentation is licensed under the CC BY 3.0 License:
  - https://creativecommons.org/licenses/by/3.0/

## Contributing

Please read through our [contributing guidelines](https://github.com/ForkAwesome/Fork-Awesome/blob/master/CONTRIBUTING.md).
Included are directions for opening issues, coding standards, and notes on development.

## Versioning

Fork Awesome will be maintained under the Semantic Versioning guidelines as much as possible. Releases will be numbered
with the following format:

`<major>.<minor>.<patch>`

And constructed with the following guidelines:

* Breaking backward compatibility bumps the major (and resets the minor and patch)
* New additions, including new icons, without breaking backward compatibility bumps the minor (and resets the patch)
* Bug fixes, changes to brand logos, and misc changes bumps the patch
* The fork started from FontAwesome 4.7 (last commit by Dave is [bdfa9823](https://github.com/ForkAwesome/Fork-Awesome/commits/master?after=b0bc8f6fb74e05c987ef7ce1525cd3ab8390a1c3+69)).
* The project starts at version 1.0.0. All references to versions before the fork are named 0.4.7

For more information on SemVer, please visit http://semver.org.

## Original author of Font Awesome:
- [Dave Gandy](https://github.com/davegandy)

## Component
To include as a [component](https://github.com/componentjs/component), just run

    $ component install ForkAwesome/Fork-Awesome

Or add

    "ForkAwesome/Fork-Awesome": "*"

to the `dependencies` in your `component.json`.

## Building on Fork Awesome

**Before you can build the project**, you must first have the following installed:

- [Ruby](https://www.ruby-lang.org/en/)
- Ruby Development Headers
  - **Ubuntu:** `sudo apt-get install ruby-dev` *(Only if you're __NOT__ using `rbenv` or `rvm`)*
  - **Windows:** [DevKit](http://rubyinstaller.org/)
- [Bundler](http://bundler.io/) (Run `gem install bundler` to install).
- [Node Package Manager (aka. `npm`)](https://docs.npmjs.com/getting-started/installing-node)

From the root of the repository, install the tools used to develop.

    $ bundle install
    $ npm install

Build the font:

    $:/src/icons make

Build the web documentation:

    $ npm run build

Or serve it on a local server on http://localhost:7998/Fork-Awesome/:

    $ npm run dev

To deploy the project and documentation on GH pages:

    $ jgd -n
