/**
 * advjalajsharma.in — consultation form handler (Google Apps Script web app).
 *
 * What it does with each request from the website form:
 *   1. Emails the details to RECIPIENT.
 *   2. Saves any uploaded documents into a private Google Drive folder
 *      ("Website consultation requests" / <date time> <name>), owned by the
 *      Google account that deploys this script. Nothing is shared publicly.
 *
 * Deploy: Deploy > New deployment > Web app
 *   Execute as: Me    Who has access: Anyone
 * Then paste the web app URL into data-endpoint="" on the form in index.html.
 */

const RECIPIENT = 'advjalaj107@gmail.com';
const ROOT_FOLDER_NAME = 'Website consultation requests';
const MAX_TOTAL_BYTES = 8 * 1024 * 1024;
const MAX_FILES = 10;
const MAX_REQUESTS_PER_HOUR = 30;
const ALLOWED = { 'application/pdf': 'pdf', 'image/jpeg': 'jpg', 'image/png': 'png' };

/** Run once from the editor to grant permissions and create the Drive folder. */
function setup() {
  getRootFolder_();
  Logger.log('Ready. Drive folder: ' + getRootFolder_().getUrl());
}

function doPost(e) {
  try {
    const d = JSON.parse((e && e.postData && e.postData.contents) || '{}');

    // Honeypot: real visitors never fill this hidden field.
    if (d.website) return json_({ ok: true });

    const name = line_(d.name, 100);
    const phone = line_(d.phone, 25);
    if (!name || phone.replace(/\D/g, '').length < 10) return json_({ ok: false, error: 'invalid' });

    // Basic flood protection.
    const cache = CacheService.getScriptCache();
    const count = Number(cache.get('requests') || 0);
    if (count >= MAX_REQUESTS_PER_HOUR) return json_({ ok: false, error: 'busy' });
    cache.put('requests', String(count + 1), 3600);

    const email = line_(d.email, 120);
    const validEmail = /^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(email) ? email : '';
    const city = ['Delhi', 'Noida'].indexOf(d.city) >= 0 ? d.city : 'Not stated';
    const type = line_(d.type, 60) || 'Not stated';
    const message = text_(d.message, 4000);
    const language = d.language === 'hi' ? 'Hindi' : 'English';

    // Save documents.
    const saved = [], skipped = [];
    let folderUrl = '';
    const files = Array.isArray(d.files) ? d.files.slice(0, MAX_FILES) : [];
    if (files.length) {
      const stamp = Utilities.formatDate(new Date(), 'Asia/Kolkata', 'yyyy-MM-dd HH.mm');
      const folder = getRootFolder_().createFolder(stamp + ' ' + safeName_(name));
      let total = 0;
      files.forEach(function (f) {
        const original = line_(f && f.name, 150) || 'document';
        const mime = String((f && f.mimeType) || '');
        let bytes;
        try { bytes = Utilities.base64Decode(String((f && f.data) || '')); } catch (err) { skipped.push(original); return; }
        if (!ALLOWED[mime] || !looksLike_(bytes, mime)) { skipped.push(original + ' (not a PDF, JPG or PNG)'); return; }
        total += bytes.length;
        if (total > MAX_TOTAL_BYTES) { skipped.push(original + ' (over the 8 MB limit)'); return; }
        let fname = safeName_(original);
        if (!new RegExp('\\.' + ALLOWED[mime] + '$|\\.jpeg$', 'i').test(fname)) fname += '.' + ALLOWED[mime];
        folder.createFile(Utilities.newBlob(bytes, mime, fname));
        saved.push(fname);
      });
      folderUrl = folder.getUrl();
    }

    const body = [
      'New consultation request from advjalajsharma.in',
      '',
      'Name:            ' + name,
      'Phone:           ' + phone,
      'Email:           ' + (validEmail || '—'),
      'Preferred city:  ' + city,
      'Type of matter:  ' + type,
      'Form language:   ' + language,
      '',
      'Particulars:',
      message || '—',
      '',
      'Documents: ' + (saved.length ? saved.length + ' saved' : 'none'),
      saved.map(function (n) { return '  • ' + n; }).join('\n'),
      skipped.length ? 'Not saved:\n' + skipped.map(function (n) { return '  • ' + n; }).join('\n') : '',
      folderUrl ? 'Private Drive folder: ' + folderUrl : '',
      '',
      'Received: ' + Utilities.formatDate(new Date(), 'Asia/Kolkata', 'dd MMM yyyy, h:mm a') + ' IST'
    ].filter(function (l) { return l !== null; }).join('\n');

    const mail = {
      to: RECIPIENT,
      subject: 'Consultation request: ' + name + ' (' + city + ', ' + type + ')',
      body: body,
      name: 'advjalajsharma.in'
    };
    if (validEmail) mail.replyTo = validEmail;
    MailApp.sendEmail(mail);

    return json_({ ok: true });
  } catch (err) {
    console.error(err);
    return json_({ ok: false, error: 'server' });
  }
}

function doGet() {
  return json_({ ok: true, service: 'advjalajsharma.in consultation form' });
}

/* ---------- helpers ---------- */
function getRootFolder_() {
  const it = DriveApp.getFoldersByName(ROOT_FOLDER_NAME);
  return it.hasNext() ? it.next() : DriveApp.createFolder(ROOT_FOLDER_NAME);
}
function json_(o) {
  return ContentService.createTextOutput(JSON.stringify(o)).setMimeType(ContentService.MimeType.JSON);
}
function line_(s, max) {
  return String(s == null ? '' : s).replace(/[\u0000-\u001f\u007f]/g, ' ').replace(/\s+/g, ' ').trim().slice(0, max);
}
function text_(s, max) {
  return String(s == null ? '' : s).replace(/\r\n?/g, '\n').replace(/[\u0000-\u0009\u000b-\u001f\u007f]/g, ' ').trim().slice(0, max);
}
function safeName_(s) {
  return String(s).replace(/[\\/:*?"<>|#%]/g, '_').replace(/^\.+/, '').slice(0, 120) || 'document';
}
/** Check the file's first bytes match its claimed type. */
function looksLike_(bytes, mime) {
  if (!bytes || bytes.length < 4) return false;
  const b0 = bytes[0] & 0xff, b1 = bytes[1] & 0xff, b2 = bytes[2] & 0xff, b3 = bytes[3] & 0xff;
  if (mime === 'application/pdf') return b0 === 0x25 && b1 === 0x50 && b2 === 0x44 && b3 === 0x46; // %PDF
  if (mime === 'image/png') return b0 === 0x89 && b1 === 0x50 && b2 === 0x4e && b3 === 0x47;       // .PNG
  if (mime === 'image/jpeg') return b0 === 0xff && b1 === 0xd8;                                      // JPEG SOI
  return false;
}
