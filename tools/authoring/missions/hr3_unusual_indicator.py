"""Hazard Recognition · Level 3 — The Unusual Indicator.

Story: Control Room Operator Farah Khan asks the trainee to confirm pump P-305
is ready for a bearing inspection. The local display reads 'ISOLATED' in green,
but the beacon is amber, the handover log mentions a test run and the
isolation record says the isolation was cancelled. Learning: a display is one
source among several; when sources disagree, report through the right channel
and hold the job. Two decisions: what to report, and what happens to the job.
"""
from authoring.dsl import Mission, T, any_flag, decide, enter, flag, inspect, not_done, tool


def build() -> Mission:
    m = Mission(
        code="hr3", id="og-hazrec-l3-unusual-indicator", category="og_hazard_recognition", level=3, minutes=14,
        title=T("The Unusual Indicator", "அசாதாரணக் குறிகாட்டி", "असामान्य संकेतक"),
        subtitle=T("When the display and the paperwork disagree", "காட்சித் திரையும் ஆவணங்களும் முரண்படும்போது", "जब डिस्प्ले और कागज़ात मेल न खाएँ"),
        description=T("A green 'ISOLATED' light, an amber beacon and a record that tells a different story.", "ஒரு பச்சை 'தனிமைப்படுத்தப்பட்டது' விளக்கு, ஒரு ஆம்பர் விளக்கு, வேறு கதை சொல்லும் ஒரு பதிவு.", "एक हरी 'आइसोलेटेड' बत्ती, एक एम्बर बीकन और एक रिकॉर्ड जो अलग कहानी कहता है।"),
        location=T("Cooling water pump house · Utility block", "குளிர்நீர் பம்ப் இல்லம் · பயன்பாட்டுப் பிரிவு", "कूलिंग वॉटर पंप हाउस · यूटिलिटी ब्लॉक"),
        site="utility", spawn=(0, -23, 0), work_point=(0, -4, 0),
    )
    m.brief(
        lines=[
            T("P-305 is due a bearing inspection. Farah in the control room wants you to confirm it is ready.", "P-305-க்கு பேரிங் ஆய்வு நிலுவையில் உள்ளது. அது தயாரா என்று உறுதிசெய்ய கட்டுப்பாட்டு அறையின் ஃபரா விரும்புகிறார்.", "P-305 का बेयरिंग निरीक्षण होना है। कंट्रोल रूम की फ़रा चाहती हैं कि आप पुष्टि करें कि यह तैयार है।"),
            T("Less guidance today: decide for yourself which sources to check.", "இன்று குறைந்த வழிகாட்டல்: எந்தத் தகவல் மூலங்களைச் சரிபார்ப்பது என்று நீங்களே முடிவு செய்யுங்கள்.", "आज कम मार्गदर्शन: कौन से स्रोत जाँचने हैं, यह आप स्वयं तय करें।"),
        ],
        task=T("Confirm whether P-305 is ready for its bearing inspection.", "P-305 பேரிங் ஆய்வுக்குத் தயாரா என்பதை உறுதிசெய்யுங்கள்.", "पुष्टि करें कि P-305 बेयरिंग निरीक्षण के लिए तैयार है या नहीं।"),
        equipment=T("Cooling water pump P-305, local status display, isolation record (fictional).", "குளிர்நீர் பம்ப் P-305, உள்ளூர் நிலைத் திரை, தனிமைப்படுத்தல் பதிவு (கற்பனை).", "कूलिंग वॉटर पंप P-305, स्थानीय स्टेटस डिस्प्ले, आइसोलेशन रिकॉर्ड (काल्पनिक)।"),
        objective=T("Compare the display with the documents, report what you find and decide on the job.", "திரையை ஆவணங்களுடன் ஒப்பிட்டு, கண்டதைப் புகாரளித்து, வேலை குறித்து முடிவு செய்யுங்கள்.", "डिस्प्ले की दस्तावेज़ों से तुलना करें, जो मिले उसे रिपोर्ट करें और काम पर निर्णय लें।"),
        information=T("The site radio point connects you to the control room.", "தள வானொலிப் புள்ளி உங்களைக் கட்டுப்பாட்டு அறையுடன் இணைக்கிறது.", "साइट रेडियो पॉइंट आपको कंट्रोल रूम से जोड़ता है।"),
        objectives=[
            T("Treat a display as one source of information, not proof.", "ஒரு திரையை ஆதாரமாக அல்ல, ஒரு தகவல் மூலமாகக் கருதுங்கள்.", "डिस्प्ले को प्रमाण नहीं, जानकारी का एक स्रोत मानें।"),
            T("Report inconsistencies through the right channel and hold the job.", "முரண்பாடுகளைச் சரியான வழியில் புகாரளித்து வேலையை நிறுத்தி வையுங்கள்.", "असंगतियों को सही माध्यम से रिपोर्ट करें और काम रोकें।"),
        ],
    )
    m.dialogue("meet", [
        ("operator", "friendly", T("Hi, I'm Farah — control room. P-305 should be isolated for the bearing crew.", "வணக்கம், நான் ஃபரா — கட்டுப்பாட்டு அறை. பேரிங் குழுவுக்காக P-305 தனிமைப்படுத்தப்பட்டிருக்க வேண்டும்.", "नमस्ते, मैं फ़रा — कंट्रोल रूम। बेयरिंग टीम के लिए P-305 आइसोलेटेड होना चाहिए।")),
        ("operator", "neutral", T("My screen's been glitchy since this afternoon's test run, so go and look for yourself.", "இன்று மதியச் சோதனை ஓட்டத்திலிருந்து என் திரை சரியாக வேலை செய்யவில்லை, எனவே நீங்களே சென்று பாருங்கள்.", "आज दोपहर के टेस्ट रन के बाद से मेरी स्क्रीन ठीक नहीं चल रही, तो आप खुद जाकर देखिए।")),
        ("operator", "serious", T("Radio me from the pump house if anything doesn't add up.", "ஏதாவது பொருந்தவில்லை என்றால் பம்ப் இல்லத்திலிருந்து எனக்கு வானொலியில் தெரிவியுங்கள்.", "अगर कुछ मेल न खाए तो पंप हाउस से मुझे रेडियो कीजिए।")),
    ])
    m.dialogue("revisit", [("operator", "neutral", T("Use the radio point by the pump house — I'll be listening.", "பம்ப் இல்லத்திற்கு அருகிலுள்ள வானொலிப் புள்ளியைப் பயன்படுத்துங்கள் — நான் கேட்டுக்கொண்டிருப்பேன்.", "पंप हाउस के पास वाला रेडियो पॉइंट इस्तेमाल करें — मैं सुन रही हूँ।"))])
    m.dialogue("radio_ack", [
        ("operator", "concerned", T("[Radio] Copy. My records agree with yours: the isolation was cancelled for the test run.", "[வானொலி] புரிந்தது. என் பதிவுகளும் உங்களுடன் ஒத்துப்போகின்றன: சோதனை ஓட்டத்திற்காகத் தனிமைப்படுத்தல் ரத்து செய்யப்பட்டது.", "[रेडियो] समझ गई। मेरे रिकॉर्ड भी आपसे मेल खाते हैं: टेस्ट रन के लिए आइसोलेशन रद्द किया गया था।")),
        ("operator", "serious", T("[Radio] That local display never updated. Don't let anyone near it until it's re-isolated and verified.", "[வானொலி] அந்த உள்ளூர்த் திரை புதுப்பிக்கப்படவே இல்லை. மீண்டும் தனிமைப்படுத்தி சரிபார்க்கும் வரை யாரையும் அருகில் விட வேண்டாம்.", "[रेडियो] वह स्थानीय डिस्प्ले कभी अपडेट नहीं हुआ। दोबारा आइसोलेट और सत्यापित होने तक किसी को पास न जाने दें।")),
    ])
    m.dialogue("unsafe", [
        ("operator", "concerned", T("[Radio] Stop right there. A green light is not a verified isolation.", "[வானொலி] அங்கேயே நில்லுங்கள். பச்சை விளக்கு என்பது சரிபார்க்கப்பட்ட தனிமைப்படுத்தல் அல்ல.", "[रेडियो] वहीं रुकिए। हरी बत्ती सत्यापित आइसोलेशन नहीं है।")),
    ])
    m.dialogue("correct", [("operator", "pleased", T("[Radio] Good call holding it. I'll raise the display fault and get the isolation redone.", "[வானொலி] நிறுத்தி வைத்தது நல்ல முடிவு. திரைக் கோளாறைப் பதிவுசெய்து தனிமைப்படுத்தலை மீண்டும் செய்ய ஏற்பாடு செய்கிறேன்.", "[रेडियो] रोककर रखना सही निर्णय। मैं डिस्प्ले की खराबी दर्ज कराती हूँ और आइसोलेशन दोबारा करवाती हूँ।"))])
    m.npc("operator", -3.0, -12.5, 180, talk=[("meet", not_done("meet_operator")), ("revisit", None)])

    m.zone("zone_pumphouse", T("Pump house P-305", "பம்ப் இல்லம் P-305", "पंप हाउस P-305"), (-6, 6, -2, 8))
    m.decor("building", -10.0, -13.0, heading=-90, w=5, d=3, h=3, sign=T("CONTROL ROOM", "கட்டுப்பாட்டு அறை", "कंट्रोल रूम"), signBg="#e8423f")
    m.decor("pump", 2.5, 6.0, tag="P-306", color="#4a6fa3", state="running")
    m.decor("pipe", 0, 9.3, len=12, y=2.6, d=0.35)
    m.decor("drum", -5.0, 0.0, count=2, color="#1f6f8b")
    m.decor("sign", -2.0, -1.4, kind="mandatory", text="world.sign.ppe")

    m.obj("pump_p305", "pump", -1.2, 3.0, tag="P-305", state="stopped",
          name=T("Pump P-305", "பம்ப் P-305", "पंप P-305"),
          details=[T("Cooling water pump P-305. It is not running.", "குளிர்நீர் பம்ப் P-305. இது இயங்கவில்லை.", "कूलिंग वॉटर पंप P-305। यह नहीं चल रहा।"),
                   T("Nothing on the pump itself shows whether it is isolated.", "பம்பில் எதுவும் அது தனிமைப்படுத்தப்பட்டதா என்று காட்டவில்லை.", "पंप पर कुछ भी नहीं दिखाता कि यह आइसोलेटेड है या नहीं।")])
    m.obj("display_p305", "panel", 3.6, 1.0, -30, kind="indicator", prompt="read", title="P-305",
          screens={"default": [(T("RUN: STOPPED", "இயக்கம்: நிறுத்தப்பட்டது", "रन: बंद"), "amber"), (T("ISOLATED ✓", "தனிமைப்படுத்தப்பட்டது ✓", "आइसोलेटेड ✓"), "green"), (T("Last update 09:12", "கடைசிப் புதுப்பிப்பு 09:12", "अंतिम अपडेट 09:12"), "grey")],
                   "fault": [(T("RUN: STOPPED", "இயக்கம்: நிறுத்தப்பட்டது", "रन: बंद"), "amber"), (T("ISOLATION: NOT VERIFIED", "தனிமைப்படுத்தல்: சரிபார்க்கப்படவில்லை", "आइसोलेशन: सत्यापित नहीं"), "red"), (T("Display fault reported", "திரைக் கோளாறு புகாரளிக்கப்பட்டது", "डिस्प्ले खराबी रिपोर्ट की गई"), "red")]},
          beacons={"default": "amber", "fault": "red"},
          name=T("P-305 local status display", "P-305 உள்ளூர் நிலைத் திரை", "P-305 स्थानीय स्टेटस डिस्प्ले"),
          details=[T("Display: 'RUN: STOPPED' · 'ISOLATED ✓' (green).", "திரை: 'இயக்கம்: நிறுத்தப்பட்டது' · 'தனிமைப்படுத்தப்பட்டது ✓' (பச்சை).", "डिस्प्ले: 'रन: बंद' · 'आइसोलेटेड ✓' (हरा)।"),
                   T("Small print: 'Last update 09:12'. The amber beacon on top is flashing.", "சிறிய எழுத்து: 'கடைசிப் புதுப்பிப்பு 09:12'. மேலே உள்ள ஆம்பர் விளக்கு ஒளிர்கிறது.", "छोटे अक्षर: 'अंतिम अपडेट 09:12'। ऊपर का एम्बर बीकन चमक रहा है।")])
    m.obj("handover_desk", "desk", -4.0, -2.6, title=T("SHIFT DESK", "பணிமாற்ற மேசை", "शिफ्ट डेस्क"), prompt="read", kind="document", folder="#2f7ddc",
          name=T("Shift handover log", "பணிமாற்றப் பதிவேடு", "शिफ्ट हैंडओवर लॉग"),
          details=[T("13:50 — P-305 isolation removed for a 10-minute test run (ops).", "13:50 — 10 நிமிடச் சோதனை ஓட்டத்திற்காக P-305 தனிமைப்படுத்தல் நீக்கப்பட்டது (இயக்கம்).", "13:50 — 10 मिनट के टेस्ट रन के लिए P-305 का आइसोलेशन हटाया गया (ऑप्स)।"),
                   T("14:10 — test complete. Re-isolation: no entry.", "14:10 — சோதனை முடிந்தது. மீண்டும் தனிமைப்படுத்தல்: பதிவு இல்லை.", "14:10 — टेस्ट पूरा। पुनः आइसोलेशन: कोई प्रविष्टि नहीं।")])
    m.obj("iso_record", "permit_box", 5.2, -2.6, panel="document", doc_kind="record", prompt="read", kind="document",
          title=T("ISOLATION RECORD", "தனிமைப்படுத்தல் பதிவு", "आइसोलेशन रिकॉर्ड"),
          name=T("Isolation record IR-305 (fictional)", "தனிமைப்படுத்தல் பதிவு IR-305 (கற்பனை)", "आइसोलेशन रिकॉर्ड IR-305 (काल्पनिक)"),
          details=[T("Record for P-305 bearing inspection.", "P-305 பேரிங் ஆய்வுக்கான பதிவு.", "P-305 बेयरिंग निरीक्षण का रिकॉर्ड।")])
    m.evidence("ev_equipment", T("Equipment", "உபகரணம்", "उपकरण"), T("P-305 cooling water pump", "P-305 குளிர்நீர் பம்ப்", "P-305 कूलिंग वॉटर पंप"), True, doc="iso_record")
    m.evidence("ev_status", T("Isolation status", "தனிமைப்படுத்தல் நிலை", "आइसोलेशन स्थिति"), T("CANCELLED 13:50 for test run — not re-entered", "சோதனை ஓட்டத்திற்காக 13:50-க்கு ரத்து — மீண்டும் பதியப்படவில்லை", "टेस्ट रन हेतु 13:50 पर रद्द — दोबारा दर्ज नहीं"), False, doc="iso_record")
    m.evidence("ev_planner", T("Planned by", "திட்டமிட்டவர்", "योजनाकार"), T("Maintenance planning", "பராமரிப்புத் திட்டமிடல்", "मेंटेनेंस प्लानिंग"), True, doc="iso_record")
    m.obj("radio_point", "phone", 5.6, 4.5, -90, panel="comms", prompt="use", kind="communication", groups=["report"],
          name=T("Site radio point", "தள வானொலிப் புள்ளி", "साइट रेडियो पॉइंट"),
          details=[T("Channel 2 — Control room (Farah Khan).", "சேனல் 2 — கட்டுப்பாட்டு அறை (ஃபரா கான்).", "चैनल 2 — कंट्रोल रूम (फ़रा ख़ान)।")])
    m.obj("job_board", "stand", 0.0, -3.5, panel="station", prompt="review", kind="station", groups=["final"],
          title=T("BEARING JOB", "பேரிங் வேலை", "बेयरिंग कार्य"),
          name=T("Bearing job board", "பேரிங் வேலைப் பலகை", "बेयरिंग कार्य बोर्ड"),
          details=[T("Record your decision on the bearing inspection.", "பேரிங் ஆய்வு குறித்த உங்கள் முடிவைப் பதிவுசெய்யுங்கள்.", "बेयरिंग निरीक्षण पर अपना निर्णय दर्ज करें।")])
    m.group("report", T("What do you report to the control room?", "கட்டுப்பாட்டு அறைக்கு என்ன தெரிவிப்பீர்கள்?", "आप कंट्रोल रूम को क्या बताएँगे?"), [
        ("mismatch", T("Report: display says isolated, record says cancelled — please confirm", "தெரிவிக்கவும்: திரை தனிமைப்படுத்தப்பட்டது என்கிறது, பதிவு ரத்து என்கிறது — உறுதிப்படுத்துங்கள்", "बताएँ: डिस्प्ले आइसोलेटेड कहता है, रिकॉर्ड रद्द कहता है — कृपया पुष्टि करें"),
         T("Describe both sources and ask for confirmation.", "இரு மூலங்களையும் விவரித்து உறுதிப்படுத்தல் கேளுங்கள்.", "दोनों स्रोत बताकर पुष्टि माँगें।")),
        ("ready", T("Report: display shows isolated, so the crew can start", "தெரிவிக்கவும்: திரை தனிமைப்படுத்தப்பட்டது எனக் காட்டுவதால் குழு தொடங்கலாம்", "बताएँ: डिस्प्ले आइसोलेटेड दिखाता है, तो टीम शुरू कर सकती है"),
         T("Trust the green light.", "பச்சை விளக்கை நம்புங்கள்.", "हरी बत्ती पर भरोसा करें।")),
        ("later", T("Say nothing now — sort the record out after the inspection", "இப்போது எதுவும் சொல்ல வேண்டாம் — ஆய்வுக்குப் பின் பதிவைச் சரிசெய்யலாம்", "अभी कुछ न कहें — निरीक्षण के बाद रिकॉर्ड ठीक करें"),
         T("Leave the paperwork for later.", "ஆவணங்களைப் பின்னர் பார்க்கலாம்.", "कागज़ात बाद के लिए छोड़ें।")),
    ], ui="comms")
    m.group("final", T("What happens to the bearing inspection?", "பேரிங் ஆய்வுக்கு என்ன நடக்கும்?", "बेयरिंग निरीक्षण का क्या होगा?"), [
        ("hold", T("Hold the job until the isolation is redone and verified", "தனிமைப்படுத்தல் மீண்டும் செய்யப்பட்டு சரிபார்க்கப்படும் வரை வேலையை நிறுத்தி வையுங்கள்", "आइसोलेशन दोबारा होकर सत्यापित होने तक काम रोकें")),
        ("proceed", T("Proceed — the display says isolated", "தொடரவும் — திரை தனிமைப்படுத்தப்பட்டது என்கிறது", "आगे बढ़ें — डिस्प्ले आइसोलेटेड कहता है")),
    ])
    m.tools("flashlight", "spanner", "radio", flashlight=["pump_p305", "display_p305"])

    meet = m.meet("operator")
    m.briefing(meet)
    m.step("enter", title=T("Go to the P-305 pump house", "P-305 பம்ப் இல்லத்திற்குச் செல்லுங்கள்", "P-305 पंप हाउस जाएँ"),
           instruction=T("Walk to the yellow-bordered pump house area.", "மஞ்சள் எல்லையிட்ட பம்ப் இல்லப் பகுதிக்குச் செல்லுங்கள்.", "पीली सीमा वाले पंप हाउस क्षेत्र में जाएँ।"),
           trigger=enter("zone_pumphouse"), requires=["briefing"], points=5, concept="situational_awareness", scene="navigate", marker="zone_pumphouse",
           hints=[T("The pump house is straight ahead, north of the job board.", "பம்ப் இல்லம் நேரே முன்னால், வேலைப் பலகைக்கு வடக்கே உள்ளது.", "पंप हाउस सीधे आगे, कार्य बोर्ड के उत्तर में है।")])
    m.step("check_pump", title=T("Identify P-305", "P-305-ஐ அடையாளம் காணுங்கள்", "P-305 की पहचान करें"),
           instruction=T("Find the pump tagged P-305 and inspect it.", "P-305 எனக் குறியிடப்பட்ட பம்பைக் கண்டு ஆய்வு செய்யுங்கள்.", "P-305 टैग वाला पंप खोजकर निरीक्षण करें।"),
           trigger=inspect("pump_p305"), requires=["enter"], points=5, concept="equipment_identification", scene="identify", marker="pump_p305",
           hints=[T("P-306 is running; P-305 is the stopped one.", "P-306 இயங்குகிறது; P-305 நிறுத்தப்பட்டது.", "P-306 चल रहा है; P-305 बंद वाला है।")])
    m.step("read_display", title=T("Read the local status display", "உள்ளூர் நிலைத் திரையைப் படியுங்கள்", "स्थानीय स्टेटस डिस्प्ले पढ़ें"),
           instruction=T("Read everything on the display, including the small print.", "சிறிய எழுத்துகள் உட்பட திரையில் உள்ள அனைத்தையும் படியுங்கள்.", "डिस्प्ले पर सब कुछ पढ़ें, छोटे अक्षर भी।"),
           trigger=inspect("display_p305"), requires=["check_pump"], points=10, concept="status_documentation_mismatch", scene="inspect", marker="display_p305",
           hints=[T("Look at the time of the last update and the beacon colour.", "கடைசிப் புதுப்பிப்பு நேரத்தையும் விளக்கின் நிறத்தையும் பாருங்கள்.", "अंतिम अपडेट का समय और बीकन का रंग देखें।")])
    m.step("read_log", title=T("Check the shift handover log", "பணிமாற்றப் பதிவேட்டைச் சரிபாருங்கள்", "शिफ्ट हैंडओवर लॉग जाँचें"),
           instruction=T("Read the log at the shift desk.", "பணிமாற்ற மேசையில் உள்ள பதிவேட்டைப் படியுங்கள்.", "शिफ्ट डेस्क पर लॉग पढ़ें।"),
           trigger=inspect("handover_desk"), requires=["check_pump"], points=10, concept="documented_evidence", scene="documents", marker="handover_desk",
           hints=[T("What happened to P-305 this afternoon?", "இன்று மதியம் P-305-க்கு என்ன நடந்தது?", "आज दोपहर P-305 के साथ क्या हुआ?")])
    m.step("open_record", title=T("Open the isolation record", "தனிமைப்படுத்தல் பதிவைத் திறவுங்கள்", "आइसोलेशन रिकॉर्ड खोलें"),
           instruction=T("Read isolation record IR-305 in the display case.", "காட்சிப்பெட்டியில் உள்ள தனிமைப்படுத்தல் பதிவு IR-305-ஐப் படியுங்கள்.", "डिस्प्ले केस में आइसोलेशन रिकॉर्ड IR-305 पढ़ें।"),
           trigger=inspect("iso_record"), requires=["read_display", "read_log"], points=5, concept="documented_evidence", scene="documents", marker="iso_record",
           hints=[T("The record is in the glass case south-east of the pump.", "பதிவு பம்பிற்குத் தென்கிழக்கே உள்ள கண்ணாடிப் பெட்டியில் உள்ளது.", "रिकॉर्ड पंप के दक्षिण-पूर्व में काँच के केस में है।")])
    m.step("flag_status", title=T("Flag the inconsistent entry", "முரண்பட்ட பதிவைக் குறியுங்கள்", "असंगत प्रविष्टि चिह्नित करें"),
           instruction=T("Flag the record entry that contradicts the display.", "திரைக்கு முரணான பதிவை குறியுங்கள்.", "डिस्प्ले से विरोधाभासी प्रविष्टि चिह्नित करें।"),
           trigger=flag("ev_status"), requires=["open_record"], points=15, concept="status_documentation_mismatch", scene="evidence", marker="iso_record",
           hints=[T("The display says one thing about isolation; which field says the opposite?", "தனிமைப்படுத்தல் குறித்து திரை ஒன்று சொல்கிறது; எந்தப் புலம் எதிர்மாறாகச் சொல்கிறது?", "आइसोलेशन पर डिस्प्ले एक बात कहता है; कौन सा फ़ील्ड उल्टा कहता है?")])
    m.step("report", title=T("Report it to the control room", "கட்டுப்பாட்டு அறைக்குத் தெரிவியுங்கள்", "कंट्रोल रूम को रिपोर्ट करें"),
           instruction=T("Use the site radio point and choose what to report.", "தள வானொலிப் புள்ளியைப் பயன்படுத்தி என்ன தெரிவிப்பது என்று தேர்வுசெய்யுங்கள்.", "साइट रेडियो पॉइंट से चुनें कि क्या रिपोर्ट करना है।"),
           trigger=decide("report", "mismatch"), requires=["flag_status"], points=15, concept="escalation", scene="communicate", marker="radio_point",
           mistake_if_early=T("Check the record before you report — you need facts, not guesses.", "தெரிவிக்கும் முன் பதிவைச் சரிபாருங்கள் — ஊகங்கள் அல்ல, உண்மைகள் தேவை.", "रिपोर्ट से पहले रिकॉर्ड जाँचें — अनुमान नहीं, तथ्य चाहिए।"),
           hints=[T("Report both sources and ask the control room to confirm.", "இரு மூலங்களையும் தெரிவித்து கட்டுப்பாட்டு அறையை உறுதிப்படுத்தக் கேளுங்கள்.", "दोनों स्रोत बताएँ और कंट्रोल रूम से पुष्टि माँगें।")])
    m.step("decide", title=T("Decide on the bearing job", "பேரிங் வேலை குறித்து முடிவு செய்யுங்கள்", "बेयरिंग कार्य पर निर्णय लें"),
           instruction=T("Record the decision on the job board.", "வேலைப் பலகையில் முடிவைப் பதிவுசெய்யுங்கள்.", "कार्य बोर्ड पर निर्णय दर्ज करें।"),
           trigger=decide("final", "hold"), requires=["report"], points=20, concept="stop_work_authority", scene="decision", marker="job_board",
           mistake_if_early=T("Report the inconsistency before deciding on the job.", "வேலை குறித்து முடிவெடுக்கும் முன் முரண்பாட்டைத் தெரிவியுங்கள்.", "काम पर निर्णय से पहले असंगति रिपोर्ट करें।"),
           hints=[T("Can the crew safely start while the isolation is unverified?", "தனிமைப்படுத்தல் சரிபார்க்கப்படாத நிலையில் குழு பாதுகாப்பாகத் தொடங்க முடியுமா?", "आइसोलेशन असत्यापित रहते हुए क्या टीम सुरक्षित शुरू कर सकती है?")])
    m.event("display_fault", {"completed": ["report"]}, [
        {"type": "sound", "sound": "radio"},
        {"type": "dialogue", "name": "radio_ack"},
        {"type": "prop_state", "prop": "display_p305", "state": "fault"},
        {"type": "details", "object": "display_p305", "details": [T("Display now reads: 'ISOLATION: NOT VERIFIED' (red).", "திரை இப்போது: 'தனிமைப்படுத்தல்: சரிபார்க்கப்படவில்லை' (சிவப்பு).", "डिस्प्ले अब: 'आइसोलेशन: सत्यापित नहीं' (लाल)।")]},
    ])

    m.critical("ready_on_display", trigger=decide("report", "ready"), concept="status_documentation_mismatch", dialogue="unsafe",
               explanation=T("You reported the pump as ready based only on a display that had not updated since 09:12.", "09:12 முதல் புதுப்பிக்கப்படாத திரையை மட்டும் வைத்து பம்ப் தயார் என்று தெரிவித்தீர்கள்.", "आपने केवल 09:12 से अपडेट न हुए डिस्प्ले के आधार पर पंप को तैयार बताया।"),
               missing=T("A verified isolation, confirmed against the isolation record.", "தனிமைப்படுத்தல் பதிவுடன் உறுதிப்படுத்தப்பட்ட, சரிபார்க்கப்பட்ட தனிமைப்படுத்தல்.", "आइसोलेशन रिकॉर्ड से पुष्ट, सत्यापित आइसोलेशन।"))
    m.critical("proceed_job", trigger=decide("final", "proceed"), concept="stop_work_authority", dialogue="unsafe",
               explanation=T("You let the job proceed while the isolation status was contradicted by the record.", "தனிமைப்படுத்தல் நிலை பதிவால் முரண்பட்ட நிலையிலும் வேலையைத் தொடர அனுமதித்தீர்கள்.", "रिकॉर्ड के विरोधाभास के बावजूद आपने काम आगे बढ़ने दिया।"),
               missing=T("Re-isolation and verification by the authorised person before work.", "வேலைக்கு முன் அதிகாரம் பெற்றவரால் மீண்டும் தனிமைப்படுத்தலும் சரிபார்ப்பும்.", "काम से पहले अधिकृत व्यक्ति द्वारा पुनः आइसोलेशन और सत्यापन।"))
    m.critical("tool_on_pump", trigger=tool("spanner", "pump_p305"), concept="stop_work_authority", dialogue="unsafe", condition=not_done("decide"),
               explanation=T("You started work on P-305 while its isolation was unverified.", "P-305-இன் தனிமைப்படுத்தல் சரிபார்க்கப்படாத நிலையில் அதில் வேலை தொடங்கினீர்கள்.", "P-305 का आइसोलेशन असत्यापित रहते आपने उस पर काम शुरू किया।"),
               missing=T("Verified isolation and authorisation.", "சரிபார்க்கப்பட்ட தனிமைப்படுத்தலும் அனுமதியும்.", "सत्यापित आइसोलेशन और अनुमति।"))
    m.mistake("report_later", trigger=decide("report", "later"), kind="incorrect_decision", concept="escalation",
              feedback=T("Leaving it until later means the crew may start on wrong information. Report it now.", "பின்னர் பார்க்கலாம் என்றால் குழு தவறான தகவலில் தொடங்கக்கூடும். இப்போதே தெரிவியுங்கள்.", "बाद में छोड़ने का मतलब है टीम गलत जानकारी पर शुरू कर सकती है। अभी रिपोर्ट करें।"))
    m.mistake("wrong_flag", trigger=any_flag(), kind="incorrect_decision", concept="documented_evidence",
              feedback=T("That entry is correct. Find the one that contradicts the display.", "அந்தப் பதிவு சரியானது. திரைக்கு முரணானதைக் கண்டறியுங்கள்.", "वह प्रविष्टि सही है। डिस्प्ले से विरोधाभासी प्रविष्टि खोजें।"))

    m.debrief(
        success=T("You treated the green light as a claim, checked it against the record and held the job.", "பச்சை விளக்கை ஒரு கூற்றாகக் கருதி, பதிவுடன் சரிபார்த்து வேலையை நிறுத்தி வைத்தீர்கள்.", "आपने हरी बत्ती को एक दावा माना, रिकॉर्ड से जाँचा और काम रोका।"),
        critical=T("A display was trusted over the record. Next time, let disagreement hold the job.", "பதிவை விட திரை நம்பப்பட்டது. அடுத்த முறை, முரண்பாடு வேலையை நிறுத்தட்டும்.", "रिकॉर्ड के बजाय डिस्प्ले पर भरोसा किया गया। अगली बार असहमति को काम रोकने दें।"),
        failed=T("Repeated unsafe calls ended the attempt. Compare every source before deciding.", "தொடர்ந்த பாதுகாப்பற்ற முடிவுகளால் முயற்சி முடிந்தது. முடிவெடுக்கும் முன் ஒவ்வொரு மூலத்தையும் ஒப்பிடுங்கள்.", "बार-बार असुरक्षित निर्णयों से प्रयास समाप्त हुआ। निर्णय से पहले हर स्रोत की तुलना करें।"),
        lines=[
            ({"criticalRule": "ready_on_display"}, T("You reported 'ready' on the strength of a stale display.", "பழைய திரைத் தகவலை வைத்து 'தயார்' என்று தெரிவித்தீர்கள்.", "आपने पुराने डिस्प्ले के आधार पर 'तैयार' बताया।")),
            ({"criticalRule": "proceed_job"}, T("You allowed the job to proceed with the isolation unverified.", "தனிமைப்படுத்தல் சரிபார்க்கப்படாமல் வேலை தொடர அனுமதித்தீர்கள்.", "आपने असत्यापित आइसोलेशन के साथ काम आगे बढ़ने दिया।")),
            ({"stepCompleted": "read_display"}, T("You noticed the display had not updated since 09:12.", "திரை 09:12 முதல் புதுப்பிக்கப்படவில்லை என்பதைக் கவனித்தீர்கள்.", "आपने देखा कि डिस्प्ले 09:12 से अपडेट नहीं हुआ।")),
            ({"stepCompleted": "flag_status"}, T("You found the cancelled isolation in the record.", "பதிவில் ரத்தான தனிமைப்படுத்தலைக் கண்டுபிடித்தீர்கள்.", "आपने रिकॉर्ड में रद्द आइसोलेशन खोजा।")),
            ({"counterAbove": ["incorrectDecisions", 0]}, T("At least one choice delayed or confused the report.", "குறைந்தது ஒரு தேர்வு அறிக்கையைத் தாமதப்படுத்தியது அல்லது குழப்பியது.", "कम से कम एक विकल्प ने रिपोर्ट में देरी या भ्रम पैदा किया।")),
            ({"stepCompleted": "decide"}, T("You held the job until the isolation is redone — correct.", "தனிமைப்படுத்தல் மீண்டும் செய்யப்படும் வரை வேலையை நிறுத்தி வைத்தீர்கள் — சரி.", "आपने आइसोलेशन दोबारा होने तक काम रोका — सही।")),
        ],
    )
    m.comic(T("A LIGHT IS NOT PROOF", "விளக்கு ஆதாரம் அல்ல", "बत्ती प्रमाण नहीं"), [
        ("gauge", T("A display shows what it was last told — not always what is true now.", "ஒரு திரை கடைசியாகச் சொல்லப்பட்டதைக் காட்டுகிறது — இப்போதைய உண்மையை எப்போதும் அல்ல.", "डिस्प्ले वही दिखाता है जो उसे आख़िरी बार बताया गया — हमेशा अभी का सच नहीं।")),
        ("document_gap", T("Compare it with the record and the log.", "பதிவுடனும் பதிவேட்டுடனும் ஒப்பிடுங்கள்.", "इसे रिकॉर्ड और लॉग से मिलाएँ।")),
        ("radio", T("Report the mismatch and hold the job.", "முரண்பாட்டைத் தெரிவித்து வேலையை நிறுத்தி வையுங்கள்.", "असंगति रिपोर्ट करें और काम रोकें।")),
    ])
    m.report(["check_pump", "read_display", "read_log", "open_record", "flag_status"], ["report", "decide"])
    m.mcq(1, concept="status_documentation_mismatch",
          stem=T("A status display shows 'ISOLATED' but the record says the isolation was cancelled. What is true?", "ஒரு நிலைத் திரை 'தனிமைப்படுத்தப்பட்டது' எனக் காட்டுகிறது, ஆனால் பதிவு ரத்து என்கிறது. எது உண்மை?", "स्टेटस डिस्प्ले 'आइसोलेटेड' दिखाता है पर रिकॉर्ड कहता है आइसोलेशन रद्द हुआ। क्या सच है?"),
          options=[T("The display wins because it is electronic", "மின்னணு என்பதால் திரையே சரி", "डिस्प्ले सही है क्योंकि वह इलेक्ट्रॉनिक है"),
                   T("The status is unverified until the conflict is resolved", "முரண்பாடு தீரும் வரை நிலை சரிபார்க்கப்படாதது", "विरोधाभास सुलझने तक स्थिति असत्यापित है"),
                   T("The record wins because it is on paper", "காகிதத்தில் உள்ளதால் பதிவே சரி", "रिकॉर्ड सही है क्योंकि वह कागज़ पर है")],
          correct="b", explanation=T("Neither source alone proves the condition; the conflict itself means stop and confirm.", "எந்த மூலமும் தனியாக நிலையை நிரூபிக்காது; முரண்பாடே நிறுத்தி உறுதிப்படுத்த வேண்டும் என்பதைக் குறிக்கிறது.", "कोई भी स्रोत अकेले स्थिति सिद्ध नहीं करता; विरोधाभास का मतलब ही है रुकें और पुष्टि करें।"))
    m.mcq(2, concept="escalation",
          stem=T("Who should you tell about the mismatch?", "முரண்பாட்டை யாரிடம் தெரிவிக்க வேண்டும்?", "असंगति के बारे में किसे बताना चाहिए?"),
          options=[T("The control room or person responsible for the equipment status", "உபகரண நிலைக்குப் பொறுப்பான கட்டுப்பாட்டு அறை அல்லது நபர்", "उपकरण की स्थिति के लिए ज़िम्मेदार कंट्रोल रूम या व्यक्ति"),
                   T("Nobody, if you decide not to start", "நீங்கள் தொடங்கவில்லை என்றால் யாரிடமும் வேண்டாம்", "किसी को नहीं, अगर आप शुरू न करें"),
                   T("Only your friends on the crew", "குழுவில் உள்ள உங்கள் நண்பர்களிடம் மட்டும்", "केवल टीम के अपने दोस्तों को")],
          correct="a", explanation=T("Others may rely on the same wrong display; the responsible party must know.", "மற்றவர்களும் அதே தவறான திரையை நம்பக்கூடும்; பொறுப்பானவர் அறிய வேண்டும்.", "दूसरे भी उसी गलत डिस्प्ले पर भरोसा कर सकते हैं; ज़िम्मेदार व्यक्ति को पता होना चाहिए।"))
    m.mcq(3, concept="documented_evidence",
          stem=T("Which detail on the display should have made you suspicious?", "திரையில் உள்ள எந்த விவரம் உங்களைச் சந்தேகப்பட வைத்திருக்க வேண்டும்?", "डिस्प्ले का कौन सा विवरण आपको संदेह में डालना चाहिए था?"),
          options=[T("The pump tag number", "பம்ப் குறி எண்", "पंप टैग नंबर"),
                   T("The last-update time and the amber beacon", "கடைசிப் புதுப்பிப்பு நேரமும் ஆம்பர் விளக்கும்", "अंतिम अपडेट समय और एम्बर बीकन"),
                   T("The colour of the cabinet", "பெட்டியின் நிறம்", "कैबिनेट का रंग")],
          correct="b", explanation=T("An old update time and a warning beacon both hinted the display was out of date.", "பழைய புதுப்பிப்பு நேரமும் எச்சரிக்கை விளக்கும் திரை காலாவதியானது என்பதைக் குறிப்பால் காட்டின.", "पुराना अपडेट समय और चेतावनी बीकन, दोनों संकेत देते थे कि डिस्प्ले पुराना है।"))
    m.mcq(4, concept="stop_work_authority",
          stem=T("After reporting, what should happen to the bearing job?", "தெரிவித்த பிறகு, பேரிங் வேலைக்கு என்ன நடக்க வேண்டும்?", "रिपोर्ट करने के बाद बेयरिंग कार्य का क्या होना चाहिए?"),
          options=[T("Start on the parts that do not rotate", "சுழலாத பாகங்களில் தொடங்கலாம்", "न घूमने वाले हिस्सों पर शुरू करें"),
                   T("Continue if the control room is busy", "கட்டுப்பாட்டு அறை பரபரப்பாக இருந்தால் தொடரலாம்", "कंट्रोल रूम व्यस्त हो तो जारी रखें"),
                   T("Hold until the isolation is redone and verified", "தனிமைப்படுத்தல் மீண்டும் செய்யப்பட்டு சரிபார்க்கப்படும் வரை நிறுத்தி வைக்கவும்", "आइसोलेशन दोबारा होकर सत्यापित होने तक रोकें")],
          correct="c", explanation=T("Reporting is not enough on its own; the job waits for a verified condition.", "தெரிவிப்பது மட்டும் போதாது; சரிபார்க்கப்பட்ட நிலைக்காக வேலை காத்திருக்கும்.", "केवल रिपोर्ट करना काफ़ी नहीं; काम सत्यापित स्थिति की प्रतीक्षा करता है।"))
    m.spec(
        workplaceLocation="Fictional cooling water pump house.",
        equipmentType="Pump P-305 with local status display; neighbouring pump P-306 running.",
        corePrinciple="A display is one source; disagreement between sources means report and hold.",
        commonMisconceptions=["A green light proves isolation.", "Paperwork can be fixed after the job."],
        criticalDecisions=["Report 'ready' from the display", "Let the job proceed", "Start work with a tool"],
        assessmentCriteria={"correct": "Read display, log and record; flag the cancelled isolation; report the mismatch; hold the job."},
        assumptions=["No real procedure or numeric threshold is taught."],
    )
    return m
