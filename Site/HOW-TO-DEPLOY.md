# Put this site online: GitHub + Vercel

## 1. Get the files ready
1. Unzip the whole zip file (in your Files app, tap the zip and choose Extract).
2. Open the unzipped folder. You must see `index.html` right there, together with the other files.

## 2. Upload to GitHub
1. Sign in at github.com (create a free account if you need one).
2. Tap + (top right), then **New repository**. Name it `portfolio`. Choose Public or Private. Leave the README box empty. Tap **Create repository**.
3. On the empty repository page, tap **uploading an existing file**.
4. Tap **choose your files**, open the unzipped folder, select ALL the files (long-press one file, then Select all) and tap Open. On a computer, drag all the files out of the unzipped folder into the page (not the folder itself).
5. Wait until every file finishes uploading. It is about 15 MB.
6. Under Commit changes, keep "Commit directly to the main branch" and tap **Commit changes**.
7. Check: the repository's main page must list `index.html` at the top level.

## 3. Deploy on Vercel
1. Go to vercel.com and choose **Continue with GitHub**.
2. Tap **Add New**, then **Project**, and Import your `portfolio` repository (allow access if it asks).
3. Framework Preset: **Other**. Root Directory: leave as it is. Leave Build Command and Output Directory empty.
4. Tap **Deploy** and wait about 30 seconds, then tap **Visit**.
5. To keep the address mrthabik24.vercel.app: first delete the old project (its Settings, General, Delete Project), then name the new project `mrthabik24` when importing.

## 4. Update later
Open the GitHub repository, tap **Add file**, **Upload files**, choose only the changed files (same names replace the old ones) and Commit changes. Vercel redeploys by itself in about 30 seconds. After pressing Export site in the Admin panel, upload the downloaded `index.html` the same way.

## 5. If something goes wrong
- **404 page:** `index.html` is not at the top level of the repository. Move it up, or set Vercel, Settings, General, Root Directory to the folder that holds it, then redeploy.
- **Upload stops:** GitHub accepts up to 100 files at a time. Upload the missing files in a second batch.
- **Old version still shows:** wait a minute and reload, or clear the browser cache.

## 6. Optional
- Visitor counts: in your Vercel project open Analytics and click Enable.
- Google: add https://mrthabik24.vercel.app in Google Search Console and submit `sitemap.xml`. If you use another address, edit `sitemap.xml` and `robots.txt` first.
- Choose a **Private** GitHub repository if you don't want people to browse your files on GitHub. The website itself still works.
