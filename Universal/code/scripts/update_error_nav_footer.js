const fs = require('fs');

const indexPath = 'Index/website/Index.html';
const errorPath = 'Error/website/Error.html';

const indexHtml = fs.readFileSync(indexPath, 'utf8');
let errorHtml = fs.readFileSync(errorPath, 'utf8');

function extractBlock(html, startString, endString) {
    const start = html.indexOf(startString);
    if (start === -1) return null;
    const end = html.indexOf(endString, start) + endString.length;
    return html.substring(start, end);
}

// Nav ends right before <div class="section _404-content"> in Error
// In Index, it ends right before <div class="pre-loader"> or <section class="section home-hero">
// A better way is to split the strings
const indexNavStartStr = '<div class="navber-v2 w-nav"';
const indexNavStart = indexHtml.indexOf(indexNavStartStr);
const indexNavEnd = indexHtml.indexOf('<div class="pre-loader">', indexNavStart);
const navHtml = indexHtml.substring(indexNavStart, indexNavEnd);

const errorNavStart = errorHtml.indexOf(indexNavStartStr);
const errorNavEnd = errorHtml.indexOf('<div class="section _404-content">', errorNavStart);

if (indexNavStart !== -1 && indexNavEnd !== -1 && errorNavStart !== -1 && errorNavEnd !== -1) {
    errorHtml = errorHtml.substring(0, errorNavStart) + navHtml + errorHtml.substring(errorNavEnd);
    console.log("Nav successfully replaced.");
}

// Footer
const footerStartStr = '<section class="footer"';
const indexFooterStart = indexHtml.indexOf(footerStartStr);
const indexFooterEnd = indexHtml.indexOf('</section>', indexFooterStart) + '</section>'.length;
const footerHtml = indexHtml.substring(indexFooterStart, indexFooterEnd);

const errorFooterStart = errorHtml.indexOf(footerStartStr);
const errorFooterEnd = errorHtml.indexOf('</section>', errorFooterStart) + '</section>'.length;

if (indexFooterStart !== -1 && indexFooterEnd !== -1 && errorFooterStart !== -1 && errorFooterEnd !== -1) {
    errorHtml = errorHtml.substring(0, errorFooterStart) + footerHtml + errorHtml.substring(errorFooterEnd);
    console.log("Footer successfully replaced.");
}

fs.writeFileSync(errorPath, errorHtml, 'utf8');
