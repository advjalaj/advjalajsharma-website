# -*- coding: utf-8 -*-
"""Content of the legal guides on advjalajsharma.in.

Every guide answers the same six questions, in this order:
  1. What is the legal problem?
  2. What does the law say?
  3. What should you do immediately?
  4. What is the applicable limitation period?
  5. Which documents should you preserve?
  6. What happens if you miss the deadline?
Rules: plain language, no client details, no "contact me" pitch (Bar Council of India Rule 36).
"""

EN_Q = [
    "What is the legal problem?",
    "What does the law say?",
    "What should you do immediately?",
    "What is the limitation period?",
    "Which documents should you preserve?",
    "What happens if you miss the deadline?",
]
HI_Q = [
    "कानूनी समस्या क्या है?",
    "कानून क्या कहता है?",
    "तुरंत क्या करें?",
    "समय-सीमा (परिसीमा) क्या है?",
    "कौन से दस्तावेज़ संभाल कर रखें?",
    "समय-सीमा चूक जाने पर क्या होता है?",
]

ARTICLES = [
    # ------------------------------------------------------------------ cheque bounce (EN)
    {
        "slug": "cheque-bounce-what-to-do",
        "lang": "en",
        "alt": ("cheque-bounce-kya-kare", "hi"),
        "title": "Cheque Bounce: What to Do Under Section 138 NI Act | Jalaj Sharma, Advocate",
        "description": "Cheque bounced or dishonoured? What the law says, what to do immediately, the 30-day legal notice, time limits for a Section 138 case, documents to keep and what happens if you miss a deadline.",
        "keywords": "cheque bounce, cheque dishonour, Section 138 NI Act, cheque bounce legal notice, cheque bounce case, cheque bounce time limit, cheque bounce punishment",
        "tag": "Cheque bounce · Section 138 NI Act",
        "h1": "Cheque bounced? What to do under Section 138 of the NI Act",
        "month": "November 2026",
        "minutes": 3,
        "published": "2026-11-07",
        "modified": "2026-11-14",
        "summary": [
            "Keep the original cheque and the bank’s return memo.",
            "Send a legal notice within <strong>30 days</strong> of learning the cheque bounced.",
            "The drawer then has <strong>15 days</strong> to pay.",
            "If unpaid, file the complaint within <strong>one month</strong> after those 15 days.",
        ],
        "sections": [
            (EN_Q[0], """
    <p>A cheque given to you to pay a debt has come back unpaid. Banks call this a cheque being <strong>dishonoured</strong>; most people say it <strong>bounced</strong>. The usual reasons are “funds insufficient” or “exceeds arrangement”.</p>
"""),
            (EN_Q[1], """
    <p>Under <strong>Section 138 of the Negotiable Instruments Act, 1881</strong>, it is a criminal offence when a cheque given for a debt bounces and the person who issued it does not pay within 15 days of receiving your written notice.</p>
    <ul>
      <li>Punishment: up to <strong>two years’ imprisonment</strong>, a fine of up to <strong>twice the cheque amount</strong>, or both.</li>
      <li>While the case is pending, the court can order <strong>interim compensation of up to 20%</strong> of the cheque amount.</li>
      <li>The case can be <strong>settled</strong> at any stage.</li>
      <li>A cheque given as “security” can also lead to a case if the debt was actually due when it was presented.</li>
    </ul>
"""),
            (EN_Q[2], """
    <ul>
      <li>Keep the <strong>original cheque</strong> and the <strong>return memo</strong>. Do not hand the cheque back.</li>
      <li>Send a written <strong>demand notice</strong> stating the cheque details and asking for payment within 15 days.</li>
      <li>Send it by <strong>Speed Post or registered post</strong> to the correct address and keep the receipt and tracking record.</li>
    </ul>
"""),
            (EN_Q[3], """
    <div class="timeline-wrap">
      <table>
        <thead><tr><th>Step</th><th>Time limit</th></tr></thead>
        <tbody>
          <tr><td>Present the cheque</td><td>Within 3 months of the date on the cheque</td></tr>
          <tr><td>Send the legal notice</td><td>Within 30 days of learning it bounced</td></tr>
          <tr><td>Drawer pays</td><td>Within 15 days of receiving the notice</td></tr>
          <tr><td>File the complaint</td><td>Within 1 month after the 15 days end</td></tr>
        </tbody>
      </table>
    </div>
    <p>The complaint is filed before the Magistrate where <strong>your own bank branch</strong> is located, not where the drawer lives.</p>
"""),
            (EN_Q[4], """
    <ul>
      <li>The original cheque and the bank’s return memo</li>
      <li>A copy of the legal notice, the postal receipt and the tracking report</li>
      <li>Proof of the debt: agreement, invoices, bank transfers, receipts, messages or emails</li>
      <li>Your bank statement showing the cheque was presented</li>
    </ul>
"""),
            (EN_Q[5], """
    <ul>
      <li><strong>Notice sent after 30 days:</strong> no Section 138 case on that dishonour. If the cheque is still within its three-month validity, it can be presented again and the time limits start afresh from the new dishonour.</li>
      <li><strong>Complaint filed late:</strong> the court accepts it only if it is satisfied there was sufficient cause for the delay.</li>
      <li><strong>Either way,</strong> a civil suit to recover the money remains available, generally within three years.</li>
    </ul>
"""),
        ],
        "faqs": [
            ("What if the person refuses to accept the legal notice?", "If it was sent by registered or speed post to the correct address and returns as refused or unclaimed, courts generally treat it as served."),
            ("Can a cheque bounce case be settled?", "Yes. The offence is compoundable, so the parties can settle at any stage, including during trial or appeal."),
            ("I have received a cheque bounce notice. What should I do?", "Do not ignore it. Paying the cheque amount within 15 days of receiving the notice prevents the offence from arising. If you dispute the debt, reply in writing and keep a record."),
        ],
    },
    # ------------------------------------------------------------------ cheque bounce (HI)
    {
        "slug": "cheque-bounce-kya-kare",
        "lang": "hi",
        "alt": ("cheque-bounce-what-to-do", "en"),
        "title": "चेक बाउंस होने पर क्या करें? धारा 138 एनआई एक्ट | जलज शर्मा, अधिवक्ता",
        "description": "चेक बाउंस हो गया? कानून क्या कहता है, तुरंत क्या करें, 30 दिन में लीगल नोटिस, धारा 138 के केस की समय-सीमा, कौन से दस्तावेज़ रखें और समय-सीमा चूकने पर क्या होता है।",
        "keywords": "चेक बाउंस, चेक बाउंस होने पर क्या करें, चेक बाउंस लीगल नोटिस, चेक बाउंस केस, धारा 138, चेक बाउंस की सज़ा, cheque bounce",
        "tag": "चेक बाउंस · धारा 138 एनआई एक्ट",
        "h1": "चेक बाउंस होने पर क्या करें? धारा 138 एनआई एक्ट के तहत",
        "month": "नवंबर 2026",
        "minutes": 3,
        "published": "2026-11-10",
        "modified": "2026-11-14",
        "summary": [
            "मूल चेक और बैंक का रिटर्न मेमो संभाल कर रखें।",
            "चेक बाउंस की सूचना मिलने के <strong>30 दिन के भीतर</strong> लीगल नोटिस भेजें।",
            "चेक देने वाले के पास भुगतान के लिए <strong>15 दिन</strong> होते हैं।",
            "भुगतान न होने पर उन 15 दिनों के बाद <strong>एक महीने के भीतर</strong> शिकायत दायर करें।",
        ],
        "sections": [
            (HI_Q[0], """
    <p>कर्ज़ या बकाया चुकाने के लिए आपको दिया गया चेक बिना भुगतान के लौट आया है। बैंक की भाषा में इसे चेक का <strong>अनादरण (dishonour)</strong> कहते हैं; आम भाषा में <strong>चेक बाउंस</strong>। आम कारण होते हैं “Funds Insufficient” या “Exceeds Arrangement”।</p>
"""),
            (HI_Q[1], """
    <p><strong>परक्राम्य लिखत अधिनियम, 1881 की धारा 138</strong> के तहत, कर्ज़ के लिए दिया गया चेक बाउंस हो जाए और चेक देने वाला आपका लिखित नोटिस मिलने के 15 दिन के भीतर भुगतान न करे, तो यह आपराधिक अपराध है।</p>
    <ul>
      <li>सज़ा: <strong>दो साल तक की जेल</strong>, <strong>चेक राशि के दोगुने तक जुर्माना</strong>, या दोनों।</li>
      <li>केस के दौरान अदालत <strong>चेक राशि का अधिकतम 20% अंतरिम मुआवज़ा</strong> देने का आदेश दे सकती है।</li>
      <li>किसी भी चरण में <strong>समझौता</strong> हो सकता है।</li>
      <li>“सिक्योरिटी” के तौर पर दिए गए चेक पर भी केस बन सकता है, अगर चेक जमा करते समय कर्ज़ वास्तव में देय था।</li>
    </ul>
"""),
            (HI_Q[2], """
    <ul>
      <li><strong>मूल चेक</strong> और <strong>रिटर्न मेमो</strong> संभाल कर रखें। चेक वापस न करें।</li>
      <li>लिखित <strong>डिमांड नोटिस</strong> भेजें, जिसमें चेक का विवरण हो और 15 दिन में भुगतान की माँग हो।</li>
      <li>नोटिस <strong>स्पीड पोस्ट या रजिस्टर्ड पोस्ट</strong> से सही पते पर भेजें और रसीद व ट्रैकिंग रिकॉर्ड रखें।</li>
    </ul>
"""),
            (HI_Q[3], """
    <div class="timeline-wrap">
      <table>
        <thead><tr><th>चरण</th><th>समय-सीमा</th></tr></thead>
        <tbody>
          <tr><td>चेक बैंक में जमा करना</td><td>चेक की तारीख से 3 महीने के भीतर</td></tr>
          <tr><td>लीगल नोटिस भेजना</td><td>बाउंस की सूचना मिलने के 30 दिन के भीतर</td></tr>
          <tr><td>भुगतान</td><td>नोटिस मिलने के 15 दिन के भीतर</td></tr>
          <tr><td>शिकायत दायर करना</td><td>15 दिन पूरे होने के बाद 1 महीने के भीतर</td></tr>
        </tbody>
      </table>
    </div>
    <p>शिकायत उस मजिस्ट्रेट के यहाँ दायर होती है जहाँ <strong>आपकी अपनी बैंक शाखा</strong> है, चेक देने वाले के शहर में नहीं।</p>
"""),
            (HI_Q[4], """
    <ul>
      <li>मूल चेक और बैंक का रिटर्न मेमो</li>
      <li>लीगल नोटिस की प्रति, डाक रसीद और ट्रैकिंग रिपोर्ट</li>
      <li>कर्ज़ का सबूत: अनुबंध, बिल, बैंक ट्रांसफ़र, रसीदें, मैसेज या ईमेल</li>
      <li>बैंक स्टेटमेंट, जिसमें चेक जमा करना दिखे</li>
    </ul>
"""),
            (HI_Q[5], """
    <ul>
      <li><strong>30 दिन के बाद नोटिस भेजा:</strong> उस बाउंस पर धारा 138 का केस नहीं बनता। अगर चेक अभी तीन महीने की वैधता में है, तो उसे दोबारा जमा किया जा सकता है और नए बाउंस से समय-सीमा फिर शुरू होती है।</li>
      <li><strong>शिकायत देर से दायर की:</strong> अदालत तभी स्वीकार करती है जब देरी का पर्याप्त कारण हो।</li>
      <li><strong>दोनों स्थितियों में</strong> पैसे की वसूली के लिए सिविल वाद का रास्ता खुला रहता है, आमतौर पर तीन साल के भीतर।</li>
    </ul>
"""),
        ],
        "faqs": [
            ("अगर सामने वाला नोटिस लेने से मना कर दे तो क्या होगा?", "अगर नोटिस सही पते पर रजिस्टर्ड या स्पीड पोस्ट से भेजा गया था और “refused” या “unclaimed” होकर लौटा, तो अदालतें आमतौर पर उसे पहुँचा हुआ मानती हैं।"),
            ("क्या चेक बाउंस केस में समझौता हो सकता है?", "हाँ। यह अपराध समझौता-योग्य है, इसलिए ट्रायल या अपील समेत किसी भी चरण में समझौता हो सकता है।"),
            ("मुझे चेक बाउंस का नोटिस मिला है। क्या करूँ?", "नोटिस को नज़रअंदाज़ न करें। नोटिस मिलने के 15 दिन के भीतर चेक राशि चुका देने पर अपराध बनता ही नहीं। अगर आप कर्ज़ से इनकार करते हैं, तो लिखित जवाब दें और उसका रिकॉर्ड रखें।"),
        ],
    },
    # ------------------------------------------------------------------ anticipatory bail
    {
        "slug": "anticipatory-bail",
        "lang": "en",
        "title": "Anticipatory Bail Under Section 482 BNSS: What to Do | Jalaj Sharma, Advocate",
        "description": "Afraid of arrest in an FIR or complaint? What anticipatory bail is under Section 482 BNSS, what to do immediately, when to apply, documents to keep and what happens if you are arrested first.",
        "keywords": "anticipatory bail, anticipatory bail BNSS, Section 482 BNSS, anticipatory bail Delhi, fear of arrest FIR, pre-arrest bail",
        "tag": "Criminal law · Section 482 BNSS",
        "h1": "Anticipatory bail: what to do if you fear arrest",
        "month": "November 2026",
        "minutes": 3,
        "published": "2026-11-14",
        "modified": "2026-11-14",
        "summary": [
            "Get a copy of the FIR or complaint as soon as possible.",
            "Apply to the Sessions Court or High Court <strong>before</strong> any arrest.",
            "Do not contact the complainant or witnesses.",
            "Once arrested, anticipatory bail is no longer available; regular bail must be sought.",
        ],
        "sections": [
            (EN_Q[0], """
    <p>An FIR or complaint has been filed against you, or you have reason to believe one will be, for a <strong>non-bailable offence</strong>, and you fear that the police may arrest you.</p>
"""),
            (EN_Q[1], """
    <p>Under <strong>Section 482 of the Bharatiya Nagarik Suraksha Sanhita, 2023</strong> (earlier Section 438 CrPC), the <strong>Sessions Court or the High Court</strong> can direct that, if you are arrested, you be released on bail.</p>
    <ul>
      <li>The court looks at the nature and seriousness of the accusation, your past record, the risk of you fleeing, and whether the case appears to have been filed to harass you.</li>
      <li>Bail usually comes with conditions: join the investigation when called, do not leave India without permission, and do not threaten or influence witnesses.</li>
      <li>It is not available for certain serious sexual offences against minors, and some special laws restrict it.</li>
      <li>For offences punishable with up to seven years, the police are generally required to issue a <strong>notice of appearance</strong> instead of arresting straight away, if the conditions for arrest are not met.</li>
    </ul>
"""),
            (EN_Q[2], """
    <ul>
      <li>Obtain a copy of the <strong>FIR</strong>. In most cases it is available on the state police website within 24 hours.</li>
      <li>If you receive a <strong>police notice</strong>, keep it and note the date and time it asks you to appear.</li>
      <li>Collect documents that support your version of events.</li>
      <li>Do <strong>not</strong> contact the complainant or witnesses about the case.</li>
    </ul>
"""),
            (EN_Q[3], """
    <p>There is <strong>no fixed limitation period</strong>. The application must be made <strong>before arrest</strong>, as soon as you reasonably fear it. Courts generally expect you to apply promptly once the FIR is known.</p>
"""),
            (EN_Q[4], """
    <ul>
      <li>Copy of the FIR or complaint</li>
      <li>Any notice from the police</li>
      <li>Documents supporting your version: agreements, payment records, messages, emails</li>
      <li>Identity and address proof</li>
      <li>Details of any other case pending against you</li>
    </ul>
"""),
            (EN_Q[5], """
    <p>If you are arrested before applying, anticipatory bail can no longer be granted. You will have to apply for <strong>regular bail</strong>, usually after being produced before the Magistrate, which may mean some time in custody.</p>
"""),
        ],
        "faqs": [
            ("Is anticipatory bail granted for a fixed period?", "Ordinarily the Supreme Court has held that protection need not be limited to a fixed period, though a court may impose a time limit or conditions in a particular case."),
            ("Can I get interim protection while the application is heard?", "Courts often grant interim protection from arrest until the next date of hearing, depending on the facts."),
        ],
    },
    # ------------------------------------------------------------------ consumer complaint
    {
        "slug": "consumer-complaint",
        "lang": "en",
        "title": "How to File a Consumer Complaint in India | Jalaj Sharma, Advocate",
        "description": "Defective product, poor service or builder delay? What the Consumer Protection Act 2019 says, which Commission to approach, the two-year limitation period, documents to keep and what to do first.",
        "keywords": "consumer complaint, consumer court, Consumer Protection Act 2019, consumer complaint against builder, consumer forum Delhi, consumer complaint limitation",
        "tag": "Consumer law · Consumer Protection Act, 2019",
        "h1": "Filing a consumer complaint: defective goods, poor service or builder delay",
        "month": "November 2026",
        "minutes": 3,
        "published": "2026-11-14",
        "modified": "2026-11-14",
        "summary": [
            "Complain in writing to the seller or service provider first and keep a copy.",
            "File before the District, State or National Commission depending on the amount paid.",
            "You can file where you live or work.",
            "File within <strong>two years</strong> of the problem arising.",
        ],
        "sections": [
            (EN_Q[0], """
    <p>You paid for goods or a service and received something <strong>defective</strong>, a service that was <strong>deficient</strong>, or you were misled by an <strong>unfair trade practice</strong>. A common example is a builder who fails to hand over a flat on time.</p>
"""),
            (EN_Q[1], """
    <p>The <strong>Consumer Protection Act, 2019</strong> lets you file a complaint before a Consumer Commission for replacement, refund, repair or compensation. Which Commission depends on the <strong>amount you paid</strong>:</p>
    <div class="timeline-wrap">
      <table>
        <thead><tr><th>Commission</th><th>Amount paid for the goods or service</th></tr></thead>
        <tbody>
          <tr><td>District Commission</td><td>Up to ₹50 lakh</td></tr>
          <tr><td>State Commission</td><td>Above ₹50 lakh and up to ₹2 crore</td></tr>
          <tr><td>National Commission</td><td>Above ₹2 crore</td></tr>
        </tbody>
      </table>
    </div>
    <p>You may file where <strong>you live or work</strong>, and complaints can also be filed online.</p>
"""),
            (EN_Q[2], """
    <ul>
      <li>Write to the seller, service provider or builder describing the problem and keep a copy.</li>
      <li>Note dates, reference numbers and the names of people you spoke to.</li>
      <li>Take photographs of a defective product and do not discard it.</li>
      <li>A legal notice before filing is not compulsory, but it puts your demand clearly on record.</li>
    </ul>
"""),
            (EN_Q[3], """
    <p>A complaint must be filed within <strong>two years</strong> from the date the cause of action arose. A Commission can admit a late complaint if it is satisfied there was sufficient cause for the delay.</p>
"""),
            (EN_Q[4], """
    <ul>
      <li>Invoice, bill or payment receipts</li>
      <li>Warranty card, agreement, allotment letter or builder–buyer agreement</li>
      <li>All correspondence: emails, letters, chats, complaint numbers</li>
      <li>Photographs, and any inspection or expert report on the defect</li>
    </ul>
"""),
            (EN_Q[5], """
    <p>A complaint filed after two years is likely to be dismissed unless the delay is explained and condoned. Depending on the facts, a civil suit may still be possible within its own limitation period, but it is usually slower than the consumer route.</p>
"""),
        ],
        "faqs": [
            ("Do I need a lawyer to file a consumer complaint?", "No. You can file and argue it yourself, though many people choose to be represented."),
            ("Is there a fee for filing?", "Fees depend on the amount claimed and are modest; for small claims the fee is nil."),
        ],
    },
    # ------------------------------------------------------------------ mutual consent divorce
    {
        "slug": "mutual-consent-divorce",
        "lang": "en",
        "title": "Divorce by Mutual Consent: Process and Waiting Period | Jalaj Sharma, Advocate",
        "description": "How divorce by mutual consent works under Section 13B of the Hindu Marriage Act: the one-year separation, first and second motions, the six-month waiting period, documents and what to settle first.",
        "keywords": "mutual consent divorce, divorce by mutual consent, Section 13B Hindu Marriage Act, mutual divorce process Delhi, six month cooling period waiver",
        "tag": "Family law · Section 13B Hindu Marriage Act",
        "h1": "Divorce by mutual consent: the process and the waiting period",
        "month": "November 2026",
        "minutes": 3,
        "published": "2026-11-14",
        "modified": "2026-11-14",
        "summary": [
            "You must have lived separately for at least <strong>one year</strong>.",
            "Settle alimony, custody and belongings in writing before filing.",
            "File a joint petition (first motion); the second motion follows after <strong>6 months</strong>.",
            "The court can waive the six-month wait in suitable cases.",
        ],
        "sections": [
            (EN_Q[0], """
    <p>Both of you agree that the marriage has ended and want a divorce without contested litigation.</p>
"""),
            (EN_Q[1], """
    <p>For Hindus, Sikhs, Jains and Buddhists, <strong>Section 13B of the Hindu Marriage Act, 1955</strong> allows divorce by mutual consent. Marriages under the Special Marriage Act have a similar provision.</p>
    <ul>
      <li>You must have been <strong>living separately for at least one year</strong> and agree that you cannot live together.</li>
      <li>You file a <strong>joint petition</strong> in the Family Court (the first motion).</li>
      <li>The <strong>second motion</strong> is made not earlier than <strong>6 months</strong> and not later than <strong>18 months</strong> after the petition, after which the court grants the decree.</li>
      <li>The Supreme Court has held that the six-month period <strong>can be waived</strong> where the parties have settled everything and reconciliation is not possible.</li>
      <li>Either spouse may <strong>withdraw consent</strong> before the decree is passed.</li>
    </ul>
"""),
            (EN_Q[2], """
    <ul>
      <li>Agree on <strong>alimony or maintenance</strong>, usually as a one-time amount.</li>
      <li>Agree on <strong>custody and visiting rights</strong> for any children.</li>
      <li>Agree on the return of <strong>jewellery and belongings</strong>, and on any jointly held property.</li>
      <li>Agree on what happens to any <strong>other pending cases</strong> between you.</li>
      <li>Put all of this in a written settlement signed by both of you.</li>
    </ul>
"""),
            (EN_Q[3], """
    <p>There is no limitation period for filing. The time rules are: <strong>one year</strong> of separation before filing, and the second motion between <strong>6 and 18 months</strong> after the petition is filed.</p>
"""),
            (EN_Q[4], """
    <ul>
      <li>Proof of marriage: marriage certificate, photographs or invitation card</li>
      <li>Identity and address proof of both spouses</li>
      <li>Proof of separate residence for the past year</li>
      <li>The signed settlement agreement</li>
      <li>Income details and details of any children</li>
      <li>A list of jewellery and belongings to be returned</li>
    </ul>
"""),
            (EN_Q[5], """
    <p>If the second motion is not made within 18 months, the court may treat the petition as not pursued, and you may have to file afresh. If one spouse withdraws consent before the decree, the court cannot grant divorce on that petition.</p>
"""),
        ],
        "faqs": [
            ("Do both spouses have to attend court?", "Both spouses generally appear at the first and second motions; courts may allow appearance by video in suitable cases."),
            ("Can we skip the six-month waiting period?", "You can ask the court to waive it. The court considers whether you have lived apart long enough, whether mediation has failed and whether all issues are settled."),
        ],
    },
    # ------------------------------------------------------------------ legal notice received
    {
        "slug": "legal-notice-received",
        "lang": "en",
        "title": "Received a Legal Notice? What to Do Next | Jalaj Sharma, Advocate",
        "description": "Received a legal notice from a lawyer? What it means in law, what to do immediately, the time limits that matter, documents to keep and what happens if you ignore it.",
        "keywords": "received legal notice, reply to legal notice, how to reply legal notice, legal notice what to do, ignore legal notice",
        "tag": "General · Legal notices",
        "h1": "Received a legal notice? What to do next",
        "month": "November 2026",
        "minutes": 3,
        "published": "2026-11-14",
        "modified": "2026-11-14",
        "summary": [
            "Note the date you received it and keep the envelope.",
            "Do not ignore it, and do not reply in anger.",
            "Check whether a law attaches a deadline to it, such as 15 days in a cheque bounce.",
            "Reply in writing within the time given and keep proof of sending.",
        ],
        "sections": [
            (EN_Q[0], """
    <p>You have received a letter from a lawyer on someone’s behalf, demanding money, asking you to do or stop doing something, or warning that a case will be filed.</p>
"""),
            (EN_Q[1], """
    <p>A legal notice is <strong>not a court order</strong>, and in most cases the law does not force you to reply. But some notices carry legal consequences:</p>
    <ul>
      <li><strong>Cheque bounce notice:</strong> paying within 15 days of receiving it prevents the offence under Section 138 from arising.</li>
      <li><strong>Tenancy notice:</strong> a notice ending a tenancy starts the period after which eviction proceedings can follow.</li>
      <li><strong>Notice before a suit:</strong> an unanswered notice can be used later to suggest you did not dispute the claim.</li>
    </ul>
"""),
            (EN_Q[2], """
    <ul>
      <li>Write down the <strong>date you received it</strong> and keep the envelope and tracking details.</li>
      <li>Read the <strong>deadline</strong> it gives.</li>
      <li>Do not admit anything, threaten or reply in anger, by message or by phone.</li>
      <li>Gather the documents relating to the dispute.</li>
      <li>Send a <strong>written reply</strong> within the time given, preferably through an advocate, by Speed Post or registered post.</li>
    </ul>
"""),
            (EN_Q[3], """
    <p>The deadline in a notice, often 7 to 30 days, is set by the sender and is not itself a law. The time limits that matter are the ones fixed by statute, such as <strong>15 days</strong> in a cheque bounce notice. The limitation period for the sender to file a case runs on its own, whether or not you reply.</p>
"""),
            (EN_Q[4], """
    <ul>
      <li>The notice, the envelope and the tracking record</li>
      <li>Any agreement, invoice, receipt or payment record related to the dispute</li>
      <li>Messages and emails with the other side</li>
      <li>A copy of your reply and proof of posting</li>
    </ul>
"""),
            (EN_Q[5], """
    <p>In a cheque bounce matter, not paying within 15 days completes the offence and a criminal complaint can follow. In other cases, the sender may file a suit or complaint. You can still defend yourself in court, but you lose the chance to put your version on record early.</p>
"""),
        ],
    },
]
