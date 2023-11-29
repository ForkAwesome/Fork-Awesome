module.exports = {
    plugins: [
        {
            name: "removeAttrs",
            params: {
                attrs: "(glyph-name|unicode)",
            }
        },
        "removeScriptElement",
        "removeRasterImages"
    ]
};
