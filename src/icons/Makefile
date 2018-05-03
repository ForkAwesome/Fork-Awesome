FA_ROOT_FONTS_DIR = ../../fonts
FA_FONTCUSTOM_OUTPUT_DIR = ./forkawesome

build:
	@echo "Cleaning up SVG files..."
	npx svgo --quiet --pretty --config=svgo_config.json --folder=svg

	@echo "Compiling Icons into a ForkAwesome fonts..."
	bundle exec fontcustom compile

	@echo "Copying builds to root folder (package release)..."
	cp ${FA_FONTCUSTOM_OUTPUT_DIR}/forkawesome.eot ${FA_ROOT_FONTS_DIR}/forkawesome-webfont.eot
	cp ${FA_FONTCUSTOM_OUTPUT_DIR}/forkawesome.svg ${FA_ROOT_FONTS_DIR}/forkawesome-webfont.svg
	cp ${FA_FONTCUSTOM_OUTPUT_DIR}/forkawesome.ttf ${FA_ROOT_FONTS_DIR}/forkawesome-webfont.ttf
	cp ${FA_FONTCUSTOM_OUTPUT_DIR}/forkawesome.woff ${FA_ROOT_FONTS_DIR}/forkawesome-webfont.woff
	cp ${FA_FONTCUSTOM_OUTPUT_DIR}/forkawesome.woff2 ${FA_ROOT_FONTS_DIR}/forkawesome-webfont.woff2

	@echo "done."

default:
	build

.PHONY: build
