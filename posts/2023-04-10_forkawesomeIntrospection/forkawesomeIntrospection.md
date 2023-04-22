# Forkawesome introspection

This is a long post. A summary would be:

> I am personally not motivated to work further on Forkawesome; I think the project is deprecated and should be put into legacy mode.
> 
> The driving force for forking—to have a community run icon set—has not been realized. The site and font build processes are broken. The source icon files need to be reworked or remade. The project focuses on icon fonts, despite icon fonts as a technology being outdated. Many other free icon sets now exist.

This post follows another looking at the [results of a 4 month survey](https://github.com/ForkAwesome/Fork-Awesome/blob/master/posts/2023-04-05_forkawesomeSurvey/surveyResults.md).

The first section deals with the **history** of Fontawesome and what lead to it being forked into Forkawesome. You can skip it. If you're only half interested, start at [Fontawesome 5.x](#fontawesome-5x).

The second section deals with the **[state of Forkawesome](#state-of-forkawesome)**, covering: licensing, tech, aim and relevance.

I end with what could or should be done **[going forward](#going-forward)**, information for possible future maintainers and what I learned along the way. 



---

## History
### Fontawesome 1.0.0

[Fontawesome 1.0.0](https://github.com/FortAwesome/Font-Awesome/releases/tag/v1.0.0) was the sole release of series 1.x by Dave Gandy on the 10th of March 2012, _"the iconic font designed for use with Twitter Bootstrap"_. A set of 140 stylistically coherent icons, available as icon fonts, licensed under CC BY 3.0

### Fontawesome 2.0.0
[Fontawesome 2.0.0](https://github.com/FortAwesome/Font-Awesome/releases/tag/2.0.0) was the sole release of series 2.x, again by Gandy, on the 4th of June 2012. 210 icons, still CC BY 3.0.

### Fontawesome 3.x
[Fontawesome 3.0.0](https://github.com/FortAwesome/Font-Awesome/releases/tag/v3.0.0) was released by Gandy on the 2nd of January 2013. An instance of the [Fontawesome 3.x website](https://fontawesome.com/v3/) is still running; it has a 'Community' page which, emphasis added, states:

> Font Awesome has a vibrant **community** of folks helping each other out. You can get support report bugs, request new icons, **submit pull requests**, check upcoming milestones

The licensing was changed to have different licenses for different parts of the project: SIL Open Font License for the font; MIT for CSS, LESS and SASS file and CC BY 3.0 for pictograms. At the end of the licensing section, is a statement that _"Attribution is no longer required"_.

The final release of this series was [3.2.1](https://github.com/FortAwesome/Font-Awesome/releases/tag/v3.2.1) on the 17th of June 2013 with 361 icons.

### Fontawesome 4.x
[Fontawesome 4.0.0](https://github.com/FortAwesome/Font-Awesome/releases/tag/v4.0.0) was released by Gandy on the 23rd of October 2013. An instance of the [Fontawesome 4.x website](https://fontawesome.com/v4/) is still running. This saw another change in licensing, with documentation now licensed under CC BY 3.0, and the licensing of pictograms dropped.

The final release of this series, and the final release by Gandy, was [4.7.0](https://github.com/FortAwesome/Font-Awesome/releases/tag/v4.7.0) on the 24th of October 2016 with 675 icons. The licensing section for 4.7.0 is, as follows:

>- The Font Awesome font is licensed under the SIL OFL 1.1: http://scripts.sil.org/OFL
>- Font Awesome CSS, LESS, and Sass files are licensed under the MIT License: https://opensource.org/licenses/mit-license.html
>- The Font Awesome documentation is licensed under the CC BY 3.0 License: http://creativecommons.org/licenses/by/3.0/
>- Attribution is no longer required as of Font Awesome 3.0, but much appreciated: `Font Awesome by Dave Gandy - http://fontawesome.io`

### Fontawesome 5.x
Gandy created a [kickstarter](https://www.kickstarter.com/projects/232193852/font-awesome-5/) for the development of Fontawesome 5 some time before the [25th of October 2016](https://www.kickstarter.com/projects/232193852/font-awesome-5/posts/1718476). It was to be a complete redesign of the icon set, yet backwards compatible, with new features and a pro version (i.e. freemium model). It reached a final crowdfunding sum of $1,076,960, despite an initial goal of just $30,000, making it the _"most funded software kickstarter ever"_ at the time (still?) The amusing crowdfunding [video]( https://www.youtube.com/watch?v=CNoH3J7iSrA) must have helped.

[Fontawesome 5.0.6](https://github.com/FortAwesome/Font-Awesome/releases/tag/5.0.6), the initial release of the 5.x series, was released on the 6th of February 2018 by Rob Madole. (The very first release of series 5.x, 5.0.0-alpha1, was released on the 23rd of June 2017, but is no longer available.) On the 4th of February 2018 Julian Deswaef raised the [issue](https://github.com/FortAwesome/Font-Awesome/issues/12199#issuecomment-362919956) that the build system for the website and CSS, LESS & SASS was no longer shared, and that community pull requests were continuing to be refused. Madole confirmed these developments were intentional [some days later](https://github.com/FortAwesome/Font-Awesome/issues/12199#issuecomment-363168281). 

### Forkawesome 1.x
Julian made a fork of Fontawesome 4.7.0, naming it Forkawesome in early February. In an [early commit](https://github.com/ForkAwesome/Fork-Awesome/commit/410f4bb583876fbd98fb114f15f884d06122af1a) he explained:

> Following concerns regarding [the development of Font Awesome](https://github.com/FortAwesome/Font-Awesome/issues/12199#issuecomment-362919956), the PR Freeze since Oct 2016 and the direction Fort Awesome is taking with the version 5.0 of their project, we are forking Font Awesome (4.7), in order to build on this incredible tool Dave Gandy has given us, while at the same time allowing this project to be run by a distributed community of contributors.

Julian exploded the webfont into individual SVG glyphs on the [13th of February 2018](https://github.com/ForkAwesome/Fork-Awesome/commit/8ed3619f719732acc04f9f5bb58284784449c9f4) and added a build process to generate icon fonts from the SVGs using [fontcustom](https://github.com/FontCustom/fontcustom) [5 days later](https://github.com/ForkAwesome/Fork-Awesome/commit/4469d13ec9a49e49155c3b863fe9ae9c433ac25e) (Fontawesome never released their build process for their icon fonts.) [Forkawesome 1.0.0](https://github.com/ForkAwesome/Fork-Awesome/releases/tag/1.0.0) was released later that same day, on the 18th of February 2018.

There was strong initial activity with many new icons added and other improvements to project. Things got gradually quieter, with a no foreseeable release after [1.1.7](https://github.com/ForkAwesome/Fork-Awesome/releases/tag/1.1.7) on the 28th of February 2019. I had been using Forkawesome for a couple of things and, noticing the inactivity, asked around in [April 2021](https://github.com/ForkAwesome/Fork-Awesome/issues/292) to see if there was interest in reactivating it. A small group assembled, and Julian joined some of these initial calls, passing over permissions and information as necessary.

The new team had multiple calls, and eventually managed to release version [1.2.0](https://github.com/ForkAwesome/Fork-Awesome/releases/tag/1.2.0), with  796 icons, on August the 26th 2021. At this point the team was just two of us, and when the other had to drop out, I was too far out my depth to continue. 1.2.0 is the last release to date.

![](img/Screenshot%20from%202023-04-07%2022-54-23.png)
—_code frequency in the Forkawesome repository from 2012 with big spike at the time of fork_

---

## State of Forkawesome
### Licensing
Julian created the source SVGs for Forkawesome by 'exploding' the webfont from Fontawesome 4.7.0 which was licensed under the SIL OFL (Open Font License) 1.1. I am not very familiar with the license, but after reading into it, it is clearly tailored for fonts. Users may embed OFL fonts in documents, apps or other works ["without any kind of attribution"](https://scripts.sil.org/cms/scripts/page.php?item_id=OFL-FAQ_web#e71fabc0), and such works may be sold. Users may not sell the font standalone, and must license derivatives with the OFL (i.e. copyleft/sharealike). Presumably the OFL applies to the individual source SVGs even though they aren't really fonts any more.

The current [Fontawesome Free licensing page](https://fontawesome.com/license/free) incorrectly states _"Attribution is required by MIT, SIL OFL, and CC BY licenses"_ since, as far as I can tell, attribution is only required in CC BY. The current Forkawesome webfonts are still licensed under OFL, meaning it should be possible to explode them in the same way now. However, there is no SVG [webfont](https://github.com/FortAwesome/Font-Awesome/tree/6.x/webfonts) any more, so work would need to proceed from a .ttf or .woff2

### Technical
#### Build
Forkawesome uses [fontcustom](https://github.com/FontCustom/fontcustom), a ruby gem, to build the icon font from the source SVGs. Fontcustom received its last commit 6 years ago. Some node packages are also used in the build chain to optimize SVGs and process LESS. It uses Jekyll (also Ruby) to make the website.

Building on latest Ubuntu doesn't work. This was the case when we took over the project in April 2021. Dion found the quickest way to set up a working development environment was to set up a [VM with Ubuntu 18.04](https://pad.kanthaus.online/s/_TbBWoaLU#). Somehow Shine and I got something working without using a VM by using rbenv or RVM (still suppressing lots of errors.) I decided to give try building before writing this but I didn't manage... dependencies wanting older versions of Ruby, dependencies being outdated to breaking point, rbenv and rvm seemingly not working... Then again, I'm very unfamiliar with Ruby, and perhaps some Ruby-pro could get it all figured out in a flash.

#### Icon font
Forkawesome started and continued primarily as an icon font. Icon fonts present(ed) a convenient way for developers to include vector icons in their projects: Internet Explorer didn't support SVGs until version 9. IE8 is now, thankfully, a long time gone and there are many downsides to using icon fonts instead of SVGs. This [article](https://css-tricks.com/icon-fonts-vs-svg/) by Chris Coyier of CSS-Tricks from 2014 and this [article](https://www.irigoyen.dev/blog/2021/02/17/stop-using-icon-fonts/) by Michael Irigoyen from 2021 outline the details better than I will here.

In short, icon fonts:
- are treated as fonts by browsers, and anti-aliased as such, which can decrease sharpness
- are positioned as pseudo elements, which are more complex/surprising to work with
- present an accessibility issue for screen-readers unless [extra care is taken](https://forkaweso.me/Fork-Awesome/accessibility/))
- need to be compiled per project, otherwise they contain unused icons

This last point bears emphasis: suppose, optimistically, a site uses 70 icons from Forkawesome. That means over 90% of the icon font was transferred and not used. The Forkawesome .woff2 + accompanying .css is 146.8 kB → ~ 130 kB wasted.

Icon fonts are a hack for <IE8. Any advantage they offer developers are outweighed by costs to users and network. All that said, the Forkawesome icon fonts do work OK!

#### SVG
The Forkawesome SVGs cannot reliably be used right now, since many are positioned off-center, or extend past their viewbox. In the following example (included in this post's repo), the Forkawesome heart SVG is significantly cut off, while the mastodon SVG is fine:

![](img/Screenshot%20from%202023-04-09%2017-08-21.png)
—*example showing 2 mastodon and 2 heart icon SVGs, from Forkawesome 1.2.0 and Fontawesome 6.4.0 respectively.*

About [5 issues](https://github.com/ForkAwesome/Fork-Awesome/issues/200) relate to this.

#### Distribution
Aside from the Github repository with releases as tagged commits, Forkawesome is distributed via:
- packagist.org (PHP) https://packagist.org/packages/forkawesome/fork-awesome
- npmjs.org (Node) https://www.npmjs.com/package/fork-awesome
- jsdelivr.com (webfont CDN) https://www.jsdelivr.com/package/npm/fork-awesome

The CDN [stats](https://www.jsdelivr.com/package/npm/fork-awesome?tab=stats) report ~ 1M requests and ~50 Gb bandwidth per day. Fontawesome (4.7.0!), in comparison, has ~15M requests per day, ~550 Gb bandwidth.

![](img/Screenshot%20from%202023-04-07%2022-54-23.png)
—*chart of forkawesome CDN stats since January 2023. There is a slight increas in 1.2.0 usage over the time period.*

I wonder if a lot of the CDN use is driven by some Wordpress plugins? Because Fontawesome has ~70K Github stars compared to 1200 for Forkawesome. To me that suggests significant use by non-nerds. (Additional complicating factor: Fontawesome now delivers personalized webfont CDNs, much of their traffic will not be shown in this chart.)

![](img/Screenshot%20from%202023-04-08%2016-19-51.png)
—*chart of Github stars for for Fontawesome and Forkawesome*

### Aim
What was the aim of Forkawesome in the first place? It seems to me to have been a resistance against the enclosure of a common resource:
- the website build process was removed 
- pull requests were no longer accepted
- CDN use for Fontawesome 5.x+ requires an account
- the project went freemium

However:
- the website is almost a detail: most users probably don't care about building the site. More important is the icon font build process, which Fontawesome _never_ released: that is something Julian added after forking.
- that pull requests are no longer accepted is also more of a detail: Fontawesome still accepts icon requests via Github issues, and the significant majority of Forkawesome icon requests are Github issues. I presume most people simply care about whether the icon is integrated into the set. As it stands, users are more likely to get an icon integrated in Fontawesome (regular updates) than Forkawesome (no update upcoming)
- Forkawesome requiring an account is justified on the grounds that Fontawesome personalizes your SVG/SVG sprite/icon font/etc to just the icons you need... this could probably be done without an account.
- there is no "however" for going freemium. Getting over 30X what they asked for, then (partly) paywalling?

It seems to me it was a resistance above all of the spiritual change in Fontawesome going from community to commercial. Forkawesome was an attempt to keep the project going as a community.

### Relevance
There are now many, good icon sets. Aside from Fontawesome 6.4.0 free with its 2,020 icons, Ionicons (MIT) has 1,300, Google Material icons (Apache 2.0) has 2,832... Everything has the basics, and most have the well-known brands. What is usually missing is the 'good-and-not-yet-popular.' 

I think it's telling that most of the icons that have been added to Forkawesome have been small, open-source, federated or programming related. Fontawesome still lacks many icons Forkawesome now has: Pixelfed, Scuttlebutt, La(TeX), Gitea etc.

While it would be to have all the icons you possibly want in one place, perhaps the taget audience mostly struggle to find _any_ place with coverage of the 'good-and-not-yet-popular'. And that seems to be something Wakest initiated with this [wiki page for fediverse icons](https://joinfediverse.wiki/Fediverse_project_branding). The wiki platform seems to be a much better fit for community, much more DIY/DIT ("always accepting pull requests") than the default-restrictive git*** paradigm. 

---

## Going forward
Given everything I know, I think Forkawesome is mostly deprecated. While that is sad, considering the work that's gone in and the seeming failure of community against commerce, I think it would be worse to drag along.

My plan would be to put the project into legacy mode: putting pointers on the website and Github towards projects that supersede Forkawesome and slowly archiving. 

However, the survey I ran indicated most respondents would like to see the project reactivated, so I will first make an attempt to see if anyone else wants to take it over.

To anyone wanting to restart Forkawesome: Firstly the build processes for the icon font and website need to be fixed or made new. Then I would recommend remaking the source SVGs by exploding the current Fontawesome webfonts, since it has many more icons, with improved design. I would recommend abandoning icon fonts altogether, but if desired, providing a good way for personalized use.

I also want to be open that the last point—Forkawesome CDN currently transferring A Big Number of unused icons, gigabytes of wasted internet traffic—makes me feel quite uncomfortable. By not shutting down the CDN, which I could, I'm enabling its use. In the long term, I think it should be shut down.

This has been quite a negative article, so let me finish with some positive points! I learned some super valuable lessons:
- maintenance is a lot of work and responsibility
- do not even *think* about maintaining a project you didn't get running smoothly, locally first
- battling with an outdated/broken dev. env. you're unfamiliar with is very demoralizing
- it is important not to romanticise forking

I want to say thanks to Julian, for making the fork (100% the right decision at the time,) for all the work he put in and for trusting me to take over the project. Shine, for those long work sessions, showing me the ropes of professional Github use and getting 1.2.0 launched. Dion for figuring out _a_ way to get the project building! Vince, Hyde, Wakest, Tilmann and anyone else who dropped by to offer support and advice.

Thanks for reading!

