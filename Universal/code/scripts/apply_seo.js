const fs = require('fs');
const path = require('path');

const rootDir = 'C:\\Users\\angam\\Downloads\\Nexyra Website';
const baseUrl = 'https://www.nexyratech.com';
const logoUrl = `${baseUrl}/Universal/images/Nexyra%20Logo.png`;

function getFiles(dir, files = []) {
    const fileList = fs.readdirSync(dir);
    for (const file of fileList) {
        const name = `${dir}/${file}`;
        if (fs.statSync(name).isDirectory()) {
            getFiles(name, files);
        } else if (name.endsWith('.html')) {
            files.push(name);
        }
    }
    return files;
}

const htmlFiles = getFiles(rootDir);
let sitemapUrls = [];

const commonKeywords = "IT Company South Africa, Cybersecurity Consulting, Zero Trust Solutions, DevSecOps pipelines, Agile SAFe Transformation, Cloud Infrastructure Security, Data Security, Nexyra Tech";

for (const file of htmlFiles) {
    if(file.includes('Cookie System')) continue; // Skip isolated cookie system

    let content = fs.readFileSync(file, 'utf-8');
    
    // Determine page specifics
    const filename = path.basename(file, '.html');
    let title = "";
    let desc = "";
    let relUrl = "";

    if (filename === 'Index') {
        title = "Nexyra Tech | Best IT & Cybersecurity Company in South Africa";
        desc = "Nexyra Tech is a premier cybersecurity and technology consulting firm in South Africa specializing in Zero Trust architecture, Cloud Infrastructure Security, and DevSecOps.";
        relUrl = "/";
    } else if (filename === 'About') {
        title = "About Nexyra Tech | Elite Cybersecurity Experts";
        desc = "Learn how Nexyra Tech engineers resilient, scalable cybersecurity solutions tailored to your unique environment.";
        relUrl = "/about";
    } else if (filename === 'Main Page' && file.includes('Services')) {
        title = "Our Services | Zero Trust, Cloud Security & DevSecOps | Nexyra Tech";
        desc = "Explore our core specialties: Zero Trust Architecture, Cloud & Data Security, DevSecOps pipelines, and Agile (SAFe) Transformations.";
        relUrl = "/services";
    } else if (filename === 'Contact') {
        title = "Contact Nexyra Tech | IT Consulting South Africa";
        desc = "Get in touch with Nexyra Tech to secure your organization's most critical assets with expert consulting and engineering.";
        relUrl = "/contact";
    } else if (filename === 'Blog Main Page') {
        title = "Cybersecurity Blog & Insights | Nexyra Tech";
        desc = "Read the latest insights on cybersecurity threats, Zero Trust, and Cloud Security from the experts at Nexyra Tech.";
        relUrl = "/blog";
    } else if (filename.startsWith('Blog Sub') || filename.startsWith('Blog ')) {
        // Try to extract existing title if possible
        const titleMatch = content.match(/<title>(.*?)<\/title>/);
        let origTitle = titleMatch ? titleMatch[1].split('|')[0].trim() : filename;
        title = `${origTitle} | Nexyra Tech Blog`;
        desc = `Read our detailed breakdown on ${origTitle}. Nexyra Tech provides elite insights on modern cybersecurity challenges.`;
        relUrl = `/blog/${filename.toLowerCase().replace(/ /g, '-')}`;
    } else {
        title = `${filename} | Nexyra Tech`;
        desc = "Nexyra Tech is a premier cybersecurity and technology consulting firm in South Africa.";
        relUrl = `/${filename.toLowerCase().replace(/ /g, '-')}`;
    }

    const fullUrl = `${baseUrl}${relUrl}`;
    sitemapUrls.push(fullUrl);

    // Remove existing meta tags to prevent duplicates
    content = content.replace(/<title>.*?<\/title>\s*/gi, '');
    content = content.replace(/<meta[^>]*name=["']description["'][^>]*>\s*/gi, '');
    content = content.replace(/<meta[^>]*name=["']keywords["'][^>]*>\s*/gi, '');
    content = content.replace(/<meta[^>]*property=["']og:.*?["'][^>]*>\s*/gi, '');
    content = content.replace(/<meta[^>]*property=["']twitter:.*?["'][^>]*>\s*/gi, '');
    content = content.replace(/<meta[^>]*name=["']twitter:.*?["'][^>]*>\s*/gi, '');

    // Construct new meta block
    const metaBlock = `
<title>${title}</title>
<meta name="description" content="${desc}" />
<meta name="keywords" content="${commonKeywords}" />
<meta property="og:title" content="${title}" />
<meta property="og:description" content="${desc}" />
<meta property="og:image" content="${logoUrl}" />
<meta property="og:url" content="${fullUrl}" />
<meta property="og:type" content="website" />
<meta name="twitter:card" content="summary_large_image" />
<meta name="twitter:title" content="${title}" />
<meta name="twitter:description" content="${desc}" />
<meta name="twitter:image" content="${logoUrl}" />
`;

    // Inject metaBlock right after <head>
    content = content.replace(/<head>/i, `<head>${metaBlock}`);
    
    fs.writeFileSync(file, content, 'utf-8');
    console.log(`Updated SEO for ${file}`);
}

// Generate sitemap.xml
const sitemapContent = `<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">
${sitemapUrls.map(url => `  <url>\n    <loc>${url}</loc>\n    <changefreq>weekly</changefreq>\n    <priority>${url === baseUrl + '/' ? '1.0' : '0.8'}</priority>\n  </url>`).join('\n')}
</urlset>`;

fs.writeFileSync(path.join(rootDir, 'sitemap.xml'), sitemapContent, 'utf-8');
console.log('Created sitemap.xml');

// Generate robots.txt
const robotsContent = `User-agent: *
Allow: /

Sitemap: ${baseUrl}/sitemap.xml`;

fs.writeFileSync(path.join(rootDir, 'robots.txt'), robotsContent, 'utf-8');
console.log('Created robots.txt');
