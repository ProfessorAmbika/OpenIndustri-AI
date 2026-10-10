"""PPE Awareness · Level 5 — Ready for the Worksite? (competency challenge).

Story: The trainee and contractor Mani prepare for a filter change at the
fuel-oil skid. After the trainee has kitted up from the original task card,
the control room radios that the scope now includes opening a drain line
(line-breaking), and the safety officer posts a revised card requiring a face
shield and chemical-resistant gloves. One face shield in the store is cracked.
Mani has no eye protection. Linked decisions: buddy check and final readiness.
"""
from authoring.dsl import Mission, T, decide, enter, flag, inspect, not_done, select


def build() -> Mission:
    m = Mission(
        code="ppe5", id="og-ppe-l5-ready-for-worksite", category="og_ppe", level=5, minutes=16,
        title=T("Ready for the Worksite?", "பணியிடத்திற்குத் தயாரா?", "कार्यस्थल के लिए तैयार?"),
        subtitle=T("Competency challenge: requirements, condition and change", "திறன் சவால்: தேவைகள், நிலை, மாற்றம்", "दक्षता चुनौती: आवश्यकताएँ, स्थिति और बदलाव"),
        description=T("You're suited up. Then the job changes.", "நீங்கள் தயாராகிவிட்டீர்கள். பிறகு வேலை மாறுகிறது.", "आप तैयार हैं। फिर काम बदल जाता है।"),
        location=T("Fuel-oil filter skid · Workshop yard", "எரிபொருள் எண்ணெய் வடிகட்டி அமைப்பு · பணிமனை முற்றம்", "फ़्यूल-ऑयल फ़िल्टर स्किड · वर्कशॉप यार्ड"),
        site="workshop", time="dusk", spawn=(0, -23, 0), work_point=(0, -5, 0),
    )
    m.brief(
        lines=[
            T("Filter change on the fuel-oil skid with Mani. Kit up from task card TC-50.", "மணியுடன் எரிபொருள் எண்ணெய் அமைப்பில் வடிகட்டி மாற்றம். பணி அட்டை TC-50-இன்படி தயாராகுங்கள்.", "मणि के साथ फ़्यूल-ऑयल स्किड पर फ़िल्टर बदलना। टास्क कार्ड TC-50 से तैयार हों।"),
            T("Competency challenge: requirements can change. Stay alert.", "திறன் சவால்: தேவைகள் மாறலாம். விழிப்புடன் இருங்கள்.", "दक्षता चुनौती: आवश्यकताएँ बदल सकती हैं। सतर्क रहें।"),
        ],
        task=T("Be ready — properly — for the job as it actually is when you start.", "நீங்கள் தொடங்கும்போது உண்மையில் இருக்கும் வேலைக்கு — சரியாக — தயாராக இருங்கள்.", "शुरू करते समय काम जैसा वास्तव में है, उसके लिए — सही ढंग से — तैयार रहें।"),
        equipment=T("Filter skid F-50, PPE store, task card board (fictional).", "வடிகட்டி அமைப்பு F-50, PPE களஞ்சியம், பணி அட்டைப் பலகை (கற்பனை).", "फ़िल्टर स्किड F-50, PPE स्टोर, टास्क कार्ड बोर्ड (काल्पनिक)।"),
        objective=T("Match PPE to the current requirements, check its condition and check your buddy.", "PPE-ஐத் தற்போதைய தேவைகளுடன் பொருத்தி, அதன் நிலையையும் உங்கள் துணையையும் சரிபாருங்கள்.", "PPE को वर्तमान आवश्यकताओं से मिलाएँ, उसकी स्थिति और अपने साथी को जाँचें।"),
        information=T("Revised cards replace earlier ones. Requirements here are fictional teaching content.", "திருத்தப்பட்ட அட்டைகள் முந்தையவற்றை மாற்றுகின்றன. இங்குள்ள தேவைகள் கற்பனைக் கற்பித்தல் உள்ளடக்கம்.", "संशोधित कार्ड पहले वाले की जगह लेते हैं। यहाँ की आवश्यकताएँ काल्पनिक शिक्षण सामग्री हैं।"),
        objectives=[
            T("Re-check PPE when the task scope changes.", "பணி வரம்பு மாறும்போது PPE-ஐ மீண்டும் சரிபார்த்தல்.", "कार्य का दायरा बदलने पर PPE दोबारा जाँचना।"),
            T("Combine specification, condition and buddy checks before declaring ready.", "தயார் என்று அறிவிக்கும் முன் விவரக்குறிப்பு, நிலை, துணைச் சரிபார்ப்புகளை இணைத்தல்.", "तैयार घोषित करने से पहले विनिर्देश, स्थिति और साथी जाँच जोड़ना।"),
        ],
    )
    m.dialogue("meet", [
        ("safety_officer", "neutral", T("Filter change on F-50. Card TC-50 is on the board. Mani's your buddy today.", "F-50-இல் வடிகட்டி மாற்றம். TC-50 அட்டை பலகையில் உள்ளது. இன்று மணி உங்கள் துணை.", "F-50 पर फ़िल्टर बदलना। TC-50 कार्ड बोर्ड पर है। आज मणि आपका साथी है।")),
        ("safety_officer", "serious", T("This is your competency run. I'll only step in if you're about to get hurt.", "இது உங்கள் திறன் ஓட்டம். நீங்கள் காயமடையப் போகும்போது மட்டுமே தலையிடுவேன்.", "यह आपकी दक्षता परीक्षा है। मैं तभी दखल दूँगी जब आपको चोट लगने वाली हो।")),
    ])
    m.dialogue("scope_change", [
        ("operator", "serious", T("[Radio] Maintenance, control room. Scope change on F-50: you'll also open the drain line on the filter body.", "[வானொலி] பராமரிப்பு, கட்டுப்பாட்டு அறை. F-50-இல் வரம்பு மாற்றம்: வடிகட்டி உடலின் வடிகால் வரியையும் நீங்கள் திறப்பீர்கள்.", "[रेडियो] मेंटेनेंस, कंट्रोल रूम। F-50 का दायरा बदला: आप फ़िल्टर बॉडी की ड्रेन लाइन भी खोलेंगे।")),
        ("safety_officer", "serious", T("[Radio] Revised card TC-50 rev B is on the board. Check it before anyone starts.", "[வானொலி] திருத்தப்பட்ட அட்டை TC-50 rev B பலகையில் உள்ளது. யாரும் தொடங்கும் முன் சரிபாருங்கள்.", "[रेडियो] संशोधित कार्ड TC-50 rev B बोर्ड पर है। कोई शुरू करे उससे पहले जाँचें।")),
    ])
    m.dialogue("mani", [
        ("contractor", "friendly", T("Ready when you are! Glasses? Nah, left them in the van. It's just a filter.", "நீங்கள் தயாரானால் நானும் தயார்! கண்ணாடியா? இல்லை, வேனில் விட்டுவிட்டேன். இது வெறும் வடிகட்டி.", "जब आप तैयार, मैं तैयार! चश्मा? नहीं, वैन में छोड़ आया। बस फ़िल्टर ही तो है।"),
         [(T("Mani, the card lists eye protection for both of us. Grab a pair from the store first.", "மணி, அட்டை நம் இருவருக்கும் கண் பாதுகாப்பைப் பட்டியலிடுகிறது. முதலில் களஞ்சியத்திலிருந்து ஒன்றை எடுங்கள்.", "मणि, कार्ड हम दोनों के लिए आँखों की सुरक्षा बताता है। पहले स्टोर से एक ले लो।"), "buddy", "check", "mani_ok"),
          (T("Your call, Mani", "உங்கள் விருப்பம், மணி", "तुम्हारी मर्ज़ी, मणि"), "buddy", "ignore", None)]),
    ])
    m.dialogue("mani_ok", [("contractor", "pleased", T("Fair point. Grabbed some. Thanks for checking.", "சரியான கருத்து. எடுத்துக்கொண்டேன். சரிபார்த்ததற்கு நன்றி.", "सही बात। ले लिया। जाँचने के लिए धन्यवाद।"))])
    m.dialogue("unsafe", [("safety_officer", "concerned", T("Stop. That isn't ready for the job as it is now.", "நிறுத்துங்கள். இப்போதுள்ள வேலைக்கு அது தயாரானது அல்ல.", "रुकिए। यह अभी के काम के लिए तैयार नहीं है।"))])
    m.dialogue("correct", [("safety_officer", "pleased", T("Current card, serviceable kit, buddy checked. That's ready.", "தற்போதைய அட்டை, சேவைக்கு உகந்த உபகரணம், துணை சரிபார்க்கப்பட்டார். அதுதான் தயார்.", "वर्तमान कार्ड, उपयोग-योग्य सामान, साथी जाँचा। यही तैयार है।"))])
    m.npc("safety_officer", -3, -12, 180, talk=[("meet", not_done("meet_safety_officer"))])
    m.npc("contractor", 1.6, 1.5, 200, talk=[("mani", not_done("buddy")), ("mani_ok", None)], briefing=False)
    m.npc("operator", -9.0, -9.0, 120, briefing=False)

    m.zone("zone_skid", T("Filter skid F-50", "வடிகட்டி அமைப்பு F-50", "फ़िल्टर स्किड F-50"), (-4, 5, 5, 11))
    m.decor("tape", 0.5, 8.0, w=9, d=6, color="#ffc23d")
    m.decor("compressor", 0.5, 8.5, tag="F-50")
    m.decor("drum", 4.0, 9.5, count=2, color="#3a3a3a")
    m.decor("sign", -2.0, 4.6, kind="mandatory", text="world.sign.ppe")
    m.obj("task_board", "board", -4.0, -4.0, kind="information", prompt="read",
          title=T("TASK CARD TC-50", "பணி அட்டை TC-50", "टास्क कार्ड TC-50"),
          lines=[T("Filter change F-50", "F-50 வடிகட்டி மாற்றம்", "F-50 फ़िल्टर बदलना"), T("PPE: helmet, glasses, general gloves", "PPE: தலைக்கவசம், கண்ணாடி, பொதுக் கையுறை", "PPE: हेलमेट, चश्मा, सामान्य दस्ताने")],
          name=T("Task card board", "பணி அட்டைப் பலகை", "टास्क कार्ड बोर्ड"),
          details=[T("TC-50: Filter change F-50. PPE: helmet, safety glasses, general gloves.", "TC-50: F-50 வடிகட்டி மாற்றம். PPE: தலைக்கவசம், பாதுகாப்புக் கண்ணாடி, பொதுக் கையுறை.", "TC-50: F-50 फ़िल्टर बदलना। PPE: हेलमेट, सेफ्टी चश्मा, सामान्य दस्ताने।")])
    m.obj("ppe_store", "locker", 3.5, -3.5, panel="inventory", prompt="open", kind="station", groups=["ready"],
          name=T("PPE store", "PPE களஞ்சியம்", "PPE स्टोर"),
          details=[T("Check the specification and condition of every item.", "ஒவ்வொரு பொருளின் விவரக்குறிப்பையும் நிலையையும் சரிபாருங்கள்.", "हर वस्तु का विनिर्देश और स्थिति जाँचें।")])
    m.item("helmet", "ppe_store", "helmet", T("Safety helmet", "பாதுகாப்புத் தலைக்கவசம்", "सेफ्टी हेलमेट"), T("Good condition.", "நல்ல நிலை.", "अच्छी हालत।"))
    m.item("glasses", "ppe_store", "glasses", T("Safety glasses", "பாதுகாப்புக் கண்ணாடி", "सेफ्टी चश्मा"), T("Good condition.", "நல்ல நிலை.", "अच्छी हालत।"))
    m.item("gloves_gen", "ppe_store", "gloves_leather", T("General gloves", "பொதுக் கையுறை", "सामान्य दस्ताने"), T("Good condition. General handling only.", "நல்ல நிலை. பொதுக் கையாளுதலுக்கு மட்டும்.", "अच्छी हालत। केवल सामान्य हैंडलिंग।"))
    m.item("gloves_chem", "ppe_store", "gloves_chem", T("Chemical-resistant gloves", "வேதிப்பொருள்-எதிர்ப்புக் கையுறை", "रसायन-प्रतिरोधी दस्ताने"), T("Good condition. Label: chemical-resistant.", "நல்ல நிலை. குறி: வேதிப்பொருள்-எதிர்ப்பு.", "अच्छी हालत। लेबल: रसायन-प्रतिरोधी।"))
    m.item("shield_cracked", "ppe_store", "faceshield", T("Face shield (A)", "முகக் கவசம் (A)", "फेस शील्ड (A)"), T("Visor cracked across the middle.", "முகத்திரையின் நடுவில் விரிசல்.", "वाइज़र बीच से टूटा हुआ।"), defect=True)
    m.item("shield_ok", "ppe_store", "faceshield", T("Face shield (B)", "முகக் கவசம் (B)", "फेस शील्ड (B)"), T("Good condition.", "நல்ல நிலை.", "अच्छी हालत।"))
    m.group("buddy", T("Mani has no eye protection. Your response?", "மணியிடம் கண் பாதுகாப்பு இல்லை. உங்கள் பதில்?", "मणि के पास आँखों की सुरक्षा नहीं। आपका जवाब?"), [
        ("check", T("Point it out and wait for him", "சுட்டிக்காட்டி அவருக்காகக் காத்திருத்தல்", "बताकर उसका इंतज़ार करना")),
        ("ignore", T("Leave it to him", "அவரிடமே விடுதல்", "उस पर छोड़ना")),
    ])
    m.group("ready", T("Declare readiness for F-50", "F-50-க்குத் தயார்நிலையை அறிவியுங்கள்", "F-50 के लिए तैयारी घोषित करें"), [
        ("ready_rev_b", T("Ready — kit matches TC-50 rev B and has been inspected", "தயார் — உபகரணம் TC-50 rev B-உடன் பொருந்துகிறது, ஆய்வு செய்யப்பட்டது", "तैयार — सामान TC-50 rev B से मेल खाता है और जाँचा गया है")),
        ("ready_original", T("Ready — kit matches the original TC-50", "தயார் — உபகரணம் அசல் TC-50-உடன் பொருந்துகிறது", "तैयार — सामान मूल TC-50 से मेल खाता है")),
    ])

    meet = m.meet("safety_officer")
    m.briefing(meet)
    m.step("read_card", title=T("Read task card TC-50", "பணி அட்டை TC-50-ஐப் படியுங்கள்", "टास्क कार्ड TC-50 पढ़ें"), instruction=T("Read the card on the task board.", "பணிப் பலகையில் உள்ள அட்டையைப் படியுங்கள்.", "टास्क बोर्ड का कार्ड पढ़ें।"),
           trigger=inspect("task_board"), requires=["briefing"], points=5, concept="ppe_task_requirements", scene="documents",
           hints=[T("West of the walkway.", "நடைபாதைக்கு மேற்கே.", "रास्ते के पश्चिम में।")])
    m.step("open_store", title=T("Open the PPE store", "PPE களஞ்சியத்தைத் திறவுங்கள்", "PPE स्टोर खोलें"), instruction=T("Open the store.", "களஞ்சியத்தைத் திறவுங்கள்.", "स्टोर खोलें।"),
           trigger=inspect("ppe_store"), requires=["read_card"], points=5, concept="ppe_task_requirements", scene="ppe",
           hints=[T("East of the walkway.", "நடைபாதைக்குக் கிழக்கே.", "रास्ते के पूर्व में।")])
    m.step("take_helmet", title=T("Helmet", "தலைக்கவசம்", "हेलमेट"), instruction=T("Select a helmet.", "தலைக்கவசத்தைத் தேர்ந்தெடுங்கள்.", "हेलमेट चुनें।"),
           trigger=select("helmet"), requires=["open_store"], points=5, concept="ppe_task_requirements", scene="ppe", hints=[T("On the card.", "அட்டையில் உள்ளது.", "कार्ड में है।")])
    m.step("take_glasses", title=T("Eye protection", "கண் பாதுகாப்பு", "आँखों की सुरक्षा"), instruction=T("Select safety glasses.", "பாதுகாப்புக் கண்ணாடியைத் தேர்ந்தெடுங்கள்.", "सेफ्टी चश्मा चुनें।"),
           trigger=select("glasses"), requires=["open_store"], points=5, concept="ppe_task_requirements", scene="ppe", hints=[T("On the card.", "அட்டையில் உள்ளது.", "कार्ड में है।")])
    m.step("take_gloves_gen", title=T("Gloves", "கையுறை", "दस्ताने"), instruction=T("Select the gloves the card lists.", "அட்டை பட்டியலிடும் கையுறைகளைத் தேர்ந்தெடுங்கள்.", "कार्ड में लिखे दस्ताने चुनें।"),
           trigger=select("gloves_gen"), requires=["open_store"], points=5, concept="ppe_task_requirements", scene="ppe", hints=[T("On the card.", "அட்டையில் உள்ளது.", "कार्ड में है।")])
    m.step("reread_card", title=T("Read the revised task card", "திருத்தப்பட்ட பணி அட்டையைப் படியுங்கள்", "संशोधित टास्क कार्ड पढ़ें"), instruction=T("The scope changed. Read TC-50 rev B on the board.", "வரம்பு மாறியது. பலகையில் TC-50 rev B-ஐப் படியுங்கள்.", "दायरा बदल गया। बोर्ड पर TC-50 rev B पढ़ें।"),
           trigger=inspect("task_board"), requires=["take_helmet", "take_glasses", "take_gloves_gen"], points=10, concept="change_reassessment", scene="change",
           hints=[T("A scope change can change the PPE.", "வரம்பு மாற்றம் PPE-ஐ மாற்றலாம்.", "दायरा बदलने से PPE बदल सकता है।")])
    m.step("take_gloves_chem", title=T("Gloves for line-breaking", "வரி திறப்புக்கான கையுறை", "लाइन ब्रेकिंग के लिए दस्ताने"), instruction=T("Select the gloves rev B requires.", "rev B கோரும் கையுறைகளைத் தேர்ந்தெடுங்கள்.", "rev B में माँगे गए दस्ताने चुनें।"),
           trigger=select("gloves_chem"), requires=["reread_card"], points=10, concept="ppe_specification", scene="ppe", hints=[T("Read the labels.", "குறிகளைப் படியுங்கள்.", "लेबल पढ़ें।")])
    m.step("flag_shield", title=T("Check the face shields", "முகக் கவசங்களைச் சரிபாருங்கள்", "फेस शील्ड जाँचें"), instruction=T("Report the damaged face shield.", "சேதமடைந்த முகக் கவசத்தைத் தெரிவியுங்கள்.", "क्षतिग्रस्त फेस शील्ड रिपोर्ट करें।"),
           trigger=flag("shield_cracked"), requires=["reread_card"], points=10, concept="ppe_condition", scene="inspect", hints=[T("Two shields; one is not serviceable.", "இரண்டு கவசங்கள்; ஒன்று சேவைக்கு உகந்ததல்ல.", "दो शील्ड; एक उपयोग-योग्य नहीं।")])
    m.step("take_shield", title=T("Face shield", "முகக் கவசம்", "फेस शील्ड"), instruction=T("Select the serviceable face shield.", "சேவைக்கு உகந்த முகக் கவசத்தைத் தேர்ந்தெடுங்கள்.", "उपयोग-योग्य फेस शील्ड चुनें।"),
           trigger=select("shield_ok"), requires=["flag_shield"], points=10, concept="ppe_condition", scene="ppe", hints=[T("Shield B.", "கவசம் B.", "शील्ड B।")])
    m.step("buddy", title=T("Buddy check with Mani", "மணியுடன் துணைச் சரிபார்ப்பு", "मणि के साथ बडी चेक"), instruction=T("Talk to Mani before declaring ready.", "தயார் என்று அறிவிக்கும் முன் மணியுடன் பேசுங்கள்.", "तैयार घोषित करने से पहले मणि से बात करें।"),
           trigger=decide("buddy", "check"), requires=["reread_card"], points=10, concept="ppe_completeness", scene="communicate", hints=[T("Look at what Mani is wearing.", "மணி என்ன அணிந்துள்ளார் என்று பாருங்கள்.", "देखें मणि ने क्या पहना है।")])
    m.step("declare", title=T("Declare readiness", "தயார்நிலையை அறிவியுங்கள்", "तैयारी घोषित करें"), instruction=T("Declare readiness at the PPE store.", "PPE களஞ்சியத்தில் தயார்நிலையை அறிவியுங்கள்.", "PPE स्टोर पर तैयारी घोषित करें।"),
           trigger=decide("ready", "ready_rev_b"), requires=["take_gloves_chem", "take_shield", "buddy"], points=15, concept="ppe_completeness", scene="decision",
           mistake_if_early=T("Something on the current card or in your buddy check is still open.", "தற்போதைய அட்டையிலோ துணைச் சரிபார்ப்பிலோ ஏதோ இன்னும் நிலுவையில் உள்ளது.", "वर्तमान कार्ड या बडी चेक में कुछ अभी बाकी है।"),
           hints=[T("Current card + inspected kit + buddy.", "தற்போதைய அட்டை + ஆய்வு செய்த உபகரணம் + துணை.", "वर्तमान कार्ड + जाँचा सामान + साथी।")])
    m.step("enter_skid", title=T("Go to filter skid F-50", "வடிகட்டி அமைப்பு F-50-க்குச் செல்லுங்கள்", "फ़िल्टर स्किड F-50 पर जाएँ"), instruction=T("Enter the skid area to start.", "தொடங்க அமைப்புப் பகுதிக்குள் செல்லுங்கள்.", "शुरू करने के लिए स्किड क्षेत्र में जाएँ।"),
           trigger=enter("zone_skid"), requires=["declare"], points=10, concept="situational_awareness", scene="navigate", hints=[T("Behind the yellow tape.", "மஞ்சள் நாடாவுக்குப் பின்னால்.", "पीली टेप के पीछे।")])
    m.event("scope_change", {"completed": ["take_helmet", "take_glasses", "take_gloves_gen"]}, [
        {"type": "sound", "sound": "radio"},
        {"type": "banner", "text": T("Scope change: drain line opening added", "வரம்பு மாற்றம்: வடிகால் வரி திறப்பு சேர்க்கப்பட்டது", "दायरा बदला: ड्रेन लाइन खोलना जोड़ा गया"), "style": "danger"},
        {"type": "dialogue", "name": "scope_change"},
        {"type": "details", "object": "task_board", "details": [
            T("TC-50 rev B: filter change F-50 + open drain line (line-breaking).", "TC-50 rev B: F-50 வடிகட்டி மாற்றம் + வடிகால் வரி திறப்பு (வரி திறப்பு).", "TC-50 rev B: F-50 फ़िल्टर बदलना + ड्रेन लाइन खोलना (लाइन ब्रेकिंग)।"),
            T("PPE: helmet, glasses, CHEMICAL-RESISTANT gloves, FACE SHIELD.", "PPE: தலைக்கவசம், கண்ணாடி, வேதிப்பொருள்-எதிர்ப்புக் கையுறை, முகக் கவசம்.", "PPE: हेलमेट, चश्मा, रसायन-प्रतिरोधी दस्ताने, फेस शील्ड।"),
            T("Rev A is withdrawn.", "Rev A திரும்பப் பெறப்பட்டது.", "Rev A वापस लिया गया।")]},
    ], delay=0.5)

    m.critical("ready_old_card", trigger=decide("ready", "ready_original"), concept="change_reassessment", dialogue="unsafe",
               explanation=T("You declared ready against a withdrawn card. The job now includes line-breaking.", "திரும்பப் பெறப்பட்ட அட்டையின்படி தயார் என்று அறிவித்தீர்கள். வேலை இப்போது வரி திறப்பையும் உள்ளடக்கியது.", "आपने वापस लिए गए कार्ड के आधार पर तैयार घोषित किया। काम में अब लाइन ब्रेकिंग शामिल है।"),
               missing=T("PPE matching TC-50 rev B.", "TC-50 rev B-உடன் பொருந்தும் PPE.", "TC-50 rev B से मेल खाता PPE।"))
    m.critical("cracked_shield", trigger=select("shield_cracked"), concept="ppe_condition", dialogue="unsafe",
               explanation=T("You selected a face shield with a cracked visor.", "முகத்திரையில் விரிசல் உள்ள முகக் கவசத்தைத் தேர்ந்தெடுத்தீர்கள்.", "आपने टूटे वाइज़र वाली फेस शील्ड चुनी।"),
               missing=T("A serviceable face shield.", "சேவைக்கு உகந்த முகக் கவசம்.", "उपयोग-योग्य फेस शील्ड।"))
    m.critical("enter_early", trigger=enter("zone_skid"), condition=not_done("declare"), concept="ppe_completeness", dialogue="unsafe",
               explanation=T("You entered the skid area before declaring readiness.", "தயார்நிலையை அறிவிக்கும் முன் அமைப்புப் பகுதிக்குள் நுழைந்தீர்கள்.", "तैयारी घोषित करने से पहले आप स्किड क्षेत्र में गए।"),
               missing=T("A completed readiness check.", "முடிக்கப்பட்ட தயார்நிலைச் சரிபார்ப்பு.", "पूरी तैयारी जाँच।"))
    m.mistake("ignore_buddy", trigger=decide("buddy", "ignore"), kind="incorrect_decision", concept="ppe_completeness",
              feedback=T("A buddy check is a check, not a suggestion. Talk to Mani again.", "துணைச் சரிபார்ப்பு ஒரு சரிபார்ப்பு, பரிந்துரை அல்ல. மணியுடன் மீண்டும் பேசுங்கள்.", "बडी चेक एक जाँच है, सुझाव नहीं। मणि से फिर बात करें।"))
    m.mistake("wrong_defect", trigger={"type": "evidence_flagged"}, kind="incorrect_decision", concept="ppe_condition",
              feedback=T("That item is serviceable.", "அந்தப் பொருள் சேவைக்கு உகந்தது.", "वह वस्तु उपयोग-योग्य है।"))

    m.debrief(
        success=T("You re-checked when the scope changed, rejected the cracked shield and checked your buddy. Ready means ready.", "வரம்பு மாறியபோது மீண்டும் சரிபார்த்து, விரிசல் கவசத்தை நிராகரித்து, துணையைச் சரிபார்த்தீர்கள். தயார் என்றால் தயார்.", "दायरा बदलने पर आपने दोबारा जाँचा, टूटी शील्ड ठुकराई और साथी जाँचा। तैयार मतलब तैयार।"),
        critical=T("Readiness was declared against outdated or damaged kit. Re-check whenever the job changes.", "காலாவதியான அல்லது சேதமடைந்த உபகரணத்துடன் தயார்நிலை அறிவிக்கப்பட்டது. வேலை மாறும்போதெல்லாம் மீண்டும் சரிபாருங்கள்.", "पुराने या क्षतिग्रस्त सामान के साथ तैयारी घोषित हुई। काम बदलने पर हर बार दोबारा जाँचें।"),
        failed=T("Repeated unsafe choices ended the challenge.", "தொடர்ந்த பாதுகாப்பற்ற தேர்வுகள் சவாலை முடித்தன.", "बार-बार असुरक्षित विकल्पों से चुनौती समाप्त हुई।"),
        lines=[
            ({"criticalRule": "ready_old_card"}, T("You declared ready against the withdrawn card.", "திரும்பப் பெறப்பட்ட அட்டையின்படி தயார் என்று அறிவித்தீர்கள்.", "आपने वापस लिए गए कार्ड के अनुसार तैयार घोषित किया।")),
            ({"criticalRule": "cracked_shield"}, T("You selected a cracked face shield.", "விரிசல் முகக் கவசத்தைத் தேர்ந்தெடுத்தீர்கள்.", "आपने टूटी फेस शील्ड चुनी।")),
            ({"stepCompleted": "reread_card"}, T("You went back to the board when the scope changed.", "வரம்பு மாறியபோது பலகைக்குத் திரும்பிச் சென்றீர்கள்.", "दायरा बदलने पर आप बोर्ड पर लौटे।")),
            ({"stepCompleted": "buddy"}, T("You checked your buddy, not just yourself.", "உங்களை மட்டுமல்ல, உங்கள் துணையையும் சரிபார்த்தீர்கள்.", "आपने केवल खुद को नहीं, साथी को भी जाँचा।")),
        ],
    )
    m.comic(T("READY MEANS READY NOW", "தயார் என்றால் இப்போதே தயார்", "तैयार मतलब अभी तैयार"), [
        ("change", T("The job changed, so the requirement changed.", "வேலை மாறியது, எனவே தேவையும் மாறியது.", "काम बदला, तो आवश्यकता बदली।")),
        ("torn_glove", T("Check condition, not just presence.", "இருப்பை மட்டுமல்ல, நிலையையும் சரிபாருங்கள்.", "केवल मौजूदगी नहीं, स्थिति भी जाँचें।")),
        ("team", T("Ready includes your buddy.", "தயார் என்பதில் உங்கள் துணையும் அடங்குவார்.", "तैयार में आपका साथी भी शामिल है।")),
    ])
    m.report(["read_card", "reread_card", "take_gloves_chem", "flag_shield", "take_shield"], ["buddy", "declare"])
    m.mcq(1, concept="change_reassessment",
          stem=T("You're kitted up, then the task scope changes. What now?", "நீங்கள் தயாராகிவிட்டீர்கள், பிறகு பணி வரம்பு மாறுகிறது. இப்போது என்ன?", "आप तैयार हैं, फिर कार्य का दायरा बदलता है। अब क्या?"),
          options=[T("Carry on — you already checked", "தொடருங்கள் — ஏற்கனவே சரிபார்த்தீர்கள்", "जारी रखें — पहले ही जाँच लिया"), T("Re-check PPE against the revised requirements", "திருத்தப்பட்ட தேவைகளுடன் PPE-ஐ மீண்டும் சரிபாருங்கள்", "संशोधित आवश्यकताओं से PPE दोबारा जाँचें"), T("Ask Mani what he thinks", "மணியிடம் அவர் கருத்தைக் கேளுங்கள்", "मणि से उसकी राय पूछें")],
          correct="b", explanation=T("A changed scope can bring new hazards and new PPE.", "மாறிய வரம்பு புதிய அபாயங்களையும் புதிய PPE-யையும் கொண்டுவரலாம்.", "बदला दायरा नए खतरे और नया PPE ला सकता है।"))
    m.mcq(2, concept="ppe_condition",
          stem=T("Two face shields are available; one is cracked. Which do you take?", "இரண்டு முகக் கவசங்கள் உள்ளன; ஒன்றில் விரிசல். எதை எடுப்பீர்கள்?", "दो फेस शील्ड हैं; एक टूटी है। कौन सी लेंगे?"),
          options=[T("The serviceable one, and report the cracked one", "சேவைக்கு உகந்ததை எடுத்து, விரிசலானதைத் தெரிவிப்பேன்", "उपयोग-योग्य वाली, और टूटी की रिपोर्ट"), T("Either — both are face shields", "எதுவும் — இரண்டும் முகக் கவசங்கள்தான்", "कोई भी — दोनों फेस शील्ड हैं"), T("The cracked one, so the good one is saved", "நல்லது மிச்சமாக, விரிசலானதை", "टूटी वाली, ताकि अच्छी बची रहे")],
          correct="a", explanation=T("Damaged PPE is reported and not used.", "சேதமடைந்த PPE தெரிவிக்கப்படுகிறது, பயன்படுத்தப்படுவதில்லை.", "क्षतिग्रस्त PPE रिपोर्ट होता है, इस्तेमाल नहीं।"))
    m.mcq(3, concept="ppe_completeness",
          stem=T("What does a buddy check add?", "துணைச் சரிபார்ப்பு எதைச் சேர்க்கிறது?", "बडी चेक क्या जोड़ता है?"),
          options=[T("Nothing if you checked yourself", "நீங்கள் உங்களைச் சரிபார்த்திருந்தால் எதுவுமில்லை", "कुछ नहीं, अगर आपने खुद को जाँचा"), T("A second set of eyes on both people's readiness", "இருவரின் தயார்நிலையின் மீது இரண்டாவது பார்வை", "दोनों की तैयारी पर एक दूसरी नज़र"), T("It replaces the task card", "அது பணி அட்டையை மாற்றுகிறது", "यह टास्क कार्ड की जगह लेता है")],
          correct="b", explanation=T("People miss their own gaps; a buddy catches them.", "மக்கள் தங்கள் குறைகளைத் தவறவிடுவார்கள்; துணை அவற்றைப் பிடிப்பார்.", "लोग अपनी कमियाँ नहीं देखते; साथी पकड़ लेता है।"))
    m.mcq(4, concept="ppe_specification",
          stem=T("Rev B adds line-breaking. Are general gloves still enough?", "Rev B வரி திறப்பைச் சேர்க்கிறது. பொதுக் கையுறைகள் இன்னும் போதுமா?", "Rev B लाइन ब्रेकिंग जोड़ता है। क्या सामान्य दस्ताने अब भी काफ़ी हैं?"),
          options=[T("Yes, gloves are gloves", "ஆம், கையுறை என்றால் கையுறைதான்", "हाँ, दस्ताने तो दस्ताने हैं"), T("No — rev B specifies chemical-resistant gloves", "இல்லை — rev B வேதிப்பொருள்-எதிர்ப்புக் கையுறைகளைக் குறிப்பிடுகிறது", "नहीं — rev B रसायन-प्रतिरोधी दस्ताने बताता है"), T("Only if they are new", "புதியவை என்றால் மட்டும்", "केवल अगर नए हों")],
          correct="b", explanation=T("The current card's specification decides.", "தற்போதைய அட்டையின் விவரக்குறிப்பே தீர்மானிக்கிறது.", "वर्तमान कार्ड का विनिर्देश तय करता है।"))
    m.spec(
        workplaceLocation="Fictional fuel-oil filter skid, dusk.",
        corePrinciple="Readiness = current requirements + serviceable kit + buddy check; re-check on scope change.",
        commonMisconceptions=["Once checked, always ready.", "Any face shield will do.", "My buddy's PPE is their business."],
        criticalDecisions=["Declare ready on the withdrawn card", "Select the cracked shield", "Enter before declaring"],
        scenarioChange="After initial kit selection, a scripted radio call adds line-breaking and posts rev B.",
        assessmentCriteria={"correct": "Kit up from rev A; re-read rev B; chemical gloves; flag cracked shield; take shield B; buddy check; declare; enter."},
    )
    return m
