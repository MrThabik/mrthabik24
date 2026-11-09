module.exports = (req, res) => {
  const host = req.headers["x-forwarded-host"] || req.headers.host || "localhost";
  res.statusCode = 200;
  res.setHeader("Content-Type", "text/plain; charset=utf-8");
  res.setHeader("Cache-Control", "public, s-maxage=86400");
  res.end("User-agent: *\nAllow: /\nDisallow: /private/\nSitemap: https://" + host + "/sitemap.xml\n");
};
