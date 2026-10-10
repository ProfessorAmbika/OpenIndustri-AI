"""Hazard Recognition · Level 5 — The Hazard Hunt (competency challenge).

Story: The trainee is assigned to replace pressure gauge PI-520 on a process
line next to the loading bay. Minimal hints. The area holds several genuine
hazards (oil spill on the access route, a weeping flange, an empty
extinguisher bracket, combustible packaging against a hot line) plus things
that look alarming but are fine. A job card missing its permit reference
completes the picture. Linked decisions: what to report, and whether the job
proceeds. Combines principles from Levels 1–4.
"""
from authoring.dsl import Mission, T, any_flag, decide, enter, flag, inspect, not_done, tool


def build() -> Mission:
    m = Mission(
        code="hr5", id="og-hazrec-l5-hazard-hunt", category="og_hazard_recognition", level=5, minutes=18,
        title=T("The Hazard Hunt", "அபாய வேட்டை", "खतरे की खोज"),
        subtitle=T("Competency challenge: find them all, then decide", "திறன் சவால்: அனைத்தையும் கண்டறிந்து, பின்னர் முடிவு செய்யுங்கள்", "दक्षता चुनौती: सब खोजें, फिर निर्णय लें"),
        description=T("A small gauge swap in a busy corner of the plant. How many hazards can you find?", "ஆலையின் பரபரப்பான மூலையில் ஒரு சிறிய அளவி மாற்றம். எத்தனை அபாயங்களைக் கண்டறிய முடியும்?", "प्लांट के व्यस्त कोने में एक छोटा गेज बदलना। आप कितने खतरे खोज सकते हैं?"),
        location=T("Line 520 beside the loading bay", "ஏற்றுமதித் தளத்தருகே வரி 520", "लोडिंग बे के पास लाइन 520"),
        site="yard", time="dusk", spawn=(0, -23, 0), work_point=(0, -4, 0),
    )
    m.brief(
        lines=[
            T("Replace pressure gauge PI-520. Before any work, survey the area and report what you find.", "அழுத்த அளவி PI-520-ஐ மாற்றுங்கள். எந்த வேலைக்கும் முன், பகுதியை ஆய்வு செய்து கண்டதைப் புகாரளியுங்கள்.", "प्रेशर गेज PI-520 बदलें। कोई भी काम करने से पहले क्षेत्र का सर्वे करें और जो मिले उसे रिपोर्ट करें।"),
            T("This is a competency challenge: hints are limited.", "இது ஒரு திறன் சவால்: குறிப்புகள் குறைவு.", "यह एक दक्षता चुनौती है: संकेत सीमित हैं।"),
        ],
        task=T("Survey the work area around PI-520 and decide whether the job can go ahead.", "PI-520-ஐச் சுற்றியுள்ள பணிப் பகுதியை ஆய்வு செய்து வேலை தொடரலாமா என்று முடிவு செய்யுங்கள்.", "PI-520 के आसपास कार्य क्षेत्र का सर्वे करें और तय करें कि काम हो सकता है या नहीं।"),
        equipment=T("Gauge PI-520 on line 520, job card JC-520 (fictional).", "வரி 520-இல் அளவி PI-520, வேலை அட்டை JC-520 (கற்பனை).", "लाइन 520 पर गेज PI-520, जॉब कार्ड JC-520 (काल्पनिक)।"),
        objective=T("Find the genuine hazards, report them through the radio point, and make the go/no-go call.", "உண்மையான அபாயங்களைக் கண்டறிந்து, வானொலிப் புள்ளி வழியாகப் புகாரளித்து, தொடரலாமா வேண்டாமா என்று முடிவு செய்யுங்கள்.", "असली खतरे खोजें, रेडियो पॉइंट से रिपोर्ट करें और जाना/न जाना तय करें।"),
        information=T("Not everything that looks odd is a hazard. Not every hazard looks odd.", "விசித்திரமாகத் தெரிவதெல்லாம் அபாயம் அல்ல. எல்லா அபாயங்களும் விசித்திரமாகத் தெரிவதில்லை.", "हर अजीब दिखने वाली चीज़ खतरा नहीं। हर खतरा अजीब नहीं दिखता।"),
        objectives=[
            T("Combine hazard spotting, document checks and escalation in one job.", "அபாயக் கண்டறிதல், ஆவணச் சரிபார்ப்பு, மேலிடத் தெரிவிப்பு ஆகியவற்றை ஒரே வேலையில் இணையுங்கள்.", "खतरे पहचानना, दस्तावेज़ जाँच और आगे बढ़ाना एक ही काम में जोड़ें।"),
            T("Make a defensible go/no-go decision from the evidence.", "சான்றுகளிலிருந்து நியாயப்படுத்தக்கூடிய தொடர/நிறுத்த முடிவை எடுங்கள்.", "प्रमाण से उचित ठहराने योग्य जाना/न जाना निर्णय लें।"),
        ],
    )
    m.dialogue("meet", [
        ("supervisor", "neutral", T("Gauge swap on PI-520. Ten-minute job — if the area lets you.", "PI-520-இல் அளவி மாற்றம். பத்து நிமிட வேலை — பகுதி அனுமதித்தால்.", "PI-520 पर गेज बदलना। दस मिनट का काम — अगर क्षेत्र इजाज़त दे।")),
        ("supervisor", "serious", T("Survey first. Radio me everything you find, then make the call. I won't hold your hand on this one.", "முதலில் ஆய்வு செய்யுங்கள். கண்ட அனைத்தையும் எனக்கு வானொலியில் தெரிவித்து, பின்னர் முடிவெடுங்கள். இதில் நான் வழிகாட்ட மாட்டேன்.", "पहले सर्वे करें। जो भी मिले मुझे रेडियो करें, फिर फ़ैसला लें। इसमें मैं हाथ नहीं पकड़ूँगा।")),
    ])
    m.dialogue("revisit", [("supervisor", "neutral", T("I'm waiting for your report on the radio.", "உங்கள் அறிக்கைக்காக வானொலியில் காத்திருக்கிறேன்.", "मैं रेडियो पर आपकी रिपोर्ट का इंतज़ार कर रहा हूँ।"))])
    m.dialogue("radio_ack", [("supervisor", "serious", T("[Radio] Got it — spill, leak, missing extinguisher, packing on the hot line, no permit reference. That's a no-go until we sort it.", "[வானொலி] புரிந்தது — கசிவு எண்ணெய், கசியும் ஃபிளேஞ்ச், இல்லாத தீயணைப்பான், சூடான வரியில் பொதிகள், அனுமதி எண் இல்லை. சரிசெய்யும் வரை இது தொடரக்கூடாது.", "[रेडियो] समझ गया — तेल का फैलाव, रिसाव, गायब अग्निशामक, गर्म लाइन पर पैकिंग, परमिट संदर्भ नहीं। ठीक होने तक यह नहीं होगा।"))])
    m.dialogue("unsafe", [("supervisor", "concerned", T("Stop. You found the hazards — now let them change the decision.", "நிறுத்துங்கள். அபாயங்களைக் கண்டுபிடித்தீர்கள் — இப்போது அவை முடிவை மாற்றட்டும்.", "रुकिए। आपने खतरे खोजे — अब उन्हें निर्णय बदलने दीजिए।"))])
    m.dialogue("correct", [("supervisor", "pleased", T("That's a complete survey and a clear call. That's what competence looks like.", "இது முழுமையான ஆய்வும் தெளிவான முடிவும். திறமை என்பது இதுதான்.", "यह पूरा सर्वे और साफ़ निर्णय है। दक्षता ऐसी ही दिखती है।"))])
    m.npc("supervisor", -3, -12, 180, talk=[("meet", not_done("meet_supervisor")), ("revisit", None)])

    m.zone("zone_line520", T("Line 520 work area", "வரி 520 பணிப் பகுதி", "लाइन 520 कार्य क्षेत्र"), (-8, 8, -2, 10))
    m.decor("pipe", 0, 8.0, len=16, y=1.0, d=0.34, color="#8a96a8")
    m.decor("pipe", 0, 8.6, len=16, y=1.6, d=0.22, color="#e8423f")
    m.decor("building", 13.0, 3.0, heading=90, w=8, d=5, h=4, sign=T("LOADING BAY", "ஏற்றுமதித் தளம்", "लोडिंग बे"))
    m.decor("crate", 6.5, -1.0, color="#c49a5c")
    m.decor("cone", 1.6, -1.5)
    m.decor("cone", -1.6, -1.5)
    m.obj("gauge_pi520", "gauge", 0.0, 6.6, tag="PI-520", state="normal",
          name=T("Pressure gauge PI-520", "அழுத்த அளவி PI-520", "प्रेशर गेज PI-520"),
          details=[T("The gauge to be replaced. The needle sits in the green band.", "மாற்ற வேண்டிய அளவி. முள் பச்சைப் பட்டையில் உள்ளது.", "बदला जाने वाला गेज। सुई हरी पट्टी में है।")])
    m.obj("spill", "spill", -3.0, 3.0, size=2.0, kind="hazard",
          name=T("Dark patch on the access route", "அணுகல் வழியில் கருமையான திட்டு", "रास्ते पर काला धब्बा"),
          details=[T("An oil spill across the route to PI-520. Slippery and unreported.", "PI-520-க்கான வழியின் குறுக்கே எண்ணெய் சிந்தல். வழுக்கும், புகாரளிக்கப்படவில்லை.", "PI-520 के रास्ते पर तेल फैला है। फिसलन भरा और अनरिपोर्टेड।")])
    m.obj("flange_520", "leak", 4.5, 6.6, state="on", kind="hazard",
          name=T("Flange on line 520", "வரி 520-இல் ஃபிளேஞ்ச்", "लाइन 520 पर फ्लेंज"),
          details=[T("Product is dripping from the flange joint.", "ஃபிளேஞ்ச் இணைப்பிலிருந்து பொருள் சொட்டுகிறது.", "फ्लेंज जोड़ से उत्पाद टपक रहा है।")])
    m.obj("ext_point", "extinguisher", -6.5, 1.0, 90, state="missing", kind="hazard",
          name=T("Fire point FP-9", "தீப் புள்ளி FP-9", "फायर पॉइंट FP-9"),
          details=[T("The bracket is empty. The extinguisher is missing.", "தாங்கி காலியாக உள்ளது. தீயணைப்பான் இல்லை.", "ब्रैकेट खाली है। अग्निशामक गायब है।")])
    m.obj("packing", "combustibles", -4.0, 8.0, kind="hazard",
          name=T("Packaging stacked against line 520", "வரி 520-க்கு எதிராக அடுக்கப்பட்ட பொதிகள்", "लाइन 520 से सटी पैकेजिंग"),
          details=[T("Cardboard and rags are piled against the red-painted hot line.", "சிவப்பு வண்ணம் பூசிய சூடான வரிக்கு எதிராக அட்டைப்பெட்டிகளும் துணிகளும் குவிக்கப்பட்டுள்ளன.", "लाल रंगी गर्म लाइन से सटे गत्ते और कपड़े ढेर हैं।")])
    m.obj("drums_ok", "drum", 6.0, 2.0, count=4, color="#2fbf71", kind="equipment",
          name=T("Drums in the bunded store", "அணை அமைந்த கிடங்கில் உள்ள பீப்பாய்கள்", "बंड वाले स्टोर में ड्रम"),
          details=[T("Labelled, closed and stored inside a drip tray. Nothing out of place.", "குறியிடப்பட்டு, மூடப்பட்டு, சொட்டுத் தட்டில் வைக்கப்பட்டுள்ளன. எதுவும் தவறில்லை.", "लेबल लगे, बंद और ड्रिप ट्रे में रखे। कुछ भी गलत नहीं।")])
    m.obj("job_card", "permit_box", 3.0, -2.6, panel="document", doc_kind="record", prompt="read", kind="document",
          title=T("JOB CARD", "வேலை அட்டை", "जॉब कार्ड"),
          name=T("Job card JC-520 (fictional)", "வேலை அட்டை JC-520 (கற்பனை)", "जॉब कार्ड JC-520 (काल्पनिक)"),
          details=[T("Task: replace pressure gauge PI-520.", "பணி: அழுத்த அளவி PI-520-ஐ மாற்றுதல்.", "कार्य: प्रेशर गेज PI-520 बदलना।")])
    m.evidence("ev_task", T("Task", "பணி", "कार्य"), T("Replace PI-520 like-for-like", "PI-520-ஐ அதே வகையால் மாற்றுதல்", "PI-520 को समान से बदलना"), True, doc="job_card")
    m.evidence("ev_permit_ref", T("Work permit reference", "பணி அனுமதி எண்", "कार्य परमिट संदर्भ"), T("— (blank)", "— (காலி)", "— (खाली)"), False, doc="job_card")
    m.evidence("ev_isolation", T("Gauge isolation", "அளவி தனிமைப்படுத்தல்", "गेज आइसोलेशन"), T("Root valve to be closed by operations", "வேர் வால்வை இயக்கக் குழு மூட வேண்டும்", "रूट वाल्व ऑपरेशंस द्वारा बंद किया जाना है"), True, doc="job_card")
    m.obj("radio_point", "phone", -6.0, -3.0, 90, panel="comms", prompt="use", kind="communication", groups=["report"],
          name=T("Site radio point", "தள வானொலிப் புள்ளி", "साइट रेडियो पॉइंट"),
          details=[T("Channel 1 — Maintenance supervisor.", "சேனல் 1 — பராமரிப்பு மேற்பார்வையாளர்.", "चैनल 1 — मेंटेनेंस सुपरवाइज़र।")])
    m.obj("decision_board", "stand", 0.0, -3.6, panel="station", prompt="review", kind="station", groups=["final"],
          title=T("GO / NO-GO", "தொடர் / நிறுத்து", "जाना / न जाना"),
          name=T("Go/no-go board", "தொடர்/நிறுத்து பலகை", "जाना/न जाना बोर्ड"),
          details=[T("Record the go/no-go decision for JC-520.", "JC-520-க்கான தொடர்/நிறுத்து முடிவைப் பதிவுசெய்யுங்கள்.", "JC-520 के लिए जाना/न जाना निर्णय दर्ज करें।")])
    m.group("report", T("What do you report?", "என்ன புகாரளிப்பீர்கள்?", "आप क्या रिपोर्ट करेंगे?"), [
        ("all", T("All findings: spill, leak, missing extinguisher, packing on hot line, no permit reference", "அனைத்துக் கண்டுபிடிப்புகளும்: எண்ணெய், கசிவு, இல்லாத தீயணைப்பான், சூடான வரியில் பொதிகள், அனுமதி எண் இல்லை", "सभी निष्कर्ष: तेल फैलाव, रिसाव, गायब अग्निशामक, गर्म लाइन पर पैकिंग, परमिट संदर्भ नहीं")),
        ("leak_only", T("Only the leaking flange — the rest is housekeeping", "கசியும் ஃபிளேஞ்ச் மட்டும் — மற்றவை வீட்டுப் பராமரிப்பு", "केवल रिसता फ्लेंज — बाकी साफ़-सफ़ाई है")),
        ("drums", T("The drums near the loading bay look suspicious", "ஏற்றுமதித் தளத்தருகே உள்ள பீப்பாய்கள் சந்தேகமாகத் தெரிகின்றன", "लोडिंग बे के पास के ड्रम संदिग्ध लगते हैं")),
    ], ui="comms")
    m.group("final", T("Go or no-go for JC-520?", "JC-520-க்கு தொடரவா நிறுத்தவா?", "JC-520 के लिए जाना या न जाना?"), [
        ("no_go", T("No-go: hold the job until the findings are resolved and a permit is in place", "நிறுத்து: கண்டுபிடிப்புகள் தீர்க்கப்பட்டு அனுமதி கிடைக்கும் வரை வேலையை நிறுத்தி வையுங்கள்", "न जाएँ: निष्कर्ष सुलझने और परमिट होने तक काम रोकें")),
        ("go", T("Go: it is only a gauge, it will take ten minutes", "தொடர்: இது ஒரு அளவி மட்டுமே, பத்து நிமிடம் ஆகும்", "जाएँ: यह सिर्फ़ गेज है, दस मिनट लगेंगे")),
        ("fix_first", T("Tighten the leaking flange yourself first, then do the gauge", "முதலில் கசியும் ஃபிளேஞ்சை நீங்களே இறுக்குங்கள், பின்னர் அளவியை மாற்றுங்கள்", "पहले रिसता फ्लेंज खुद कसें, फिर गेज बदलें")),
    ])
    m.tools("flashlight", "spanner", "radio", flashlight=["flange_520", "gauge_pi520", "spill", "packing"])

    meet = m.meet("supervisor")
    m.briefing(meet)
    m.step("enter", title=T("Enter the line 520 work area", "வரி 520 பணிப் பகுதிக்குள் நுழையுங்கள்", "लाइन 520 कार्य क्षेत्र में जाएँ"),
           instruction=T("Walk into the work area.", "பணிப் பகுதிக்குள் செல்லுங்கள்.", "कार्य क्षेत्र में जाएँ।"),
           trigger=enter("zone_line520"), requires=["briefing"], points=5, concept="situational_awareness", scene="navigate", marker="zone_line520",
           hints=[T("North of the go/no-go board.", "தொடர்/நிறுத்து பலகைக்கு வடக்கே.", "जाना/न जाना बोर्ड के उत्तर में।")])
    m.step("find_gauge", title=T("Locate PI-520", "PI-520-ஐக் கண்டறியுங்கள்", "PI-520 खोजें"),
           instruction=T("Find the gauge named on the job card.", "வேலை அட்டையில் குறிப்பிட்ட அளவியைக் கண்டறியுங்கள்.", "जॉब कार्ड में बताया गेज खोजें।"),
           trigger=inspect("gauge_pi520"), requires=["enter"], points=5, concept="equipment_identification", scene="identify",
           hints=[T("The gauge stands on a post by the pipe rack.", "அளவி குழாய் அடுக்குக்கு அருகில் ஒரு கம்பத்தில் உள்ளது.", "गेज पाइप रैक के पास एक खंभे पर है।")])
    m.step("h_spill", title=T("Hazard: access route", "அபாயம்: அணுகல் வழி", "खतरा: पहुँच मार्ग"), instruction=T("Find the hazard on the route to the gauge.", "அளவிக்கான வழியில் உள்ள அபாயத்தைக் கண்டறியுங்கள்.", "गेज के रास्ते का खतरा खोजें।"),
           trigger=inspect("spill"), requires=["enter"], points=8, concept="hazard_identification", scene="hazards",
           hints=[T("Look at the ground, not just the equipment.", "உபகரணத்தை மட்டுமல்ல, தரையையும் பாருங்கள்.", "केवल उपकरण नहीं, ज़मीन भी देखें।")])
    m.step("h_leak", title=T("Hazard: line integrity", "அபாயம்: வரியின் நேர்மை", "खतरा: लाइन की अखंडता"), instruction=T("Find the loss of containment on line 520.", "வரி 520-இல் உள்ள கசிவைக் கண்டறியுங்கள்.", "लाइन 520 पर रिसाव खोजें।"),
           trigger=inspect("flange_520"), requires=["enter"], points=8, concept="hazard_identification", scene="hazards",
           hints=[T("Something is dripping east of the gauge.", "அளவிக்குக் கிழக்கே ஏதோ சொட்டுகிறது.", "गेज के पूर्व में कुछ टपक रहा है।")])
    m.step("h_extinguisher", title=T("Hazard: emergency equipment", "அபாயம்: அவசர உபகரணம்", "खतरा: आपातकालीन उपकरण"), instruction=T("Check the fire point on the west side.", "மேற்குப் பக்கத் தீப் புள்ளியைச் சரிபாருங்கள்.", "पश्चिमी ओर का फायर पॉइंट जाँचें।"),
           trigger=inspect("ext_point"), requires=["enter"], points=8, concept="fire_hazard_spotting", scene="hazards",
           hints=[T("Is everything that should be at the fire point actually there?", "தீப் புள்ளியில் இருக்க வேண்டியவை உண்மையில் உள்ளனவா?", "क्या फायर पॉइंट पर जो होना चाहिए वह सच में है?")])
    m.step("h_packing", title=T("Hazard: combustibles", "அபாயம்: எரியக்கூடியவை", "खतरा: ज्वलनशील"), instruction=T("Find the combustible material near a hot line.", "சூடான வரிக்கு அருகிலுள்ள எரியக்கூடிய பொருளைக் கண்டறியுங்கள்.", "गर्म लाइन के पास ज्वलनशील सामग्री खोजें।"),
           trigger=inspect("packing"), requires=["enter"], points=8, concept="combustibles_awareness", scene="hazards",
           hints=[T("Red paint on a line marks it as hot in this plant.", "இந்த ஆலையில் வரியின் சிவப்பு வண்ணம் அது சூடானது என்பதைக் குறிக்கிறது.", "इस प्लांट में लाइन पर लाल रंग उसे गर्म दर्शाता है।")])
    m.step("card", title=T("Check the job card", "வேலை அட்டையைச் சரிபாருங்கள்", "जॉब कार्ड जाँचें"), instruction=T("Open JC-520 and flag anything missing.", "JC-520-ஐத் திறந்து இல்லாததைக் குறியுங்கள்.", "JC-520 खोलें और जो गायब है उसे चिह्नित करें।"),
           trigger=flag("ev_permit_ref"), requires=["find_gauge"], points=12, concept="documented_evidence", scene="documents",
           hints=[T("Which field should never be blank before work starts?", "வேலை தொடங்கும் முன் எந்தப் புலம் காலியாக இருக்கக்கூடாது?", "काम शुरू होने से पहले कौन सा फ़ील्ड कभी खाली नहीं होना चाहिए?")])
    m.step("report", title=T("Report your findings", "உங்கள் கண்டுபிடிப்புகளைத் தெரிவியுங்கள்", "अपने निष्कर्ष रिपोर्ट करें"), instruction=T("Use the radio point and report.", "வானொலிப் புள்ளியைப் பயன்படுத்தித் தெரிவியுங்கள்.", "रेडियो पॉइंट से रिपोर्ट करें।"),
           trigger=decide("report", "all"), requires=["h_spill", "h_leak", "h_extinguisher", "h_packing", "card"], points=15, concept="escalation", scene="communicate",
           mistake_if_early=T("Your survey isn't complete yet. Keep looking before you report.", "உங்கள் ஆய்வு இன்னும் முடியவில்லை. தெரிவிக்கும் முன் தொடர்ந்து தேடுங்கள்.", "आपका सर्वे अभी पूरा नहीं हुआ। रिपोर्ट से पहले और खोजें।"),
           hints=[T("A partial report gives a partial picture.", "பகுதி அறிக்கை பகுதி நிலையையே காட்டும்.", "अधूरी रिपोर्ट अधूरी तस्वीर देती है।")])
    m.step("decide", title=T("Make the go/no-go call", "தொடர்/நிறுத்து முடிவை எடுங்கள்", "जाना/न जाना निर्णय लें"), instruction=T("Record your decision on the board.", "பலகையில் உங்கள் முடிவைப் பதிவுசெய்யுங்கள்.", "बोर्ड पर अपना निर्णय दर्ज करें।"),
           trigger=decide("final", "no_go"), requires=["report"], points=15, concept="stop_work_authority", scene="decision",
           mistake_if_early=T("Report what you found before making the call.", "முடிவெடுக்கும் முன் கண்டதைத் தெரிவியுங்கள்.", "निर्णय से पहले जो मिला उसे रिपोर्ट करें।"),
           hints=[T("Could this job be done safely with what you found?", "நீங்கள் கண்டவற்றுடன் இந்த வேலையைப் பாதுகாப்பாகச் செய்ய முடியுமா?", "जो आपको मिला उसके साथ क्या यह काम सुरक्षित हो सकता है?")])
    m.event("radio_reply", {"completed": ["report"]}, [{"type": "sound", "sound": "radio"}, {"type": "dialogue", "name": "radio_ack"}])

    m.critical("go_anyway", trigger=decide("final", "go"), concept="stop_work_authority", dialogue="unsafe",
               explanation=T("You gave a 'go' with five open findings, including no permit reference.", "அனுமதி எண் இல்லாதது உட்பட ஐந்து தீர்க்கப்படாத கண்டுபிடிப்புகளுடன் 'தொடர்' என்றீர்கள்.", "परमिट संदर्भ न होने सहित पाँच खुले निष्कर्षों के साथ आपने 'जाएँ' कहा।"),
               missing=T("Resolution of the findings and a valid permit.", "கண்டுபிடிப்புகளின் தீர்வும் செல்லுபடியான அனுமதியும்.", "निष्कर्षों का समाधान और वैध परमिट।"))
    m.critical("fix_leak_yourself", trigger=decide("final", "fix_first"), concept="no_untrained_intervention", dialogue="unsafe",
               explanation=T("Tightening a leaking live flange is outside your task and authorisation.", "கசியும் இயக்க ஃபிளேஞ்சை இறுக்குவது உங்கள் பணிக்கும் அனுமதிக்கும் அப்பாற்பட்டது.", "रिसते चालू फ्लेंज को कसना आपके कार्य और अनुमति से बाहर है।"),
               missing=T("Reporting the leak so the responsible team can make it safe.", "பொறுப்பான குழு பாதுகாப்பாக்க கசிவைத் தெரிவித்தல்.", "रिसाव की रिपोर्ट ताकि ज़िम्मेदार टीम उसे सुरक्षित करे।"))
    m.critical("spanner_live", trigger=tool("spanner", "flange_520", "gauge_pi520"), concept="no_untrained_intervention", dialogue="unsafe", condition=not_done("decide"),
               explanation=T("You put a tool on line 520 before the findings were resolved or a permit existed.", "கண்டுபிடிப்புகள் தீர்க்கப்படும் முன்போ அனுமதி கிடைக்கும் முன்போ வரி 520-இல் கருவியைப் பயன்படுத்தினீர்கள்.", "निष्कर्ष सुलझने या परमिट होने से पहले आपने लाइन 520 पर औज़ार लगाया।"),
               missing=T("A permit and resolved findings.", "அனுமதியும் தீர்க்கப்பட்ட கண்டுபிடிப்புகளும்.", "परमिट और सुलझे निष्कर्ष।"))
    m.mistake("partial_report", trigger=decide("report", "leak_only"), kind="incorrect_decision", concept="escalation",
              feedback=T("Spills, missing fire equipment and missing permits are not 'housekeeping'. Report everything.", "சிந்தல்கள், இல்லாத தீ உபகரணம், இல்லாத அனுமதிகள் 'வீட்டுப் பராமரிப்பு' அல்ல. அனைத்தையும் தெரிவியுங்கள்.", "फैलाव, गायब अग्नि उपकरण और गायब परमिट 'साफ़-सफ़ाई' नहीं हैं। सब रिपोर्ट करें।"))
    m.mistake("false_alarm", trigger=decide("report", "drums"), kind="incorrect_decision", concept="hazard_identification",
              feedback=T("Those drums are labelled, closed and bunded. Report the real findings.", "அந்தப் பீப்பாய்கள் குறியிடப்பட்டு, மூடப்பட்டு, அணைக்குள் உள்ளன. உண்மையான கண்டுபிடிப்புகளைத் தெரிவியுங்கள்.", "वे ड्रम लेबल वाले, बंद और बंड में हैं। असली निष्कर्ष रिपोर्ट करें।"))
    m.mistake("drums_advisory", trigger=inspect("drums_ok"), kind="advisory", concept="hazard_identification",
              feedback=T("Checked: these drums are stored correctly. Not every odd-looking thing is a hazard.", "சரிபார்க்கப்பட்டது: இந்தப் பீப்பாய்கள் சரியாக வைக்கப்பட்டுள்ளன. விசித்திரமாகத் தெரிவதெல்லாம் அபாயம் அல்ல.", "जाँचा: ये ड्रम सही रखे हैं। हर अजीब दिखने वाली चीज़ खतरा नहीं।"))
    m.mistake("wrong_flag", trigger=any_flag(), kind="incorrect_decision", concept="documented_evidence",
              feedback=T("That field is complete. Which one is missing?", "அந்தப் புலம் முழுமையானது. எது இல்லை?", "वह फ़ील्ड पूरा है। कौन सा गायब है?"))

    m.debrief(
        success=T("Complete survey, accurate report, clear no-go. Competency challenge passed.", "முழுமையான ஆய்வு, துல்லியமான அறிக்கை, தெளிவான நிறுத்தம். திறன் சவால் தேர்ச்சி.", "पूरा सर्वे, सटीक रिपोर्ट, साफ़ न जाना। दक्षता चुनौती पास।"),
        critical=T("The survey was good but the decision overrode it. Let your findings decide.", "ஆய்வு நன்றாக இருந்தது, ஆனால் முடிவு அதை மீறியது. உங்கள் கண்டுபிடிப்புகள் முடிவு செய்யட்டும்.", "सर्वे अच्छा था पर निर्णय ने उसे अनदेखा किया। अपने निष्कर्षों को निर्णय करने दें।"),
        failed=T("Repeated unsafe actions ended the challenge. Survey, report, then decide.", "தொடர்ந்த பாதுகாப்பற்ற செயல்கள் சவாலை முடித்தன. ஆய்வு, அறிக்கை, பின்னர் முடிவு.", "बार-बार असुरक्षित कार्यों ने चुनौती समाप्त की। सर्वे, रिपोर्ट, फिर निर्णय।"),
        lines=[
            ({"criticalRule": "go_anyway"}, T("You chose 'go' despite open findings.", "தீர்க்கப்படாத கண்டுபிடிப்புகள் இருந்தும் 'தொடர்' என்றீர்கள்.", "खुले निष्कर्षों के बावजूद आपने 'जाएँ' चुना।")),
            ({"criticalRule": "fix_leak_yourself"}, T("You tried to fix a live leak yourself.", "இயக்கக் கசிவை நீங்களே சரிசெய்ய முயன்றீர்கள்.", "आपने चालू रिसाव खुद ठीक करने की कोशिश की।")),
            ({"stepCompleted": "h_extinguisher"}, T("You noticed the empty fire point — easy to miss.", "காலியான தீப் புள்ளியைக் கவனித்தீர்கள் — தவறவிடுவது எளிது.", "आपने खाली फायर पॉइंट देखा — छूटना आसान है।")),
            ({"stepCompleted": "card"}, T("You found the missing permit reference.", "இல்லாத அனுமதி எண்ணைக் கண்டுபிடித்தீர்கள்.", "आपने गायब परमिट संदर्भ खोजा।")),
            ({"counterAbove": ["incorrectDecisions", 0]}, T("One report was incomplete or chased a false alarm.", "ஒரு அறிக்கை முழுமையற்றதாக இருந்தது அல்லது தவறான எச்சரிக்கையைத் துரத்தியது.", "एक रिपोर्ट अधूरी थी या झूठे अलार्म के पीछे गई।")),
            ({"stepCompleted": "decide"}, T("No-go with clear reasons: the right call.", "தெளிவான காரணங்களுடன் நிறுத்தம்: சரியான முடிவு.", "स्पष्ट कारणों के साथ न जाना: सही निर्णय।")),
        ],
    )
    m.comic(T("SURVEY · REPORT · DECIDE", "ஆய்வு · அறிக்கை · முடிவு", "सर्वे · रिपोर्ट · निर्णय"), [
        ("magnifier", T("Look at the ground, the equipment, the emergency kit and the paperwork.", "தரை, உபகரணம், அவசரக் கருவிகள், ஆவணங்கள் அனைத்தையும் பாருங்கள்.", "ज़मीन, उपकरण, आपात सामग्री और कागज़ात सब देखें।")),
        ("radio", T("Report everything — a partial report hides risk.", "அனைத்தையும் தெரிவியுங்கள் — பகுதி அறிக்கை ஆபத்தை மறைக்கும்.", "सब रिपोर्ट करें — अधूरी रिपोर्ट जोखिम छिपाती है।")),
        ("stop_sign", T("Small job or not, open hazards mean no-go.", "சிறிய வேலையோ இல்லையோ, தீர்க்கப்படாத அபாயங்கள் என்றால் நிறுத்தம்.", "छोटा काम हो या बड़ा, खुले खतरे मतलब न जाना।")),
    ])
    m.report(["find_gauge", "h_spill", "h_leak", "h_extinguisher", "h_packing", "card"], ["report", "decide"])
    m.mcq(1, concept="hazard_identification",
          stem=T("During a pre-job survey, what should you look at?", "வேலைக்கு முந்தைய ஆய்வில் எதைப் பார்க்க வேண்டும்?", "काम से पहले सर्वे में क्या देखना चाहिए?"),
          options=[T("Only the equipment you will work on", "நீங்கள் வேலை செய்யும் உபகரணம் மட்டும்", "केवल वह उपकरण जिस पर काम करना है"),
                   T("The ground, nearby equipment, emergency equipment and documents", "தரை, அருகிலுள்ள உபகரணம், அவசர உபகரணம், ஆவணங்கள்", "ज़मीन, आसपास के उपकरण, आपात उपकरण और दस्तावेज़"),
                   T("Only what the job card lists", "வேலை அட்டை பட்டியலிடுவது மட்டும்", "केवल जो जॉब कार्ड में लिखा है")],
          correct="b", explanation=T("In this scenario hazards were on the ground, on the line, at the fire point and in the paperwork.", "இந்தச் சூழலில் அபாயங்கள் தரையிலும், வரியிலும், தீப் புள்ளியிலும், ஆவணங்களிலும் இருந்தன.", "इस परिदृश्य में खतरे ज़मीन, लाइन, फायर पॉइंट और कागज़ात में थे।"))
    m.mcq(2, concept="escalation",
          stem=T("You found five issues. What should your report include?", "ஐந்து பிரச்சினைகளைக் கண்டீர்கள். உங்கள் அறிக்கையில் என்ன இருக்க வேண்டும்?", "आपको पाँच समस्याएँ मिलीं। आपकी रिपोर्ट में क्या होना चाहिए?"),
          options=[T("All five", "ஐந்தும்", "सभी पाँच"), T("Only the most serious one", "மிகவும் தீவிரமான ஒன்று மட்டும்", "केवल सबसे गंभीर"), T("None, if you are not doing the job", "நீங்கள் வேலை செய்யவில்லை என்றால் எதுவுமில்லை", "कोई नहीं, अगर आप काम नहीं कर रहे")],
          correct="a", explanation=T("Each finding needs action by someone; leaving any out hides it.", "ஒவ்வொரு கண்டுபிடிப்புக்கும் ஒருவரின் நடவடிக்கை தேவை; எதையாவது விட்டால் அது மறைந்துவிடும்.", "हर निष्कर्ष पर किसी की कार्रवाई चाहिए; कोई छोड़ने से वह छिप जाता है।"))
    m.mcq(3, concept="no_untrained_intervention",
          stem=T("A flange near your job is leaking. Should you tighten it?", "உங்கள் வேலைக்கு அருகிலுள்ள ஒரு ஃபிளேஞ்ச் கசிகிறது. அதை இறுக்க வேண்டுமா?", "आपके काम के पास एक फ्लेंज रिस रहा है। क्या आपको उसे कसना चाहिए?"),
          options=[T("Yes, it is quick", "ஆம், அது விரைவானது", "हाँ, यह जल्दी है"),
                   T("No — report it so the responsible team makes it safe", "இல்லை — பொறுப்பான குழு பாதுகாப்பாக்கத் தெரிவியுங்கள்", "नहीं — रिपोर्ट करें ताकि ज़िम्मेदार टीम सुरक्षित करे"),
                   T("Only if nobody is watching", "யாரும் பார்க்கவில்லை என்றால் மட்டும்", "केवल अगर कोई नहीं देख रहा")],
          correct="b", explanation=T("Work on live, leaking equipment is outside the trainee's task and authorisation.", "இயக்கத்தில் கசியும் உபகரணத்தில் வேலை செய்வது பயிற்சியாளரின் பணிக்கும் அனுமதிக்கும் அப்பாற்பட்டது.", "चालू, रिसते उपकरण पर काम प्रशिक्षु के कार्य और अनुमति से बाहर है।"))
    m.mcq(4, concept="stop_work_authority",
          stem=T("The job is small but there are open hazards and no permit reference. Decision?", "வேலை சிறியது, ஆனால் தீர்க்கப்படாத அபாயங்களும் அனுமதி எண் இல்லாததும் உள்ளன. முடிவு?", "काम छोटा है पर खुले खतरे हैं और परमिट संदर्भ नहीं। निर्णय?"),
          options=[T("Go — small jobs are low risk", "தொடர் — சிறிய வேலைகளில் ஆபத்து குறைவு", "जाएँ — छोटे काम कम जोखिम वाले हैं"),
                   T("Go, but quickly", "தொடர், ஆனால் விரைவாக", "जाएँ, पर जल्दी"),
                   T("No-go until findings are resolved and the permit is in place", "கண்டுபிடிப்புகள் தீர்க்கப்பட்டு அனுமதி கிடைக்கும் வரை நிறுத்தம்", "निष्कर्ष सुलझने और परमिट होने तक न जाएँ")],
          correct="c", explanation=T("The size of the job does not change what the evidence says.", "வேலையின் அளவு சான்று சொல்வதை மாற்றாது.", "काम का आकार प्रमाण की बात नहीं बदलता।"))
    m.spec(
        workplaceLocation="Fictional line 520 beside a loading bay, at dusk.",
        equipmentType="Gauge PI-520, flange with drip, fire point with missing extinguisher, combustibles near red-painted line, correctly stored drums (distractor).",
        corePrinciple="Combine hazard recognition, document checks and escalation; open findings mean no-go.",
        commonMisconceptions=["Small jobs need small checks.", "Only report the worst thing.", "Quick fixes are helpful."],
        criticalDecisions=["Go with open findings", "Fix the leak yourself", "Use a tool before the decision"],
        assessmentCriteria={"correct": "Find 4 hazards + missing permit ref; report all; no-go."},
    )
    return m
