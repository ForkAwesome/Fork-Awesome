---
---
PATH  := ../node_modules/.bin:$(PATH)

FA_ROOT_DIRECTORY = assets/fork-awesome
FA_LESS_DIRECTORY = assets/fork-awesome/less
FA_SCSS_DIRECTORY = assets/fork-awesome/scss
FA_CSS_DIRECTORY = assets/fork-awesome/css

FA_LESS_MODERN = ${FA_LESS_DIRECTORY}/fork-awesome.less
FA_SCSS_MODERN = ${FA_SCSS_DIRECTORY}/fork-awesome.scss

FA_CSS_MODERN = ${FA_CSS_DIRECTORY}/fork-awesome.css
FA_CSS_MODERN_MIN = ${FA_CSS_DIRECTORY}/fork-awesome.min.css

SITE_LESS_DIRECTORY = assets/less
SITE_CSS_DIRECTORY = assets/css

SITE_LESS = ${SITE_LESS_DIRECTORY}/site.less
SITE_CSS = ${SITE_CSS_DIRECTORY}/site.css

build:
	@echo "Compiling Less files"
	@mkdir -p ${FA_CSS_DIRECTORY}

	lessc ${FA_LESS_MODERN} ${FA_CSS_MODERN}
	lessc --clean-css="--compatibility=ie8" --source-map ${FA_CSS_MODERN} ${FA_CSS_MODERN_MIN}

	lessc --clean-css="--compatibility=ie8" --source-map ${SITE_LESS} ${SITE_CSS}

	@echo "Moving CSS, LESS & SASS to /"
	cp -r ${FA_ROOT_DIRECTORY}/ ../

	@echo "Moving font files to assets"
	cp -r ../fonts ${FA_ROOT_DIRECTORY}/

	@echo "Updating Readme"
	mv README.md-nobuild ../README.md

	@echo "Generating zip file"
	cd assets && mv fork-awesome fork-awesome-{{ site.forkawesome.version }} && zip -r9 fork-awesome-{{ site.forkawesome.version }}.zip fork-awesome-{{ site.forkawesome.version }} && mv fork-awesome-{{ site.forkawesome.version }} fork-awesome

	# TODO: figure out why this was here and remove it if unused. It blocked running local less version
	# find .. -type f ! -perm 644 -exec chmod 644 {} \;

default: build


.PHONY: build
