/* Court fee calculator — ad valorem fee on a plaint in a money suit.
   Haryana: Court-fees Act 1870, Schedule I as amended by the Court Fees (Haryana Amendment) Act 2009.
     The published chart shows ₹1,38,000 as the base at ₹30 lakh; the rows before and after only
     add up with ₹1,38,800, so that figure is used here.
   Uttar Pradesh: Court-fees Act 1870, Schedule I, Article 1, as applicable in UP
     ("or part thereof": each part-unit is charged in full). */
(function () {
  var stateEl = document.getElementById('c-state');
  var amtEl = document.getElementById('c-amt');
  var wordsEl = document.getElementById('c-words');
  var resultEl = document.getElementById('result');
  var slabsEl = document.getElementById('slabs');

  function inr(n, paise) {
    return '₹' + Number(n).toLocaleString('en-IN', { minimumFractionDigits: paise ? 2 : 0, maximumFractionDigits: paise ? 2 : 0 });
  }
  function lang() { return document.documentElement.getAttribute('data-lang') === 'hi' ? 'hi' : 'en'; }

  /* ---------- Haryana ---------- */
  var HR = [
    [0, 15000, 0, 2.5],
    [15000, 27000, 375, 3.5],
    [27000, 39000, 795, 4.5],
    [39000, 51000, 1335, 5.5],
    [51000, 63000, 1995, 6.5],
    [63000, 75000, 2775, 7.5],
    [75000, 500000, 3675, 6.5],
    [500000, 1000000, 31300, 5.5],
    [1000000, 2000000, 58800, 4.5],
    [2000000, 3000000, 103800, 3.5],
    [3000000, 4500000, 138800, 2.5],
    [4500000, 6000000, 176300, 1.5]
  ];
  function haryana(v) {
    for (var i = 0; i < HR.length; i++) {
      var s = HR[i];
      if (v <= s[1]) {
        var fee = s[2] + (v - s[0]) * s[3] / 100;
        return { fee: Math.round(fee), row: i, how: s[2] ? [inr(s[2]) + ' + ' + s[3] + '% × ' + inr(v - s[0]), inr(s[2]) + ' + ' + s[3] + '% × ' + inr(v - s[0])] : [s[3] + '% × ' + inr(v), s[3] + '% × ' + inr(v)] };
      }
    }
    return { over: true };
  }
  function hrRows() {
    return HR.map(function (s) {
      var range = (s[0] ? inr(s[0]) : '₹0') + ' – ' + inr(s[1]);
      var fee = s[2] ? inr(s[2]) + ' + ' + s[3] + '%' : s[3] + '%';
      var feeHi = s[2] ? inr(s[2]) + ' + ' + s[3] + '%' : s[3] + '%';
      return [range, fee + (s[2] ? ' of the amount above ' + inr(s[0]) : ' of the amount'), feeHi + (s[2] ? ', ' + inr(s[0]) + ' से ऊपर की राशि पर' : ' राशि पर')];
    });
  }

  /* ---------- Uttar Pradesh ---------- */
  // [from, to, base fee at "from", rate per unit, unit]
  var UP = [
    [0, 100, 0, 0.5, 5],
    [100, 300, 10, 1.25, 10],
    [300, 500, 35, 1.5, 10],
    [500, 1000, 65, 2.25, 10],
    [1000, 5000, 177.5, 12, 100],
    [5000, 10000, 657.5, 20, 200],
    [10000, Infinity, 1157.5, 37.5, 500]
  ];
  function up(v) {
    for (var i = 0; i < UP.length; i++) {
      var s = UP[i];
      if (v <= s[1]) {
        var units = Math.ceil((v - s[0]) / s[4]);
        var fee = s[2] + units * s[3];
        var part = inr(s[3], true) + ' × ' + units.toLocaleString('en-IN');
        return { fee: fee, row: i, paise: true, how: [
          (s[2] ? inr(s[2], true) + ' + ' : '') + part + ' (' + units.toLocaleString('en-IN') + ' units of ' + inr(s[4]) + ' or part above ' + inr(s[0]) + ')',
          (s[2] ? inr(s[2], true) + ' + ' : '') + part + ' (' + inr(s[0]) + ' से ऊपर हर ' + inr(s[4]) + ' या उसके भाग की ' + units.toLocaleString('en-IN') + ' इकाइयाँ)'
        ] };
      }
    }
  }
  function upRows() {
    return UP.map(function (s) {
      var range = s[1] === Infinity ? 'Above ' + inr(s[0]) : (s[0] ? inr(s[0]) : '₹0') + ' – ' + inr(s[1]);
      var rangeHi = s[1] === Infinity ? inr(s[0]) + ' से ऊपर' : range;
      return [range, inr(s[3], true) + ' per ' + inr(s[4]) + ' or part' + (s[0] ? ', plus ' + inr(s[2], true) : ''), inr(s[3], true) + ' प्रति ' + inr(s[4]) + ' या उसका भाग' + (s[0] ? ', साथ में ' + inr(s[2], true) : ''), rangeHi];
    });
  }

  /* ---------- amount in words (Indian system) ---------- */
  function words(v) {
    if (!v) return '';
    var cr = Math.floor(v / 1e7), l = Math.floor((v % 1e7) / 1e5), th = Math.floor((v % 1e5) / 1e3), r = v % 1e3;
    var hi = lang() === 'hi';
    var parts = [];
    if (cr) parts.push(cr.toLocaleString('en-IN') + (hi ? ' करोड़' : ' crore'));
    if (l) parts.push(l + (hi ? ' लाख' : ' lakh'));
    if (th) parts.push(th + (hi ? ' हज़ार' : ' thousand'));
    if (r) parts.push(r);
    return parts.join(' ') + (hi ? ' रुपये' : ' rupees');
  }

  function parseAmt() {
    var n = Number(String(amtEl.value).replace(/[^\d]/g, ''));
    return isFinite(n) ? n : 0;
  }

  function renderSlabs(state, row) {
    var hi = lang() === 'hi';
    if (state === 'delhi') { slabsEl.innerHTML = ''; return; }
    var rows = state === 'haryana' ? hrRows() : upRows();
    var h = '<table><thead><tr><th>' + (hi ? 'दावा राशि' : 'Amount claimed') + '</th><th>' + (hi ? 'फ़ीस' : 'Fee') + '</th></tr></thead><tbody>';
    rows.forEach(function (r, i) {
      var range = state === 'up' && hi ? r[3] : r[0];
      h += '<tr' + (i === row ? ' class="on"' : '') + '><td>' + range + '</td><td>' + (hi ? r[2] : r[1]) + '</td></tr>';
    });
    if (state === 'haryana') h += '<tr' + (row === 'over' ? ' class="on"' : '') + '><td>' + (hi ? '₹60,00,000 से ऊपर' : 'Above ₹60,00,000') + '</td><td>' + (hi ? 'प्रकाशित चार्ट में नहीं' : 'Not covered by the published chart') + '</td></tr>';
    slabsEl.innerHTML = h + '</tbody></table>';
  }

  function render() {
    var hi = lang() === 'hi';
    var state = stateEl.value;
    var v = parseAmt();
    wordsEl.textContent = words(v);
    var k = '<p class="k">' + (hi ? 'अनुमानित कोर्ट फ़ीस' : 'Indicative court fee') + '</p>';

    if (state === 'delhi') {
      resultEl.innerHTML = '<p class="warn">' + (hi
        ? 'दिल्ली की अनुसूची अभी सत्यापित की जा रही है। सही राशि के लिए अदालत की वर्तमान कोर्ट फ़ीस तालिका देखें।'
        : 'The Delhi schedule is being verified and is not included yet. Please check the court’s current court fee table for the exact amount.') + '</p>';
      renderSlabs(state, null);
      return;
    }
    if (!v) {
      resultEl.innerHTML = k + '<p class="how">' + (hi ? 'दावा राशि लिखें।' : 'Enter the amount claimed.') + '</p>';
      renderSlabs(state, null);
      return;
    }
    var r = state === 'haryana' ? haryana(v) : up(v);
    if (r.over) {
      resultEl.innerHTML = k + '<p class="warn">' + (hi
        ? '₹60 लाख से अधिक के दावे प्रकाशित चार्ट में शामिल नहीं हैं। अदालत की वर्तमान अनुसूची देखें।'
        : 'Claims above ₹60 lakh are not covered by the published Haryana chart. Please check the court’s current schedule.') + '</p>';
      renderSlabs(state, 'over');
      return;
    }
    resultEl.innerHTML = k +
      '<p class="fee">' + inr(r.fee, r.paise) + '</p>' +
      '<p class="how">' + (hi ? 'गणना: ' : 'Calculation: ') + (hi ? r.how[1] : r.how[0]) + '</p>' +
      '<p class="src">' + (hi ? 'केवल अनुमान। दायर करने से पहले अदालत की वर्तमान अनुसूची से पुष्टि करें।' : 'Indicative only. Confirm against the court’s current schedule before filing.') + '</p>';
    renderSlabs(state, r.row);
  }

  amtEl.addEventListener('input', function () {
    var pos = amtEl.value.length - amtEl.selectionStart;
    var n = parseAmt();
    amtEl.value = n ? n.toLocaleString('en-IN') : '';
    try { var p = Math.max(0, amtEl.value.length - pos); amtEl.setSelectionRange(p, p); } catch (e) {}
    render();
  });
  stateEl.addEventListener('change', render);
  document.getElementById('calc').addEventListener('submit', function (e) { e.preventDefault(); });
  document.querySelectorAll('.lang button').forEach(function (b) { b.addEventListener('click', function () { setTimeout(render, 0); }); });
  render();
})();
