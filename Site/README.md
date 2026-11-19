# Thaseen Shabik N – portfolio (standalone site)

Plain files, no server and no account needed. Host the whole folder anywhere.

## Put it online (Vercel)
`index.html` must sit at the very top of what you upload, next to `vercel.json`, `api`, `assets` and `private`. If Vercel shows "404: NOT FOUND" right after a deploy that took under a second, the files are inside an extra folder.
Fix: either move the files up so `index.html` is at the top of the project or repository, or open the project on Vercel, go to Settings, General, Root Directory, enter the folder that contains `index.html`, save, and redeploy.
Settings for a new project: Framework Preset = Other, leave the Build Command and Output Directory empty.
You need HTTPS (Vercel and Netlify give it automatically).

## Sitemap, robots and clean addresses
- `/sitemap.xml` and `/robots.txt` are made automatically by the two small files in `api/`, using whatever domain the site is opened on, so they stay right after you add a custom domain. Submit `https://your-domain/sitemap.xml` in Google Search Console.
- Addresses such as `/project`, `/resume`, `/skills` and `/contact` open the matching page (set in `vercel.json`). On Netlify, add rules for these in a `_redirects` file instead.

## Certificates, project and resume pages
These pages open directly with no access code. The images are drawn onto the page instead of being placed as normal pictures, so there is no Save image option or long-press save. The page also blocks right-click, drag, copy and print, shows a moving watermark with your name and the time, and blurs the page when the window loses focus or Print Screen is pressed.
Be aware that no website can stop a screenshot or a screen recording. Those are done by the phone or computer itself, and the watermark is there to discourage and trace them. A technical visitor can still find the image files in `private/`.

Change or add images: put them in `private/<track>/` (tracks: intern, originals, esim, project, resume), then run `python tools/make_manifest.py` and upload the folder again. Images show in file-name order.

## Admin, Editor, Full control
Open with Ctrl+Alt+A / E / F, or tap the name in the header 7 times. Sign-in is checked in the browser, so it keeps out casual visitors only. It is not strong security, because the sign-in hashes are visible in the page.
This is a static site, so changes are not saved on the server. After editing, press **Export site**, then replace `index.html` with the downloaded file and redeploy. Maintenance mode works the same way: turn it on, export, redeploy.

## Notes
- Fonts load from Google Fonts when online. Offline they fall back to ordinary serif fonts. To make the site fully offline, download the font files and host them yourself.
- The page blocks right-click, copy and print on private pages. That only deters casual copying; screenshots can't be blocked.

## Image quality
Certificates, CV pages and your internship letter are stored at print-sharp resolution, and project photos at their original size. Tap any image on a private page to open it full screen, then pinch or scroll to zoom. The Naan Mudhalvan page is about 11 MB, so it takes a few seconds to open on mobile data.

## Added features (how to switch them on)
- **Open to work badge, key numbers, project video, message form:** open the Editor (Ctrl+Alt+E) and fill in the matching boxes, then Export site. Empty boxes stay hidden. The project video box takes a file you put in `assets/`, for example `assets/project.mp4`.
- **Email alerts for the message form:** create a free form at formspree.io, paste its link into the "Message form endpoint" box, then Export site. Without it, the form opens the visitor's email app instead.
- **Tamil and English:** the button in the header switches the page. The Tamil text is stored separately from the English text, so if you edit the English experience or skills, the Tamil version stays as it was. Please have a Tamil speaker check my translation.
- **QR code:** shown at the bottom of the Contact section. It points to the address the site is opened on, so it becomes your real web address after you host it.
- **Save my contact:** downloads a contact card (.vcf) with your name, phone and email.
- **Install on the home screen:** works on https hosting. On a phone, open the site in Chrome and choose Add to Home screen.
- **Visitor counts:** in the Vercel dashboard open your project, then Analytics, and click Enable. No code changes are needed. It counts visits without tracking people.
- **Custom domain:** in Vercel open the project, then Settings, Domains, and add your domain (for example thaseenshabik.in). Buy the domain at any registrar and follow the DNS steps Vercel shows.

