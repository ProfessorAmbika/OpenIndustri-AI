"""Hazard Recognition · Level 4 — The Changed Work Area.

Story: R. Kannan briefs the trainee on a straightforward valve-gland check at
the tank-farm manifold. While the trainee is on the job, a contract crew
arrives: a scaffold goes up beside the manifold, a water-jetting hose is laid
across the walkway and a drain cover is lifted. Nothing in the briefing
covered this. Learning: when the work area changes after the briefing, the
original assessment no longer covers it — pause and get it reviewed.
"""
from authoring.dsl import Mission, T, decide, enter, inspect, not_done, talk, tool


def build() -> Mission:
    m = Mission(
        code="hr4", id="og-hazrec-l4-changed-work-area", category="og_hazard_recognition", level=4, minutes=15,
        title=T("The Changed Work Area", "மாறிய பணிப் பகுதி", "बदला हुआ कार्य क्षेत्र"),
        subtitle=T("The briefing was right — an hour ago", "விளக்கம் சரியானதுதான் — ஒரு மணி நேரத்திற்கு முன்பு", "ब्रीफिंग सही थी — एक घंटे पहले"),
        description=T("Halfway through a simple check, the area around you changes.", "ஒரு எளிய சரிபார்ப்பின் நடுவில், உங்களைச் சுற்றியுள்ள பகுதி மாறுகிறது.", "एक सामान्य जाँच के बीच में आपके आसपास का क्षेत्र बदल जाता है।"),
        location=T("Tank farm manifold · North bund", "தொட்டிப் பண்ணை மேனிஃபோல்ட் · வடக்கு அணை", "टैंक फार्म मैनिफोल्ड · उत्तरी बंड"),
        site="tank_farm", time="overcast", spawn=(0, -23, 0), work_point=(0, -3, 0),
    )
    m.brief(
        lines=[
            T("Kannan wants the gland on manifold valve MV-7 checked for weeping.", "மேனிஃபோல்ட் வால்வு MV-7-இன் கிளாண்டில் கசிவு உள்ளதா என்று கண்ணன் சரிபார்க்கச் சொல்கிறார்.", "कन्नन चाहते हैं कि मैनिफोल्ड वाल्व MV-7 के ग्लैंड में रिसाव जाँचा जाए।"),
            T("The area was walked this morning: clear, dry and quiet.", "இன்று காலை பகுதி சுற்றிப் பார்க்கப்பட்டது: தெளிவாக, உலர்ந்து, அமைதியாக இருந்தது.", "आज सुबह क्षेत्र देखा गया: साफ़, सूखा और शांत।"),
        ],
        task=T("Inspect valve MV-7 and the manifold area.", "வால்வு MV-7-ஐயும் மேனிஃபோல்ட் பகுதியையும் ஆய்வு செய்யுங்கள்.", "वाल्व MV-7 और मैनिफोल्ड क्षेत्र का निरीक्षण करें।"),
        equipment=T("Manifold valve MV-7 (fictional).", "மேனிஃபோல்ட் வால்வு MV-7 (கற்பனை).", "मैनिफोल्ड वाल्व MV-7 (काल्पनिक)।"),
        objective=T("Complete the check — and notice if the conditions you were briefed on change.", "சரிபார்ப்பை முடியுங்கள் — உங்களுக்கு விளக்கப்பட்ட நிலைமைகள் மாறினால் கவனியுங்கள்.", "जाँच पूरी करें — और ध्यान दें कि ब्रीफिंग वाली परिस्थितियाँ बदलती हैं या नहीं।"),
        information=T("Area assessment AA-12 was written at 07:00 for an empty work area.", "பகுதி மதிப்பீடு AA-12 காலை 07:00-க்கு வெற்றுப் பணிப் பகுதிக்காக எழுதப்பட்டது.", "क्षेत्र आकलन AA-12 सुबह 07:00 बजे खाली कार्य क्षेत्र के लिए लिखा गया था।"),
        objectives=[
            T("Recognise when the work area no longer matches the briefing.", "பணிப் பகுதி விளக்கத்துடன் பொருந்தாதபோது அடையாளம் காணுங்கள்.", "पहचानें कि कब कार्य क्षेत्र ब्रीफिंग से मेल नहीं खाता।"),
            T("Pause and request a fresh review instead of carrying on.", "தொடர்வதற்குப் பதிலாக நிறுத்தி புதிய மறுஆய்வைக் கோருங்கள்.", "जारी रखने के बजाय रुकें और नई समीक्षा माँगें।"),
        ],
    )
    m.dialogue("meet", [
        ("supervisor", "friendly", T("Simple one today. Look at the gland on MV-7, tell me if it's weeping.", "இன்று எளிய வேலை. MV-7-இன் கிளாண்டைப் பார்த்து, கசிகிறதா என்று சொல்லுங்கள்.", "आज आसान काम है। MV-7 का ग्लैंड देखकर बताइए कि रिस रहा है या नहीं।")),
        ("supervisor", "neutral", T("I walked the area at seven. Nothing else going on up there.", "ஏழு மணிக்கு பகுதியைச் சுற்றிப் பார்த்தேன். அங்கே வேறு எதுவும் நடக்கவில்லை.", "मैंने सात बजे क्षेत्र देखा था। वहाँ और कुछ नहीं चल रहा।")),
    ])
    m.dialogue("revisit", [("supervisor", "neutral", T("If anything up there doesn't match what I told you, come and tell me.", "அங்கே எதுவும் நான் சொன்னதுடன் பொருந்தவில்லை என்றால், வந்து சொல்லுங்கள்.", "अगर वहाँ कुछ भी मेरी बताई बात से मेल न खाए, तो आकर बताइए।"))])
    m.dialogue("arrival", [
        ("self", "concerned", T("Wait — that scaffold wasn't here a minute ago. And who laid that hose?", "பொறுங்கள் — அந்தச் சாரம் ஒரு நிமிடம் முன்பு இங்கே இல்லை. அந்தக் குழாயை யார் போட்டது?", "रुको — वह मचान एक मिनट पहले यहाँ नहीं था। और वह होज़ किसने बिछाई?")),
    ])
    m.dialogue("crew", [
        ("contractor", "friendly", T("Morning! We're jetting the bund drains. Scaffold's for the tank nozzle.", "காலை வணக்கம்! நாங்கள் அணை வடிகால்களை நீர் அழுத்தத்தில் சுத்தம் செய்கிறோம். சாரம் தொட்டி நாசிலுக்காக.", "सुप्रभात! हम बंड की नालियाँ जेटिंग से साफ़ कर रहे हैं। मचान टैंक नोज़ल के लिए है।")),
        ("contractor", "neutral", T("Nobody told you? Huh. Our permit says the area was clear.", "உங்களிடம் யாரும் சொல்லவில்லையா? ம்ம். எங்கள் அனுமதிச்சீட்டில் பகுதி காலியாக இருந்தது என்று உள்ளது.", "किसी ने नहीं बताया? हम्म। हमारे परमिट में लिखा है कि क्षेत्र खाली था।"),
         [(T("I'll pause my job and get the area reviewed with my supervisor", "என் வேலையை நிறுத்தி, மேற்பார்வையாளருடன் பகுதியை மறுஆய்வு செய்கிறேன்", "मैं अपना काम रोककर सुपरवाइज़र के साथ क्षेत्र की समीक्षा करवाता हूँ"), "crew", "coordinate", None),
          (T("Fine — you do your job, I'll do mine", "சரி — நீங்கள் உங்கள் வேலையைச் செய்யுங்கள், நான் என்னுடையதைச் செய்கிறேன்", "ठीक है — आप अपना काम करें, मैं अपना"), "crew", "ignore", None)]),
    ])
    m.dialogue("unsafe", [
        ("supervisor", "concerned", T("No. The assessment I gave you was for an empty area. It isn't empty any more.", "இல்லை. நான் கொடுத்த மதிப்பீடு வெற்றுப் பகுதிக்கானது. இப்போது அது வெற்றாக இல்லை.", "नहीं। मैंने जो आकलन दिया था वह खाली क्षेत्र के लिए था। अब वह खाली नहीं है।")),
    ])
    m.dialogue("correct", [("supervisor", "pleased", T("Thanks for stopping. Two crews, one area, two permits that don't know about each other — that's how surprises happen.", "நிறுத்தியதற்கு நன்றி. இரண்டு குழுக்கள், ஒரு பகுதி, ஒன்றையொன்று அறியாத இரண்டு அனுமதிகள் — அப்படித்தான் ஆச்சரியங்கள் நடக்கின்றன.", "रुकने के लिए धन्यवाद। दो टीमें, एक क्षेत्र, दो परमिट जो एक-दूसरे को नहीं जानते — ऐसे ही अनहोनी होती है।"))])
    m.npc("supervisor", -2.5, -12, 180, talk=[("meet", not_done("meet_supervisor")), ("revisit", None)])
    m.npc("contractor", 4.8, 6.2, 225, talk=[("crew", not_done("talk_crew")), ("crew", None)], hidden_until="inspect_valve", briefing=False)

    m.zone("zone_manifold", T("Manifold area", "மேனிஃபோல்ட் பகுதி", "मैनिफोल्ड क्षेत्र"), (-6, 7, -1, 9))
    m.decor("pipe", 0.5, 8.8, len=12, y=1.0, d=0.34, color="#8a96a8")
    m.decor("pipe", 0.5, 8.8, len=12, y=1.8, d=0.26, color="#ffc23d")
    m.decor("tank", 9.5, 13.5, tag="TK-4", r=2.2, h=6)
    m.decor("sign", -4.5, -1.5, kind="mandatory", text="world.sign.ppe")
    m.obj("valve_mv7", "valve", -1.0, 4.0, 0, tag="MV-7", state="open",
          name=T("Manifold valve MV-7", "மேனிஃபோல்ட் வால்வு MV-7", "मैनिफोल्ड वाल्व MV-7"),
          details=[T("Gland nut is dry. No visible weeping at the stem.", "கிளாண்ட் நட் உலர்ந்துள்ளது. தண்டில் கசிவு தெரியவில்லை.", "ग्लैंड नट सूखा है। स्टेम पर कोई रिसाव नहीं दिखता।"),
                   T("The gland check itself is complete.", "கிளாண்ட் சரிபார்ப்பு முடிந்தது.", "ग्लैंड जाँच स्वयं पूरी हो गई।")])
    m.obj("scaffold_new", "scaffold", 3.6, 3.6, 0, hidden_until="inspect_valve", kind="hazard", tagColor="#e8423f",
          name=T("Newly erected scaffold", "புதிதாக அமைக்கப்பட்ட சாரம்", "नया खड़ा किया मचान"),
          details=[T("Scaffold tag: RED — 'Not ready for use'. Erected beside the manifold minutes ago.", "சாரக் குறிச்சீட்டு: சிவப்பு — 'பயன்பாட்டுக்குத் தயாரில்லை'. சில நிமிடங்களுக்கு முன் மேனிஃபோல்டு அருகே அமைக்கப்பட்டது.", "मचान टैग: लाल — 'उपयोग के लिए तैयार नहीं'। कुछ मिनट पहले मैनिफोल्ड के पास खड़ा किया गया।"),
                   T("Work overhead may start above your access route.", "உங்கள் அணுகல் வழிக்கு மேலே மேல்நிலை வேலை தொடங்கலாம்.", "आपके आने-जाने के रास्ते के ऊपर काम शुरू हो सकता है।")])
    m.obj("hose_new", "hose", -1.5, 1.4, 0, hidden_until="inspect_valve", kind="hazard",
          name=T("Water-jetting hose across the walkway", "நடைபாதையின் குறுக்கே நீர் அழுத்தக் குழாய்", "रास्ते के आर-पार वॉटर-जेटिंग होज़"),
          details=[T("A high-pressure jetting hose now crosses your only walkway out.", "உயர் அழுத்த நீர்க் குழாய் இப்போது உங்கள் ஒரே வெளிவழி நடைபாதையைக் கடக்கிறது.", "एक हाई-प्रेशर जेटिंग होज़ अब आपके एकमात्र निकास रास्ते को पार करती है।"),
                   T("It is pressurised — not yours to move.", "அது அழுத்தத்தில் உள்ளது — அதை நகர்த்துவது உங்கள் வேலை அல்ல.", "यह दबाव में है — इसे हटाना आपका काम नहीं।")])
    m.obj("drain_open", "drain", -4.2, 5.5, 0, hidden_until="inspect_valve", state="open", kind="hazard",
          name=T("Uncovered bund drain", "மூடப்படாத அணை வடிகால்", "खुली बंड नाली"),
          details=[T("Drain cover lifted for jetting. Open pit beside the valve.", "நீர் அழுத்தச் சுத்தத்திற்காக வடிகால் மூடி அகற்றப்பட்டுள்ளது. வால்வுக்கு அருகில் திறந்த குழி.", "जेटिंग के लिए नाली का ढक्कन हटाया गया। वाल्व के पास खुला गड्ढा।")])
    m.obj("assessment", "stand", 2.5, -2.8, panel="station", prompt="review", kind="station", groups=["final"],
          title=T("AREA ASSESSMENT AA-12", "பகுதி மதிப்பீடு AA-12", "क्षेत्र आकलन AA-12"),
          name=T("Area assessment board AA-12", "பகுதி மதிப்பீட்டுப் பலகை AA-12", "क्षेत्र आकलन बोर्ड AA-12"),
          details=[T("Written 07:00: 'Manifold area clear. No other work. Walkways dry.'", "07:00-க்கு எழுதப்பட்டது: 'மேனிஃபோல்ட் பகுதி காலியானது. வேறு வேலை இல்லை. நடைபாதைகள் உலர்ந்தவை.'", "07:00 बजे लिखा: 'मैनिफोल्ड क्षेत्र खाली। कोई अन्य काम नहीं। रास्ते सूखे।'")])
    m.evidence("ev_other_work", T("Other work in the area", "பகுதியில் உள்ள பிற வேலை", "क्षेत्र में अन्य कार्य"), T("Assessment: none. Now: scaffold + jetting crew", "மதிப்பீடு: எதுவுமில்லை. இப்போது: சாரம் + நீர் அழுத்தக் குழு", "आकलन: कोई नहीं। अब: मचान + जेटिंग टीम"), False)
    m.evidence("ev_valve", T("Valve MV-7 gland", "வால்வு MV-7 கிளாண்ட்", "वाल्व MV-7 ग्लैंड"), T("Checked — dry", "சரிபார்க்கப்பட்டது — உலர்ந்தது", "जाँचा गया — सूखा"), True)
    m.group("final", T("The area has changed since the briefing. What now?", "விளக்கத்திற்குப் பின் பகுதி மாறியுள்ளது. இப்போது என்ன?", "ब्रीफिंग के बाद क्षेत्र बदल गया है। अब क्या?"), [
        ("pause_review", T("Pause and ask Kannan for a fresh area review", "நிறுத்தி, புதிய பகுதி மறுஆய்வுக்காக கண்ணனிடம் கேளுங்கள்", "रुकें और कन्नन से नई क्षेत्र समीक्षा माँगें")),
        ("carry_on", T("Carry on — the morning assessment covers this area", "தொடரவும் — காலை மதிப்பீடு இந்தப் பகுதியை உள்ளடக்கியது", "जारी रखें — सुबह का आकलन इस क्षेत्र को कवर करता है")),
        ("move_hose", T("Move the hose out of the way and keep working", "குழாயை வழியிலிருந்து நகர்த்தி வேலையைத் தொடருங்கள்", "होज़ रास्ते से हटाकर काम जारी रखें")),
    ])
    m.group("crew", T("How do you respond to the contract crew?", "ஒப்பந்தக் குழுவுக்கு எப்படிப் பதிலளிப்பீர்கள்?", "आप कॉन्ट्रैक्ट टीम को कैसे जवाब देंगे?"), [
        ("coordinate", T("Pause and get the area reviewed with the supervisor", "நிறுத்தி மேற்பார்வையாளருடன் பகுதியை மறுஆய்வு செய்தல்", "रुककर सुपरवाइज़र के साथ क्षेत्र की समीक्षा")),
        ("ignore", T("Work side by side without coordinating", "ஒருங்கிணைக்காமல் அருகருகே வேலை செய்தல்", "बिना समन्वय साथ-साथ काम")),
    ])
    m.tools("flashlight", "radio", flashlight=["valve_mv7", "drain_open"])

    meet = m.meet("supervisor")
    m.briefing(meet)
    m.step("enter", title=T("Go to the manifold area", "மேனிஃபோல்ட் பகுதிக்குச் செல்லுங்கள்", "मैनिफोल्ड क्षेत्र जाएँ"),
           instruction=T("Walk to the yellow-bordered manifold area.", "மஞ்சள் எல்லையிட்ட மேனிஃபோல்ட் பகுதிக்குச் செல்லுங்கள்.", "पीली सीमा वाले मैनिफोल्ड क्षेत्र में जाएँ।"),
           trigger=enter("zone_manifold"), requires=["briefing"], points=5, concept="situational_awareness", scene="navigate", marker="zone_manifold",
           hints=[T("Head north from the briefing point.", "விளக்கப் புள்ளியிலிருந்து வடக்கே செல்லுங்கள்.", "ब्रीफिंग पॉइंट से उत्तर की ओर जाएँ।")])
    m.step("inspect_valve", title=T("Check the gland on MV-7", "MV-7-இன் கிளாண்டைச் சரிபாருங்கள்", "MV-7 का ग्लैंड जाँचें"),
           instruction=T("Inspect manifold valve MV-7.", "மேனிஃபோல்ட் வால்வு MV-7-ஐ ஆய்வு செய்யுங்கள்.", "मैनिफोल्ड वाल्व MV-7 का निरीक्षण करें।"),
           trigger=inspect("valve_mv7"), requires=["enter"], points=10, concept="equipment_identification", scene="inspect", marker="valve_mv7",
           hints=[T("MV-7 is the red handwheel on the manifold.", "MV-7 மேனிஃபோல்டில் உள்ள சிவப்புக் கைச்சக்கரம்.", "MV-7 मैनिफोल्ड पर लाल हैंडव्हील है।")])
    m.step("see_scaffold", title=T("Look at what has changed: the scaffold", "என்ன மாறியது என்று பாருங்கள்: சாரம்", "देखें क्या बदला: मचान"),
           instruction=T("Inspect the scaffold that has appeared beside the manifold.", "மேனிஃபோல்டு அருகே தோன்றிய சாரத்தை ஆய்வு செய்யுங்கள்.", "मैनिफोल्ड के पास दिखे मचान का निरीक्षण करें।"),
           trigger=inspect("scaffold_new"), requires=["inspect_valve"], points=10, concept="change_reassessment", scene="change", marker="scaffold_new",
           hints=[T("What is new since the briefing?", "விளக்கத்திற்குப் பின் என்ன புதிதாக வந்துள்ளது?", "ब्रीफिंग के बाद नया क्या है?")])
    m.step("see_hose", title=T("Check the walkway", "நடைபாதையைச் சரிபாருங்கள்", "रास्ता जाँचें"),
           instruction=T("Inspect the hose that now crosses the walkway.", "இப்போது நடைபாதையைக் கடக்கும் குழாயை ஆய்வு செய்யுங்கள்.", "अब रास्ता पार करती होज़ का निरीक्षण करें।"),
           trigger=inspect("hose_new"), requires=["inspect_valve"], points=10, concept="change_reassessment", scene="change", marker="hose_new",
           hints=[T("Look down at your route out.", "உங்கள் வெளிவழியைக் கீழே பாருங்கள்.", "अपने बाहर जाने के रास्ते पर नीचे देखें।")])
    m.step("see_drain", title=T("Check the ground near the valve", "வால்வுக்கு அருகிலுள்ள தரையைச் சரிபாருங்கள்", "वाल्व के पास ज़मीन जाँचें"),
           instruction=T("Inspect the bund drain west of the valve.", "வால்வுக்கு மேற்கே உள்ள அணை வடிகாலை ஆய்வு செய்யுங்கள்.", "वाल्व के पश्चिम में बंड नाली का निरीक्षण करें।"),
           trigger=inspect("drain_open"), requires=["inspect_valve"], points=10, concept="hazard_identification", scene="change", marker="drain_open",
           hints=[T("Something on the ground is open that was closed this morning.", "இன்று காலை மூடியிருந்த ஏதோ ஒன்று தரையில் திறந்துள்ளது.", "ज़मीन पर कुछ खुला है जो सुबह बंद था।")])
    m.step("talk_crew", title=T("Speak to the contract crew", "ஒப்பந்தக் குழுவுடன் பேசுங்கள்", "कॉन्ट्रैक्ट टीम से बात करें"),
           instruction=T("Talk to Mani, the contract technician, and agree what happens next.", "ஒப்பந்தத் தொழில்நுட்பர் மணியுடன் பேசி அடுத்து என்ன என்று ஒப்புக்கொள்ளுங்கள்.", "कॉन्ट्रैक्ट टेक्नीशियन मणि से बात करें और आगे क्या होगा तय करें।"),
           trigger=decide("crew", "coordinate"), requires=["see_scaffold", "see_hose"], points=10, concept="escalation", scene="communicate", marker="contractor",
           hints=[T("Two crews in one area need to be coordinated by someone with authority.", "ஒரு பகுதியில் இரண்டு குழுக்களை அதிகாரம் உள்ள ஒருவர் ஒருங்கிணைக்க வேண்டும்.", "एक क्षेत्र में दो टीमों का समन्वय किसी अधिकृत व्यक्ति को करना चाहिए।")])
    m.step("review_board", title=T("Compare with the morning assessment", "காலை மதிப்பீட்டுடன் ஒப்பிடுங்கள்", "सुबह के आकलन से तुलना करें"),
           instruction=T("Open assessment board AA-12 and flag what no longer matches.", "மதிப்பீட்டுப் பலகை AA-12-ஐத் திறந்து இனி பொருந்தாததைக் குறியுங்கள்.", "आकलन बोर्ड AA-12 खोलें और जो अब मेल नहीं खाता उसे चिह्नित करें।"),
           trigger={"type": "evidence_flagged", "target": "ev_other_work"}, requires=["talk_crew", "see_drain"], points=15, concept="change_reassessment", scene="evidence", marker="assessment",
           hints=[T("The assessment describes an empty area.", "மதிப்பீடு ஒரு வெற்றுப் பகுதியை விவரிக்கிறது.", "आकलन एक खाली क्षेत्र का वर्णन करता है।")])
    m.step("decide", title=T("Decide how to continue", "எப்படித் தொடர்வது என்று முடிவு செய்யுங்கள்", "तय करें कि आगे कैसे बढ़ें"),
           instruction=T("Record your decision at the assessment board.", "மதிப்பீட்டுப் பலகையில் உங்கள் முடிவைப் பதிவுசெய்யுங்கள்.", "आकलन बोर्ड पर अपना निर्णय दर्ज करें।"),
           trigger=decide("final", "pause_review"), requires=["review_board"], points=20, concept="change_reassessment", scene="decision", marker="assessment",
           mistake_if_early=T("Look at everything that changed before deciding.", "முடிவெடுக்கும் முன் மாறிய அனைத்தையும் பாருங்கள்.", "निर्णय से पहले जो कुछ बदला सब देखें।"),
           hints=[T("Is the 07:00 assessment still a true picture of this area?", "07:00 மதிப்பீடு இந்தப் பகுதியின் உண்மையான நிலையா?", "क्या 07:00 का आकलन अब भी इस क्षेत्र की सही तस्वीर है?")])
    m.event("crew_arrives", {"completed": ["inspect_valve"]}, [
        {"type": "banner", "text": T("A contract crew has started work in your area", "உங்கள் பகுதியில் ஒரு ஒப்பந்தக் குழு வேலை தொடங்கியுள்ளது", "आपके क्षेत्र में एक कॉन्ट्रैक्ट टीम ने काम शुरू किया है"), "style": "danger"},
        {"type": "sound", "sound": "warning"},
        {"type": "dialogue", "name": "arrival"},
    ], delay=0.6)

    m.critical("carry_on_old_assessment", trigger=decide("final", "carry_on"), concept="change_reassessment", dialogue="unsafe",
               explanation=T("You relied on a 07:00 assessment of an empty area after a crew, scaffold, hose and open drain appeared.", "ஒரு குழு, சாரம், குழாய், திறந்த வடிகால் தோன்றிய பின்னும் வெற்றுப் பகுதிக்கான 07:00 மதிப்பீட்டை நம்பினீர்கள்.", "टीम, मचान, होज़ और खुली नाली दिखने के बाद भी आपने खाली क्षेत्र के 07:00 आकलन पर भरोसा किया।"),
               missing=T("A fresh review of the changed area by the person who authorised your work.", "உங்கள் வேலையை அனுமதித்தவரால் மாறிய பகுதியின் புதிய மறுஆய்வு.", "आपका काम अधिकृत करने वाले व्यक्ति द्वारा बदले हुए क्षेत्र की नई समीक्षा।"))
    m.critical("move_pressurised_hose", trigger=decide("final", "move_hose"), concept="change_reassessment", dialogue="unsafe",
               explanation=T("Moving another crew's pressurised equipment creates a new hazard and does not make the area match the assessment.", "மற்றொரு குழுவின் அழுத்த உபகரணத்தை நகர்த்துவது புதிய அபாயத்தை உருவாக்குகிறது; பகுதியை மதிப்பீட்டுடன் பொருத்தாது.", "दूसरी टीम का दबाव वाला उपकरण हटाना नया खतरा बनाता है और क्षेत्र को आकलन से मेल नहीं कराता।"),
               missing=T("Coordination between both crews through the supervisor.", "மேற்பார்வையாளர் வழியாக இரு குழுக்களுக்கும் இடையிலான ஒருங்கிணைப்பு.", "सुपरवाइज़र के माध्यम से दोनों टीमों में समन्वय।"))
    m.mistake("ignore_crew", trigger=decide("crew", "ignore"), kind="incorrect_decision", concept="escalation",
              feedback=T("Working side by side without coordination is how crews surprise each other. Talk to Mani again.", "ஒருங்கிணைப்பு இல்லாமல் அருகருகே வேலை செய்வதே குழுக்கள் ஒன்றையொன்று ஆச்சரியப்படுத்தும் வழி. மணியுடன் மீண்டும் பேசுங்கள்.", "बिना समन्वय साथ-साथ काम करना ही टीमों को चौंकाता है। मणि से फिर बात करें।"))
    m.mistake("wrong_flag", trigger={"type": "evidence_flagged"}, kind="incorrect_decision", concept="documented_evidence",
              feedback=T("That entry still matches the area. Flag what has changed.", "அந்தப் பதிவு இன்னும் பகுதியுடன் பொருந்துகிறது. மாறியதைக் குறியுங்கள்.", "वह प्रविष्टि अब भी क्षेत्र से मेल खाती है। जो बदला उसे चिह्नित करें।"))

    m.debrief(
        success=T("You noticed the change, spoke to the other crew and paused for a fresh review.", "மாற்றத்தைக் கவனித்து, மற்ற குழுவுடன் பேசி, புதிய மறுஆய்வுக்காக நிறுத்தினீர்கள்.", "आपने बदलाव देखा, दूसरी टीम से बात की और नई समीक्षा के लिए रुके।"),
        critical=T("The area changed but the decision didn't. An assessment only covers the conditions it describes.", "பகுதி மாறியது, ஆனால் முடிவு மாறவில்லை. ஒரு மதிப்பீடு அது விவரிக்கும் நிலைமைகளை மட்டுமே உள்ளடக்கும்.", "क्षेत्र बदला पर निर्णय नहीं। आकलन केवल उन्हीं परिस्थितियों को कवर करता है जिनका वह वर्णन करता है।"),
        failed=T("The attempt ended after repeated unsafe choices. Stop when the picture changes.", "தொடர்ந்த பாதுகாப்பற்ற தேர்வுகளால் முயற்சி முடிந்தது. நிலைமை மாறும்போது நிறுத்துங்கள்.", "बार-बार असुरक्षित विकल्पों से प्रयास समाप्त हुआ। तस्वीर बदले तो रुकें।"),
        lines=[
            ({"criticalRule": "carry_on_old_assessment"}, T("You carried on under an assessment that no longer described the area.", "பகுதியை இனி விவரிக்காத மதிப்பீட்டின் கீழ் தொடர்ந்தீர்கள்.", "आप उस आकलन पर जारी रहे जो अब क्षेत्र का वर्णन नहीं करता था।")),
            ({"criticalRule": "move_pressurised_hose"}, T("You chose to move another crew's pressurised hose.", "மற்றொரு குழுவின் அழுத்தக் குழாயை நகர்த்தத் தேர்ந்தெடுத்தீர்கள்.", "आपने दूसरी टीम की दबाव वाली होज़ हटाना चुना।")),
            ({"stepCompleted": "see_drain"}, T("You spotted the open drain beside the valve.", "வால்வுக்கு அருகில் திறந்த வடிகாலைக் கண்டீர்கள்.", "आपने वाल्व के पास खुली नाली देखी।")),
            ({"counterAbove": ["incorrectDecisions", 0]}, T("One choice skipped coordination or flagged the wrong entry.", "ஒரு தேர்வு ஒருங்கிணைப்பைத் தவிர்த்தது அல்லது தவறான பதிவைக் குறித்தது.", "एक विकल्प ने समन्वय छोड़ा या गलत प्रविष्टि चिह्नित की।")),
            ({"stepCompleted": "decide"}, T("You paused for a fresh review — the right call when conditions change.", "புதிய மறுஆய்வுக்காக நிறுத்தினீர்கள் — நிலைமை மாறும்போது சரியான முடிவு.", "आप नई समीक्षा के लिए रुके — परिस्थिति बदलने पर सही निर्णय।")),
        ],
    )
    m.comic(T("THE PICTURE CHANGED", "நிலைமை மாறியது", "तस्वीर बदल गई"), [
        ("change", T("The briefing described the area as it was — not as it is now.", "விளக்கம் பகுதியை அப்போது இருந்தபடி விவரித்தது — இப்போது இருப்பது போல அல்ல.", "ब्रीफिंग ने क्षेत्र को वैसा बताया जैसा वह था — जैसा अब है वैसा नहीं।")),
        ("team", T("Two crews in one area must know about each other.", "ஒரு பகுதியில் இரண்டு குழுக்கள் ஒன்றையொன்று அறிந்திருக்க வேண்டும்.", "एक क्षेत्र में दो टीमों को एक-दूसरे के बारे में पता होना चाहिए।")),
        ("stop_sign", T("New conditions? Pause and get it reviewed.", "புதிய நிலைமைகளா? நிறுத்தி மறுஆய்வு செய்யுங்கள்.", "नई परिस्थितियाँ? रुकें और समीक्षा करवाएँ।")),
    ])
    m.report(["inspect_valve", "see_scaffold", "see_hose", "see_drain", "review_board"], ["talk_crew", "decide"])
    m.mcq(1, concept="change_reassessment",
          stem=T("Your briefing described an empty area, but a new crew has started work nearby. What does that mean?", "உங்கள் விளக்கம் வெற்றுப் பகுதியை விவரித்தது, ஆனால் அருகில் ஒரு புதிய குழு வேலை தொடங்கியுள்ளது. அதன் பொருள் என்ன?", "आपकी ब्रीफिंग ने खाली क्षेत्र बताया, पर पास में एक नई टीम ने काम शुरू किया है। इसका क्या अर्थ है?"),
          options=[T("The briefing no longer covers the area; it needs reviewing", "விளக்கம் இனி பகுதியை உள்ளடக்காது; மறுஆய்வு தேவை", "ब्रीफिंग अब क्षेत्र को कवर नहीं करती; समीक्षा चाहिए"),
                   T("Nothing — your briefing is still valid all day", "எதுவுமில்லை — உங்கள் விளக்கம் நாள் முழுவதும் செல்லும்", "कुछ नहीं — आपकी ब्रीफिंग पूरे दिन मान्य है"),
                   T("You should finish quickly before they get in the way", "அவர்கள் இடையூறு செய்யும் முன் விரைவாக முடிக்க வேண்டும்", "उनके बीच में आने से पहले जल्दी काम ख़त्म करें")],
          correct="a", explanation=T("An assessment only covers the conditions it describes.", "ஒரு மதிப்பீடு அது விவரிக்கும் நிலைமைகளை மட்டுமே உள்ளடக்கும்.", "आकलन केवल उन्हीं परिस्थितियों को कवर करता है जिनका वह वर्णन करता है।"))
    m.mcq(2, concept="change_reassessment",
          stem=T("A pressurised hose from another crew blocks your walkway. What should you do?", "மற்றொரு குழுவின் அழுத்தக் குழாய் உங்கள் நடைபாதையைத் தடுக்கிறது. என்ன செய்ய வேண்டும்?", "दूसरी टीम की दबाव वाली होज़ आपका रास्ता रोकती है। क्या करना चाहिए?"),
          options=[T("Move it yourself", "நீங்களே நகர்த்துங்கள்", "खुद हटा दें"),
                   T("Step over it and carry on", "அதைத் தாண்டிச் சென்று தொடருங்கள்", "उसके ऊपर से निकलकर जारी रखें"),
                   T("Leave it and raise it with your supervisor and the crew", "அதை விட்டுவிட்டு மேற்பார்வையாளரிடமும் குழுவிடமும் தெரிவியுங்கள்", "उसे छोड़ें और सुपरवाइज़र व टीम को बताएँ")],
          correct="c", explanation=T("Other crews' equipment is coordinated, not moved by you.", "மற்ற குழுக்களின் உபகரணம் ஒருங்கிணைக்கப்படுகிறது, நீங்கள் நகர்த்துவதில்லை.", "दूसरी टीमों के उपकरण का समन्वय किया जाता है, आप उसे नहीं हटाते।"))
    m.mcq(3, concept="hazard_identification",
          stem=T("Which of these was a NEW hazard after the crew arrived?", "குழு வந்த பிறகு இவற்றில் எது புதிய அபாயம்?", "टीम आने के बाद इनमें से कौन सा नया खतरा था?"),
          options=[T("The open bund drain beside the valve", "வால்வுக்கு அருகிலுள்ள திறந்த அணை வடிகால்", "वाल्व के पास खुली बंड नाली"),
                   T("The colour of the valve handwheel", "வால்வுக் கைச்சக்கரத்தின் நிறம்", "वाल्व हैंडव्हील का रंग"),
                   T("The tank name plate", "தொட்டிப் பெயர்ப் பலகை", "टैंक की नाम-पट्टिका")],
          correct="a", explanation=T("The drain had been covered that morning; jetting work opened it.", "அந்த வடிகால் காலையில் மூடப்பட்டிருந்தது; நீர் அழுத்த வேலை அதைத் திறந்தது.", "नाली सुबह ढकी थी; जेटिंग के काम ने उसे खोल दिया।"))
    m.mcq(4, concept="escalation",
          stem=T("Who should resolve two crews working in the same area?", "ஒரே பகுதியில் வேலை செய்யும் இரண்டு குழுக்களை யார் ஒருங்கிணைக்க வேண்டும்?", "एक ही क्षेत्र में काम करती दो टीमों का मामला कौन सुलझाए?"),
          options=[T("Whichever crew arrived first", "முதலில் வந்த குழு", "जो टीम पहले पहुँची"),
                   T("The supervisors or permit authority for the area", "பகுதிக்கான மேற்பார்வையாளர்கள் அல்லது அனுமதி அதிகாரி", "क्षेत्र के सुपरवाइज़र या परमिट प्राधिकारी"),
                   T("The trainee on site", "தளத்தில் உள்ள பயிற்சியாளர்", "साइट पर मौजूद प्रशिक्षु")],
          correct="b", explanation=T("Coordination sits with the people who authorise work in the area.", "ஒருங்கிணைப்பு, பகுதியில் வேலையை அனுமதிப்பவர்களிடம் உள்ளது.", "समन्वय उन लोगों का काम है जो क्षेत्र में काम अधिकृत करते हैं।"))
    m.spec(
        workplaceLocation="Fictional tank-farm manifold.",
        equipmentType="Manifold valve MV-7; scaffold, jetting hose and open drain introduced mid-mission.",
        corePrinciple="When the work area changes after the briefing, the original assessment no longer covers it.",
        commonMisconceptions=["A morning briefing covers the whole day.", "I can tidy away another crew's equipment."],
        criticalDecisions=["Carry on under the old assessment", "Move a pressurised hose"],
        assessmentCriteria={"correct": "Notice scaffold, hose and drain; coordinate with the crew; flag the outdated assessment; pause for review."},
        scenarioChange="After the valve check, a pre-scripted contract crew appears (scaffold, hose, open drain).",
    )
    return m
