##
# Generate an all-contributors badge with the number of contributors

require "json"

module Jekyll
  class AllContributors < Generator
    def generate(site)
      all_contributors_rc = File.read(File.join(Dir.pwd, '.all-contributorsrc'))
      all_contributors = JSON.parse(all_contributors_rc)
      total_contributors = all_contributors['contributors'].length
      site.pages.each do |page|
        page.data['total_contributors'] = total_contributors
      end
    end
  end
end
