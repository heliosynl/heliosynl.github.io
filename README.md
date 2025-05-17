# Helios Li's Personal Website
**Powered by [Academic pages](https://academicpages.github.io/)**
Academic Pages is a Github Pages template for academic websites.

## See more in [my website](https://heliosynl.github.io)

## Running locally
Run `bundle exec jekyll serve -l -H localhost` to generate the HTML and serve it from `localhost:4000` the local server will automatically rebuild and refresh the pages on change.

if cant, 
- `sudo apt update && sudo apt upgrade -y`
- `bundle config set --local path 'vendor/bundle'`
- `bundle install`
- `bundle exec jekyll serve -l -H localhost`

## notes
### 2025Feb04
```
[2025-02-04 09:23:52] ERROR '/images/favicon-32x32.png' not found.
[2025-02-04 09:23:52] ERROR '/images/favicon-16x16.png' not found.
[2025-02-04 09:23:52] ERROR '/images/favicon-96x96.png' not found.
[2025-02-04 09:23:52] ERROR '/images/android-chrome-192x192.png' not found.
```

### 2025Apr27
Changed files compared to template:
/_config.yml
/README.md
/_teaching
/_talks
/_research
/_records
/_publications
/_posts
/_pages/about.md
/_pages/codes.html
/_pages/cv.md
/_pages/notes.html
/_pages/posts.html
/_pages/publications.html
/_pages/records.html
/_pages/research.html
/_pages/sitemap.md
/_notes
/_layouts/single_notes.html
/_includes/comments-providers/custom.html
/_includes/archive-post.html
/_includes/archive-single_backup.html
/_includes/archive-single-talk.html
/_includes/archive-single.html
/images
/files
/_data/navigation.yml
/_codes

remove
/_portfolio