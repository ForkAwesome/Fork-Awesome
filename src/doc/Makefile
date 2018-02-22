---
---
PATH := ../../node_modules/.bin:$(PATH)

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

	bundle exec lessc ${FA_LESS_MODERN} > ${FA_CSS_MODERN}
	bundle exec lessc --clean-css="--compatibility=ie8" ${FA_LESS_MODERN} > ${FA_CSS_MODERN_MIN}
#	sass ${FA_SCSS_MODERN} ${FA_CSS_MODERN}

	bundle exec lessc --clean-css="--compatibility=ie8" ${SITE_LESS} > ${SITE_CSS}

	@echo "Moving font filse and README"
	cp -r ${FA_ROOT_DIRECTORY}/* ../
	mv README.md-nobuild ../README.md

	@echo "Generating zip file"
	cd assets && mv fork-awesome fork-awesome-{{ site.forkawesome.version }} && zip -r9 fork-awesome-{{ site.forkawesome.version }}.zip fork-awesome-{{ site.forkawesome.version }} && mv fork-awesome-{{ site.forkawesome.version }} fork-awesome

	find .. -type f ! -perm 644 -exec chmod 644 {} \;

default: build


.PHONY: build
