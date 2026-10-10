"""PPE Awareness · Level 1 — Suit Up for the Shift.

Story: Safety Officer Priya Nair hands the trainee a reviewed task card for
cleaning a strainer basket in the workshop yard. The trainee reads the card,
collects exactly what it lists from the PPE store and confirms before entering
the work zone. Learning: PPE follows the reviewed task requirements (from the
employer's assessment), not habit or guesswork.
"""
from authoring.dsl import Mission, T, decide, enter, inspect, not_done, select


def build() -> Mission:
    m = Mission(
        code="ppe1", id="og-ppe-l1-suit-up", category="og_ppe", level=1, minutes=10,
        title=T("Suit Up for the Shift", "பணிக்கு முன் தயாராகுங்கள்", "शिफ्ट के लिए तैयार हो जाइए"),
        subtitle=T("Read the task card, then pick your PPE", "பணி அட்டையைப் படியுங்கள், பின்னர் PPE-ஐத் தேர்வுசெய்யுங்கள்", "टास्क कार्ड पढ़ें, फिर अपना PPE चुनें"),
        description=T("Your first job needs the right protection — and the task card says what that is.", "உங்கள் முதல் வேலைக்குச் சரியான பாதுகாப்பு தேவை — அது என்ன என்று பணி அட்டை கூறுகிறது.", "आपके पहले काम के लिए सही सुरक्षा चाहिए — और टास्क कार्ड बताता है कि वह क्या है।"),
        location=T("PPE store · Workshop yard", "PPE களஞ்சியம் · பணிமனை முற்றம்", "PPE स्टोर · वर्कशॉप यार्ड"),
        site="workshop", spawn=(0, -23, 0), work_point=(0, -5, 0),
    )
    m.brief(
        lines=[
            T("Priya has a reviewed task card for cleaning strainer basket S-14.", "ஸ்ட்ரெய்னர் கூடை S-14-ஐச் சுத்தம் செய்வதற்கான மறுஆய்வு செய்யப்பட்ட பணி அட்டை பிரியாவிடம் உள்ளது.", "प्रिया के पास स्ट्रेनर बास्केट S-14 साफ़ करने का समीक्षित टास्क कार्ड है।"),
            T("The card lists the PPE for this task. Take exactly that from the PPE store.", "இந்தப் பணிக்கான PPE பட்டியல் அட்டையில் உள்ளது. அதையே PPE களஞ்சியத்திலிருந்து எடுங்கள்.", "कार्ड में इस काम के लिए PPE की सूची है। PPE स्टोर से ठीक वही लें।"),
        ],
        task=T("Collect the PPE listed on the task card and report to the work zone.", "பணி அட்டையில் உள்ள PPE-ஐ எடுத்துக்கொண்டு பணி மண்டலத்திற்குச் செல்லுங்கள்.", "टास्क कार्ड में लिखा PPE लें और कार्य क्षेत्र में रिपोर्ट करें।"),
        equipment=T("Task card TC-14, PPE store (fictional).", "பணி அட்டை TC-14, PPE களஞ்சியம் (கற்பனை).", "टास्क कार्ड TC-14, PPE स्टोर (काल्पनिक)।"),
        objective=T("Match your PPE to the reviewed task card before entering the zone.", "மண்டலத்திற்குள் நுழையும் முன் உங்கள் PPE-ஐ மறுஆய்வு செய்யப்பட்ட பணி அட்டையுடன் பொருத்துங்கள்.", "क्षेत्र में जाने से पहले अपने PPE को समीक्षित टास्क कार्ड से मिलाएँ।"),
        information=T("In real work, PPE comes from your employer's task assessment. This card is a fictional example.", "உண்மையான வேலையில், PPE உங்கள் முதலாளியின் பணி மதிப்பீட்டிலிருந்து வருகிறது. இந்த அட்டை ஒரு கற்பனை எடுத்துக்காட்டு.", "वास्तविक काम में PPE आपके नियोक्ता के कार्य आकलन से आता है। यह कार्ड एक काल्पनिक उदाहरण है।"),
        objectives=[
            T("Read task-specific PPE requirements.", "பணி சார்ந்த PPE தேவைகளைப் படித்தல்.", "कार्य-विशिष्ट PPE आवश्यकताएँ पढ़ना।"),
            T("Select the listed PPE and confirm before entering the zone.", "பட்டியலிடப்பட்ட PPE-ஐத் தேர்ந்தெடுத்து, மண்டலத்திற்குள் நுழையும் முன் உறுதிப்படுத்துதல்.", "सूचीबद्ध PPE चुनना और क्षेत्र में जाने से पहले पुष्टि करना।"),
        ],
    )
    m.dialogue("meet", [
        ("safety_officer", "friendly", T("Welcome! I'm Priya, Safety Officer. First job: strainer basket S-14.", "வருக! நான் பிரியா, பாதுகாப்பு அலுவலர். முதல் வேலை: ஸ்ட்ரெய்னர் கூடை S-14.", "स्वागत है! मैं प्रिया, सेफ्टी ऑफिसर। पहला काम: स्ट्रेनर बास्केट S-14।")),
        ("safety_officer", "neutral", T("The task card on the board tells you what PPE this job needs. Not what you like, not what you wore yesterday.", "இந்த வேலைக்கு என்ன PPE தேவை என்று பலகையில் உள்ள பணி அட்டை சொல்கிறது. உங்களுக்குப் பிடித்ததோ நேற்று அணிந்ததோ அல்ல.", "बोर्ड पर लगा टास्क कार्ड बताता है कि इस काम को कौन सा PPE चाहिए। न जो आपको पसंद, न जो कल पहना था।")),
        ("safety_officer", "serious", T("Card first, store second, zone last.", "முதலில் அட்டை, பின்னர் களஞ்சியம், கடைசியாக மண்டலம்.", "पहले कार्ड, फिर स्टोर, आख़िर में क्षेत्र।")),
    ])
    m.dialogue("revisit", [("safety_officer", "neutral", T("Card first, store second, zone last.", "முதலில் அட்டை, பின்னர் களஞ்சியம், கடைசியாக மண்டலம்.", "पहले कार्ड, फिर स्टोर, आख़िर में क्षेत्र।"))])
    m.dialogue("unsafe", [("safety_officer", "concerned", T("Stop at the barrier. Your PPE doesn't match the task card yet.", "தடுப்பிலேயே நில்லுங்கள். உங்கள் PPE இன்னும் பணி அட்டையுடன் பொருந்தவில்லை.", "बैरियर पर रुकिए। आपका PPE अभी टास्क कार्ड से मेल नहीं खाता।"))])
    m.dialogue("correct", [("safety_officer", "pleased", T("Card, store, zone — in that order. Nicely done.", "அட்டை, களஞ்சியம், மண்டலம் — அந்த வரிசையில். நன்றாகச் செய்தீர்கள்.", "कार्ड, स्टोर, क्षेत्र — इसी क्रम में। बढ़िया।"))])
    m.npc("safety_officer", -3.0, -12.0, 180, talk=[("meet", not_done("meet_safety_officer")), ("revisit", None)])

    m.zone("zone_strainer", T("Strainer S-14 work zone", "ஸ்ட்ரெய்னர் S-14 பணி மண்டலம்", "स्ट्रेनर S-14 कार्य क्षेत्र"), (-5, 5, 4, 11))
    m.decor("tape", 0, 7.5, w=10, d=7, color="#ffc23d")
    m.decor("sign", -1.6, 3.6, kind="mandatory", text="world.sign.ppe")
    m.decor("leak", 0, 8.0, state="off")
    m.decor("toolcart", 3.0, 8.5)
    m.decor("crate", -6.5, -2.0)
    m.obj("task_card", "board", -4.0, -4.0, kind="information", prompt="read",
          title=T("TASK CARD TC-14", "பணி அட்டை TC-14", "टास्क कार्ड TC-14"),
          lines=[T("Task: clean strainer basket S-14", "பணி: ஸ்ட்ரெய்னர் கூடை S-14 சுத்தம்", "कार्य: स्ट्रेनर बास्केट S-14 सफ़ाई"),
                 T("PPE: helmet, safety glasses, general gloves, coverall, safety boots", "PPE: தலைக்கவசம், பாதுகாப்புக் கண்ணாடி, பொதுக் கையுறை, மேலுடை, பாதுகாப்புக் காலணி", "PPE: हेलमेट, सेफ्टी चश्मा, सामान्य दस्ताने, कवरऑल, सेफ्टी बूट"),
                 T("Reviewed by: P. Nair (fictional)", "மறுஆய்வு: பி. நாயர் (கற்பனை)", "समीक्षक: पी. नायर (काल्पनिक)")],
          name=T("Task card TC-14", "பணி அட்டை TC-14", "टास्क कार्ड TC-14"),
          details=[T("Task: clean strainer basket S-14 (fictional).", "பணி: ஸ்ட்ரெய்னர் கூடை S-14 சுத்தம் (கற்பனை).", "कार्य: स्ट्रेनर बास्केट S-14 सफ़ाई (काल्पनिक)।"),
                   T("Required PPE: helmet, safety glasses, general-handling gloves, coverall, safety boots.", "தேவையான PPE: தலைக்கவசம், பாதுகாப்புக் கண்ணாடி, பொதுக் கையாளும் கையுறை, மேலுடை, பாதுகாப்புக் காலணி.", "आवश्यक PPE: हेलमेट, सेफ्टी चश्मा, सामान्य हैंडलिंग दस्ताने, कवरऑल, सेफ्टी बूट।"),
                   T("You are already wearing safety boots and a coverall.", "நீங்கள் ஏற்கனவே பாதுகாப்புக் காலணியும் மேலுடையும் அணிந்துள்ளீர்கள்.", "आप पहले से सेफ्टी बूट और कवरऑल पहने हुए हैं।")])
    m.obj("ppe_store", "locker", 3.5, -3.5, panel="inventory", prompt="open", kind="station", groups=["loadout"],
          name=T("PPE store", "PPE களஞ்சியம்", "PPE स्टोर"),
          details=[T("Take what the task card lists. Everything here is in good condition.", "பணி அட்டை பட்டியலிடுவதை எடுங்கள். இங்குள்ள அனைத்தும் நல்ல நிலையில் உள்ளன.", "जो टास्क कार्ड में है वह लें। यहाँ सब कुछ अच्छी हालत में है।")])
    m.item("helmet", "ppe_store", "helmet", T("Safety helmet", "பாதுகாப்புத் தலைக்கவசம்", "सेफ्टी हेलमेट"), T("Good condition.", "நல்ல நிலை.", "अच्छी हालत।"))
    m.item("glasses", "ppe_store", "glasses", T("Safety glasses", "பாதுகாப்புக் கண்ணாடி", "सेफ्टी चश्मा"), T("Good condition.", "நல்ல நிலை.", "अच्छी हालत।"))
    m.item("gloves_gen", "ppe_store", "gloves_leather", T("General-handling gloves", "பொதுக் கையாளும் கையுறை", "सामान्य हैंडलिंग दस्ताने"), T("Good condition.", "நல்ல நிலை.", "अच्छी हालत।"))
    m.item("welding_mask", "ppe_store", "welding_helmet", T("Welding helmet", "வெல்டிங் தலைக்கவசம்", "वेल्डिंग हेलमेट"), T("For welding tasks.", "வெல்டிங் பணிகளுக்கு.", "वेल्डिंग कार्यों के लिए।"))
    m.item("harness", "ppe_store", "harness", T("Full-body harness", "முழு உடல் சேணம்", "फुल-बॉडी हार्नेस"), T("For work at height.", "உயரத்தில் வேலைக்கு.", "ऊँचाई पर काम के लिए।"))
    m.group("loadout", T("Confirm your PPE for task TC-14", "TC-14 பணிக்கான உங்கள் PPE-ஐ உறுதிப்படுத்துங்கள்", "TC-14 कार्य के लिए अपना PPE पुष्ट करें"), [
        ("confirm", T("My PPE matches task card TC-14", "என் PPE பணி அட்டை TC-14-உடன் பொருந்துகிறது", "मेरा PPE टास्क कार्ड TC-14 से मेल खाता है")),
        ("skip_glasses", T("Skip the glasses — it's a quick job", "கண்ணாடியைத் தவிர்க்கவும் — இது விரைவான வேலை", "चश्मा छोड़ दें — काम जल्दी का है")),
    ])

    meet = m.meet("safety_officer")
    m.briefing(meet)
    m.step("read_card", title=T("Read task card TC-14", "பணி அட்டை TC-14-ஐப் படியுங்கள்", "टास्क कार्ड TC-14 पढ़ें"),
           instruction=T("Read the task card on the board west of the walkway.", "நடைபாதைக்கு மேற்கே உள்ள பலகையில் பணி அட்டையைப் படியுங்கள்.", "रास्ते के पश्चिम में बोर्ड पर टास्क कार्ड पढ़ें।"),
           trigger=inspect("task_card"), requires=["briefing"], points=10, concept="ppe_task_requirements", scene="documents", marker="task_card",
           hints=[T("The card is on the green-headed board.", "அட்டை பச்சைத் தலைப்புப் பலகையில் உள்ளது.", "कार्ड हरे शीर्ष वाले बोर्ड पर है।")])
    m.step("open_store", title=T("Open the PPE store", "PPE களஞ்சியத்தைத் திறவுங்கள்", "PPE स्टोर खोलें"),
           instruction=T("Go to the blue PPE store and open it.", "நீல PPE களஞ்சியத்திற்குச் சென்று திறவுங்கள்.", "नीले PPE स्टोर पर जाकर उसे खोलें।"),
           trigger=inspect("ppe_store"), requires=["read_card"], points=5, concept="ppe_task_requirements", scene="ppe", marker="ppe_store",
           hints=[T("The store is east of the walkway.", "களஞ்சியம் நடைபாதைக்குக் கிழக்கே உள்ளது.", "स्टोर रास्ते के पूर्व में है।")])
    for sid, item, title, instr in [
        ("take_helmet", "helmet", T("Take a safety helmet", "பாதுகாப்புத் தலைக்கவசத்தை எடுங்கள்", "सेफ्टी हेलमेट लें"),
         T("In the PPE store, press Select on the safety helmet.", "PPE களஞ்சியத்தில், பாதுகாப்புத் தலைக்கவசத்தின் 'தேர்ந்தெடு' அழுத்தவும்.", "PPE स्टोर में सेफ्टी हेलमेट पर 'चुनें' दबाएँ।")),
        ("take_glasses", "glasses", T("Take safety glasses", "பாதுகாப்புக் கண்ணாடியை எடுங்கள்", "सेफ्टी चश्मा लें"),
         T("In the PPE store, press Select on the safety glasses.", "PPE களஞ்சியத்தில், பாதுகாப்புக் கண்ணாடியின் 'தேர்ந்தெடு' அழுத்தவும்.", "PPE स्टोर में सेफ्टी चश्मे पर 'चुनें' दबाएँ।")),
        ("take_gloves", "gloves_gen", T("Take general-handling gloves", "பொதுக் கையாளும் கையுறைகளை எடுங்கள்", "सामान्य हैंडलिंग दस्ताने लें"),
         T("In the PPE store, press Select on the general-handling gloves.", "PPE களஞ்சியத்தில், பொதுக் கையாளும் கையுறைகளின் 'தேர்ந்தெடு' அழுத்தவும்.", "PPE स्टोर में सामान्य हैंडलिंग दस्तानों पर 'चुनें' दबाएँ।")),
    ]:
        m.step(sid, title=title, instruction=instr,
               trigger=select(item), requires=["open_store"], points=10, concept="ppe_task_requirements", scene="ppe", marker="ppe_store",
               hints=[T("Check the task card list.", "பணி அட்டைப் பட்டியலைச் சரிபாருங்கள்.", "टास्क कार्ड की सूची जाँचें।")])
    m.step("confirm", title=T("Confirm your PPE", "உங்கள் PPE-ஐ உறுதிப்படுத்துங்கள்", "अपना PPE पुष्ट करें"),
           instruction=T("Confirm your loadout in the PPE store.", "PPE களஞ்சியத்தில் உங்கள் தொகுப்பை உறுதிப்படுத்துங்கள்.", "PPE स्टोर में अपना सेट पुष्ट करें।"),
           trigger=decide("loadout", "confirm"), requires=["take_helmet", "take_glasses", "take_gloves"], points=15, concept="ppe_completeness", scene="decision", marker="ppe_store",
           mistake_if_early=T("Your loadout doesn't match the task card yet. Compare item by item.", "உங்கள் தொகுப்பு இன்னும் பணி அட்டையுடன் பொருந்தவில்லை. ஒவ்வொன்றாக ஒப்பிடுங்கள்.", "आपका सेट अभी टास्क कार्ड से मेल नहीं खाता। एक-एक कर मिलाएँ।"),
           hints=[T("Helmet, glasses and gloves — then confirm.", "தலைக்கவசம், கண்ணாடி, கையுறை — பின்னர் உறுதிப்படுத்துங்கள்.", "हेलमेट, चश्मा और दस्ताने — फिर पुष्टि करें।")])
    m.step("enter_zone", title=T("Enter the strainer work zone", "ஸ்ட்ரெய்னர் பணி மண்டலத்திற்குள் நுழையுங்கள்", "स्ट्रेनर कार्य क्षेत्र में जाएँ"),
           instruction=T("Walk into the taped work zone north of the store.", "களஞ்சியத்திற்கு வடக்கே நாடா கட்டிய பணி மண்டலத்திற்குள் செல்லுங்கள்.", "स्टोर के उत्तर में टेप लगे कार्य क्षेत्र में जाएँ।"),
           trigger=enter("zone_strainer"), requires=["confirm"], points=10, concept="ppe_completeness", scene="navigate", marker="zone_strainer",
           hints=[T("The zone is behind the yellow tape.", "மண்டலம் மஞ்சள் நாடாவுக்குப் பின்னால் உள்ளது.", "क्षेत्र पीली टेप के पीछे है।")])
    m.step("check_strainer", title=T("Check in at strainer S-14", "ஸ்ட்ரெய்னர் S-14-இல் பதிவு செய்யுங்கள்", "स्ट्रेनर S-14 पर पहुँचें"),
           instruction=T("Inspect the strainer housing to start the job.", "வேலையைத் தொடங்க ஸ்ட்ரெய்னர் உறையை ஆய்வு செய்யுங்கள்.", "काम शुरू करने के लिए स्ट्रेनर हाउसिंग का निरीक्षण करें।"),
           trigger=inspect("strainer"), requires=["enter_zone"], points=10, concept="situational_awareness", scene="inspect", marker="strainer",
           hints=[T("The strainer is the grey housing in the zone.", "ஸ்ட்ரெய்னர் மண்டலத்தில் உள்ள சாம்பல் நிற உறை.", "स्ट्रेनर क्षेत्र में धूसर हाउसिंग है।")])
    m.obj("strainer", "compressor", 0, 8.0, tag="S-14",
          name=T("Strainer S-14", "ஸ்ட்ரெய்னர் S-14", "स्ट्रेनर S-14"),
          details=[T("Strainer housing S-14. The cleaning job starts here once your PPE is right.", "ஸ்ட்ரெய்னர் உறை S-14. உங்கள் PPE சரியாக இருந்தால் சுத்தம் செய்யும் வேலை இங்கே தொடங்கும்.", "स्ट्रेनर हाउसिंग S-14। PPE सही होने पर सफ़ाई का काम यहाँ शुरू होता है।")])

    m.critical("enter_without_ppe", trigger=enter("zone_strainer"), condition=not_done("confirm"), concept="ppe_completeness", dialogue="unsafe",
               explanation=T("You entered the work zone before your PPE matched the task card.", "உங்கள் PPE பணி அட்டையுடன் பொருந்தும் முன் பணி மண்டலத்திற்குள் நுழைந்தீர்கள்.", "आपका PPE टास्क कार्ड से मेल खाने से पहले आप कार्य क्षेत्र में चले गए।"),
               missing=T("The PPE listed on task card TC-14, confirmed before entry.", "நுழைவதற்கு முன் உறுதிப்படுத்தப்பட்ட, பணி அட்டை TC-14-இல் உள்ள PPE.", "प्रवेश से पहले पुष्ट, टास्क कार्ड TC-14 में दिया PPE।"))
    m.critical("skip_eye_protection", trigger=decide("loadout", "skip_glasses"), concept="ppe_task_requirements", dialogue="unsafe",
               explanation=T("The task card requires safety glasses. A 'quick job' does not change the requirement.", "பணி அட்டை பாதுகாப்புக் கண்ணாடியைக் கோருகிறது. 'விரைவான வேலை' தேவையை மாற்றாது.", "टास्क कार्ड सेफ्टी चश्मा माँगता है। 'जल्दी का काम' आवश्यकता नहीं बदलता।"),
               missing=T("Every item listed on the task card.", "பணி அட்டையில் உள்ள ஒவ்வொரு பொருளும்.", "टास्क कार्ड की हर वस्तु।"))
    for item, en, ta, hi in [("welding_mask", "A welding helmet isn't on this task card. Take what the card lists.", "வெல்டிங் தலைக்கவசம் இந்தப் பணி அட்டையில் இல்லை. அட்டை பட்டியலிடுவதை எடுங்கள்.", "वेल्डिंग हेलमेट इस टास्क कार्ड में नहीं है। कार्ड में लिखा लें।"),
                             ("harness", "There's no work at height in this task. Take what the card lists.", "இந்தப் பணியில் உயரத்தில் வேலை இல்லை. அட்டை பட்டியலிடுவதை எடுங்கள்.", "इस काम में ऊँचाई पर काम नहीं है। कार्ड में लिखा लें।")]:
        m.mistake(f"extra_{item}", trigger=select(item), kind="advisory", concept="ppe_task_requirements", feedback=T(en, ta, hi))

    m.debrief(
        success=T("You read the card, took exactly what it listed and confirmed before entering.", "அட்டையைப் படித்து, அது பட்டியலிட்டதையே எடுத்து, நுழையும் முன் உறுதிப்படுத்தினீர்கள்.", "आपने कार्ड पढ़ा, ठीक वही लिया जो लिखा था और प्रवेश से पहले पुष्टि की।"),
        critical=T("The job started before the PPE matched the card. The card is the requirement, not a suggestion.", "PPE அட்டையுடன் பொருந்தும் முன் வேலை தொடங்கியது. அட்டை ஒரு தேவை, பரிந்துரை அல்ல.", "PPE कार्ड से मेल खाने से पहले काम शुरू हुआ। कार्ड एक आवश्यकता है, सुझाव नहीं।"),
        failed=T("Repeated unsafe choices ended the attempt. Card, store, zone — in that order.", "தொடர்ந்த பாதுகாப்பற்ற தேர்வுகள் முயற்சியை முடித்தன. அட்டை, களஞ்சியம், மண்டலம் — அந்த வரிசையில்.", "बार-बार असुरक्षित विकल्पों से प्रयास समाप्त हुआ। कार्ड, स्टोर, क्षेत्र — इसी क्रम में।"),
        lines=[
            ({"criticalRule": "enter_without_ppe"}, T("You walked into the zone before confirming your PPE.", "PPE-ஐ உறுதிப்படுத்தும் முன் மண்டலத்திற்குள் நுழைந்தீர்கள்.", "PPE पुष्ट करने से पहले आप क्षेत्र में गए।")),
            ({"criticalRule": "skip_eye_protection"}, T("You chose to skip required eye protection.", "தேவையான கண் பாதுகாப்பைத் தவிர்க்கத் தேர்ந்தெடுத்தீர்கள்.", "आपने आवश्यक आँखों की सुरक्षा छोड़ना चुना।")),
            ({"stepCompleted": "read_card"}, T("You started with the task card — the right first step.", "பணி அட்டையுடன் தொடங்கினீர்கள் — சரியான முதல் படி.", "आपने टास्क कार्ड से शुरू किया — सही पहला कदम।")),
            ({"stepCompleted": "confirm"}, T("You confirmed your loadout against the card before entering.", "நுழையும் முன் உங்கள் தொகுப்பை அட்டையுடன் உறுதிப்படுத்தினீர்கள்.", "प्रवेश से पहले आपने अपना सेट कार्ड से पुष्ट किया।")),
        ],
    )
    m.comic(T("CARD · STORE · ZONE", "அட்டை · களஞ்சியம் · மண்டலம்", "कार्ड · स्टोर · क्षेत्र"), [
        ("document_gap", T("The task card says what protection this job needs.", "இந்த வேலைக்கு என்ன பாதுகாப்பு தேவை என்று பணி அட்டை சொல்கிறது.", "टास्क कार्ड बताता है कि इस काम को कौन सी सुरक्षा चाहिए।")),
        ("ppe", T("Take exactly that — no more guessing.", "அதையே எடுங்கள் — ஊகிக்க வேண்டாம்.", "ठीक वही लें — अनुमान नहीं।")),
        ("stop_sign", T("No match, no entry.", "பொருந்தவில்லையா, நுழைவு இல்லை.", "मेल नहीं, प्रवेश नहीं।")),
    ])
    m.report(["read_card", "take_helmet", "take_glasses", "take_gloves"], ["confirm"])
    m.mcq(1, concept="ppe_task_requirements",
          stem=T("Where should your PPE requirements for a task come from?", "ஒரு பணிக்கான உங்கள் PPE தேவைகள் எங்கிருந்து வர வேண்டும்?", "किसी कार्य के लिए आपकी PPE आवश्यकताएँ कहाँ से आनी चाहिए?"),
          options=[T("The reviewed task assessment or card for that job", "அந்த வேலைக்கான மறுஆய்வு செய்யப்பட்ட பணி மதிப்பீடு அல்லது அட்டை", "उस काम का समीक्षित कार्य आकलन या कार्ड"),
                   T("Whatever you wore on your last job", "உங்கள் கடைசி வேலையில் அணிந்தவை", "जो आपने पिछले काम में पहना"),
                   T("Whatever is closest in the store", "களஞ்சியத்தில் அருகில் இருப்பவை", "स्टोर में जो सबसे पास हो")],
          correct="a", explanation=T("PPE is task-specific; the reviewed task requirements set it.", "PPE பணி சார்ந்தது; மறுஆய்வு செய்யப்பட்ட பணித் தேவைகள் அதைத் தீர்மானிக்கின்றன.", "PPE कार्य-विशिष्ट है; समीक्षित कार्य आवश्यकताएँ इसे तय करती हैं।"))
    m.mcq(2, concept="ppe_completeness",
          stem=T("When should you confirm your PPE?", "உங்கள் PPE-ஐ எப்போது உறுதிப்படுத்த வேண்டும்?", "अपना PPE कब पुष्ट करना चाहिए?"),
          options=[T("After the job starts", "வேலை தொடங்கிய பிறகு", "काम शुरू होने के बाद"), T("Before entering the work zone", "பணி மண்டலத்திற்குள் நுழையும் முன்", "कार्य क्षेत्र में जाने से पहले"), T("Only if a supervisor is watching", "மேற்பார்வையாளர் பார்த்தால் மட்டும்", "केवल अगर सुपरवाइज़र देख रहा हो")],
          correct="b", explanation=T("Protection has to be in place before you are exposed.", "நீங்கள் வெளிப்படும் முன் பாதுகாப்பு இருக்க வேண்டும்.", "जोखिम में आने से पहले सुरक्षा होनी चाहिए।"))
    m.mcq(3, concept="ppe_task_requirements",
          stem=T("The job is short. Can you skip an item the task card lists?", "வேலை குறுகியது. பணி அட்டை பட்டியலிடும் ஒரு பொருளைத் தவிர்க்கலாமா?", "काम छोटा है। क्या टास्क कार्ड की कोई वस्तु छोड़ सकते हैं?"),
          options=[T("Yes, if it takes less than five minutes", "ஆம், ஐந்து நிமிடங்களுக்குக் குறைவாக இருந்தால்", "हाँ, अगर पाँच मिनट से कम लगे"), T("Yes, if it is uncomfortable", "ஆம், அசௌகரியமாக இருந்தால்", "हाँ, अगर असुविधाजनक हो"), T("No — the requirement does not depend on how long the job takes", "இல்லை — தேவை வேலையின் நேரத்தைப் பொறுத்ததல்ல", "नहीं — आवश्यकता काम की अवधि पर निर्भर नहीं")],
          correct="c", explanation=T("Hazards don't wait for long jobs; the listed PPE applies throughout.", "அபாயங்கள் நீண்ட வேலைகளுக்காகக் காத்திருப்பதில்லை; பட்டியலிட்ட PPE முழுவதும் பொருந்தும்.", "खतरे लंबे काम का इंतज़ार नहीं करते; सूचीबद्ध PPE पूरे समय लागू है।"))
    m.mcq(4, concept="ppe_completeness",
          stem=T("You took a harness that the card doesn't list. What is the best view?", "அட்டையில் இல்லாத சேணத்தை எடுத்தீர்கள். சிறந்த பார்வை எது?", "आपने ऐसा हार्नेस लिया जो कार्ड में नहीं। सबसे अच्छा दृष्टिकोण क्या है?"),
          options=[T("Extra PPE replaces missing PPE", "கூடுதல் PPE இல்லாத PPE-க்கு மாற்று", "अतिरिक्त PPE गायब PPE की जगह लेता है"), T("Extra items don't make up for a missing listed item", "கூடுதல் பொருட்கள் இல்லாத பட்டியல் பொருளை ஈடுசெய்யாது", "अतिरिक्त वस्तुएँ गायब सूचीबद्ध वस्तु की भरपाई नहीं करतीं"), T("The more PPE the better, always", "எப்போதும் அதிக PPE சிறந்தது", "हमेशा जितना ज़्यादा PPE उतना अच्छा")],
          correct="b", explanation=T("What matters is the protection the task requires, item by item.", "முக்கியமானது பணிக்குத் தேவையான பாதுகாப்பு, ஒவ்வொன்றாக.", "मायने रखती है वह सुरक्षा जो काम माँगता है, एक-एक करके।"))
    m.spec(
        workplaceLocation="Fictional workshop yard and PPE store.",
        equipmentType="Strainer S-14; PPE store with helmet, glasses, gloves, welding helmet, harness.",
        corePrinciple="PPE follows the reviewed task requirements; confirm before entering the zone.",
        commonMisconceptions=["Short jobs need less PPE.", "More PPE is always better."],
        criticalDecisions=["Enter zone before confirming", "Skip eye protection"],
        assessmentCriteria={"correct": "Read card; select helmet, glasses, gloves; confirm; enter zone; check in at strainer."},
        note2="Task card contents are fictional teaching content, not an employer PPE assessment.",
    )
    return m
