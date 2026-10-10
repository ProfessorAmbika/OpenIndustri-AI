"""Hazard Recognition · Level 2 — The Warning Behind the Pipes.

Story: Senior Technician Joseph Raj asks the trainee to get ready for a gasket
change on flange F-12 (line 210). The work order says the line is drained, but
in the congested spool area the relevant warnings are out of sight: a tag on
valve XV-210 behind the pipework and a sign behind the exchanger. Learning:
hazard information is not always where you first look; conflicting
information is reported, never resolved by assumption or by removing a tag.
"""
from authoring.dsl import Mission, T, any_flag, decide, enter, flag, inspect, not_done, tool


def build() -> Mission:
    m = Mission(
        code="hr2", id="og-hazrec-l2-warning-behind-pipes", category="og_hazard_recognition", level=2, minutes=12,
        title=T("The Warning Behind the Pipes", "குழாய்களுக்குப் பின்னால் உள்ள எச்சரிக்கை", "पाइपों के पीछे की चेतावनी"),
        subtitle=T("Find the warnings a crowded workstation hides", "நெரிசலான பணியிடம் மறைக்கும் எச்சரிக்கைகளைக் கண்டறியுங்கள்", "भीड़भाड़ वाले कार्यस्थल में छिपी चेतावनियाँ खोजें"),
        description=T(
            "A gasket job looks routine — until you look behind the pipework.",
            "ஒரு கேஸ்கெட் வேலை சாதாரணமாகத் தெரிகிறது — குழாய்களுக்குப் பின்னால் பார்க்கும் வரை.",
            "गैसकेट का काम सामान्य लगता है — जब तक आप पाइपों के पीछे नहीं देखते।",
        ),
        location=T("Spool area, line 210 · Process unit", "ஸ்பூல் பகுதி, வரி 210 · செயல்முறைப் பிரிவு", "स्पूल क्षेत्र, लाइन 210 · प्रोसेस यूनिट"),
        site="process", spawn=(0, -23, 0), work_point=(0, -3.5, 0),
    )
    m.brief(
        lines=[
            T("Joseph needs flange F-12 on line 210 prepared for a gasket change.", "வரி 210-இல் உள்ள F-12 ஃபிளேஞ்சை கேஸ்கெட் மாற்றத்திற்குத் தயார் செய்ய ஜோசப் விரும்புகிறார்.", "जोसेफ चाहते हैं कि लाइन 210 का फ्लेंज F-12 गैसकेट बदलने के लिए तैयार हो।"),
            T("The spool area is crowded. Not every warning is visible from the walkway.", "ஸ்பூல் பகுதி நெரிசலாக உள்ளது. எல்லா எச்சரிக்கைகளும் நடைபாதையிலிருந்து தெரிவதில்லை.", "स्पूल क्षेत्र भीड़भाड़ वाला है। हर चेतावनी रास्ते से दिखाई नहीं देती।"),
        ],
        task=T("Check the area around flange F-12 before any work starts.", "எந்த வேலையும் தொடங்கும் முன் F-12 ஃபிளேஞ்சைச் சுற்றியுள்ள பகுதியைச் சரிபாருங்கள்.", "कोई भी काम शुरू होने से पहले फ्लेंज F-12 के आसपास का क्षेत्र जाँचें।"),
        equipment=T("Line 210, flange F-12, valve XV-210 (fictional).", "வரி 210, ஃபிளேஞ்ச் F-12, வால்வு XV-210 (கற்பனை).", "लाइन 210, फ्लेंज F-12, वाल्व XV-210 (काल्पनिक)।"),
        objective=T("Find all hazard information around the job and decide whether work can start.", "வேலையைச் சுற்றியுள்ள எல்லா அபாயத் தகவல்களையும் கண்டறிந்து, வேலை தொடங்கலாமா என்று முடிவு செய்யுங்கள்.", "काम के आसपास की सारी खतरा जानकारी खोजें और तय करें कि काम शुरू हो सकता है या नहीं।"),
        information=T("Work order WO-3107 states the line is drained. Walk around the equipment.", "பணி ஆணை WO-3107 வரி வடிகட்டப்பட்டதாகக் கூறுகிறது. உபகரணத்தைச் சுற்றி நடந்து பாருங்கள்.", "वर्क ऑर्डर WO-3107 कहता है कि लाइन खाली है। उपकरण के चारों ओर चलकर देखें।"),
        objectives=[
            T("Look for hazard information that is out of sight from the walkway.", "நடைபாதையிலிருந்து தெரியாத அபாயத் தகவலைத் தேடுங்கள்.", "रास्ते से न दिखने वाली खतरा जानकारी खोजें।"),
            T("Report conflicting information instead of resolving it by assumption.", "முரண்பட்ட தகவலை ஊகத்தால் தீர்க்காமல் புகாரளியுங்கள்.", "विरोधी जानकारी को अनुमान से सुलझाने के बजाय रिपोर्ट करें।"),
        ],
    )

    # ------------------------------------------------------------------ people & dialogue
    m.dialogue("meet", [
        ("senior_tech", "friendly", T("Morning! You're with me today. Gasket change on F-12, line 210.", "காலை வணக்கம்! இன்று நீங்கள் என்னுடன். வரி 210, F-12-இல் கேஸ்கெட் மாற்றம்.", "सुप्रभात! आज आप मेरे साथ हैं। लाइन 210 के F-12 पर गैसकेट बदलना है।")),
        ("senior_tech", "neutral", T("The work order says the line's drained. Easy job, on paper.", "பணி ஆணையில் வரி வடிகட்டப்பட்டது என்று உள்ளது. காகிதத்தில் எளிதான வேலை.", "वर्क ऑर्डर में लिखा है कि लाइन खाली है। कागज़ पर आसान काम।")),
        ("senior_tech", "serious", T("But that spool area is a jungle of pipes. Walk all the way round before you trust anything.", "ஆனால் அந்த ஸ்பூல் பகுதி குழாய்களின் காடு. எதையும் நம்பும் முன் முழுவதும் சுற்றிப் பாருங்கள்.", "लेकिन वह स्पूल क्षेत्र पाइपों का जंगल है। किसी बात पर भरोसा करने से पहले पूरा चक्कर लगाइए।")),
        ("self", "neutral", T("Paper says drained. Let's see what the plant says.", "காகிதம் வடிகட்டப்பட்டது என்கிறது. ஆலை என்ன சொல்கிறது என்று பார்ப்போம்.", "कागज़ कहता है खाली है। देखते हैं प्लांट क्या कहता है।")),
    ])
    m.dialogue("revisit", [
        ("senior_tech", "neutral", T("Found anything behind those pipes yet? Tags hide in the strangest places.", "அந்தக் குழாய்களுக்குப் பின்னால் ஏதாவது கிடைத்ததா? குறிச்சீட்டுகள் விசித்திரமான இடங்களில் ஒளிந்திருக்கும்.", "उन पाइपों के पीछे कुछ मिला? टैग अजीब जगहों पर छिपे होते हैं।")),
    ])
    m.dialogue("unsafe", [
        ("senior_tech", "concerned", T("Hold it! Two pieces of information disagree and you picked the convenient one.", "நிறுத்துங்கள்! இரண்டு தகவல்கள் முரண்படுகின்றன, நீங்கள் வசதியானதைத் தேர்ந்தெடுத்தீர்கள்.", "रुकिए! दो जानकारियाँ आपस में मेल नहीं खातीं और आपने सुविधाजनक वाली चुन ली।")),
        ("senior_tech", "serious", T("When the plant and the paperwork disagree, we stop and ask. Every time.", "ஆலையும் ஆவணங்களும் முரண்படும்போது, நாம் நிறுத்தி கேட்கிறோம். ஒவ்வொரு முறையும்.", "जब प्लांट और कागज़ात मेल न खाएँ, हम रुकते हैं और पूछते हैं। हर बार।")),
    ])
    m.dialogue("correct", [
        ("senior_tech", "pleased", T("Good catch. I'll call the area authority — that tag says the line is live, whatever the work order thinks.", "நல்ல கண்டுபிடிப்பு. பகுதி அதிகாரியை அழைக்கிறேன் — பணி ஆணை என்ன சொன்னாலும், அந்தக் குறிச்சீட்டு வரி இயக்கத்தில் உள்ளது என்கிறது.", "बढ़िया पकड़। मैं क्षेत्र प्राधिकारी को बुलाता हूँ — वर्क ऑर्डर कुछ भी कहे, वह टैग कहता है कि लाइन चालू है।")),
    ])
    m.npc("senior_tech", -2.5, -12, 180, talk=[("meet", not_done("meet_senior_tech")), ("revisit", None)])

    # ------------------------------------------------------------------ world
    m.zone("zone_spool", T("Spool area — line 210", "ஸ்பூல் பகுதி — வரி 210", "स्पूल क्षेत्र — लाइन 210"), (-7, 7, -2, 9))
    m.zone("zone_live", T("Live process area", "இயக்கத்திலுள்ள செயல்முறைப் பகுதி", "चालू प्रोसेस क्षेत्र"), (9, 14, 0, 7), restricted=True)
    m.decor("tape", 11.5, 3.5, w=5, d=7)
    m.decor("sign", 8.6, 1.0, heading=90, kind="prohibition", text="world.sign.authorisedOnly")
    m.decor("exchanger", 3.2, 5.0, heading=0)
    m.decor("pipe", -1.0, 1.0, len=7, y=1.3, d=0.32, color="#8a96a8")
    m.decor("pipe", -1.0, 1.0, len=7, y=2.4, d=0.24, color="#1f6f8b")
    m.decor("pipe", -3.0, 7.6, heading=90, len=4, y=1.0, d=0.28, color="#ffc23d")
    m.decor("compressor", -1.0, 12.0, tag="K-210")
    m.decor("drum", 6.0, -1.5, count=2)
    m.decor("scaffold", -5.5, 3.0, heading=90)

    m.obj("flange_f12", "leak", -1.0, 3.6, 0, state="off",
          name=T("Flange F-12 (line 210)", "ஃபிளேஞ்ச் F-12 (வரி 210)", "फ्लेंज F-12 (लाइन 210)"),
          details=[
              T("Bolted flange on line 210 — the job location in work order WO-3107.", "வரி 210-இல் போல்ட் செய்யப்பட்ட ஃபிளேஞ்ச் — பணி ஆணை WO-3107-இல் உள்ள வேலை இடம்.", "लाइन 210 पर बोल्ट किया फ्लेंज — वर्क ऑर्डर WO-3107 में दिया कार्य स्थल।"),
              T("From the walkway, no tag or sign is visible on this flange.", "நடைபாதையிலிருந்து இந்த ஃபிளேஞ்சில் எந்தக் குறிச்சீட்டோ அடையாளமோ தெரியவில்லை.", "रास्ते से इस फ्लेंज पर कोई टैग या संकेत नहीं दिखता।"),
          ])
    m.obj("flange_f11", "leak", -1.0, 6.6, 0, state="off",
          name=T("Flange F-11 (line 211)", "ஃபிளேஞ்ச் F-11 (வரி 211)", "फ्लेंज F-11 (लाइन 211)"),
          details=[T("Flange on the neighbouring line 211. Not part of this job.", "அருகிலுள்ள வரி 211-இன் ஃபிளேஞ்ச். இந்த வேலையின் பகுதி அல்ல.", "पड़ोसी लाइन 211 का फ्लेंज। इस काम का हिस्सा नहीं।")])
    m.obj("valve_xv210", "valve", -5.6, 6.2, -90, state="tagged", tag="XV-210",
          name=T("Valve XV-210 (behind the pipework)", "வால்வு XV-210 (குழாய்களுக்குப் பின்னால்)", "वाल्व XV-210 (पाइपों के पीछे)"),
          details=[
              T("A tag hangs on the handwheel: 'LINE 210 IN SERVICE — DO NOT OPEN'. Dated today, 05:30.", "கைச்சக்கரத்தில் ஒரு குறிச்சீட்டு: 'வரி 210 இயக்கத்தில் — திறக்க வேண்டாம்'. இன்றைய தேதி, 05:30.", "हैंडव्हील पर एक टैग: 'लाइन 210 सेवा में — न खोलें'। आज की तारीख, 05:30।"),
              T("This tag is only visible from the west side of the spool area.", "இந்தக் குறிச்சீட்டு ஸ்பூல் பகுதியின் மேற்குப் பக்கத்திலிருந்து மட்டுமே தெரியும்.", "यह टैग केवल स्पूल क्षेत्र के पश्चिमी ओर से दिखता है।"),
          ], kind="warning")
    m.obj("sign_hidden", "sign", 3.2, 6.6, 180, signKind="warning",
          text=T("Line 210 returned to service — check with area authority", "வரி 210 மீண்டும் இயக்கத்தில் — பகுதி அதிகாரியிடம் சரிபார்க்கவும்", "लाइन 210 फिर से सेवा में — क्षेत्र प्राधिकारी से जाँचें"),
          name=T("Warning sign (behind the exchanger)", "எச்சரிக்கை அடையாளம் (வெப்பப் பரிமாற்றிக்குப் பின்னால்)", "चेतावनी संकेत (एक्सचेंजर के पीछे)"),
          details=[
              T("Sign: 'Line 210 returned to service — check with area authority before any work.'", "அடையாளம்: 'வரி 210 மீண்டும் இயக்கத்தில் — எந்த வேலைக்கும் முன் பகுதி அதிகாரியிடம் சரிபார்க்கவும்.'", "संकेत: 'लाइन 210 फिर से सेवा में — किसी भी काम से पहले क्षेत्र प्राधिकारी से जाँचें।'"),
              T("It faces the north walkway, so you only see it from behind the exchanger.", "இது வடக்கு நடைபாதையை நோக்கியுள்ளது, எனவே வெப்பப் பரிமாற்றிக்குப் பின்னாலிருந்து மட்டுமே தெரியும்.", "यह उत्तरी रास्ते की ओर है, इसलिए एक्सचेंजर के पीछे से ही दिखता है।"),
          ], kind="warning", prompt="read")
    m.obj("area_board", "board", -4.5, -3.2, 0, prompt="read", kind="information",
          title=T("SPOOL AREA LOG", "ஸ்பூல் பகுதி பதிவேடு", "स्पूल क्षेत्र लॉग"),
          lines=[
              T("05:30 Line 210 back in service (ops)", "05:30 வரி 210 மீண்டும் இயக்கத்தில் (இயக்கம்)", "05:30 लाइन 210 फिर सेवा में (ऑप्स)"),
              T("Scaffold on west side: tag check pending", "மேற்குப் பக்க சாரம்: குறிச்சீட்டு சரிபார்ப்பு நிலுவையில்", "पश्चिमी ओर मचान: टैग जाँच लंबित"),
          ],
          name=T("Spool area log board", "ஸ்பூல் பகுதி பதிவுப் பலகை", "स्पूल क्षेत्र लॉग बोर्ड"),
          details=[
              T("Shift log, 05:30: 'Line 210 back in service (ops)'.", "பணிமாற்றப் பதிவு, 05:30: 'வரி 210 மீண்டும் இயக்கத்தில் (இயக்கம்)'.", "शिफ्ट लॉग, 05:30: 'लाइन 210 फिर सेवा में (ऑप्स)'।"),
              T("Note: 'Scaffold on west side — tag check pending.'", "குறிப்பு: 'மேற்குப் பக்க சாரம் — குறிச்சீட்டு சரிபார்ப்பு நிலுவையில்.'", "नोट: 'पश्चिमी ओर मचान — टैग जाँच लंबित।'"),
          ])
    m.obj("review_station", "stand", 3.4, -3.4, 0, panel="station", prompt="review", kind="station", groups=["final"],
          name=T("Job review station", "வேலை மறுஆய்வு நிலையம்", "कार्य समीक्षा स्टेशन"),
          details=[T("Compare what the work order says with what you found in the area.", "பணி ஆணை சொல்வதை நீங்கள் பகுதியில் கண்டதுடன் ஒப்பிடுங்கள்.", "वर्क ऑर्डर जो कहता है उसकी तुलना क्षेत्र में मिली जानकारी से करें।")])

    m.evidence("ev_job", T("Job location", "வேலை இடம்", "कार्य स्थल"), T("Flange F-12, line 210 (work order WO-3107)", "ஃபிளேஞ்ச் F-12, வரி 210 (பணி ஆணை WO-3107)", "फ्लेंज F-12, लाइन 210 (वर्क ऑर्डर WO-3107)"), True)
    m.evidence("ev_line_status", T("Line 210 status", "வரி 210 நிலை", "लाइन 210 की स्थिति"),
               T("Work order: 'drained'. Valve tag, sign and log: 'in service'. Not resolved.", "பணி ஆணை: 'வடிகட்டப்பட்டது'. வால்வுக் குறிச்சீட்டு, அடையாளம், பதிவு: 'இயக்கத்தில்'. தீர்க்கப்படவில்லை.", "वर्क ऑर्डर: 'खाली'। वाल्व टैग, संकेत और लॉग: 'सेवा में'। अनसुलझा।"), False)
    m.evidence("ev_requester", T("Requested by", "கோரியவர்", "अनुरोधकर्ता"), T("Maintenance planning, signed", "பராமரிப்புத் திட்டமிடல், கையொப்பமிடப்பட்டது", "मेंटेनेंस प्लानिंग, हस्ताक्षरित"), True)
    m.group("final", T("What do you do about the F-12 job?", "F-12 வேலை குறித்து என்ன செய்வீர்கள்?", "F-12 के काम के बारे में आप क्या करेंगे?"), [
        ("stop_report", T("Stop and report the conflict to Joseph and the area authority", "நிறுத்தி, முரண்பாட்டை ஜோசப்பிடமும் பகுதி அதிகாரியிடமும் தெரிவிக்கவும்", "रुकें और विरोधाभास जोसेफ व क्षेत्र प्राधिकारी को बताएँ")),
        ("start", T("Start — the work order says the line is drained", "தொடங்கவும் — பணி ஆணை வரி வடிகட்டப்பட்டது என்கிறது", "शुरू करें — वर्क ऑर्डर कहता है लाइन खाली है")),
        ("remove_tag", T("Remove the tag — it is probably left over from an old job", "குறிச்சீட்டை அகற்றவும் — அது பழைய வேலையில் விடப்பட்டிருக்கலாம்", "टैग हटा दें — यह शायद किसी पुराने काम का बचा हुआ है")),
    ])
    m.tools("flashlight", "spanner", "radio", flashlight=["flange_f12", "flange_f11", "valve_xv210"])

    # ------------------------------------------------------------------ steps
    meet = m.meet("senior_tech")
    m.briefing(meet)
    m.step("enter_area", title=T("Go to the spool area on line 210", "வரி 210-இன் ஸ்பூல் பகுதிக்குச் செல்லுங்கள்", "लाइन 210 के स्पूल क्षेत्र में जाएँ"),
           instruction=T("Walk north along the walkway into the yellow-bordered spool area.", "நடைபாதை வழியாக வடக்கே மஞ்சள் எல்லையிட்ட ஸ்பூல் பகுதிக்குள் செல்லுங்கள்.", "रास्ते से उत्तर की ओर पीली सीमा वाले स्पूल क्षेत्र में जाएँ।"),
           trigger=enter("zone_spool"), requires=["briefing"], points=5, concept="situational_awareness", scene="navigate", marker="zone_spool",
           hints=[T("The spool area is the yellow rectangle north of the review station.", "ஸ்பூல் பகுதி மறுஆய்வு நிலையத்திற்கு வடக்கே உள்ள மஞ்சள் செவ்வகம்.", "स्पूल क्षेत्र समीक्षा स्टेशन के उत्तर में पीला आयत है।")])
    m.step("locate_flange", title=T("Locate flange F-12", "ஃபிளேஞ்ச் F-12-ஐக் கண்டறியுங்கள்", "फ्लेंज F-12 खोजें"),
           instruction=T("Find the flange named in the work order and inspect it (E).", "பணி ஆணையில் குறிப்பிட்ட ஃபிளேஞ்சைக் கண்டறிந்து ஆய்வு செய்யுங்கள் (E).", "वर्क ऑर्डर में बताया फ्लेंज खोजें और उसका निरीक्षण करें (E)।"),
           trigger=inspect("flange_f12"), requires=["enter_area"], points=10, concept="equipment_identification", scene="identify", marker="flange_f12",
           hints=[T("F-12 is on the nearer spool. F-11 belongs to line 211.", "F-12 அருகிலுள்ள ஸ்பூலில் உள்ளது. F-11 வரி 211-க்கு உரியது.", "F-12 पास वाले स्पूल पर है। F-11 लाइन 211 का है।")])
    m.step("read_log", title=T("Read the spool area log", "ஸ்பூல் பகுதிப் பதிவேட்டைப் படியுங்கள்", "स्पूल क्षेत्र लॉग पढ़ें"),
           instruction=T("Read the log board at the south-west corner of the area.", "பகுதியின் தென்மேற்கு மூலையில் உள்ள பதிவுப் பலகையைப் படியுங்கள்.", "क्षेत्र के दक्षिण-पश्चिमी कोने का लॉग बोर्ड पढ़ें।"),
           trigger=inspect("area_board"), requires=["locate_flange"], points=10, concept="hidden_hazard_info", scene="documents", marker="area_board",
           hints=[T("Shift logs record changes since the work order was written.", "பணி ஆணை எழுதப்பட்ட பின் ஏற்பட்ட மாற்றங்களை பணிமாற்றப் பதிவுகள் பதிவுசெய்கின்றன.", "शिफ्ट लॉग वर्क ऑर्डर लिखे जाने के बाद के बदलाव दर्ज करते हैं।")])
    m.step("find_tag", title=T("Check the valve behind the pipework", "குழாய்களுக்குப் பின்னால் உள்ள வால்வைச் சரிபாருங்கள்", "पाइपों के पीछे वाला वाल्व जाँचें"),
           instruction=T("Walk round to the west side of the spool and inspect valve XV-210.", "ஸ்பூலின் மேற்குப் பக்கம் சுற்றிச் சென்று வால்வு XV-210-ஐ ஆய்வு செய்யுங்கள்.", "स्पूल के पश्चिमी ओर जाकर वाल्व XV-210 का निरीक्षण करें।"),
           trigger=inspect("valve_xv210"), requires=["locate_flange"], points=15, concept="hidden_hazard_info", scene="hazards", marker="valve_xv210",
           hints=[T("Something is hanging on a handwheel on the far west side.", "மேற்குக் கோடியில் ஒரு கைச்சக்கரத்தில் ஏதோ தொங்குகிறது.", "दूर पश्चिमी ओर एक हैंडव्हील पर कुछ लटका है।"),
                  T("Go round the scaffold to reach XV-210.", "XV-210-ஐ அடைய சாரத்தைச் சுற்றிச் செல்லுங்கள்.", "XV-210 तक पहुँचने के लिए मचान के चारों ओर जाएँ।")])
    m.step("find_sign", title=T("Look behind the exchanger", "வெப்பப் பரிமாற்றிக்குப் பின்னால் பாருங்கள்", "एक्सचेंजर के पीछे देखें"),
           instruction=T("Walk to the north side of the exchanger and read the sign there.", "வெப்பப் பரிமாற்றியின் வடக்குப் பக்கம் சென்று அங்குள்ள அடையாளத்தைப் படியுங்கள்.", "एक्सचेंजर के उत्तरी ओर जाकर वहाँ का संकेत पढ़ें।"),
           trigger=inspect("sign_hidden"), requires=["locate_flange"], points=15, concept="hidden_hazard_info", scene="hazards", marker="sign_hidden",
           hints=[T("Signs can face a different walkway from the one you came in on.", "நீங்கள் வந்த நடைபாதையை விட வேறு நடைபாதையை அடையாளங்கள் நோக்கியிருக்கலாம்.", "संकेत उस रास्ते के बजाय किसी दूसरे रास्ते की ओर हो सकते हैं जिससे आप आए।")])
    m.step("review", title=T("Review the job at the review station", "மறுஆய்வு நிலையத்தில் வேலையை மறுஆய்வு செய்யுங்கள்", "समीक्षा स्टेशन पर काम की समीक्षा करें"),
           instruction=T("Open the job review station south-east of the spool area.", "ஸ்பூல் பகுதிக்குத் தென்கிழக்கே உள்ள வேலை மறுஆய்வு நிலையத்தைத் திறவுங்கள்.", "स्पूल क्षेत्र के दक्षिण-पूर्व में कार्य समीक्षा स्टेशन खोलें।"),
           trigger=inspect("review_station"), requires=["find_tag", "find_sign", "read_log"], points=5, concept="documented_evidence", scene="evidence", marker="review_station",
           hints=[T("The review station is the blue lectern beside the walkway.", "மறுஆய்வு நிலையம் நடைபாதைக்கு அருகில் உள்ள நீல மேசை.", "समीक्षा स्टेशन रास्ते के पास नीला स्टैंड है।")])
    m.step("flag_conflict", title=T("Flag the unresolved information", "தீர்க்கப்படாத தகவலைக் குறியுங்கள்", "अनसुलझी जानकारी चिह्नित करें"),
           instruction=T("In the review, flag the entry where the sources disagree.", "மறுஆய்வில், தகவல் மூலங்கள் முரண்படும் பதிவைக் குறியுங்கள்.", "समीक्षा में वह प्रविष्टि चिह्नित करें जहाँ स्रोत मेल नहीं खाते।"),
           trigger=flag("ev_line_status"), requires=["review"], points=15, concept="status_documentation_mismatch", scene="evidence", marker="review_station",
           hints=[T("Which entry has two different answers depending on where you looked?", "எங்கே பார்த்தீர்கள் என்பதைப் பொறுத்து இரண்டு வெவ்வேறு பதில்கள் கொண்ட பதிவு எது?", "किस प्रविष्टि के दो अलग उत्तर हैं, इस पर निर्भर करते हुए कि आपने कहाँ देखा?")])
    m.step("decide", title=T("Decide what happens to the job", "வேலைக்கு என்ன நடக்கும் என்று முடிவு செய்யுங்கள்", "तय करें कि काम का क्या होगा"),
           instruction=T("Make the decision at the review station.", "மறுஆய்வு நிலையத்தில் முடிவை எடுங்கள்.", "समीक्षा स्टेशन पर निर्णय लें।"),
           trigger=decide("final", "stop_report"), requires=["flag_conflict"], points=20, concept="escalation", scene="decision", marker="review_station",
           mistake_if_early=T("Find and flag the conflicting information before deciding.", "முடிவெடுக்கும் முன் முரண்பட்ட தகவலைக் கண்டறிந்து குறியுங்கள்.", "निर्णय से पहले विरोधी जानकारी खोजकर चिह्नित करें।"),
           hints=[T("When sources disagree, who should resolve it — you, or the area authority?", "தகவல் மூலங்கள் முரண்படும்போது யார் தீர்க்க வேண்டும் — நீங்களா, பகுதி அதிகாரியா?", "जब स्रोत मेल न खाएँ, तो कौन सुलझाए — आप, या क्षेत्र प्राधिकारी?")])

    # ------------------------------------------------------------------ rules
    m.critical("start_on_paper", trigger=decide("final", "start"), concept="status_documentation_mismatch", dialogue="unsafe",
               explanation=T("You chose to start because the work order said 'drained', while the tag, sign and log in the area said the line is in service.",
                             "பகுதியில் உள்ள குறிச்சீட்டு, அடையாளம், பதிவு ஆகியவை வரி இயக்கத்தில் உள்ளது என்று கூறியபோதும், பணி ஆணை 'வடிகட்டப்பட்டது' என்றதால் தொடங்கத் தேர்ந்தெடுத்தீர்கள்.",
                             "क्षेत्र में टैग, संकेत और लॉग कहते थे कि लाइन सेवा में है, फिर भी आपने वर्क ऑर्डर के 'खाली' कहने पर शुरू करना चुना।"),
               missing=T("Confirmation from the area authority of the actual line status.", "உண்மையான வரி நிலை குறித்து பகுதி அதிகாரியின் உறுதிப்படுத்தல்.", "लाइन की वास्तविक स्थिति की क्षेत्र प्राधिकारी से पुष्टि।"))
    m.critical("remove_warning", trigger=decide("final", "remove_tag"), concept="hidden_hazard_info", dialogue="unsafe",
               explanation=T("Warning tags are never removed because they look old. The tag was dated today and matched the log.",
                             "பழையதாகத் தெரிவதால் எச்சரிக்கைக் குறிச்சீட்டுகளை ஒருபோதும் அகற்றக்கூடாது. அந்தக் குறிச்சீட்டு இன்றைய தேதியில் இருந்தது, பதிவுடனும் பொருந்தியது.",
                             "चेतावनी टैग पुराने दिखने के कारण कभी नहीं हटाए जाते। टैग पर आज की तारीख थी और वह लॉग से मेल खाता था।"),
               missing=T("Only the person who placed a tag, or the area authority, may decide whether it can be removed.", "குறிச்சீட்டை வைத்தவர் அல்லது பகுதி அதிகாரி மட்டுமே அதை அகற்றலாமா என்று முடிவு செய்யலாம்.", "टैग हटाया जा सकता है या नहीं, यह केवल टैग लगाने वाला या क्षेत्र प्राधिकारी तय कर सकता है।"))
    m.critical("spanner_on_line", trigger=tool("spanner", "flange_f12", "flange_f11", "valve_xv210"), concept="status_documentation_mismatch", dialogue="unsafe",
               condition=not_done("decide"),
               explanation=T("You started loosening equipment on line 210 while its status was unresolved.", "வரி 210-இன் நிலை தீர்க்கப்படாத போதே அதன் உபகரணத்தைத் தளர்த்தத் தொடங்கினீர்கள்.", "लाइन 210 की स्थिति अनसुलझी रहते हुए आपने उसके उपकरण को खोलना शुरू कर दिया।"),
               missing=T("A confirmed safe condition and authorisation before any tool touches the line.", "எந்தக் கருவியும் வரியைத் தொடும் முன் உறுதிப்படுத்தப்பட்ட பாதுகாப்பான நிலையும் அனுமதியும்.", "किसी भी औज़ार के लाइन छूने से पहले पुष्टि की गई सुरक्षित स्थिति और अनुमति।"))
    m.mistake("wrong_flag", trigger=any_flag(), kind="incorrect_decision", concept="documented_evidence",
              feedback=T("That entry is consistent across the sources. Look for the one that disagrees.", "அந்தப் பதிவு எல்லா மூலங்களிலும் ஒத்துப்போகிறது. முரண்படுவதைத் தேடுங்கள்.", "वह प्रविष्टि सभी स्रोतों में एक जैसी है। जो मेल नहीं खाती उसे खोजें।"))
    m.mistake("live_area", trigger=enter("zone_live"), kind="invalid_action", concept="situational_awareness",
              feedback=T("That taped area is live process plant and not part of your job. Step back out.", "அந்த நாடா கட்டிய பகுதி இயக்கத்திலுள்ள ஆலை, உங்கள் வேலையின் பகுதி அல்ல. வெளியே வாருங்கள்.", "वह टेप लगा क्षेत्र चालू प्लांट है और आपके काम का हिस्सा नहीं। बाहर आ जाइए।"))
    m.mistake("wrong_flange", trigger=inspect("flange_f11"), kind="advisory", concept="equipment_identification",
              feedback=T("F-11 belongs to line 211. Your job is F-12 on line 210.", "F-11 வரி 211-க்கு உரியது. உங்கள் வேலை வரி 210-இல் உள்ள F-12.", "F-11 लाइन 211 का है। आपका काम लाइन 210 का F-12 है।"))

    m.debrief(
        success=T("You walked the whole area, found the hidden tag and sign, and stopped the job for confirmation.", "நீங்கள் முழுப் பகுதியையும் சுற்றிப் பார்த்து, மறைந்திருந்த குறிச்சீட்டையும் அடையாளத்தையும் கண்டுபிடித்து, உறுதிப்படுத்தலுக்காக வேலையை நிறுத்தினீர்கள்.", "आपने पूरा क्षेत्र देखा, छिपा टैग और संकेत खोजा, और पुष्टि के लिए काम रोका।"),
        critical=T("You found the information, but a decision ignored it. Next time, let the conflict stop the job.", "தகவலைக் கண்டுபிடித்தீர்கள், ஆனால் ஒரு முடிவு அதைப் புறக்கணித்தது. அடுத்த முறை, முரண்பாடு வேலையை நிறுத்தட்டும்.", "आपने जानकारी खोजी, लेकिन एक निर्णय ने उसे अनदेखा किया। अगली बार विरोधाभास को काम रोकने दें।"),
        failed=T("The attempt ended after repeated unsafe actions. Walk the area again and let the warnings guide you.", "மீண்டும் மீண்டும் பாதுகாப்பற்ற செயல்களால் முயற்சி முடிந்தது. பகுதியை மீண்டும் சுற்றிப் பார்த்து எச்சரிக்கைகள் உங்களை வழிநடத்தட்டும்.", "बार-बार असुरक्षित कार्यों के बाद प्रयास समाप्त हुआ। क्षेत्र फिर से देखें और चेतावनियों को मार्गदर्शन करने दें।"),
        lines=[
            ({"criticalRule": "start_on_paper"}, T("You trusted the work order over three warnings in the field.", "களத்தில் இருந்த மூன்று எச்சரிக்கைகளை விட பணி ஆணையை நம்பினீர்கள்.", "आपने मैदान की तीन चेतावनियों के बजाय वर्क ऑर्डर पर भरोसा किया।")),
            ({"criticalRule": "remove_warning"}, T("You chose to remove a warning tag that was not yours.", "உங்களுடையதல்லாத எச்சரிக்கைக் குறிச்சீட்டை அகற்றத் தேர்ந்தெடுத்தீர்கள்.", "आपने ऐसा चेतावनी टैग हटाना चुना जो आपका नहीं था।")),
            ({"criticalRule": "spanner_on_line"}, T("A tool touched line 210 before its status was confirmed.", "வரி 210-இன் நிலை உறுதிசெய்யப்படும் முன் ஒரு கருவி அதைத் தொட்டது.", "लाइन 210 की स्थिति की पुष्टि से पहले एक औज़ार ने उसे छुआ।")),
            ({"stepCompleted": "find_tag"}, T("You walked round the scaffold and found the tag on XV-210.", "சாரத்தைச் சுற்றிச் சென்று XV-210-இல் குறிச்சீட்டைக் கண்டீர்கள்.", "आपने मचान के चारों ओर जाकर XV-210 पर टैग खोजा।")),
            ({"stepCompleted": "find_sign"}, T("You checked behind the exchanger and read the hidden sign.", "வெப்பப் பரிமாற்றிக்குப் பின்னால் சரிபார்த்து மறைந்திருந்த அடையாளத்தைப் படித்தீர்கள்.", "आपने एक्सचेंजर के पीछे जाँचकर छिपा संकेत पढ़ा।")),
            ({"counterAbove": ["incorrectDecisions", 0]}, T("At least one consistent entry was flagged as a problem.", "குறைந்தது ஒரு சரியான பதிவு பிரச்சினையாகக் குறிக்கப்பட்டது.", "कम से कम एक सही प्रविष्टि को समस्या के रूप में चिह्नित किया गया।")),
            ({"counterAbove": ["invalidActions", 0]}, T("You entered the taped live area. Stay inside your job boundary.", "நாடா கட்டிய இயக்கப் பகுதிக்குள் நுழைந்தீர்கள். உங்கள் வேலை எல்லைக்குள் இருங்கள்.", "आप टेप लगे चालू क्षेत्र में गए। अपने काम की सीमा में रहें।")),
            ({"stepCompleted": "decide"}, T("You stopped and escalated the conflict — the right call.", "நீங்கள் நிறுத்தி முரண்பாட்டை மேலிடத்துக்குத் தெரிவித்தீர்கள் — சரியான முடிவு.", "आपने रुककर विरोधाभास आगे बढ़ाया — सही निर्णय।")),
        ],
    )
    m.comic(T("LOOK BEHIND THE PIPES", "குழாய்களுக்குப் பின்னால் பாருங்கள்", "पाइपों के पीछे देखो"), [
        ("magnifier", T("Hazard information is not always on the side you walk up to.", "அபாயத் தகவல் எப்போதும் நீங்கள் வரும் பக்கத்தில் இருப்பதில்லை.", "खतरे की जानकारी हमेशा उस ओर नहीं होती जिधर से आप आते हैं।")),
        ("document_gap", T("When paperwork and the plant disagree, the job waits.", "ஆவணங்களும் ஆலையும் முரண்படும்போது, வேலை காத்திருக்கும்.", "जब कागज़ात और प्लांट मेल न खाएँ, तो काम रुकता है।")),
        ("stop_sign", T("Report it. Never 'tidy up' a warning that isn't yours.", "புகாரளியுங்கள். உங்களுடையதல்லாத எச்சரிக்கையை ஒருபோதும் 'சுத்தம்' செய்யாதீர்கள்.", "रिपोर्ट करें। जो चेतावनी आपकी नहीं, उसे कभी 'साफ़' न करें।")),
    ])
    m.report(["locate_flange", "read_log", "find_tag", "find_sign", "flag_conflict"], ["decide"])

    m.mcq(1, concept="hidden_hazard_info",
          stem=T("Why walk all the way round equipment in a congested area before a job?", "நெரிசலான பகுதியில் வேலைக்கு முன் உபகரணத்தை ஏன் முழுவதும் சுற்றிப் பார்க்க வேண்டும்?", "भीड़भाड़ वाले क्षेत्र में काम से पहले उपकरण के चारों ओर क्यों घूमना चाहिए?"),
          options=[T("To find tags, signs or notes that are not visible from one side", "ஒரு பக்கத்திலிருந்து தெரியாத குறிச்சீட்டுகள், அடையாளங்கள், குறிப்புகளைக் கண்டறிய", "एक ओर से न दिखने वाले टैग, संकेत या नोट खोजने के लिए"),
                   T("To save time later in the job", "பின்னர் வேலையில் நேரத்தை மிச்சப்படுத்த", "बाद में काम में समय बचाने के लिए"),
                   T("It is not needed if the work order is signed", "பணி ஆணை கையொப்பமிடப்பட்டிருந்தால் தேவையில்லை", "वर्क ऑर्डर पर हस्ताक्षर हों तो ज़रूरी नहीं")],
          correct="a", explanation=T("In this scenario both key warnings were only visible from behind the pipework.", "இந்தச் சூழலில் இரண்டு முக்கிய எச்சரிக்கைகளும் குழாய்களுக்குப் பின்னாலிருந்து மட்டுமே தெரிந்தன.", "इस परिदृश्य में दोनों मुख्य चेतावनियाँ केवल पाइपों के पीछे से दिखती थीं।"))
    m.mcq(2, concept="status_documentation_mismatch",
          stem=T("The work order says 'drained' but a tag on the valve says 'in service'. What do you do?", "பணி ஆணை 'வடிகட்டப்பட்டது' என்கிறது, ஆனால் வால்வுக் குறிச்சீட்டு 'இயக்கத்தில்' என்கிறது. என்ன செய்வீர்கள்?", "वर्क ऑर्डर 'खाली' कहता है पर वाल्व का टैग 'सेवा में' कहता है। आप क्या करेंगे?"),
          options=[T("Follow the work order because it is the official document", "அதிகாரப்பூர்வ ஆவணம் என்பதால் பணி ஆணையைப் பின்பற்றுவேன்", "वर्क ऑर्डर का पालन करूँगा क्योंकि वह आधिकारिक दस्तावेज़ है"),
                   T("Stop and report the conflict to the person in charge", "நிறுத்தி, முரண்பாட்டை பொறுப்பாளரிடம் தெரிவிப்பேன்", "रुककर विरोधाभास प्रभारी व्यक्ति को बताऊँगा"),
                   T("Open the valve slightly to see which is right", "எது சரி என்று பார்க்க வால்வைச் சற்றுத் திறப்பேன்", "कौन सही है देखने के लिए वाल्व थोड़ा खोलूँगा")],
          correct="b", explanation=T("Conflicting information is resolved by the responsible authority, not by the trainee testing it.", "முரண்பட்ட தகவலை பொறுப்பான அதிகாரி தீர்க்கிறார்; பயிற்சியாளர் சோதித்துப் பார்ப்பதால் அல்ல.", "विरोधी जानकारी ज़िम्मेदार प्राधिकारी सुलझाता है, प्रशिक्षु उसे परखकर नहीं।"))
    m.mcq(3, concept="hidden_hazard_info",
          stem=T("You find a warning tag that looks old. What is the right action?", "பழையதாகத் தோன்றும் எச்சரிக்கைக் குறிச்சீட்டைக் காண்கிறீர்கள். சரியான செயல் எது?", "आपको एक पुराना दिखने वाला चेतावनी टैग मिलता है। सही कार्य क्या है?"),
          options=[T("Remove it so it does not confuse others", "மற்றவர்களைக் குழப்பாமல் இருக்க அகற்றுவேன்", "उसे हटा दूँगा ताकि दूसरे भ्रमित न हों"),
                   T("Ignore it if the job is urgent", "வேலை அவசரமென்றால் புறக்கணிப்பேன்", "काम ज़रूरी हो तो अनदेखा करूँगा"),
                   T("Leave it in place and report it", "அதை அப்படியே விட்டுவிட்டுப் புகாரளிப்பேன்", "उसे वहीं छोड़कर रिपोर्ट करूँगा")],
          correct="c", explanation=T("Only the person who placed a tag or the area authority decides whether it can be removed.", "குறிச்சீட்டை வைத்தவர் அல்லது பகுதி அதிகாரி மட்டுமே அதை அகற்றலாமா என்று முடிவு செய்கிறார்.", "टैग हटाया जा सकता है या नहीं, यह केवल टैग लगाने वाला या क्षेत्र प्राधिकारी तय करता है।"))
    m.mcq(4, concept="escalation",
          stem=T("Which of these counts as hazard information for a job?", "ஒரு வேலைக்கான அபாயத் தகவலாக இவற்றில் எது கணக்கிடப்படும்?", "इनमें से कौन किसी काम के लिए खतरे की जानकारी मानी जाएगी?"),
          options=[T("Only signs at the area entrance", "பகுதி நுழைவாயிலில் உள்ள அடையாளங்கள் மட்டும்", "केवल क्षेत्र के प्रवेश पर लगे संकेत"),
                   T("Tags, signs, logs and notes around the job", "வேலையைச் சுற்றியுள்ள குறிச்சீட்டுகள், அடையாளங்கள், பதிவுகள், குறிப்புகள்", "काम के आसपास के टैग, संकेत, लॉग और नोट"),
                   T("Only what the work order says", "பணி ஆணை சொல்வது மட்டும்", "केवल वह जो वर्क ऑर्डर कहता है")],
          correct="b", explanation=T("The log, tag and sign together showed the line was back in service.", "பதிவு, குறிச்சீட்டு, அடையாளம் மூன்றும் சேர்ந்து வரி மீண்டும் இயக்கத்தில் உள்ளதைக் காட்டின.", "लॉग, टैग और संकेत ने मिलकर दिखाया कि लाइन फिर से सेवा में थी।"))

    m.spec(
        workplaceLocation="Fictional process unit, spool area of line 210.",
        equipmentType="Bolted flange F-12, isolation valve XV-210, exchanger, compressor K-210 (decor).",
        corePrinciple="Hazard information is not always visible from where you start; conflicting information is escalated, never resolved by assumption.",
        commonMisconceptions=["If I cannot see a warning, there is none.", "An old-looking tag can be removed.", "The work order overrides field information."],
        criticalDecisions=["Start on the strength of the work order", "Remove a warning tag", "Use a tool on the line before confirmation"],
        assessmentCriteria={"correct": "Find tag, sign and log; flag the unresolved status; stop and report.", "criticalCategories": ["start_on_paper", "remove_warning", "spanner_on_line"]},
        assumptions=["No real procedure is taught.", "No numerical thresholds are used."],
    )
    return m
