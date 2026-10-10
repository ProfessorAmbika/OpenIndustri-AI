"""PPE Awareness · Level 3 — The Incorrect Equipment.

Story: The trainee must collect a sample from the caustic dosing skid. The
reviewed task card specifies chemical-resistant gloves, chemical goggles and a
face shield. The store holds look-alikes: leather gloves, cotton gloves,
safety glasses. Senior Technician Joseph insists 'gloves are gloves'.
Learning: similar-looking PPE can have different specifications; match the
specification on the task card, not the appearance.
"""
from authoring.dsl import Mission, T, decide, enter, inspect, not_done, select


def build() -> Mission:
    m = Mission(
        code="ppe3", id="og-ppe-l3-incorrect-equipment", category="og_ppe", level=3, minutes=12,
        title=T("The Incorrect Equipment", "தவறான உபகரணம்", "गलत उपकरण"),
        subtitle=T("Gloves are not just gloves", "கையுறைகள் வெறும் கையுறைகள் அல்ல", "दस्ताने बस दस्ताने नहीं होते"),
        description=T("Three pairs of gloves look alike. Only one is right for this job.", "மூன்று ஜோடி கையுறைகள் ஒரே மாதிரி தெரிகின்றன. இந்த வேலைக்கு ஒன்று மட்டுமே சரி.", "तीन जोड़ी दस्ताने एक जैसे दिखते हैं। इस काम के लिए केवल एक सही है।"),
        location=T("Caustic dosing skid · Utility block", "காஸ்டிக் சேர்ப்பு அமைப்பு · பயன்பாட்டுப் பிரிவு", "कॉस्टिक डोज़िंग स्किड · यूटिलिटी ब्लॉक"),
        site="utility", spawn=(0, -23, 0), work_point=(0, -5, 0),
    )
    m.brief(
        lines=[
            T("Collect a sample from the caustic dosing skid sample point.", "காஸ்டிக் சேர்ப்பு அமைப்பின் மாதிரிப் புள்ளியிலிருந்து மாதிரி சேகரியுங்கள்.", "कॉस्टिक डोज़िंग स्किड के सैंपल पॉइंट से सैंपल लें।"),
            T("The task card specifies the PPE. Read the specification, not just the item name.", "பணி அட்டை PPE-ஐக் குறிப்பிடுகிறது. பொருளின் பெயரை மட்டுமல்ல, விவரக்குறிப்பையும் படியுங்கள்.", "टास्क कार्ड PPE बताता है। केवल वस्तु का नाम नहीं, विनिर्देश पढ़ें।"),
        ],
        task=T("Collect the PPE specified on task card TC-31 and confirm before sampling.", "பணி அட்டை TC-31-இல் குறிப்பிட்ட PPE-ஐ எடுத்து, மாதிரி எடுக்கும் முன் உறுதிப்படுத்துங்கள்.", "टास्क कार्ड TC-31 में बताया PPE लें और सैंपल से पहले पुष्टि करें।"),
        equipment=T("Caustic dosing skid, sample point SP-31, PPE store (fictional).", "காஸ்டிக் சேர்ப்பு அமைப்பு, மாதிரிப் புள்ளி SP-31, PPE களஞ்சியம் (கற்பனை).", "कॉस्टिक डोज़िंग स्किड, सैंपल पॉइंट SP-31, PPE स्टोर (काल्पनिक)।"),
        objective=T("Choose PPE by specification and resist the 'gloves are gloves' shortcut.", "விவரக்குறிப்பின்படி PPE-ஐத் தேர்ந்தெடுத்து, 'கையுறை என்றால் கையுறைதான்' என்ற குறுக்குவழியைத் தவிர்க்கவும்.", "विनिर्देश के अनुसार PPE चुनें और 'दस्ताने तो दस्ताने हैं' वाले शॉर्टकट से बचें।"),
        information=T("Labels on each item show its intended use. The specification on the card is fictional teaching content.", "ஒவ்வொரு பொருளின் குறியும் அதன் பயன்பாட்டைக் காட்டுகிறது. அட்டையில் உள்ள விவரக்குறிப்பு கற்பனைக் கற்பித்தல் உள்ளடக்கம்.", "हर वस्तु का लेबल उसका उपयोग बताता है। कार्ड का विनिर्देश काल्पनिक शिक्षण सामग्री है।"),
        objectives=[
            T("Distinguish similar-looking PPE by its specification.", "ஒத்த தோற்றமுடைய PPE-ஐ அதன் விவரக்குறிப்பால் வேறுபடுத்துதல்.", "एक जैसे दिखने वाले PPE को उसके विनिर्देश से अलग पहचानना।"),
            T("Hold to the task requirement when a colleague suggests a shortcut.", "சக ஊழியர் குறுக்குவழி கூறும்போதும் பணித் தேவையைப் பின்பற்றுதல்.", "साथी के शॉर्टकट सुझाने पर भी कार्य आवश्यकता पर टिके रहना।"),
        ],
    )
    m.dialogue("meet", [
        ("senior_tech", "friendly", T("Sample run on the caustic skid. Card's on the board — TC-31.", "காஸ்டிக் அமைப்பில் மாதிரி எடுப்பு. அட்டை பலகையில் உள்ளது — TC-31.", "कॉस्टिक स्किड पर सैंपल। कार्ड बोर्ड पर है — TC-31।")),
    ])
    m.dialogue("shortcut", [
        ("senior_tech", "neutral", T("Honestly, grab any gloves. Gloves are gloves.", "உண்மையில், ஏதாவது கையுறையை எடுங்கள். கையுறை என்றால் கையுறைதான்.", "सच कहूँ तो कोई भी दस्ताने ले लो। दस्ताने तो दस्ताने हैं।"),
         [(T("I'll match the specification on the card, Joseph", "நான் அட்டையில் உள்ள விவரக்குறிப்பைப் பின்பற்றுகிறேன், ஜோசப்", "मैं कार्ड के विनिर्देश से मिलाऊँगा, जोसेफ"), "advice", "follow_card", "joseph_ok"),
          (T("Fine — whatever's nearest", "சரி — அருகில் இருப்பதை", "ठीक है — जो पास हो"), "advice", "any_gloves", None)]),
    ])
    m.dialogue("joseph_ok", [("senior_tech", "pleased", T("Ha — fair. Old habits. The card's right, I'm wrong.", "ஹா — சரிதான். பழைய பழக்கம். அட்டை சரி, நான் தவறு.", "हा — ठीक है। पुरानी आदत। कार्ड सही है, मैं गलत।"))])
    m.dialogue("revisit", [("senior_tech", "neutral", T("Go by the card. I'll be here.", "அட்டைப்படி செல்லுங்கள். நான் இங்கே இருப்பேன்.", "कार्ड के अनुसार चलो। मैं यहीं हूँ।"))])
    m.dialogue("unsafe", [("senior_tech", "concerned", T("Hang on — that isn't what TC-31 specifies. Check the labels.", "பொறுங்கள் — TC-31 குறிப்பிடுவது அது அல்ல. குறிகளைச் சரிபாருங்கள்.", "रुको — TC-31 यह नहीं बताता। लेबल जाँचो।"))])
    m.dialogue("correct", [("senior_tech", "pleased", T("Spec matched, item by item. That's the habit I should have.", "விவரக்குறிப்பு ஒவ்வொன்றாகப் பொருந்தியது. எனக்கு இருக்க வேண்டிய பழக்கம் இதுதான்.", "विनिर्देश एक-एक कर मिलाया। यही आदत मुझे होनी चाहिए।"))])
    m.npc("senior_tech", -3, -12, 180, talk=[("meet", not_done("meet_senior_tech")), ("shortcut", not_done("advice")), ("joseph_ok", None)])

    m.zone("zone_skid", T("Caustic dosing skid", "காஸ்டிக் சேர்ப்பு அமைப்பு", "कॉस्टिक डोज़िंग स्किड"), (-5, 5, 4, 11))
    m.decor("tape", 0, 7.5, w=10, d=7, color="#ffc23d")
    m.decor("tank", -2.5, 8.5, tag="TK-31", r=1.2, h=3, color="#e9eef5")
    m.decor("sign", 1.8, 3.6, kind="warning", text=T("Corrosive chemical — task card PPE only", "அரிக்கும் வேதிப்பொருள் — பணி அட்டை PPE மட்டும்", "संक्षारक रसायन — केवल टास्क कार्ड PPE"))
    m.decor("hose_reel", -5.8, 5.5, heading=90)
    m.obj("sample_point", "valve", 2.0, 7.5, tag="SP-31", wheel="#2fbf71",
          name=T("Sample point SP-31", "மாதிரிப் புள்ளி SP-31", "सैंपल पॉइंट SP-31"),
          details=[T("Sample point on the caustic line. Sampling starts here once PPE is confirmed.", "காஸ்டிக் வரியில் உள்ள மாதிரிப் புள்ளி. PPE உறுதிசெய்யப்பட்டதும் மாதிரி எடுப்பு இங்கே தொடங்கும்.", "कॉस्टिक लाइन पर सैंपल पॉइंट। PPE पुष्ट होने पर सैंपलिंग यहाँ से शुरू होती है।")])
    m.obj("task_card", "board", -4.0, -4.0, kind="information", prompt="read", accent="#ff7a1a",
          title=T("TASK CARD TC-31", "பணி அட்டை TC-31", "टास्क कार्ड TC-31"),
          lines=[T("Task: caustic sample at SP-31", "பணி: SP-31-இல் காஸ்டிக் மாதிரி", "कार्य: SP-31 पर कॉस्टिक सैंपल"),
                 T("Gloves: CHEMICAL-RESISTANT type", "கையுறை: வேதிப்பொருள்-எதிர்ப்பு வகை", "दस्ताने: रसायन-प्रतिरोधी प्रकार"),
                 T("Eyes/face: chemical goggles + face shield", "கண்/முகம்: வேதிக் கண்ணாடி + முகக் கவசம்", "आँख/चेहरा: केमिकल गॉगल्स + फेस शील्ड")],
          name=T("Task card TC-31", "பணி அட்டை TC-31", "टास्क कार्ड TC-31"),
          details=[T("Gloves: chemical-resistant type, as labelled for this chemical (fictional spec).", "கையுறை: இந்த வேதிப்பொருளுக்கெனக் குறியிடப்பட்ட வேதிப்பொருள்-எதிர்ப்பு வகை (கற்பனை விவரக்குறிப்பு).", "दस्ताने: इस रसायन के लिए लेबल वाले रसायन-प्रतिरोधी प्रकार (काल्पनिक विनिर्देश)।"),
                   T("Eyes and face: chemical goggles AND a face shield.", "கண்கள், முகம்: வேதிக் கண்ணாடி மற்றும் முகக் கவசம்.", "आँखें और चेहरा: केमिकल गॉगल्स और फेस शील्ड।")])
    m.obj("ppe_store", "locker", 3.5, -3.5, panel="inventory", prompt="open", kind="station", groups=["loadout"],
          name=T("PPE store", "PPE களஞ்சியம்", "PPE स्टोर"),
          details=[T("Read each label. Several items look alike.", "ஒவ்வொரு குறியையும் படியுங்கள். பல பொருட்கள் ஒரே மாதிரி தெரிகின்றன.", "हर लेबल पढ़ें। कई वस्तुएँ एक जैसी दिखती हैं।")])
    m.item("gloves_chem", "ppe_store", "gloves_chem", T("Gloves — green", "கையுறை — பச்சை", "दस्ताने — हरे"), T("Label: chemical-resistant, for this chemical group.", "குறி: வேதிப்பொருள்-எதிர்ப்பு, இந்த வேதிக் குழுவுக்கு.", "लेबल: रसायन-प्रतिरोधी, इस रसायन समूह के लिए।"))
    m.item("gloves_leather", "ppe_store", "gloves_leather", T("Gloves — tan", "கையுறை — பழுப்பு", "दस्ताने — भूरे"), T("Label: general handling / abrasion. Not chemical-resistant.", "குறி: பொதுக் கையாளுதல் / உராய்வு. வேதிப்பொருள்-எதிர்ப்பு அல்ல.", "लेबल: सामान्य हैंडलिंग / घर्षण। रसायन-प्रतिरोधी नहीं।"))
    m.item("gloves_cotton", "ppe_store", "gloves_cotton", T("Gloves — white", "கையுறை — வெள்ளை", "दस्ताने — सफ़ेद"), T("Label: cotton liner. Not chemical-resistant.", "குறி: பருத்தி உள்ளுறை. வேதிப்பொருள்-எதிர்ப்பு அல்ல.", "लेबल: सूती लाइनर। रसायन-प्रतिरोधी नहीं।"))
    m.item("goggles", "ppe_store", "goggles", T("Goggles — sealed", "கண்ணாடி — மூடிய வகை", "गॉगल्स — सील्ड"), T("Label: chemical splash goggles.", "குறி: வேதித் தெறிப்புக் கண்ணாடி.", "लेबल: केमिकल स्प्लैश गॉगल्स।"))
    m.item("glasses", "ppe_store", "glasses", T("Glasses — open frame", "கண்ணாடி — திறந்த சட்டம்", "चश्मा — खुला फ़्रेम"), T("Label: impact safety glasses. Not splash goggles.", "குறி: மோதல் பாதுகாப்புக் கண்ணாடி. தெறிப்புக் கண்ணாடி அல்ல.", "लेबल: इम्पैक्ट सेफ्टी चश्मा। स्प्लैश गॉगल्स नहीं।"))
    m.item("faceshield", "ppe_store", "faceshield", T("Face shield", "முகக் கவசம்", "फेस शील्ड"), T("Label: face shield, worn over goggles.", "குறி: முகக் கவசம், கண்ணாடிக்கு மேல் அணிவது.", "लेबल: फेस शील्ड, गॉगल्स के ऊपर पहनें।"))
    m.group("advice", T("Joseph says 'gloves are gloves'. Your answer?", "'கையுறை என்றால் கையுறைதான்' என்கிறார் ஜோசப். உங்கள் பதில்?", "जोसेफ कहते हैं 'दस्ताने तो दस्ताने हैं'। आपका जवाब?"), [
        ("follow_card", T("Match the card's specification", "அட்டையின் விவரக்குறிப்பைப் பின்பற்றுதல்", "कार्ड के विनिर्देश से मिलाना")),
        ("any_gloves", T("Take whatever is nearest", "அருகில் இருப்பதை எடுத்தல்", "जो पास हो वह लेना")),
    ])
    m.group("loadout", T("Confirm your PPE for TC-31", "TC-31-க்கான உங்கள் PPE-ஐ உறுதிப்படுத்துங்கள்", "TC-31 के लिए अपना PPE पुष्ट करें"), [
        ("confirm", T("My PPE matches the TC-31 specification", "என் PPE TC-31 விவரக்குறிப்புடன் பொருந்துகிறது", "मेरा PPE TC-31 विनिर्देश से मेल खाता है")),
        ("thicker", T("Use the leather gloves — they're thicker, so safer", "தோல் கையுறைகளைப் பயன்படுத்துங்கள் — தடிமனானவை, எனவே பாதுகாப்பானவை", "चमड़े के दस्ताने लें — मोटे हैं, तो ज़्यादा सुरक्षित")),
    ])

    meet = m.meet("senior_tech")
    m.briefing(meet)
    m.step("advice", title=T("Respond to Joseph's shortcut", "ஜோசப்பின் குறுக்குவழிக்குப் பதிலளியுங்கள்", "जोसेफ के शॉर्टकट का जवाब दें"),
           instruction=T("Talk to Joseph again and answer his suggestion.", "ஜோசப்புடன் மீண்டும் பேசி அவரது பரிந்துரைக்குப் பதிலளியுங்கள்.", "जोसेफ से फिर बात करें और उनके सुझाव का जवाब दें।"),
           trigger=decide("advice", "follow_card"), requires=["briefing"], points=10, concept="ppe_specification", scene="communicate", marker="senior_tech",
           hints=[T("What decides which gloves you need — habit, or the card?", "எந்தக் கையுறை தேவை என்பதை எது தீர்மானிக்கிறது — பழக்கமா, அட்டையா?", "कौन से दस्ताने चाहिए यह क्या तय करता है — आदत या कार्ड?")])
    m.step("read_card", title=T("Read task card TC-31", "பணி அட்டை TC-31-ஐப் படியுங்கள்", "टास्क कार्ड TC-31 पढ़ें"), instruction=T("Read the specification on the orange-headed board.", "ஆரஞ்சுத் தலைப்புப் பலகையில் உள்ள விவரக்குறிப்பைப் படியுங்கள்.", "नारंगी शीर्ष वाले बोर्ड पर विनिर्देश पढ़ें।"),
           trigger=inspect("task_card"), requires=["briefing"], points=10, concept="ppe_task_requirements", scene="documents", marker="task_card",
           hints=[T("The board is west of the walkway.", "பலகை நடைபாதைக்கு மேற்கே உள்ளது.", "बोर्ड रास्ते के पश्चिम में है।")])
    m.step("open_store", title=T("Open the PPE store", "PPE களஞ்சியத்தைத் திறவுங்கள்", "PPE स्टोर खोलें"), instruction=T("Open the store and read every label.", "களஞ்சியத்தைத் திறந்து ஒவ்வொரு குறியையும் படியுங்கள்.", "स्टोर खोलें और हर लेबल पढ़ें।"),
           trigger=inspect("ppe_store"), requires=["read_card"], points=5, concept="ppe_specification", scene="ppe", marker="ppe_store",
           hints=[T("East of the walkway.", "நடைபாதைக்குக் கிழக்கே.", "रास्ते के पूर्व में।")])
    m.step("take_gloves", title=T("Take the specified gloves", "குறிப்பிட்ட கையுறைகளை எடுங்கள்", "बताए गए दस्ताने लें"), instruction=T("Select the gloves whose label matches the card.", "குறி அட்டையுடன் பொருந்தும் கையுறைகளைத் தேர்ந்தெடுங்கள்.", "जिन दस्तानों का लेबल कार्ड से मेल खाए उन्हें चुनें।"),
           trigger=select("gloves_chem"), requires=["open_store"], points=15, concept="ppe_specification", scene="ppe", marker="ppe_store",
           hints=[T("Colour doesn't decide it; the label does.", "நிறம் தீர்மானிக்காது; குறிதான் தீர்மானிக்கும்.", "रंग तय नहीं करता; लेबल करता है।")])
    m.step("take_goggles", title=T("Take the specified eye protection", "குறிப்பிட்ட கண் பாதுகாப்பை எடுங்கள்", "बताई गई आँखों की सुरक्षा लें"), instruction=T("Select the splash goggles.", "தெறிப்புக் கண்ணாடியைத் தேர்ந்தெடுங்கள்.", "स्प्लैश गॉगल्स चुनें।"),
           trigger=select("goggles"), requires=["open_store"], points=10, concept="ppe_specification", scene="ppe", marker="ppe_store",
           hints=[T("Open-frame glasses are a different specification.", "திறந்த சட்டக் கண்ணாடி வேறு விவரக்குறிப்பு.", "खुले फ़्रेम का चश्मा अलग विनिर्देश है।")])
    m.step("take_shield", title=T("Take the face shield", "முகக் கவசத்தை எடுங்கள்", "फेस शील्ड लें"), instruction=T("Select the face shield.", "முகக் கவசத்தைத் தேர்ந்தெடுங்கள்.", "फेस शील्ड चुनें।"),
           trigger=select("faceshield"), requires=["open_store"], points=10, concept="ppe_task_requirements", scene="ppe", marker="ppe_store",
           hints=[T("The card asks for goggles AND a shield.", "அட்டை கண்ணாடியும் கவசமும் கோருகிறது.", "कार्ड गॉगल्स और शील्ड दोनों माँगता है।")])
    m.step("confirm", title=T("Confirm against the specification", "விவரக்குறிப்புடன் உறுதிப்படுத்துங்கள்", "विनिर्देश से पुष्टि करें"), instruction=T("Confirm your loadout in the store.", "களஞ்சியத்தில் உங்கள் தொகுப்பை உறுதிப்படுத்துங்கள்.", "स्टोर में अपना सेट पुष्ट करें।"),
           trigger=decide("loadout", "confirm"), requires=["take_gloves", "take_goggles", "take_shield", "advice"], points=15, concept="ppe_specification", scene="decision", marker="ppe_store",
           mistake_if_early=T("Not everything the card specifies is selected yet.", "அட்டை குறிப்பிடும் அனைத்தும் இன்னும் தேர்ந்தெடுக்கப்படவில்லை.", "कार्ड में बताई हर चीज़ अभी नहीं चुनी गई।"),
           hints=[T("Gloves, goggles and shield — all three, all to spec.", "கையுறை, கண்ணாடி, கவசம் — மூன்றும், விவரக்குறிப்பின்படி.", "दस्ताने, गॉगल्स और शील्ड — तीनों, विनिर्देश के अनुसार।")])
    m.step("go_sample", title=T("Go to sample point SP-31", "மாதிரிப் புள்ளி SP-31-க்குச் செல்லுங்கள்", "सैंपल पॉइंट SP-31 पर जाएँ"), instruction=T("Inspect the sample point to start sampling.", "மாதிரி எடுப்பைத் தொடங்க மாதிரிப் புள்ளியை ஆய்வு செய்யுங்கள்.", "सैंपलिंग शुरू करने के लिए सैंपल पॉइंट का निरीक्षण करें।"),
           trigger=inspect("sample_point"), requires=["confirm"], points=10, concept="situational_awareness", scene="inspect", marker="sample_point",
           mistake_if_early=T("Confirm your PPE before you approach the sample point.", "மாதிரிப் புள்ளியை அணுகும் முன் உங்கள் PPE-ஐ உறுதிப்படுத்துங்கள்.", "सैंपल पॉइंट के पास जाने से पहले अपना PPE पुष्ट करें।"),
           hints=[T("The green valve inside the taped area.", "நாடா கட்டிய பகுதிக்குள் உள்ள பச்சை வால்வு.", "टेप वाले क्षेत्र के अंदर हरा वाल्व।")])

    m.critical("wrong_spec_confirmed", trigger=decide("loadout", "thicker"), concept="ppe_specification", dialogue="unsafe",
               explanation=T("Thickness is not a specification. Leather gloves are labelled 'not chemical-resistant'.", "தடிமன் ஒரு விவரக்குறிப்பு அல்ல. தோல் கையுறைகள் 'வேதிப்பொருள்-எதிர்ப்பு அல்ல' எனக் குறியிடப்பட்டுள்ளன.", "मोटाई कोई विनिर्देश नहीं है। चमड़े के दस्तानों पर 'रसायन-प्रतिरोधी नहीं' लिखा है।"),
               missing=T("Chemical-resistant gloves as specified on TC-31.", "TC-31-இல் குறிப்பிட்டபடி வேதிப்பொருள்-எதிர்ப்புக் கையுறைகள்.", "TC-31 के अनुसार रसायन-प्रतिरोधी दस्ताने।"))
    m.critical("enter_skid_unconfirmed", trigger=enter("zone_skid"), condition=not_done("confirm"), concept="ppe_completeness", dialogue="unsafe",
               explanation=T("You entered the corrosive-chemical area before your PPE was confirmed against the card.", "உங்கள் PPE அட்டையுடன் உறுதிசெய்யப்படும் முன் அரிக்கும் வேதிப்பொருள் பகுதிக்குள் நுழைந்தீர்கள்.", "आपका PPE कार्ड से पुष्ट होने से पहले आप संक्षारक रसायन क्षेत्र में गए।"),
               missing=T("Confirmed TC-31 PPE before entry.", "நுழைவதற்கு முன் உறுதிப்படுத்தப்பட்ட TC-31 PPE.", "प्रवेश से पहले पुष्ट TC-31 PPE।"))
    for item, fb in [
        ("gloves_leather", T("Tan gloves are for abrasion, not chemicals. Read the label.", "பழுப்புக் கையுறைகள் உராய்வுக்கானவை, வேதிப்பொருளுக்கு அல்ல. குறியைப் படியுங்கள்.", "भूरे दस्ताने घर्षण के लिए हैं, रसायन के लिए नहीं। लेबल पढ़ें।")),
        ("gloves_cotton", T("Cotton liners are not chemical-resistant. Read the label.", "பருத்தி உள்ளுறைகள் வேதிப்பொருள்-எதிர்ப்பு அல்ல. குறியைப் படியுங்கள்.", "सूती लाइनर रसायन-प्रतिरोधी नहीं हैं। लेबल पढ़ें।")),
        ("glasses", T("Open-frame glasses are not splash goggles. Read the label.", "திறந்த சட்டக் கண்ணாடி தெறிப்புக் கண்ணாடி அல்ல. குறியைப் படியுங்கள்.", "खुले फ़्रेम का चश्मा स्प्लैश गॉगल्स नहीं है। लेबल पढ़ें।")),
    ]:
        m.mistake(f"wrong_{item}", trigger=select(item), kind="incorrect_decision", concept="ppe_specification", feedback=fb)
    m.mistake("any_gloves", trigger=decide("advice", "any_gloves"), kind="incorrect_decision", concept="ppe_specification",
              feedback=T("'Gloves are gloves' is exactly the misconception this job tests. Talk to Joseph again.", "'கையுறை என்றால் கையுறைதான்' என்பதே இந்த வேலை சோதிக்கும் தவறான கருத்து. ஜோசப்புடன் மீண்டும் பேசுங்கள்.", "'दस्ताने तो दस्ताने हैं' — यही ग़लतफ़हमी यह काम परखता है। जोसेफ से फिर बात करें।"))

    m.debrief(
        success=T("You chose by specification, not appearance — and talked Joseph out of a bad habit.", "தோற்றத்தால் அல்ல, விவரக்குறிப்பால் தேர்ந்தெடுத்தீர்கள் — ஜோசப்பின் தவறான பழக்கத்தையும் மாற்றினீர்கள்.", "आपने रूप से नहीं, विनिर्देश से चुना — और जोसेफ की गलत आदत भी छुड़ाई।"),
        critical=T("Look-alike PPE was accepted against the specification. Read labels every time.", "விவரக்குறிப்புக்கு மாறாக ஒத்த தோற்ற PPE ஏற்கப்பட்டது. ஒவ்வொரு முறையும் குறிகளைப் படியுங்கள்.", "विनिर्देश के विरुद्ध एक जैसा दिखने वाला PPE स्वीकार हुआ। हर बार लेबल पढ़ें।"),
        failed=T("Repeated unsafe choices ended the attempt.", "தொடர்ந்த பாதுகாப்பற்ற தேர்வுகள் முயற்சியை முடித்தன.", "बार-बार असुरक्षित विकल्पों से प्रयास समाप्त हुआ।"),
        lines=[
            ({"criticalRule": "wrong_spec_confirmed"}, T("You confirmed leather gloves for a chemical task.", "வேதிப் பணிக்குத் தோல் கையுறைகளை உறுதிப்படுத்தினீர்கள்.", "आपने रासायनिक काम के लिए चमड़े के दस्ताने पुष्ट किए।")),
            ({"criticalRule": "enter_skid_unconfirmed"}, T("You entered the skid area before confirming PPE.", "PPE-ஐ உறுதிப்படுத்தும் முன் அமைப்புப் பகுதிக்குள் நுழைந்தீர்கள்.", "PPE पुष्ट करने से पहले आप स्किड क्षेत्र में गए।")),
            ({"counterAbove": ["incorrectDecisions", 0]}, T("At least one look-alike item was picked before the right one.", "சரியானதற்கு முன் குறைந்தது ஒரு ஒத்த தோற்றப் பொருள் தேர்ந்தெடுக்கப்பட்டது.", "सही वस्तु से पहले कम से कम एक एक-जैसी वस्तु चुनी गई।")),
            ({"stepCompleted": "advice"}, T("You held to the card when a senior colleague suggested a shortcut.", "மூத்த சக ஊழியர் குறுக்குவழி கூறியபோதும் அட்டையைப் பின்பற்றினீர்கள்.", "वरिष्ठ साथी के शॉर्टकट सुझाने पर भी आप कार्ड पर टिके रहे।")),
        ],
    )
    m.comic(T("READ THE LABEL", "குறியைப் படியுங்கள்", "लेबल पढ़ो"), [
        ("ppe", T("Same shape, different job.", "ஒரே வடிவம், வேறு வேலை.", "एक ही आकार, अलग काम।")),
        ("magnifier", T("The specification is on the card and on the label.", "விவரக்குறிப்பு அட்டையிலும் குறியிலும் உள்ளது.", "विनिर्देश कार्ड और लेबल पर है।")),
        ("approval", T("Match them item by item.", "ஒவ்வொன்றாகப் பொருத்துங்கள்.", "एक-एक कर मिलाएँ।")),
    ])
    m.report(["read_card", "take_gloves", "take_goggles", "take_shield"], ["advice", "confirm"])
    m.mcq(1, concept="ppe_specification",
          stem=T("Two pairs of gloves look similar. How do you choose?", "இரண்டு ஜோடி கையுறைகள் ஒரே மாதிரி தெரிகின்றன. எப்படித் தேர்ந்தெடுப்பீர்கள்?", "दो जोड़ी दस्ताने एक जैसे दिखते हैं। कैसे चुनेंगे?"),
          options=[T("By colour", "நிறத்தால்", "रंग से"), T("By the label matching the task specification", "பணி விவரக்குறிப்புடன் பொருந்தும் குறியால்", "कार्य विनिर्देश से मेल खाते लेबल से"), T("By thickness", "தடிமனால்", "मोटाई से")],
          correct="b", explanation=T("Only the specification tells you what a glove protects against.", "ஒரு கையுறை எதிலிருந்து பாதுகாக்கிறது என்பதை விவரக்குறிப்பு மட்டுமே சொல்லும்.", "केवल विनिर्देश बताता है कि दस्ताना किससे बचाता है।"))
    m.mcq(2, concept="ppe_specification",
          stem=T("Are impact safety glasses the same as chemical splash goggles?", "மோதல் பாதுகாப்புக் கண்ணாடியும் வேதித் தெறிப்புக் கண்ணாடியும் ஒன்றா?", "क्या इम्पैक्ट सेफ्टी चश्मा और केमिकल स्प्लैश गॉगल्स एक हैं?"),
          options=[T("Yes", "ஆம்", "हाँ"), T("Only if they are new", "புதியவை என்றால் மட்டும்", "केवल अगर नए हों"), T("No — they have different specifications", "இல்லை — அவற்றின் விவரக்குறிப்புகள் வேறு", "नहीं — उनके विनिर्देश अलग हैं")],
          correct="c", explanation=T("In this scenario the labels state different intended uses.", "இந்தச் சூழலில் குறிகள் வெவ்வேறு பயன்பாடுகளைக் கூறுகின்றன.", "इस परिदृश्य में लेबल अलग उपयोग बताते हैं।"))
    m.mcq(3, concept="ppe_specification",
          stem=T("A senior colleague says 'gloves are gloves'. What do you do?", "ஒரு மூத்த சக ஊழியர் 'கையுறை என்றால் கையுறைதான்' என்கிறார். என்ன செய்வீர்கள்?", "एक वरिष्ठ साथी कहते हैं 'दस्ताने तो दस्ताने हैं'। आप क्या करेंगे?"),
          options=[T("Follow the task card specification anyway", "எப்படியும் பணி அட்டை விவரக்குறிப்பைப் பின்பற்றுவேன்", "फिर भी टास्क कार्ड विनिर्देश का पालन करूँगा"), T("Agree — they have more experience", "ஒப்புக்கொள்வேன் — அவருக்கு அதிக அனுபவம்", "मान लूँगा — उनके पास ज़्यादा अनुभव है"), T("Wear two pairs of the wrong type", "தவறான வகையில் இரண்டு ஜோடி அணிவேன்", "गलत प्रकार के दो जोड़े पहनूँगा")],
          correct="a", explanation=T("Experience doesn't change the requirement; the task card does.", "அனுபவம் தேவையை மாற்றாது; பணி அட்டைதான் மாற்றும்.", "अनुभव आवश्यकता नहीं बदलता; टास्क कार्ड बदलता है।"))
    m.mcq(4, concept="ppe_task_requirements",
          stem=T("TC-31 asks for goggles AND a face shield. Is the shield alone enough?", "TC-31 கண்ணாடியும் முகக் கவசமும் கோருகிறது. கவசம் மட்டும் போதுமா?", "TC-31 गॉगल्स और फेस शील्ड दोनों माँगता है। क्या केवल शील्ड काफ़ी है?"),
          options=[T("Yes, it covers more", "ஆம், அது அதிகம் மூடுகிறது", "हाँ, यह ज़्यादा ढकती है"), T("No — the card lists both", "இல்லை — அட்டை இரண்டையும் பட்டியலிடுகிறது", "नहीं — कार्ड दोनों बताता है"), T("Only on cloudy days", "மேகமூட்டமான நாட்களில் மட்டும்", "केवल बादल वाले दिन")],
          correct="b", explanation=T("Each listed item is required; one does not replace another.", "பட்டியலிட்ட ஒவ்வொரு பொருளும் தேவை; ஒன்று மற்றொன்றை மாற்றாது.", "हर सूचीबद्ध वस्तु आवश्यक है; एक दूसरी की जगह नहीं लेती।"))
    m.spec(
        workplaceLocation="Fictional caustic dosing skid.",
        corePrinciple="Similar-looking PPE can have different specifications; match the task card's specification.",
        commonMisconceptions=["Gloves are gloves.", "Thicker means safer.", "A face shield replaces goggles."],
        criticalDecisions=["Confirm leather gloves", "Enter the skid before confirming"],
        assessmentCriteria={"correct": "Answer Joseph by the card; select chemical gloves, goggles, face shield; confirm; go to sample point."},
        note2="No chemical name, concentration or glove material standard is specified; labels are fictional.",
    )
    return m
