# Fork Awesome
### A fork of the iconic font and CSS toolkit

[![npm](https://img.shields.io/npm/v/fork-awesome.svg?style=flat&colorB=CB3837)](https://www.npmjs.com/package/fork-awesome)
[![All Contributors](https://img.shields.io/badge/all_contributors-106-orange.svg?style=flat-square)](CONTRIBUTORS.md)
[![JSDeliver](https://data.jsdelivr.com/v1/package/npm/fork-awesome/badge)](https://www.jsdelivr.com/package/npm/fork-awesome)
[![CDNJS](https://img.shields.io/cdnjs/v/fork-awesome.svg?style=flat-square)](https://cdnjs.com/libraries/fork-awesome)
[![Build Status](https://travis-ci.org/ForkAwesome/Fork-Awesome.svg?branch=master)](https://travis-ci.org/ForkAwesome/Fork-Awesome)

Fork Awesome is a full suite of 733 pictographic icons for easy scalable vector graphics on websites, originally created by [Dave Gandy](https://twitter.com/davegandy) and now maintained by a community.

Following concerns regarding [the development of Font Awesome](https://github.com/FortAwesome/Font-Awesome/issues/12199#issuecomment-362919956), the PR Freeze since Oct 2016 and the direction [Fort Awesome](https://fortawesome.com/) is taking with the version 5.0 of their project, we are forking Font Awesome (4.7), in order to build on this amazing tool Dave Gandy has given us, while at the same time allowing this project to be run by a distributed community of contributors.

A tremendous gratitude is given to the whole team behind [Font Awesome](https://fontawesome.com), and you are encouraged to support them and buy Font Awesome Pro for your project.

That said, if you believe in distributed open source design and wish to be part of this new adventure, please start submitting patches and suggestions of improvement.

Also, if you care about owning the build process of your icon font, this project will give you that. The whole pipeline is shared and free to use for any purpose. You could be spinning your own icon font with your clever name by just forking this project and changing a few settings.

## How to use
There is a full page in our documentation website that explains [how to use Fork Awesome in your web project](http://forkawesome.github.io/Fork-Awesome/get-started/). It ranges from just pointing to a CSS file on a CDN, hosting it on your own server or even adapting the LESS and SCSS files to your own liking.

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

We also take great pride in recognizing any contributions made to this project. Whether you've written a blogpost about it, fixed a typo in the documentation or submitted new icons or code patches, we will happily list you in our [contributors list](CONTRIBUTORS.md).

## Versioning

Fork Awesome will be maintained under the Semantic Versioning guidelines as much as possible. Releases will be numbered
with the following format:

`<major>.<minor>.<patch>`

And constructed with the following guidelines:

* Breaking backward compatibility bumps the major (and resets the minor and patch)
* Big changes, without breaking backward compatibility, bumps the minor (and resets the patch)
* Bug fixes, small adaptations, adding a few icons and misc changes bumps the patch
* The fork started from FontAwesome 4.7 (last commit by Dave is [bdfa9823](https://github.com/ForkAwesome/Fork-Awesome/commits/master?after=b0bc8f6fb74e05c987ef7ce1525cd3ab8390a1c3+69)).
* The project starts at version 1.0.0. All references to versions before the fork are named 0.4.7

For more information on SemVer, please visit http://semver.org.

## Component
To include as a [component](https://github.com/componentjs/component), just run

    $ component install ForkAwesome/Fork-Awesome

Or add

    "ForkAwesome/Fork-Awesome": "*"

to the `dependencies` in your `component.json`.

## Building Fork Awesome

**Before you can build the project**, you must first have the following installed:

- [Ruby](https://www.ruby-lang.org/en/)
- Ruby Development Headers
  - **Ubuntu:** `sudo apt-get install ruby-dev` *(Only if you're __NOT__ using `rbenv` or `rvm`)*
  - **Windows:** [DevKit](http://rubyinstaller.org/)
  - **macOS:** no extra step required
- [Bundler](http://bundler.io/) (Run `gem install bundler` to install).
- [Node Package Manager (aka. `npm`)](https://docs.npmjs.com/getting-started/installing-node)

From the root of the repository, install the tools used to develop.

    $ bundle install
    $ npm install

Build the font:

    $:/src/icons make

Build the web documentation:

    $ npm run build

Or serve it on a local server on http://localhost:7998:

    $ npm run dev
