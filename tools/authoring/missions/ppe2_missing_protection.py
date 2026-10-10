"""PPE Awareness · Level 2 — The Missing Protection.

Story: The trainee is sent to take a reading inside the compressor house. The
entry sign lists hearing protection; the PPE store's ear-defender hook is
empty. Contractor Mani is about to walk in without any. Learning: an
incomplete PPE arrangement is discovered before entry, reported, and not
improvised around; colleagues are stopped, politely.
"""
from authoring.dsl import Mission, T, decide, enter, flag, inspect, not_done, select


def build() -> Mission:
    m = Mission(
        code="ppe2", id="og-ppe-l2-missing-protection", category="og_ppe", level=2, minutes=11,
        title=T("The Missing Protection", "இல்லாத பாதுகாப்பு", "गायब सुरक्षा"),
        subtitle=T("An empty hook in the PPE store", "PPE களஞ்சியத்தில் ஒரு காலியான கொக்கி", "PPE स्टोर में एक खाली हुक"),
        description=T("The sign says one thing, the store has another. What happens at the door?", "அடையாளம் ஒன்று சொல்கிறது, களஞ்சியத்தில் வேறு உள்ளது. கதவருகே என்ன நடக்கும்?", "संकेत कुछ कहता है, स्टोर में कुछ और है। दरवाज़े पर क्या होगा?"),
        location=T("Compressor house K-3 · Utility block", "அழுத்தி இல்லம் K-3 · பயன்பாட்டுப் பிரிவு", "कंप्रेसर हाउस K-3 · यूटिलिटी ब्लॉक"),
        site="utility", spawn=(0, -23, 0), work_point=(0, -5, 0),
    )
    m.brief(
        lines=[
            T("Take the oil-level reading on compressor K-3 inside the compressor house.", "அழுத்தி இல்லத்திற்குள் உள்ள அழுத்தி K-3-இன் எண்ணெய் அளவைப் பதிவுசெய்யுங்கள்.", "कंप्रेसर हाउस के अंदर कंप्रेसर K-3 की ऑयल-लेवल रीडिंग लें।"),
            T("Check the entry requirements at the door before you go in.", "உள்ளே செல்லும் முன் கதவருகே நுழைவுத் தேவைகளைச் சரிபாருங்கள்.", "अंदर जाने से पहले दरवाज़े पर प्रवेश आवश्यकताएँ जाँचें।"),
        ],
        task=T("Take the K-3 oil-level reading.", "K-3 எண்ணெய் அளவைப் பதிவுசெய்யுங்கள்.", "K-3 की ऑयल-लेवल रीडिंग लें।"),
        equipment=T("Compressor K-3, compressor house entry sign, PPE store (fictional).", "அழுத்தி K-3, அழுத்தி இல்ல நுழைவு அடையாளம், PPE களஞ்சியம் (கற்பனை).", "कंप्रेसर K-3, कंप्रेसर हाउस प्रवेश संकेत, PPE स्टोर (काल्पनिक)।"),
        objective=T("Enter only when your PPE matches the posted requirements.", "உங்கள் PPE அறிவிக்கப்பட்ட தேவைகளுடன் பொருந்தும்போது மட்டுமே நுழையுங்கள்.", "केवल तभी प्रवेश करें जब आपका PPE लिखी आवश्यकताओं से मेल खाए।"),
        information=T("The compressor house is a posted hearing-protection area in this scenario.", "இந்தச் சூழலில் அழுத்தி இல்லம் செவிப் பாதுகாப்பு அறிவிக்கப்பட்ட பகுதி.", "इस परिदृश्य में कंप्रेसर हाउस श्रवण-सुरक्षा क्षेत्र घोषित है।"),
        objectives=[
            T("Notice when required PPE is missing before entry.", "நுழைவதற்கு முன் தேவையான PPE இல்லாததைக் கவனித்தல்.", "प्रवेश से पहले आवश्यक PPE की कमी पहचानना।"),
            T("Report the gap and stop others entering unprotected.", "குறைபாட்டைத் தெரிவித்து, பாதுகாப்பின்றி மற்றவர்கள் நுழைவதைத் தடுத்தல்.", "कमी रिपोर्ट करना और दूसरों को बिना सुरक्षा जाने से रोकना।"),
        ],
    )
    m.dialogue("meet", [
        ("safety_officer", "friendly", T("Quick job: oil level on K-3. The compressor house has its own entry sign — read it.", "விரைவான வேலை: K-3-இன் எண்ணெய் அளவு. அழுத்தி இல்லத்திற்குத் தனி நுழைவு அடையாளம் உள்ளது — படியுங்கள்.", "छोटा काम: K-3 का ऑयल लेवल। कंप्रेसर हाउस का अपना प्रवेश संकेत है — उसे पढ़िए।")),
        ("safety_officer", "neutral", T("If anything on that sign isn't available, you don't go in. You tell me.", "அந்த அடையாளத்தில் உள்ள எதுவும் கிடைக்கவில்லை என்றால், உள்ளே போக வேண்டாம். என்னிடம் சொல்லுங்கள்.", "उस संकेत की कोई चीज़ उपलब्ध न हो, तो आप अंदर नहीं जाते। मुझे बताते हैं।")),
    ])
    m.dialogue("revisit", [("safety_officer", "neutral", T("Read the sign, check the store, and tell me if something's missing.", "அடையாளத்தைப் படியுங்கள், களஞ்சியத்தைச் சரிபாருங்கள், ஏதாவது இல்லையென்றால் சொல்லுங்கள்.", "संकेत पढ़िए, स्टोर जाँचिए, और कुछ गायब हो तो बताइए।"))])
    m.dialogue("mani", [
        ("contractor", "friendly", T("Going in? Me too. No ear defenders left, but it's only two minutes.", "உள்ளே போகிறீர்களா? நானும். காது பாதுகாப்பு இல்லை, ஆனால் இரண்டு நிமிடம்தான்.", "अंदर जा रहे हो? मैं भी। कान के डिफ़ेंडर नहीं बचे, पर दो मिनट ही तो है।"),
         [(T("Mani, hold on — the sign requires hearing protection. Let's get some first.", "மணி, பொறுங்கள் — அடையாளம் செவிப் பாதுகாப்பைக் கோருகிறது. முதலில் எடுத்துக்கொள்வோம்.", "मणि, रुको — संकेत श्रवण सुरक्षा माँगता है। पहले वह ले लें।"), "mani", "stop", "mani_ok"),
          (T("Fair enough, two minutes won't hurt", "சரி, இரண்டு நிமிடம் பாதிக்காது", "ठीक है, दो मिनट से कुछ नहीं होगा"), "mani", "let_go", None)]),
    ])
    m.dialogue("mani_ok", [("contractor", "pleased", T("Yeah… fair. I'll wait with you.", "ஆமாம்… சரிதான். உங்களுடன் காத்திருக்கிறேன்.", "हाँ… ठीक है। मैं तुम्हारे साथ इंतज़ार करता हूँ।"))])
    m.dialogue("unsafe", [("safety_officer", "concerned", T("Not without hearing protection. The sign isn't optional.", "செவிப் பாதுகாப்பின்றி இல்லை. அடையாளம் விருப்பத்திற்குரியதல்ல.", "श्रवण सुरक्षा के बिना नहीं। संकेत वैकल्पिक नहीं है।"))])
    m.dialogue("correct", [("safety_officer", "pleased", T("Thanks for flagging it — stores are bringing ear defenders now. And thanks for stopping Mani.", "தெரிவித்ததற்கு நன்றி — களஞ்சியம் இப்போது காது பாதுகாப்பைக் கொண்டு வருகிறது. மணியை நிறுத்தியதற்கும் நன்றி.", "बताने के लिए धन्यवाद — स्टोर अब ईयर डिफ़ेंडर ला रहा है। और मणि को रोकने के लिए भी धन्यवाद।"))])
    m.npc("safety_officer", -3, -12, 180, talk=[("meet", not_done("meet_safety_officer")), ("revisit", None)])
    m.npc("contractor", 2.4, 1.2, 180, talk=[("mani", not_done("stop_mani")), ("mani_ok", None)], briefing=False)

    m.zone("zone_khouse", T("Compressor house K-3", "அழுத்தி இல்லம் K-3", "कंप्रेसर हाउस K-3"), (-4, 4, 5, 12), restricted=False)
    m.decor("exit", 0, 4.4, wall=9, state="clear")
    m.decor("wall", -4.5, 8.5, heading=90, len=8)
    m.decor("wall", 4.5, 8.5, heading=90, len=8)
    m.decor("wall", 0, 12.5, len=9)
    m.decor("compressor", 2.0, 10.0, tag="K-4")
    m.decor("compressor", -1.5, 7.8, tag="K-3")
    m.obj("entry_sign", "sign", -2.2, 3.8, signKind="mandatory", kind="information", prompt="read",
          text=T("Hearing protection, helmet and glasses required", "செவிப் பாதுகாப்பு, தலைக்கவசம், கண்ணாடி தேவை", "श्रवण सुरक्षा, हेलमेट और चश्मा आवश्यक"),
          name=T("Compressor house entry sign", "அழுத்தி இல்ல நுழைவு அடையாளம்", "कंप्रेसर हाउस प्रवेश संकेत"),
          details=[T("Required in this area: hearing protection, safety helmet, safety glasses.", "இந்தப் பகுதியில் தேவை: செவிப் பாதுகாப்பு, பாதுகாப்புத் தலைக்கவசம், பாதுகாப்புக் கண்ணாடி.", "इस क्षेत्र में आवश्यक: श्रवण सुरक्षा, सेफ्टी हेलमेट, सेफ्टी चश्मा।")])
    m.obj("ppe_store", "locker", 4.5, -3.0, -90, panel="inventory", prompt="open", kind="station", groups=["entry"],
          name=T("PPE store (utility block)", "PPE களஞ்சியம் (பயன்பாட்டுப் பிரிவு)", "PPE स्टोर (यूटिलिटी ब्लॉक)"),
          details=[T("Check each hook against the entry sign.", "ஒவ்வொரு கொக்கியையும் நுழைவு அடையாளத்துடன் சரிபாருங்கள்.", "हर हुक को प्रवेश संकेत से मिलाएँ।")])
    m.item("helmet", "ppe_store", "helmet", T("Safety helmet", "பாதுகாப்புத் தலைக்கவசம்", "सेफ्टी हेलमेट"), T("Good condition.", "நல்ல நிலை.", "अच्छी हालत।"))
    m.item("glasses", "ppe_store", "glasses", T("Safety glasses", "பாதுகாப்புக் கண்ணாடி", "सेफ्टी चश्मा"), T("Good condition.", "நல்ல நிலை.", "अच्छी हालत।"))
    m.item("ear_hook", "ppe_store", "earmuff", T("Ear defenders hook", "காது பாதுகாப்புக் கொக்கி", "ईयर डिफ़ेंडर हुक"), T("EMPTY — no ear defenders in stock.", "காலி — காது பாதுகாப்பு கையிருப்பில் இல்லை.", "खाली — ईयर डिफ़ेंडर स्टॉक में नहीं।"), defect=True)
    m.item("gloves", "ppe_store", "gloves_cotton", T("Cotton gloves", "பருத்திக் கையுறை", "सूती दस्ताने"), T("Good condition. Not listed on the sign.", "நல்ல நிலை. அடையாளத்தில் இல்லை.", "अच्छी हालत। संकेत में नहीं।"))
    m.group("mani", T("Mani is about to enter without hearing protection. Your response?", "மணி செவிப் பாதுகாப்பின்றி நுழையப் போகிறார். உங்கள் பதில்?", "मणि बिना श्रवण सुरक्षा जाने वाला है। आपका जवाब?"), [
        ("stop", T("Stop him and explain the requirement", "அவரை நிறுத்தி தேவையை விளக்குதல்", "उसे रोककर आवश्यकता समझाना")),
        ("let_go", T("Let him go in", "அவரை உள்ளே செல்ல விடுதல்", "उसे अंदर जाने देना")),
    ])
    m.group("entry", T("Hearing protection is not available. What do you do?", "செவிப் பாதுகாப்பு கிடைக்கவில்லை. என்ன செய்வீர்கள்?", "श्रवण सुरक्षा उपलब्ध नहीं। आप क्या करेंगे?"), [
        ("wait_report", T("Don't enter. Report the missing ear defenders and wait for stock", "நுழைய வேண்டாம். இல்லாத காது பாதுகாப்பைத் தெரிவித்து கையிருப்புக்காகக் காத்திருங்கள்", "प्रवेश न करें। गायब ईयर डिफ़ेंडर की रिपोर्ट करें और स्टॉक का इंतज़ार करें")),
        ("go_quick", T("Go in quickly without them", "அவை இல்லாமல் விரைவாக உள்ளே செல்லுங்கள்", "उनके बिना जल्दी अंदर जाएँ")),
        ("improvise", T("Stuff tissue in your ears and go in", "காதுகளில் காகிதம் வைத்துக்கொண்டு உள்ளே செல்லுங்கள்", "कानों में टिश्यू ठूँसकर अंदर जाएँ")),
    ])

    meet = m.meet("safety_officer")
    m.briefing(meet)
    m.step("read_sign", title=T("Read the entry sign", "நுழைவு அடையாளத்தைப் படியுங்கள்", "प्रवेश संकेत पढ़ें"),
           instruction=T("Read the blue sign at the compressor house door.", "அழுத்தி இல்லக் கதவருகே உள்ள நீல அடையாளத்தைப் படியுங்கள்.", "कंप्रेसर हाउस के दरवाज़े पर नीला संकेत पढ़ें।"),
           trigger=inspect("entry_sign"), requires=["briefing"], points=10, concept="ppe_task_requirements", scene="documents", marker="entry_sign",
           hints=[T("Requirements are posted at the door.", "தேவைகள் கதவருகே அறிவிக்கப்பட்டுள்ளன.", "आवश्यकताएँ दरवाज़े पर लिखी हैं।")])
    m.step("open_store", title=T("Check the PPE store", "PPE களஞ்சியத்தைச் சரிபாருங்கள்", "PPE स्टोर जाँचें"),
           instruction=T("Open the PPE store on the east side.", "கிழக்குப் பக்க PPE களஞ்சியத்தைத் திறவுங்கள்.", "पूर्वी ओर का PPE स्टोर खोलें।"),
           trigger=inspect("ppe_store"), requires=["read_sign"], points=5, concept="ppe_completeness", scene="ppe", marker="ppe_store",
           hints=[T("The store faces the walkway.", "களஞ்சியம் நடைபாதையை நோக்கியுள்ளது.", "स्टोर रास्ते की ओर है।")])
    m.step("take_helmet", title=T("Take a helmet", "தலைக்கவசத்தை எடுங்கள்", "हेलमेट लें"), instruction=T("Select the safety helmet.", "பாதுகாப்புத் தலைக்கவசத்தைத் தேர்ந்தெடுங்கள்.", "सेफ्टी हेलमेट चुनें।"),
           trigger=select("helmet"), requires=["open_store"], points=5, concept="ppe_task_requirements", scene="ppe", marker="ppe_store",
           hints=[T("Listed on the sign.", "அடையாளத்தில் உள்ளது.", "संकेत में लिखा है।")])
    m.step("take_glasses", title=T("Take safety glasses", "பாதுகாப்புக் கண்ணாடியை எடுங்கள்", "सेफ्टी चश्मा लें"), instruction=T("Select the safety glasses.", "பாதுகாப்புக் கண்ணாடியைத் தேர்ந்தெடுங்கள்.", "सेफ्टी चश्मा चुनें।"),
           trigger=select("glasses"), requires=["open_store"], points=5, concept="ppe_task_requirements", scene="ppe", marker="ppe_store",
           hints=[T("Listed on the sign.", "அடையாளத்தில் உள்ளது.", "संकेत में लिखा है।")])
    m.step("flag_missing", title=T("Report the missing item", "இல்லாத பொருளைத் தெரிவியுங்கள்", "गायब वस्तु रिपोर्ट करें"),
           instruction=T("Report the empty hook as a defect in the store.", "களஞ்சியத்தில் காலியான கொக்கியைக் குறைபாடாகத் தெரிவியுங்கள்.", "स्टोर में खाली हुक को खराबी के रूप में रिपोर्ट करें।"),
           trigger=flag("ear_hook"), requires=["open_store"], points=15, concept="ppe_completeness", scene="report", marker="ppe_store",
           hints=[T("Compare each item the sign requires with what is on the hooks.", "அடையாளம் கோரும் ஒவ்வொரு பொருளையும் கொக்கிகளில் உள்ளவற்றுடன் ஒப்பிடுங்கள்.", "संकेत की हर वस्तु को हुक पर रखी चीज़ों से मिलाएँ।")])
    m.step("stop_mani", title=T("Stop Mani going in unprotected", "பாதுகாப்பின்றி மணி உள்ளே செல்வதைத் தடுங்கள்", "मणि को बिना सुरक्षा अंदर जाने से रोकें"),
           instruction=T("Talk to Mani at the door.", "கதவருகே மணியுடன் பேசுங்கள்.", "दरवाज़े पर मणि से बात करें।"),
           trigger=decide("mani", "stop"), requires=["flag_missing"], points=15, concept="ppe_completeness", scene="communicate", marker="contractor",
           hints=[T("He is about to enter without what the sign requires.", "அடையாளம் கோருவது இல்லாமல் அவர் நுழையப் போகிறார்.", "वह संकेत की आवश्यकता के बिना अंदर जाने वाला है।")])
    m.step("decide", title=T("Decide on entry", "நுழைவு குறித்து முடிவு செய்யுங்கள்", "प्रवेश पर निर्णय लें"),
           instruction=T("Record your entry decision at the PPE store.", "PPE களஞ்சியத்தில் உங்கள் நுழைவு முடிவைப் பதிவுசெய்யுங்கள்.", "PPE स्टोर पर अपना प्रवेश निर्णय दर्ज करें।"),
           trigger=decide("entry", "wait_report"), requires=["stop_mani", "take_helmet", "take_glasses"], points=20, concept="ppe_completeness", scene="decision", marker="ppe_store",
           mistake_if_early=T("Check the sign, the store and the people at the door first.", "முதலில் அடையாளம், களஞ்சியம், கதவருகே உள்ளவர்களைச் சரிபாருங்கள்.", "पहले संकेत, स्टोर और दरवाज़े पर मौजूद लोगों को देखें।"),
           hints=[T("Protection that isn't there can't protect you.", "இல்லாத பாதுகாப்பு உங்களைப் பாதுகாக்காது.", "जो सुरक्षा नहीं है वह आपको नहीं बचा सकती।")])

    m.critical("enter_unprotected", trigger=enter("zone_khouse"), concept="ppe_completeness", dialogue="unsafe",
               explanation=T("You entered a posted hearing-protection area without hearing protection.", "செவிப் பாதுகாப்பு அறிவிக்கப்பட்ட பகுதிக்குள் செவிப் பாதுகாப்பின்றி நுழைந்தீர்கள்.", "आप श्रवण-सुरक्षा क्षेत्र में बिना श्रवण सुरक्षा के गए।"),
               missing=T("All PPE on the entry sign, including hearing protection.", "செவிப் பாதுகாப்பு உட்பட நுழைவு அடையாளத்தில் உள்ள அனைத்து PPE-யும்.", "श्रवण सुरक्षा सहित प्रवेश संकेत का पूरा PPE।"))
    m.critical("go_quick", trigger=decide("entry", "go_quick"), concept="ppe_completeness", dialogue="unsafe",
               explanation=T("'Quickly' is not a type of protection. The requirement applies however short the visit.", "'விரைவாக' என்பது பாதுகாப்பு வகை அல்ல. எவ்வளவு குறுகிய வருகையாக இருந்தாலும் தேவை பொருந்தும்.", "'जल्दी' कोई सुरक्षा नहीं है। भेंट कितनी भी छोटी हो, आवश्यकता लागू है।"),
               missing=T("Hearing protection from stores.", "களஞ்சியத்திலிருந்து செவிப் பாதுகாப்பு.", "स्टोर से श्रवण सुरक्षा।"))
    m.critical("improvised_ppe", trigger=decide("entry", "improvise"), concept="ppe_specification", dialogue="unsafe",
               explanation=T("Improvised items are not PPE. Protection must be the type the task requires.", "தற்காலிகப் பொருட்கள் PPE அல்ல. பாதுகாப்பு பணிக்குத் தேவையான வகையாக இருக்க வேண்டும்.", "जुगाड़ की चीज़ें PPE नहीं हैं। सुरक्षा उसी प्रकार की होनी चाहिए जो काम माँगता है।"),
               missing=T("Proper hearing protection.", "சரியான செவிப் பாதுகாப்பு.", "उचित श्रवण सुरक्षा।"))
    m.mistake("let_mani_go", trigger=decide("mani", "let_go"), kind="incorrect_decision", concept="ppe_completeness",
              feedback=T("Mani is about to be exposed without protection. Talk to him again.", "மணி பாதுகாப்பின்றி வெளிப்படப் போகிறார். அவருடன் மீண்டும் பேசுங்கள்.", "मणि बिना सुरक्षा जोखिम में जाने वाला है। उससे फिर बात करें।"))
    m.mistake("wrong_defect", trigger={"type": "evidence_flagged"}, kind="incorrect_decision", concept="ppe_condition",
              feedback=T("That item is fine. Which hook doesn't match the sign?", "அந்தப் பொருள் சரியானது. எந்தக் கொக்கி அடையாளத்துடன் பொருந்தவில்லை?", "वह वस्तु ठीक है। कौन सा हुक संकेत से मेल नहीं खाता?"))
    m.mistake("gloves_extra", trigger=select("gloves"), kind="advisory", concept="ppe_task_requirements",
              feedback=T("Gloves aren't on this sign. They won't replace hearing protection.", "கையுறைகள் இந்த அடையாளத்தில் இல்லை. அவை செவிப் பாதுகாப்புக்கு மாற்றாகாது.", "दस्ताने इस संकेत में नहीं हैं। ये श्रवण सुरक्षा की जगह नहीं लेंगे।"))

    m.debrief(
        success=T("You spotted the empty hook, reported it, stopped Mani and stayed out until protection arrives.", "காலியான கொக்கியைக் கண்டு, தெரிவித்து, மணியை நிறுத்தி, பாதுகாப்பு வரும் வரை வெளியே இருந்தீர்கள்.", "आपने खाली हुक देखा, रिपोर्ट किया, मणि को रोका और सुरक्षा आने तक बाहर रहे।"),
        critical=T("Entry happened without the required protection. Missing PPE means waiting, not improvising.", "தேவையான பாதுகாப்பின்றி நுழைவு நடந்தது. இல்லாத PPE என்றால் காத்திருத்தல், தற்காலிக மாற்று அல்ல.", "आवश्यक सुरक्षा के बिना प्रवेश हुआ। गायब PPE का मतलब इंतज़ार है, जुगाड़ नहीं।"),
        failed=T("Repeated unsafe choices ended the attempt.", "தொடர்ந்த பாதுகாப்பற்ற தேர்வுகள் முயற்சியை முடித்தன.", "बार-बार असुरक्षित विकल्पों से प्रयास समाप्त हुआ।"),
        lines=[
            ({"criticalRule": "enter_unprotected"}, T("You walked into the compressor house without hearing protection.", "செவிப் பாதுகாப்பின்றி அழுத்தி இல்லத்திற்குள் சென்றீர்கள்.", "आप बिना श्रवण सुरक्षा कंप्रेसर हाउस में गए।")),
            ({"criticalRule": "improvised_ppe"}, T("You chose an improvised substitute for PPE.", "PPE-க்குத் தற்காலிக மாற்றைத் தேர்ந்தெடுத்தீர்கள்.", "आपने PPE का जुगाड़ू विकल्प चुना।")),
            ({"stepCompleted": "flag_missing"}, T("You reported the missing ear defenders.", "இல்லாத காது பாதுகாப்பைத் தெரிவித்தீர்கள்.", "आपने गायब ईयर डिफ़ेंडर रिपोर्ट किए।")),
            ({"stepCompleted": "stop_mani"}, T("You stopped a colleague entering unprotected.", "பாதுகாப்பின்றி நுழைய இருந்த சக ஊழியரை நிறுத்தினீர்கள்.", "आपने एक साथी को बिना सुरक्षा जाने से रोका।")),
            ({"counterAbove": ["incorrectDecisions", 0]}, T("At least one choice let a gap slip by.", "குறைந்தது ஒரு தேர்வு ஒரு குறைபாட்டை நழுவ விட்டது.", "कम से कम एक विकल्प ने कमी को छूटने दिया।")),
        ],
    )
    m.comic(T("NO PROTECTION, NO ENTRY", "பாதுகாப்பு இல்லையா, நுழைவு இல்லை", "सुरक्षा नहीं, प्रवेश नहीं"), [
        ("document_gap", T("The sign at the door sets the requirement.", "கதவருகே உள்ள அடையாளம் தேவையை நிர்ணயிக்கிறது.", "दरवाज़े का संकेत आवश्यकता तय करता है।")),
        ("ppe", T("An empty hook is a finding — report it.", "காலியான கொக்கி ஒரு கண்டுபிடிப்பு — தெரிவியுங்கள்.", "खाली हुक एक निष्कर्ष है — रिपोर्ट करें।")),
        ("team", T("Look out for each other at the door.", "கதவருகே ஒருவரையொருவர் கவனித்துக்கொள்ளுங்கள்.", "दरवाज़े पर एक-दूसरे का ध्यान रखें।")),
    ])
    m.report(["read_sign", "take_helmet", "take_glasses", "flag_missing"], ["stop_mani", "decide"])
    m.mcq(1, concept="ppe_completeness",
          stem=T("The sign requires hearing protection, but none is in stock. What do you do?", "அடையாளம் செவிப் பாதுகாப்பைக் கோருகிறது, ஆனால் கையிருப்பில் இல்லை. என்ன செய்வீர்கள்?", "संकेत श्रवण सुरक्षा माँगता है, पर स्टॉक में नहीं है। आप क्या करेंगे?"),
          options=[T("Enter quickly", "விரைவாக நுழைவேன்", "जल्दी अंदर जाऊँगा"), T("Report it and wait outside until it is available", "தெரிவித்து, கிடைக்கும் வரை வெளியே காத்திருப்பேன்", "रिपोर्ट करूँगा और उपलब्ध होने तक बाहर रुकूँगा"), T("Borrow someone else's used pair without checking it", "சரிபார்க்காமல் வேறொருவரின் பயன்படுத்திய ஜோடியை இரவல் வாங்குவேன்", "बिना जाँचे किसी और की इस्तेमाल की जोड़ी उधार लूँगा")],
          correct="b", explanation=T("Missing PPE is reported; entry waits until the requirement can be met.", "இல்லாத PPE தெரிவிக்கப்படுகிறது; தேவை பூர்த்தியாகும் வரை நுழைவு காத்திருக்கும்.", "गायब PPE रिपोर्ट होता है; आवश्यकता पूरी होने तक प्रवेश रुकता है।"))
    m.mcq(2, concept="ppe_specification",
          stem=T("Is tissue paper in your ears an acceptable substitute for hearing protection?", "காதுகளில் காகிதம் வைப்பது செவிப் பாதுகாப்புக்கு ஏற்ற மாற்றா?", "क्या कानों में टिश्यू पेपर श्रवण सुरक्षा का स्वीकार्य विकल्प है?"),
          options=[T("Yes, in an emergency", "ஆம், அவசரத்தில்", "हाँ, आपात स्थिति में"), T("Yes, for short visits", "ஆம், குறுகிய வருகைகளுக்கு", "हाँ, छोटी भेंट के लिए"), T("No — improvised items are not PPE", "இல்லை — தற்காலிகப் பொருட்கள் PPE அல்ல", "नहीं — जुगाड़ की चीज़ें PPE नहीं हैं")],
          correct="c", explanation=T("PPE is equipment of the type the task requires, not an improvised substitute.", "PPE என்பது பணிக்குத் தேவையான வகை உபகரணம், தற்காலிக மாற்று அல்ல.", "PPE वह उपकरण है जो काम माँगता है, जुगाड़ू विकल्प नहीं।"))
    m.mcq(3, concept="ppe_completeness",
          stem=T("A colleague is about to enter without required PPE. What is the best action?", "ஒரு சக ஊழியர் தேவையான PPE இல்லாமல் நுழையப் போகிறார். சிறந்த செயல் எது?", "एक साथी बिना आवश्यक PPE के जाने वाला है। सबसे अच्छा कार्य क्या है?"),
          options=[T("Say nothing — it's their choice", "எதுவும் சொல்ல மாட்டேன் — அது அவர்கள் விருப்பம்", "कुछ नहीं कहूँगा — यह उनकी मर्ज़ी है"), T("Politely stop them and explain the requirement", "மரியாதையுடன் நிறுத்தி தேவையை விளக்குவேன்", "विनम्रता से रोककर आवश्यकता समझाऊँगा"), T("Report them later", "பின்னர் அவர்களைப் பற்றிப் புகாரளிப்பேன்", "बाद में उनकी रिपोर्ट करूँगा")],
          correct="b", explanation=T("Stopping exposure before it happens matters more than reporting after.", "பின்னர் புகாரளிப்பதை விட, வெளிப்பாடு நடக்கும் முன் தடுப்பதே முக்கியம்.", "बाद में रिपोर्ट से ज़्यादा ज़रूरी है जोखिम होने से पहले रोकना।"))
    m.mcq(4, concept="ppe_task_requirements",
          stem=T("Where were the PPE requirements for the compressor house shown?", "அழுத்தி இல்லத்திற்கான PPE தேவைகள் எங்கே காட்டப்பட்டன?", "कंप्रेसर हाउस की PPE आवश्यकताएँ कहाँ दिखाई गई थीं?"),
          options=[T("On the entry sign at the door", "கதவருகே உள்ள நுழைவு அடையாளத்தில்", "दरवाज़े के प्रवेश संकेत पर"), T("On the compressor nameplate", "அழுத்தியின் பெயர்ப் பலகையில்", "कंप्रेसर की नाम-पट्टिका पर"), T("Nowhere — you have to guess", "எங்கும் இல்லை — ஊகிக்க வேண்டும்", "कहीं नहीं — अनुमान लगाना पड़ता है")],
          correct="a", explanation=T("Posted area requirements are read before entry.", "அறிவிக்கப்பட்ட பகுதித் தேவைகள் நுழைவதற்கு முன் படிக்கப்படுகின்றன.", "लिखी क्षेत्र आवश्यकताएँ प्रवेश से पहले पढ़ी जाती हैं।"))
    m.spec(
        workplaceLocation="Fictional compressor house in the utility block.",
        corePrinciple="Missing required PPE is reported and entry waits; improvised substitutes are not PPE.",
        commonMisconceptions=["Two minutes without protection is fine.", "Any substitute will do."],
        criticalDecisions=["Enter quickly", "Improvise protection", "Walk into the zone"],
        assessmentCriteria={"correct": "Read sign; take helmet/glasses; report empty hook; stop Mani; wait and report."},
        note2="No noise levels or exposure limits are stated or implied.",
    )
    return m
