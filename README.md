# Fork Awesome
### A fork of the iconic font and CSS toolkit

[![npm-badge]][npm-link] [![all-contrib]](CONTRIBUTORS.md) [![jsdeliver-badge]][jsdeliver-link] [![cdnjs-badge]][cdnjs-link] [![build-status-badge]][build-status-link] [![matrix-badge]][matrix-link]

**Fork Awesome is a suite of 796 pictographic and brand icons for easy, scalable vector graphics on websites and beyond.**

This project, as the name suggests, began as a fork of [Font Awesome](https://fontawesome.com). Font Awesome was originally created by [Dave Gandy](https://twitter.com/davegandy) and ran as a community project. However, as Font Awesome developed, pull requests from the community stopped being accepted (October 2016) and as of version 5.0 [the build system became private](https://github.com/FortAwesome/Font-Awesome/issues/12199#issuecomment-362919956) (February 2018).

With gratitude to Dave Gandy and the Font Awesome team, [Julien](https://github.com/xuv) [Deswaef](https://merveilles.town/@xuv) forked Font Awesome 4.7 into [Fork Awesome 1.0](https://github.com/ForkAwesome/Fork-Awesome/releases/tag/1.0.0) in February 2018, to continue building the amazing resource in a fully free, libre and open-source fashion, with and for the wider community. After a period of extended inactivity (i.e. no release since February 2019), several Fork Awesome users [got](https://github.com/ForkAwesome/Fork-Awesome/issues/292) [together](https://github.com/ForkAwesome/Fork-Awesome/issues/235) to try and revive the project 🌱

We are now catching up with backlogged issues and pull requests, updating technology and documentation — even reevaluating the project aims, as icon fonts gradually [become](https://www.irigoyen.dev/blog/2021/02/17/stop-using-icon-fonts/) [deprecated](https://cloudfour.com/thinks/seriously-dont-use-icon-fonts/). Come say hi in the [#forkawesome:matrix.org](https://matrix.to/#/#forkawesome:matrix.org) matrix room 🙂

## How to use
There is a full page in our documentation website that explains [how to use Fork Awesome in your web project](https://forkaweso.me/Fork-Awesome/get-started/). It ranges from just pointing to a CSS file on a CDN, hosting it on your own server or even adapting the LESS and SCSS files to your own liking.

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
- Tools required to build the font:
  - **Ubuntu:** `sudo apt-get install fontforge woff-tools woff2`

From the root of the repository, install the tools used to develop.

    $ bundle install
    $ npm ci

Build the font:

    $ make -C src/icons

Build the web documentation:

    $ npm run build

Or serve it on a local server on http://localhost:7998:

    $ npm run dev

### Build the font in a Docker container

Another possibility is to build the font using the Dockerfile provided.

First, build the Docker image:

    $ docker build -t fa-builder .

Then, run the Docker container:

    $ docker run --rm -it \
        -u $(id -u):$(id -g) \
        -v $(pwd):$(pwd) \
        -w $(pwd) \
        fa-builder

Within the container, build the font:

    $ bundle install --path vendor/bundle
    $ npm ci
    $ make -C src/icons

<!--- reference links for badges -->
[all-contrib]: https://img.shields.io/badge/all_contributors-128-orange.svg "All Contributors badge"
[build-status-badge]: https://travis-ci.org/ForkAwesome/Fork-Awesome.svg?branch=master "Build status badge"
[build-status-link]: https://travis-ci.org/ForkAwesome/Fork-Awesome
[cdnjs-badge]: https://img.shields.io/cdnjs/v/fork-awesome.svg "CDNJS badge"
[cdnjs-link]: https://cdnjs.com/libraries/fork-awesome
[jsdeliver-badge]: https://img.shields.io/jsdelivr/npm/hm/fork-awesome "JSDeliver badge"
[jsdeliver-link]: https://www.jsdelivr.com/package/npm/fork-awesome
[npm-badge]: https://img.shields.io/npm/v/fork-awesome.svg?colorB=CB3837 "NPM badge"
[npm-link]: https://www.npmjs.com/package/fork-awesome
[matrix-badge]: https://img.shields.io/matrix/forkawesome:matrix.org?label=%23forkawesome%3Amatrix.org "chat (matrix) badge"
[matrix-link]: https://matrix.to/#/#forkawesome:matrix.org
