// Builds the sitemap for whatever domain the site is opened on.
module.exports = (req, res) => {
  const host = req.headers["x-forwarded-host"] || req.headers.host || "localhost";
  const base = "https://" + host;
  const xml = '<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n  <url>\n    <loc>' + base + '/</loc>\n    <lastmod>2026-11-04</lastmod>\n    <changefreq>monthly</changefreq>\n    <priority>1.0</priority>\n  </url>\n</urlset>\n';
  res.statusCode = 200;
  res.setHeader("Content-Type", "application/xml; charset=utf-8");
  res.setHeader("Cache-Control", "public, s-maxage=86400");
  res.end(xml);
};
