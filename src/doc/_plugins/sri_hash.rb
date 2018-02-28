##
# Generate an SRI hash for a given file

require 'digest'

module Jekyll
	class GetSriHash < Liquid::Tag
		def initialize(tag_name, text, tokens)
			super
			@filename = text.strip
		end

		def render(context)
			sha256 = Digest::SHA256.file(@filename)
			"sha256-#{sha256.base64digest}"
		end
	end
end

Liquid::Template.register_tag('sri_hash', Jekyll::GetSriHash)
