"""PPE Awareness · Level 4 — The Damaged Gear (abnormal conditions).

Story: Before a valve-packing job at the pipe rack, the trainee inspects the
PPE issued from the night-shift crate: a helmet with a crack, gloves with a
split seam and goggles with a snapped strap. One spare helmet is available;
there are no spare gloves. Joseph says 'a hairline crack is nothing'.
Learning: inspect PPE before use; damaged PPE is reported and replaced, never
patched or 'made do' with; if no serviceable replacement exists, the job waits.
"""
from authoring.dsl import Mission, T, decide, flag, inspect, not_done, select


def build() -> Mission:
    m = Mission(
        code="ppe4", id="og-ppe-l4-damaged-gear", category="og_ppe", level=4, minutes=13,
        title=T("The Damaged Gear", "சேதமடைந்த உபகரணம்", "क्षतिग्रस्त उपकरण"),
        subtitle=T("Inspect before you wear", "அணியும் முன் ஆய்வு செய்யுங்கள்", "पहनने से पहले जाँचें"),
        description=T("Your kit is waiting in a crate from the night shift. Is it fit to use?", "உங்கள் உபகரணங்கள் இரவுப் பணியின் பெட்டியில் காத்திருக்கின்றன. அவை பயன்படுத்தத் தகுந்தவையா?", "आपका सामान रात की शिफ्ट के क्रेट में रखा है। क्या यह इस्तेमाल लायक है?"),
        location=T("Pipe rack access point · Process unit", "குழாய் அடுக்கு அணுகல் புள்ளி · செயல்முறைப் பிரிவு", "पाइप रैक पहुँच बिंदु · प्रोसेस यूनिट"),
        site="process", time="overcast", spawn=(0, -23, 0), work_point=(0, -5, 0),
    )
    m.brief(
        lines=[
            T("Valve packing job at the pipe rack. Your PPE is in the issue crate from the night shift.", "குழாய் அடுக்கில் வால்வுப் பேக்கிங் வேலை. உங்கள் PPE இரவுப் பணியின் வழங்கல் பெட்டியில் உள்ளது.", "पाइप रैक पर वाल्व पैकिंग का काम। आपका PPE रात की शिफ्ट के इश्यू क्रेट में है।"),
            T("Inspect every item before you use it.", "பயன்படுத்தும் முன் ஒவ்வொரு பொருளையும் ஆய்வு செய்யுங்கள்.", "उपयोग से पहले हर वस्तु की जाँच करें।"),
        ],
        task=T("Inspect your issued PPE, deal with any defects and decide whether the job can start.", "வழங்கப்பட்ட PPE-ஐ ஆய்வு செய்து, குறைபாடுகளைக் கையாண்டு, வேலை தொடங்கலாமா என்று முடிவு செய்யுங்கள்.", "मिले PPE की जाँच करें, खराबियों से निपटें और तय करें कि काम शुरू हो सकता है या नहीं।"),
        equipment=T("Issue crate IC-7, spare PPE cabinet (fictional).", "வழங்கல் பெட்டி IC-7, உதிரி PPE அலமாரி (கற்பனை).", "इश्यू क्रेट IC-7, अतिरिक्त PPE कैबिनेट (काल्पनिक)।"),
        objective=T("Use only serviceable PPE. Report damaged items; if no replacement exists, the job waits.", "சேவைக்கு உகந்த PPE-ஐ மட்டும் பயன்படுத்துங்கள். சேதமடைந்தவற்றைத் தெரிவியுங்கள்; மாற்று இல்லையென்றால் வேலை காத்திருக்கும்.", "केवल उपयोग-योग्य PPE इस्तेमाल करें। क्षतिग्रस्त वस्तुएँ रिपोर्ट करें; बदल न मिले तो काम रुकेगा।"),
        information=T("Task card TC-44 requires helmet, gloves (general handling) and goggles.", "பணி அட்டை TC-44 தலைக்கவசம், கையுறை (பொதுக் கையாளுதல்), கண்ணாடி கோருகிறது.", "टास्क कार्ड TC-44 हेलमेट, दस्ताने (सामान्य हैंडलिंग) और गॉगल्स माँगता है।"),
        objectives=[
            T("Recognise damaged PPE during a pre-use check.", "பயன்பாட்டுக்கு முந்தைய சரிபார்ப்பில் சேதமடைந்த PPE-ஐ அடையாளம் காணுதல்.", "उपयोग-पूर्व जाँच में क्षतिग्रस्त PPE पहचानना।"),
            T("Choose replacement or escalation over improvisation.", "தற்காலிக மாற்றுக்குப் பதிலாக மாற்றீடு அல்லது மேலிடத் தெரிவிப்பைத் தேர்ந்தெடுத்தல்.", "जुगाड़ के बजाय बदलाव या आगे बढ़ाना चुनना।"),
        ],
    )
    m.dialogue("meet", [
        ("safety_officer", "neutral", T("Your kit's in crate IC-7. Night shift used it. Check it properly — every item.", "உங்கள் உபகரணங்கள் IC-7 பெட்டியில் உள்ளன. இரவுப் பணி அவற்றைப் பயன்படுத்தியது. ஒவ்வொன்றையும் சரியாகச் சரிபாருங்கள்.", "आपका सामान क्रेट IC-7 में है। रात की शिफ्ट ने इसे इस्तेमाल किया। हर वस्तु ठीक से जाँचिए।")),
        ("safety_officer", "serious", T("Anything damaged comes to me. There's a spare cabinet, but it's not bottomless.", "சேதமடைந்த எதுவும் என்னிடம் வர வேண்டும். உதிரி அலமாரி உள்ளது, ஆனால் அது முடிவற்றது அல்ல.", "जो भी क्षतिग्रस्त हो मुझे बताइए। अतिरिक्त कैबिनेट है, पर वह अनंत नहीं।")),
    ])
    m.dialogue("joseph", [
        ("senior_tech", "neutral", T("That helmet? Hairline crack. I've worn worse for years. Just wear it.", "அந்தத் தலைக்கவசமா? மெல்லிய விரிசல். நான் பல ஆண்டுகள் இதைவிட மோசமானதை அணிந்திருக்கிறேன். அணிந்துகொள்ளுங்கள்.", "वह हेलमेट? बाल जितनी दरार है। मैंने सालों इससे बुरा पहना है। बस पहन लो।"),
         [(T("A cracked helmet is out of service, Joseph. I'm reporting it.", "விரிசல் விழுந்த தலைக்கவசம் பயன்பாட்டில் இல்லை, ஜோசப். நான் தெரிவிக்கிறேன்.", "दरार वाला हेलमेट सेवा से बाहर है, जोसेफ। मैं रिपोर्ट कर रहा हूँ।"), "joseph", "refuse", None),
          (T("OK, if you say so", "சரி, நீங்கள் சொன்னால்", "ठीक है, अगर आप कहते हैं"), "joseph", "accept", None)]),
    ])
    m.dialogue("joseph_done", [("senior_tech", "neutral", T("Yeah, yeah. You're right. Don't tell anyone I said that.", "ஆமாம், ஆமாம். நீங்கள் சொல்வது சரி. நான் சொன்னதை யாரிடமும் சொல்லாதீர்கள்.", "हाँ, हाँ। आप सही हो। किसी को मत बताना कि मैंने ऐसा कहा।"))])
    m.dialogue("unsafe", [("safety_officer", "concerned", T("No. Damaged PPE is out of service. It doesn't get worn, patched or 'just for today'.", "இல்லை. சேதமடைந்த PPE பயன்பாட்டில் இல்லை. அது அணியப்படாது, ஒட்டப்படாது, 'இன்று மட்டும்' என்பதும் இல்லை.", "नहीं। क्षतिग्रस्त PPE सेवा से बाहर है। न पहना जाता है, न जोड़ा जाता है, न 'आज के लिए'।"))])
    m.dialogue("correct", [("safety_officer", "pleased", T("Good. Gloves are on order — the job waits until they're here. That's the right call.", "நல்லது. கையுறைகள் ஆர்டர் செய்யப்பட்டுள்ளன — அவை வரும் வரை வேலை காத்திருக்கும். அதுதான் சரியான முடிவு.", "बढ़िया। दस्ताने मँगवाए गए हैं — उनके आने तक काम रुकेगा। यही सही निर्णय है।"))])
    m.npc("safety_officer", -3, -12, 180, talk=[("meet", not_done("meet_safety_officer"))])
    m.npc("senior_tech", 3.0, 0.8, 200, talk=[("joseph", not_done("joseph")), ("joseph_done", None)], briefing=False)

    m.decor("pipe", 0, 9.0, len=16, y=3.2, d=0.32)
    m.decor("ladder", 4.0, 8.4)
    m.decor("tape", 0, 8.0, w=8, d=3, color="#ffc23d")
    m.decor("sign", -4.5, 0.5, kind="mandatory", text="world.sign.ppe")
    m.obj("issue_crate", "locker", -2.8, 2.5, 20, panel="inventory", prompt="open", kind="station",
          title=T("ISSUE CRATE IC-7", "வழங்கல் பெட்டி IC-7", "इश्यू क्रेट IC-7"),
          name=T("Issue crate IC-7 (your kit)", "வழங்கல் பெட்டி IC-7 (உங்கள் உபகரணம்)", "इश्यू क्रेट IC-7 (आपका सामान)"),
          details=[T("Your issued PPE from the night shift. Inspect each item.", "இரவுப் பணியிலிருந்து உங்களுக்கு வழங்கப்பட்ட PPE. ஒவ்வொன்றையும் ஆய்வு செய்யுங்கள்.", "रात की शिफ्ट से मिला आपका PPE। हर वस्तु जाँचें।")])
    m.item("helmet_cracked", "issue_crate", "helmet_cracked", T("Helmet (issued)", "தலைக்கவசம் (வழங்கப்பட்டது)", "हेलमेट (जारी)"), T("Visible crack across the shell.", "ஓட்டின் குறுக்கே தெரியும் விரிசல்.", "खोल पर दिखाई देती दरार।"), defect=True)
    m.item("gloves_split", "issue_crate", "gloves_torn", T("Gloves (issued)", "கையுறை (வழங்கப்பட்டது)", "दस्ताने (जारी)"), T("Seam split along the palm.", "உள்ளங்கையில் தையல் பிரிந்துள்ளது.", "हथेली पर सिलाई फटी हुई।"), defect=True)
    m.item("goggles_ok", "issue_crate", "goggles", T("Goggles (issued)", "கண்ணாடி (வழங்கப்பட்டது)", "गॉगल्स (जारी)"), T("Lens clear, strap intact.", "லென்ஸ் தெளிவு, பட்டை நல்ல நிலையில்.", "लेंस साफ़, पट्टा ठीक।"))
    m.obj("spare_cabinet", "locker", 3.0, -3.5, panel="inventory", prompt="open", kind="station", groups=["start"],
          title=T("SPARE PPE", "உதிரி PPE", "अतिरिक्त PPE"),
          name=T("Spare PPE cabinet", "உதிரி PPE அலமாரி", "अतिरिक्त PPE कैबिनेट"),
          details=[T("Spares for replacing damaged items.", "சேதமடைந்தவற்றை மாற்றுவதற்கான உதிரிகள்.", "क्षतिग्रस्त वस्तुएँ बदलने के लिए अतिरिक्त।")])
    m.item("helmet_spare", "spare_cabinet", "helmet", T("Spare helmet", "உதிரித் தலைக்கவசம்", "अतिरिक्त हेलमेट"), T("Good condition.", "நல்ல நிலை.", "अच्छी हालत।"))
    m.item("tape_roll", "spare_cabinet", "apron", T("Repair tape", "பழுதுபார்க்கும் நாடா", "मरम्मत टेप"), T("Duct tape. Not PPE.", "ஒட்டும் நாடா. PPE அல்ல.", "डक्ट टेप। PPE नहीं।"))
    m.item("gloves_none", "spare_cabinet", "gloves_cotton", T("Glove shelf", "கையுறை அலமாரித் தட்டு", "दस्तानों की शेल्फ़"), T("EMPTY — no spare general-handling gloves.", "காலி — உதிரிப் பொதுக் கையாளும் கையுறைகள் இல்லை.", "खाली — अतिरिक्त सामान्य हैंडलिंग दस्ताने नहीं।"), defect=True)
    m.group("start", T("Gloves can't be replaced right now. What happens to the job?", "இப்போது கையுறைகளை மாற்ற முடியாது. வேலைக்கு என்ன நடக்கும்?", "अभी दस्ताने नहीं बदले जा सकते। काम का क्या होगा?"), [
        ("wait", T("Report it and hold the job until serviceable gloves arrive", "தெரிவித்து, சேவைக்கு உகந்த கையுறைகள் வரும் வரை வேலையை நிறுத்தி வையுங்கள்", "रिपोर्ट करें और उपयोग-योग्य दस्ताने आने तक काम रोकें")),
        ("tape_gloves", T("Tape the split seam and start", "பிரிந்த தையலில் நாடா ஒட்டித் தொடங்குங்கள்", "फटी सिलाई पर टेप लगाकर शुरू करें")),
        ("bare_hands", T("Start without gloves — it's only packing", "கையுறை இல்லாமல் தொடங்குங்கள் — இது பேக்கிங் மட்டுமே", "बिना दस्ताने शुरू करें — बस पैकिंग है")),
    ])
    m.group("joseph", T("Joseph says the cracked helmet is fine. Your answer?", "விரிசல் தலைக்கவசம் பரவாயில்லை என்கிறார் ஜோசப். உங்கள் பதில்?", "जोसेफ कहते हैं दरार वाला हेलमेट ठीक है। आपका जवाब?"), [
        ("refuse", T("Out of service — report it", "பயன்பாட்டில் இல்லை — தெரிவிக்கவும்", "सेवा से बाहर — रिपोर्ट करें")),
        ("accept", T("Wear it anyway", "எப்படியும் அணியவும்", "फिर भी पहनें")),
    ])

    meet = m.meet("safety_officer")
    m.briefing(meet)
    m.step("open_crate", title=T("Open your issue crate", "உங்கள் வழங்கல் பெட்டியைத் திறவுங்கள்", "अपना इश्यू क्रेट खोलें"), instruction=T("Open crate IC-7 and inspect your kit.", "IC-7 பெட்டியைத் திறந்து உங்கள் உபகரணங்களை ஆய்வு செய்யுங்கள்.", "क्रेट IC-7 खोलकर अपना सामान जाँचें।"),
           trigger=inspect("issue_crate"), requires=["briefing"], points=5, concept="ppe_condition", scene="ppe",
           hints=[T("The crate is on the west side.", "பெட்டி மேற்குப் பக்கம் உள்ளது.", "क्रेट पश्चिमी ओर है।")])
    m.step("flag_helmet", title=T("Report the damaged helmet", "சேதமடைந்த தலைக்கவசத்தைத் தெரிவியுங்கள்", "क्षतिग्रस्त हेलमेट रिपोर्ट करें"), instruction=T("Report the helmet defect.", "தலைக்கவசக் குறைபாட்டைத் தெரிவியுங்கள்.", "हेलमेट की खराबी रिपोर्ट करें।"),
           trigger=flag("helmet_cracked"), requires=["open_crate"], points=10, concept="ppe_condition", scene="inspect",
           hints=[T("Read the condition of each item.", "ஒவ்வொரு பொருளின் நிலையையும் படியுங்கள்.", "हर वस्तु की स्थिति पढ़ें।")])
    m.step("flag_gloves", title=T("Report the damaged gloves", "சேதமடைந்த கையுறைகளைத் தெரிவியுங்கள்", "क्षतिग्रस्त दस्ताने रिपोर्ट करें"), instruction=T("Report the glove defect.", "கையுறைக் குறைபாட்டைத் தெரிவியுங்கள்.", "दस्तानों की खराबी रिपोर्ट करें।"),
           trigger=flag("gloves_split"), requires=["open_crate"], points=10, concept="ppe_condition", scene="inspect",
           hints=[T("Seams matter.", "தையல்கள் முக்கியம்.", "सिलाई मायने रखती है।")])
    m.step("take_goggles", title=T("Keep the serviceable goggles", "சேவைக்கு உகந்த கண்ணாடியை வைத்துக்கொள்ளுங்கள்", "उपयोग-योग्य गॉगल्स रखें"), instruction=T("Select the goggles that passed inspection.", "ஆய்வில் தேறிய கண்ணாடியைத் தேர்ந்தெடுங்கள்.", "जाँच में ठीक निकले गॉगल्स चुनें।"),
           trigger=select("goggles_ok"), requires=["open_crate"], points=5, concept="ppe_condition", scene="ppe",
           hints=[T("Not everything in the crate is damaged.", "பெட்டியில் உள்ள அனைத்தும் சேதமடைந்தவை அல்ல.", "क्रेट की हर चीज़ खराब नहीं है।")])
    m.step("joseph", title=T("Answer Joseph about the helmet", "தலைக்கவசம் பற்றி ஜோசப்புக்குப் பதிலளியுங்கள்", "हेलमेट पर जोसेफ को जवाब दें"), instruction=T("Talk to Joseph near the crate.", "பெட்டிக்கு அருகில் ஜோசப்புடன் பேசுங்கள்.", "क्रेट के पास जोसेफ से बात करें।"),
           trigger=decide("joseph", "refuse"), requires=["flag_helmet"], points=10, concept="ppe_condition", scene="communicate",
           hints=[T("Experience doesn't repair a crack.", "அனுபவம் விரிசலைச் சரிசெய்யாது.", "अनुभव दरार नहीं भरता।")])
    m.step("open_spares", title=T("Check the spare cabinet", "உதிரி அலமாரியைச் சரிபாருங்கள்", "अतिरिक्त कैबिनेट जाँचें"), instruction=T("Open the spare PPE cabinet.", "உதிரி PPE அலமாரியைத் திறவுங்கள்.", "अतिरिक्त PPE कैबिनेट खोलें।"),
           trigger=inspect("spare_cabinet"), requires=["flag_helmet", "flag_gloves"], points=5, concept="ppe_condition", scene="ppe",
           hints=[T("East of the walkway.", "நடைபாதைக்குக் கிழக்கே.", "रास्ते के पूर्व में।")])
    m.step("take_spare_helmet", title=T("Take the spare helmet", "உதிரித் தலைக்கவசத்தை எடுங்கள்", "अतिरिक्त हेलमेट लें"), instruction=T("Select the serviceable spare helmet.", "சேவைக்கு உகந்த உதிரித் தலைக்கவசத்தைத் தேர்ந்தெடுங்கள்.", "उपयोग-योग्य अतिरिक्त हेलमेट चुनें।"),
           trigger=select("helmet_spare"), requires=["open_spares"], points=10, concept="ppe_condition", scene="ppe",
           hints=[T("Replacement, not repair.", "மாற்றீடு, பழுதுபார்ப்பு அல்ல.", "बदलाव, मरम्मत नहीं।")])
    m.step("flag_no_gloves", title=T("Report: no spare gloves", "தெரிவியுங்கள்: உதிரிக் கையுறைகள் இல்லை", "रिपोर्ट करें: अतिरिक्त दस्ताने नहीं"), instruction=T("Report the empty glove shelf.", "காலியான கையுறைத் தட்டைத் தெரிவியுங்கள்.", "खाली दस्तानों की शेल्फ़ रिपोर्ट करें।"),
           trigger=flag("gloves_none"), requires=["open_spares"], points=10, concept="ppe_completeness", scene="report",
           hints=[T("Is there a replacement for every damaged item?", "சேதமடைந்த ஒவ்வொன்றுக்கும் மாற்று உள்ளதா?", "क्या हर क्षतिग्रस्त वस्तु का विकल्प है?")])
    m.step("decide", title=T("Decide whether the job can start", "வேலை தொடங்கலாமா என்று முடிவு செய்யுங்கள்", "तय करें कि काम शुरू हो सकता है या नहीं"), instruction=T("Make the call at the spare cabinet.", "உதிரி அலமாரியில் முடிவெடுங்கள்.", "अतिरिक्त कैबिनेट पर निर्णय लें।"),
           trigger=decide("start", "wait"), requires=["take_spare_helmet", "flag_no_gloves", "take_goggles", "joseph"], points=15, concept="ppe_completeness", scene="decision",
           mistake_if_early=T("Finish inspecting and replacing before you decide.", "முடிவெடுக்கும் முன் ஆய்வையும் மாற்றீட்டையும் முடியுங்கள்.", "निर्णय से पहले जाँच और बदलाव पूरा करें।"),
           hints=[T("Can you start without serviceable gloves?", "சேவைக்கு உகந்த கையுறைகள் இல்லாமல் தொடங்க முடியுமா?", "क्या उपयोग-योग्य दस्तानों के बिना शुरू कर सकते हैं?")])

    m.critical("wear_cracked_helmet", trigger=select("helmet_cracked"), concept="ppe_condition", dialogue="unsafe",
               explanation=T("You chose to use a helmet with a visible crack.", "தெரியும் விரிசல் உள்ள தலைக்கவசத்தைப் பயன்படுத்தத் தேர்ந்தெடுத்தீர்கள்.", "आपने दिखाई देती दरार वाला हेलमेट इस्तेमाल करना चुना।"),
               missing=T("A serviceable helmet.", "சேவைக்கு உகந்த தலைக்கவசம்.", "उपयोग-योग्य हेलमेट।"))
    m.critical("use_split_gloves", trigger=select("gloves_split"), concept="ppe_condition", dialogue="unsafe",
               explanation=T("You chose gloves with a split seam.", "தையல் பிரிந்த கையுறைகளைத் தேர்ந்தெடுத்தீர்கள்.", "आपने फटी सिलाई वाले दस्ताने चुने।"),
               missing=T("Serviceable gloves.", "சேவைக்கு உகந்த கையுறைகள்.", "उपयोग-योग्य दस्ताने।"))
    m.critical("patch_ppe", trigger=decide("start", "tape_gloves"), concept="ppe_condition", dialogue="unsafe",
               explanation=T("Taped PPE is still damaged PPE.", "நாடா ஒட்டிய PPE இன்னும் சேதமடைந்த PPE-தான்.", "टेप लगा PPE अब भी क्षतिग्रस्त PPE है।"),
               missing=T("A serviceable replacement, or the job waits.", "சேவைக்கு உகந்த மாற்று, அல்லது வேலை காத்திருக்கும்.", "उपयोग-योग्य विकल्प, या काम रुकेगा।"))
    m.critical("no_gloves", trigger=decide("start", "bare_hands"), concept="ppe_completeness", dialogue="unsafe",
               explanation=T("The task card requires gloves. No gloves is not an option.", "பணி அட்டை கையுறைகளைக் கோருகிறது. கையுறை இல்லாமல் என்பது தேர்வல்ல.", "टास्क कार्ड दस्ताने माँगता है। बिना दस्ताने कोई विकल्प नहीं।"),
               missing=T("Serviceable gloves.", "சேவைக்கு உகந்த கையுறைகள்.", "उपयोग-योग्य दस्ताने।"))
    m.mistake("accept_joseph", trigger=decide("joseph", "accept"), kind="incorrect_decision", concept="ppe_condition",
              feedback=T("A cracked helmet is out of service, whatever anyone has 'got away with'. Talk to Joseph again.", "யார் எதைச் 'சமாளித்தாலும்', விரிசல் தலைக்கவசம் பயன்பாட்டில் இல்லை. ஜோசப்புடன் மீண்டும் பேசுங்கள்.", "किसी ने कुछ भी 'चला लिया' हो, दरार वाला हेलमेट सेवा से बाहर है। जोसेफ से फिर बात करें।"))
    m.mistake("tape_not_ppe", trigger=select("tape_roll"), kind="incorrect_decision", concept="ppe_condition",
              feedback=T("Tape is not PPE and cannot repair PPE.", "நாடா PPE அல்ல, PPE-ஐப் பழுதுபார்க்கவும் முடியாது.", "टेप PPE नहीं है और PPE की मरम्मत नहीं कर सकता।"))
    m.mistake("wrong_defect", trigger={"type": "evidence_flagged"}, kind="incorrect_decision", concept="ppe_condition",
              feedback=T("That item is serviceable.", "அந்தப் பொருள் சேவைக்கு உகந்தது.", "वह वस्तु उपयोग-योग्य है।"))

    m.debrief(
        success=T("You inspected, reported, replaced what you could and held the job for what you couldn't.", "ஆய்வு செய்து, தெரிவித்து, முடிந்தவற்றை மாற்றி, முடியாதவற்றுக்காக வேலையை நிறுத்தி வைத்தீர்கள்.", "आपने जाँचा, रिपोर्ट किया, जो बदला जा सका बदला और जो नहीं, उसके लिए काम रोका।"),
        critical=T("Damaged PPE was used or patched. Out of service means out of service.", "சேதமடைந்த PPE பயன்படுத்தப்பட்டது அல்லது ஒட்டப்பட்டது. பயன்பாட்டில் இல்லை என்றால் இல்லைதான்.", "क्षतिग्रस्त PPE इस्तेमाल हुआ या जोड़ा गया। सेवा से बाहर मतलब सेवा से बाहर।"),
        failed=T("Repeated unsafe choices ended the attempt.", "தொடர்ந்த பாதுகாப்பற்ற தேர்வுகள் முயற்சியை முடித்தன.", "बार-बार असुरक्षित विकल्पों से प्रयास समाप्त हुआ।"),
        lines=[
            ({"criticalRule": "wear_cracked_helmet"}, T("You selected the cracked helmet.", "விரிசல் தலைக்கவசத்தைத் தேர்ந்தெடுத்தீர்கள்.", "आपने दरार वाला हेलमेट चुना।")),
            ({"criticalRule": "patch_ppe"}, T("You chose to tape damaged gloves.", "சேதமடைந்த கையுறைகளில் நாடா ஒட்டத் தேர்ந்தெடுத்தீர்கள்.", "आपने क्षतिग्रस्त दस्तानों पर टेप लगाना चुना।")),
            ({"stepCompleted": "joseph"}, T("You stood by the inspection when a senior colleague brushed it off.", "மூத்த சக ஊழியர் புறக்கணித்தபோதும் ஆய்வை உறுதியாகப் பின்பற்றினீர்கள்.", "वरिष्ठ साथी के टालने पर भी आप जाँच पर टिके रहे।")),
            ({"stepCompleted": "flag_no_gloves"}, T("You noticed there was no replacement for the gloves.", "கையுறைகளுக்கு மாற்று இல்லை என்பதைக் கவனித்தீர்கள்.", "आपने देखा कि दस्तानों का कोई विकल्प नहीं था।")),
        ],
    )
    m.comic(T("OUT OF SERVICE MEANS OUT", "பயன்பாட்டில் இல்லை என்றால் இல்லை", "सेवा से बाहर मतलब बाहर"), [
        ("magnifier", T("Inspect every item before you put it on.", "அணியும் முன் ஒவ்வொரு பொருளையும் ஆய்வு செய்யுங்கள்.", "पहनने से पहले हर वस्तु जाँचें।")),
        ("torn_glove", T("Damaged PPE is reported — never patched.", "சேதமடைந்த PPE தெரிவிக்கப்படுகிறது — ஒருபோதும் ஒட்டப்படுவதில்லை.", "क्षतिग्रस्त PPE रिपोर्ट होता है — कभी जोड़ा नहीं जाता।")),
        ("stop_sign", T("No serviceable replacement? The job waits.", "சேவைக்கு உகந்த மாற்று இல்லையா? வேலை காத்திருக்கும்.", "उपयोग-योग्य विकल्प नहीं? काम रुकेगा।")),
    ])
    m.report(["open_crate", "flag_helmet", "flag_gloves", "take_goggles", "take_spare_helmet", "flag_no_gloves"], ["joseph", "decide"])
    m.mcq(1, concept="ppe_condition",
          stem=T("When should you inspect your PPE?", "உங்கள் PPE-ஐ எப்போது ஆய்வு செய்ய வேண்டும்?", "अपने PPE की जाँच कब करनी चाहिए?"),
          options=[T("Before each use", "ஒவ்வொரு பயன்பாட்டுக்கும் முன்", "हर उपयोग से पहले"), T("Once a year", "ஆண்டுக்கு ஒருமுறை", "साल में एक बार"), T("Only when it looks dirty", "அழுக்காகத் தெரியும்போது மட்டும்", "केवल जब गंदा दिखे")],
          correct="a", explanation=T("Damage happens between uses; a pre-use check catches it.", "பயன்பாடுகளுக்கு இடையில் சேதம் ஏற்படும்; பயன்பாட்டுக்கு முந்தைய சரிபார்ப்பு அதைப் பிடிக்கும்.", "नुकसान उपयोगों के बीच होता है; उपयोग-पूर्व जाँच उसे पकड़ती है।"))
    m.mcq(2, concept="ppe_condition",
          stem=T("Your gloves have a split seam. What do you do?", "உங்கள் கையுறைகளில் தையல் பிரிந்துள்ளது. என்ன செய்வீர்கள்?", "आपके दस्तानों की सिलाई फटी है। आप क्या करेंगे?"),
          options=[T("Tape the split", "பிரிவில் நாடா ஒட்டுவேன்", "फटी जगह टेप लगाऊँगा"), T("Report them and get a serviceable pair", "தெரிவித்து சேவைக்கு உகந்த ஜோடியைப் பெறுவேன்", "रिपोर्ट करके उपयोग-योग्य जोड़ी लूँगा"), T("Wear them inside out", "உள்புறம் வெளியே அணிவேன்", "उल्टा पहनूँगा")],
          correct="b", explanation=T("Damaged PPE is taken out of service and replaced.", "சேதமடைந்த PPE பயன்பாட்டிலிருந்து நீக்கப்பட்டு மாற்றப்படுகிறது.", "क्षतिग्रस्त PPE सेवा से हटाकर बदला जाता है।"))
    m.mcq(3, concept="ppe_completeness",
          stem=T("There is no serviceable replacement for a required item. What happens?", "தேவையான பொருளுக்குச் சேவைக்கு உகந்த மாற்று இல்லை. என்ன நடக்கும்?", "किसी आवश्यक वस्तु का उपयोग-योग्य विकल्प नहीं है। क्या होगा?"),
          options=[T("Start anyway and be careful", "எப்படியும் கவனமாகத் தொடங்குவேன்", "फिर भी सावधानी से शुरू करूँगा"), T("The job waits until it is available", "அது கிடைக்கும் வரை வேலை காத்திருக்கும்", "उपलब्ध होने तक काम रुकेगा"), T("Use the damaged one", "சேதமடைந்ததைப் பயன்படுத்துவேன்", "क्षतिग्रस्त वाला इस्तेमाल करूँगा")],
          correct="b", explanation=T("Required PPE is required; without it the task does not start.", "தேவையான PPE தேவையானதுதான்; அது இல்லாமல் பணி தொடங்காது.", "आवश्यक PPE आवश्यक है; उसके बिना काम शुरू नहीं होता।"))
    m.mcq(4, concept="ppe_condition",
          stem=T("An experienced colleague says a cracked helmet is fine. Who is right?", "அனுபவமுள்ள சக ஊழியர் விரிசல் தலைக்கவசம் பரவாயில்லை என்கிறார். யார் சரி?", "एक अनुभवी साथी कहते हैं दरार वाला हेलमेट ठीक है। कौन सही है?"),
          options=[T("The colleague, because of their experience", "அனுபவத்தால் சக ஊழியர்", "साथी, अपने अनुभव के कारण"), T("Nobody can tell", "யாராலும் சொல்ல முடியாது", "कोई नहीं बता सकता"), T("The inspection: visible damage means out of service", "ஆய்வு: தெரியும் சேதம் என்றால் பயன்பாட்டில் இல்லை", "जाँच: दिखाई देता नुकसान मतलब सेवा से बाहर")],
          correct="c", explanation=T("Condition, not experience, decides whether PPE can be used.", "PPE-ஐப் பயன்படுத்தலாமா என்பதை அனுபவம் அல்ல, நிலைதான் தீர்மானிக்கும்.", "PPE इस्तेमाल हो सकता है या नहीं, यह अनुभव नहीं, स्थिति तय करती है।"))
    m.spec(
        workplaceLocation="Fictional pipe-rack access point, overcast day.",
        corePrinciple="Inspect PPE before use; damaged PPE is reported and replaced, never patched; no replacement means the job waits.",
        commonMisconceptions=["A hairline crack is nothing.", "Tape fixes PPE.", "Short jobs can go without gloves."],
        criticalDecisions=["Select damaged helmet/gloves", "Tape gloves", "Start bare-handed"],
        assessmentCriteria={"correct": "Report helmet and gloves; keep goggles; answer Joseph; take spare helmet; report no gloves; hold the job."},
    )
    return m
