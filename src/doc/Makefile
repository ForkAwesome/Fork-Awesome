---
---
PATH  := ../node_modules/.bin:$(PATH)

FA_ROOT_DIRECTORY = assets/fork-awesome
FA_LESS_DIRECTORY = assets/fork-awesome/less
FA_SCSS_DIRECTORY = assets/fork-awesome/scss
FA_CSS_DIRECTORY = assets/fork-awesome/css

FA_LESS_MODERN = ${FA_LESS_DIRECTORY}/fork-awesome.less
FA_LESS_COMPAT = ${FA_LESS_DIRECTORY}/v5-compat.less
FA_SCSS_MODERN = ${FA_SCSS_DIRECTORY}/fork-awesome.scss

FA_CSS_MODERN = ${FA_CSS_DIRECTORY}/fork-awesome.css
FA_CSS_MODERN_MIN = ${FA_CSS_DIRECTORY}/fork-awesome.min.css
FA_CSS_COMPAT = ${FA_CSS_DIRECTORY}/v5-compat.css
FA_CSS_COMPAT_MIN = ${FA_CSS_DIRECTORY}/v5-compat.min.css

SITE_LESS_DIRECTORY = assets/less
SITE_CSS_DIRECTORY = assets/css

SITE_LESS = ${SITE_LESS_DIRECTORY}/site.less
SITE_CSS = ${SITE_CSS_DIRECTORY}/site.css

build:
	@echo "Cleaning build dirs"
	rm -rf ./less/
	rm -rf ./scss/

	@echo "Compiling Less files"
	@mkdir -p ${FA_CSS_DIRECTORY}

	lessc ${FA_LESS_MODERN} ${FA_CSS_MODERN}
	lessc --clean-css="--compatibility=ie8" --source-map ${FA_CSS_MODERN} ${FA_CSS_MODERN_MIN}

	lessc ${FA_LESS_COMPAT} ${FA_CSS_COMPAT}
	lessc --clean-css="--compatibility=ie8" --source-map ${FA_CSS_COMPAT} ${FA_CSS_COMPAT_MIN}

	lessc --clean-css="--compatibility=ie8" --source-map ${SITE_LESS} ${SITE_CSS}

	@echo "Moving CSS, LESS & SASS to /"
	mv ${FA_SCSS_DIRECTORY}/fork-awesome.scss.txt ${FA_SCSS_DIRECTORY}/fork-awesome.scss

	mv ${FA_SCSS_DIRECTORY}/animated.scss.txt ${FA_SCSS_DIRECTORY}/_animated.scss
	mv ${FA_SCSS_DIRECTORY}/bordered-pulled.scss.txt ${FA_SCSS_DIRECTORY}/_bordered-pulled.scss
	mv ${FA_SCSS_DIRECTORY}/core.scss.txt ${FA_SCSS_DIRECTORY}/_core.scss
	mv ${FA_SCSS_DIRECTORY}/fixed-width.scss.txt ${FA_SCSS_DIRECTORY}/_fixed-width.scss
	mv ${FA_SCSS_DIRECTORY}/functions.scss.txt ${FA_SCSS_DIRECTORY}/_functions.scss
	mv ${FA_SCSS_DIRECTORY}/icons.scss.txt ${FA_SCSS_DIRECTORY}/_icons.scss
	mv ${FA_SCSS_DIRECTORY}/larger.scss.txt ${FA_SCSS_DIRECTORY}/_larger.scss
	mv ${FA_SCSS_DIRECTORY}/list.scss.txt ${FA_SCSS_DIRECTORY}/_list.scss
	mv ${FA_SCSS_DIRECTORY}/mixins.scss.txt ${FA_SCSS_DIRECTORY}/_mixins.scss
	mv ${FA_SCSS_DIRECTORY}/path.scss.txt ${FA_SCSS_DIRECTORY}/_path.scss
	mv ${FA_SCSS_DIRECTORY}/rotated-flipped.scss.txt ${FA_SCSS_DIRECTORY}/_rotated-flipped.scss
	mv ${FA_SCSS_DIRECTORY}/screen-reader.scss.txt ${FA_SCSS_DIRECTORY}/_screen-reader.scss
	mv ${FA_SCSS_DIRECTORY}/stacked.scss.txt ${FA_SCSS_DIRECTORY}/_stacked.scss
	mv ${FA_SCSS_DIRECTORY}/variables.scss.txt ${FA_SCSS_DIRECTORY}/_variables.scss

	cp -r ${FA_ROOT_DIRECTORY}/* ../

	@echo "Moving font files to assets"
	cp -r "../fonts" ${FA_ROOT_DIRECTORY}/

	@echo "Updating Readme"
	mv "README.md-nobuild" "../README.md"

default: build


.PHONY: build
