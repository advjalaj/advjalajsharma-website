/* advjalajsharma.in — language switch, disclaimer and consultation form */
(function(){
  var root = document.documentElement;
  var isHome = document.body.getAttribute('data-page') === 'home';
  var lang = root.getAttribute('data-lang') || 'en';

  function store(k, v){ try{ localStorage.setItem(k, v); }catch(e){} }
  function read(k){ try{ return localStorage.getItem(k); }catch(e){ return null; } }

  /* ---------- language ---------- */
  var options = [].slice.call(document.querySelectorAll('option[data-hi]'));
  options.forEach(function(o){ o.dataset.en = o.textContent; });
  var phs = [].slice.call(document.querySelectorAll('[data-ph-en]'));

  function setLang(l){
    lang = l;
    root.setAttribute('data-lang', l);
    root.lang = l === 'hi' ? 'hi' : 'en';
    document.querySelectorAll('.lang button').forEach(function(b){ b.setAttribute('aria-pressed', b.dataset.set === l); });
    options.forEach(function(o){ o.textContent = l === 'hi' ? o.dataset.hi : o.dataset.en; });
    phs.forEach(function(el){ el.placeholder = l === 'hi' ? el.dataset.phHi : el.dataset.phEn; });
    if (typeof renderFiles === 'function') renderFiles();
    store('site-lang', l);
  }
  if (isHome){
    document.querySelectorAll('.lang button').forEach(function(b){
      b.addEventListener('click', function(){ setLang(b.dataset.set); });
    });
  }
  /* article pages: the switch is a link to the other-language article */
  document.querySelectorAll('.lang a[data-set]').forEach(function(a){
    a.addEventListener('click', function(){ store('site-lang', a.dataset.set); });
  });

  /* ---------- disclaimer ---------- */
  var gate = document.getElementById('gate');
  var seen = false;
  try{ seen = sessionStorage.getItem('disclaimer-ok') === '1'; }catch(e){}
  if (gate){
    if (seen) gate.hidden = true;
    document.getElementById('agree').addEventListener('click', function(){
      gate.hidden = true;
      try{ sessionStorage.setItem('disclaimer-ok', '1'); }catch(e){}
    });
  }

  /* ---------- consultation form ---------- */
  var form = document.getElementById('cform');
  var renderFiles;
  if (form){
    var MSG = {
      en:{name:'Enter your name.', phone:'Enter a phone number with at least 10 digits.', ok:'Tick the box to confirm you understand.',
          type:' was not added. Use PDF, JPG or PNG.', size:' was not added. Files must total 8 MB or less.', rm:'Remove',
          sending:'Sending…'},
      hi:{name:'अपना नाम लिखें।', phone:'कम से कम 10 अंकों का फ़ोन नंबर लिखें।', ok:'पुष्टि के लिए बॉक्स पर टिक करें।',
          type:' नहीं जोड़ी गई। PDF, JPG या PNG इस्तेमाल करें।', size:' नहीं जोड़ी गई। फ़ाइलें कुल 8 MB से अधिक नहीं हो सकतीं।', rm:'हटाएँ',
          sending:'भेजा जा रहा है…'}
    };
    var drop = document.getElementById('drop'), input = document.getElementById('f-files');
    var list = document.getElementById('flist'), ferr = document.getElementById('ferr');
    var err = document.getElementById('formerr'), okBox = document.getElementById('sent'), failBox = document.getElementById('failed');
    var submitBtn = form.querySelector('button[type=submit]');
    var files = [], LIMIT = 8 * 1024 * 1024, okType = /\.(pdf|jpe?g|png)$/i;

    function fmt(b){ return b < 1024*1024 ? Math.round(b/1024) + ' KB' : (b/1024/1024).toFixed(1) + ' MB'; }
    renderFiles = function(){
      list.innerHTML = '';
      files.forEach(function(f, i){
        var li = document.createElement('li'), s = document.createElement('span'), b = document.createElement('button');
        s.textContent = f.name + ' · ' + fmt(f.size);
        b.type = 'button'; b.textContent = MSG[lang].rm; b.setAttribute('aria-label', MSG[lang].rm + ' ' + f.name);
        b.addEventListener('click', function(){ files.splice(i, 1); renderFiles(); });
        li.appendChild(s); li.appendChild(b); list.appendChild(li);
      });
    };
    function addFiles(fl){
      ferr.hidden = true;
      var total = files.reduce(function(a, f){ return a + f.size; }, 0);
      [].slice.call(fl).forEach(function(f){
        if (!okType.test(f.name)){ ferr.textContent = f.name + MSG[lang].type; ferr.hidden = false; return; }
        if (total + f.size > LIMIT){ ferr.textContent = f.name + MSG[lang].size; ferr.hidden = false; return; }
        total += f.size; files.push(f);
      });
      renderFiles();
    }
    drop.addEventListener('click', function(){ input.click(); });
    drop.addEventListener('keydown', function(e){ if (e.key === 'Enter' || e.key === ' '){ e.preventDefault(); input.click(); } });
    input.addEventListener('change', function(){ addFiles(input.files); input.value = ''; });
    ['dragenter','dragover'].forEach(function(t){ drop.addEventListener(t, function(e){ e.preventDefault(); drop.classList.add('over'); }); });
    ['dragleave','drop'].forEach(function(t){ drop.addEventListener(t, function(e){ e.preventDefault(); drop.classList.remove('over'); }); });
    drop.addEventListener('drop', function(e){ if (e.dataTransfer) addFiles(e.dataTransfer.files); });

    function mimeOf(f){
      if (f.type) return f.type;
      if (/\.pdf$/i.test(f.name)) return 'application/pdf';
      if (/\.png$/i.test(f.name)) return 'image/png';
      return 'image/jpeg';
    }
    function readFile(f){
      return new Promise(function(resolve, reject){
        var r = new FileReader();
        r.onload = function(){ resolve({ name: f.name, mimeType: mimeOf(f), data: String(r.result).split(',')[1] || '' }); };
        r.onerror = function(){ reject(r.error); };
        r.readAsDataURL(f);
      });
    }
    function val(id){ return document.getElementById(id).value.trim(); }

    form.addEventListener('submit', function(e){
      e.preventDefault();
      okBox.hidden = true; failBox.hidden = true;
      var m = [];
      if (!val('f-name')) m.push(MSG[lang].name);
      if (val('f-phone').replace(/\D/g, '').length < 10) m.push(MSG[lang].phone);
      if (!document.getElementById('f-ok').checked) m.push(MSG[lang].ok);
      if (m.length){ err.textContent = m.join(' '); err.hidden = false; return; }
      err.hidden = true;

      var endpoint = form.getAttribute('data-endpoint');
      if (!endpoint){ failBox.hidden = false; return; }

      var label = submitBtn.innerHTML;
      submitBtn.disabled = true; submitBtn.textContent = MSG[lang].sending;
      var cityEl = form.querySelector('input[name=city]:checked');
      Promise.all(files.map(readFile)).then(function(encoded){
        var payload = {
          name: val('f-name'), phone: val('f-phone'), email: val('f-email'),
          city: cityEl ? cityEl.value : '', type: document.getElementById('f-type').selectedOptions[0].dataset.en || document.getElementById('f-type').value,
          message: val('f-msg'), language: lang, website: document.getElementById('f-website').value,
          files: encoded
        };
        /* text/plain keeps this a simple request, which the Google script accepts */
        return fetch(endpoint, { method: 'POST', body: JSON.stringify(payload) });
      }).then(function(res){ return res.json(); }).then(function(data){
        if (!data || !data.ok) throw new Error('rejected');
        form.reset(); files = []; renderFiles();
        okBox.hidden = false;
      }).catch(function(){
        failBox.hidden = false;
      }).then(function(){
        submitBtn.disabled = false; submitBtn.innerHTML = label;
      });
    });
  }

  /* initial language (home page only; article pages are fixed) */
  if (isHome){
    var saved = read('site-lang');
    setLang(saved === 'hi' ? 'hi' : 'en');
  }
})();