## More features
- **Share button** in the footer (opens the phone's share menu, or copies the link), **Back to top** button, and **Copy phone / Copy email** buttons in Contact.
- **Preferred interview time:** a recruiter can pick a date and time, and it is added to the WhatsApp or email invitation.
- **Search engines:** the page includes structured data about you and a short text for visitors without JavaScript. `robots.txt` keeps search engines out of `/private/`. `404.html` is shown for wrong addresses.
- **Updated date:** the footer shows the date you last pressed Export site.

## Opening the site on your own computer or phone
Unzip the whole folder first. Do not open `index.html` from inside the zip viewer, because the other files are not available there. The background video is also built into `index.html`, so it plays even if only that file is opened. The private pages, the sharper 1080p video and the install-as-app feature need the whole folder on a web host.

## Recruiter features
- **Download resume (PDF):** a one-page resume (`assets/Thaseen-Shabik-N-Resume.pdf`) is offered in the first section and in the request section. It leaves out your date of birth, religion and family details. To change it, replace that file. The full CV pages stay view-only on the Resume page.
- **LinkedIn:** paste your link (starting with https://) into the Editor's LinkedIn box and press Export site. A LinkedIn button then appears in the first section and the footer.
- **Skills at a glance** and **Open to work** are editable in the Editor.
- **Certificates:** the Naan Mudhalvan page is grouped by topic with small thumbnails that open full size. After adding or renaming images, run `python tools/make_manifest.py` (needs `pip install pillow`) to rebuild the list and the thumbnails.

## Ultra features (added November 2026)
- **Email alerts for resume and interview requests:** the "Request resume" and "Send interview request" buttons send you an email. With no setup the page uses FormSubmit (formsubmit.co). The very first request sends YOU an activation email: open it and click the activation link once, then alerts reach your inbox. To use Formspree instead, paste its link into the Editor's "Message form endpoint" box and press Export site.
- **Interview calendar:** visitors pick a day and a time slot (India time). The time goes into the WhatsApp or email invitation, and they can download a calendar file (.ics). Set your days, hours and slot length in the Editor box "Interview availability".
- **Job-fit checker:** compares a pasted job description with your skills and lists matches and gaps. The keyword lists are in `index.html` (search for FITS and GAPS) if you want to change them.
- **Skills with proof:** each skill shows a level and links to its proof. Edit the lines in the Editor box "Skills with proof" (Skill|Level|Proof text|link). Levels used: Certified, Hands-on, Trained, Project.
- **Project viewer:** tabs for the working model, block diagram and circuit diagram. Set the Editor's project video box to a video file name to add a Video tab.
- **Programme links on certificates:** each Naan Mudhalvan certificate has a Programme link. It opens the page printed on the certificate's QR code. That page is the same for all certificates, so it is not a per-certificate check.
- **Notes:** four short notes. Edit or delete them in the Editor box "Notes".
- **References:** shows quotes you add in the Editor's testimonials box, plus a button for visitors to ask for references.

## Speed and layout changes (November 2026)
- **Page size:** `index.html` no longer carries the video inside it, so the page is about 130 KB instead of 1.3 MB. Upload the whole folder, because the page needs the video and image files next to it.
- **Background video only where it helps:** laptops and large screens play the background video. Phones and tablets show a calm still picture behind the page and play only the portrait video in the hero, which saves data and battery.
- **Fonts:** the page loads 3 font families instead of 8. The Tamil font is fetched only when someone switches to Tamil.
- **Glass bottom bar:** the section links (Experience to Contact) now sit in a glass bar at the bottom of the screen. On phones it scrolls sideways. The Menu button at the top still lists everything.
- **Animations pause** when the hero is off screen, and they calm down for visitors who have reduced motion turned on.
