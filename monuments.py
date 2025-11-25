# monuments.py

# List of all available monument keys for random selection
MONUMENT_KEYS = [
    "Taj Mahal", 
    "Qutub Minar", 
    "Red Fort", 
    "Konark Temple", 
    "Charminar", 
    "Golconda Fort"
]

# --- MOCK DATA FOR DEMONSTRATION (Expanded) ---
MONUMENT_DATA_MOCK = {
    # ------------------------------------------------------------------
    # 1. TAJ MAHAL 
    # ------------------------------------------------------------------
    "Taj Mahal": {
        "name": "Taj Mahal", 
        "maps_link": "http://googleusercontent.com/maps.google.com/place/Taj+Mahal",
        "EN": {
            "display_name": "Taj Mahal",
            "history": "Commissioned in 1632 by the Mughal emperor, Shah Jahan, to house the tomb of his favorite wife, Mumtaz Mahal. It is a UNESCO World Heritage Site.",
            "arch": "A stunning example of Mughal architecture, blending Persian, Islamic, and Indian styles, built primarily of white marble with intricate inlay work.",
            "tips": "Visit at sunrise or sunset for the best light. Closed on Fridays for prayer."
        },
        "HI": {
            "display_name": "ताज महल",
            "history": "मुगल सम्राट शाहजहाँ द्वारा 1632 में अपनी प्रिय पत्नी, मुमताज महल की कब्र के लिए बनवाया गया। यह यूनेस्को विश्व धरोहर स्थल है।",
            "arch": "मुगल वास्तुकला का एक अद्भुत उदाहरण, जो फारसी, इस्लामी और भारतीय शैलियों का मिश्रण है, और मुख्य रूप से सफेद संगमरमर से बना है।",
            "tips": "सबसे अच्छी रोशनी के लिए सूर्योदय या सूर्यास्त के समय जाएँ। यह शुक्रवार को प्रार्थना के लिए बंद रहता है। "
        },
        "OD": {
            "display_name": "ତାଜ୍ ମହଲ",
            "history": "ମୋଗଲ ସମ୍ରାଟ ଶାହାଜାହାଁଙ୍କ ଦ୍ୱାରା ତାଙ୍କ ପ୍ରିୟ ପତ୍ନୀ ମୁମତାଜ ମହଲଙ୍କ ସମାଧି ପାଇଁ ୧୬୩୨ ମସିହାରେ ନିର୍ମିତ ହୋଇଥିଲା। ଏହା ଏକ ୟୁନେସ୍କୋ ବିଶ୍ୱ ଐତିହ୍ୟ ସ୍ଥଳ।",
            "arch": "ମୋଗଲ ସ୍ଥାପତ୍ୟର ଏକ ଚମତ୍କାର ଉଦାହରଣ, ଯାହା ପାରସୀ, ଇସଲାମୀୟ ଏବଂ ଭାରତୀୟ ଶୈଳୀର ମିଶ୍ରଣରେ ମୁଖ୍ୟତଃ ଧଳା ମାର୍ବଲରେ ନିର୍ମିତ।",
            "tips": "ସର୍ବୋତ୍ତମ ଆଲୋକ ପାଇଁ ସୂର୍ଯ୍ୟୋଦୟ କିମ୍ବା ସୂର୍ଯ୍ୟାସ୍ତ ସମୟରେ ପରିଦର୍ଶନ କରନ୍ତୁ। ଶୁକ୍ରବାର ଦିନ ଏହା ବନ୍ଦ ରୁହେ।"
        },
        "TE": {
            "display_name": "తాజ్ మహల్",
            "history": "మొఘల్ చక్రవర్తి షాజహాన్ తన ప్రియమైన భార్య ముంతాజ్ మహల్ సమాధి కోసం 1632లో దీనిని నిర్మించారు. ఇది యునెస్కో ప్రపంచ వారసత్వ ప్రదేశం.",
            "arch": "పర్షియన్, ఇస్లామిక్ మరియు భారతీయ శైలుల కలయికతో కూడిన మొఘల్ నిర్మాణానికి అద్భుతమైన ఉదాహరణ, ప్రధానంగా తెల్లని పాలరాతితో నిర్మించబడింది.",
            "tips": "ఉత్తమ కాంతి కోసం సూర్యోదయం లేదా సూర్యాస్తమయం సమయంలో సందర్శించండి. శుక్రవారాల్లో మూసివేయబడుతుంది।"
        }
    },
    # ------------------------------------------------------------------
    # 2. QUTUB MINAR
    # ------------------------------------------------------------------
    "Qutub Minar": {
        "name": "Qutub Minar",
        "maps_link": "http://googleusercontent.com/maps.google.com/place/Qutub+Minar",
        "EN": {
            "display_name": "Qutub Minar",
            "history": "A UNESCO World Heritage Site in Delhi, constructed starting in 1192 by Qutb-ud-din Aibak. It is the tallest brick minaret in the world.",
            "arch": "Indo-Islamic architecture. The tower is a tapering structure with fluted columns and is surrounded by several historically significant monuments.",
            "tips": "Best viewed in the late afternoon. Don't miss the Iron Pillar in the complex, famous for not rusting."
        },
        "HI": {
            "display_name": "क़ुतुब मीनार",
            "history": "दिल्ली में एक यूनेस्को विश्व धरोहर स्थल, जिसका निर्माण 1192 में कुतुब-उद-दीन ऐबक द्वारा शुरू किया गया था। यह दुनिया की सबसे ऊंची ईंटों से बनी मीनार है।",
            "arch": "इंडो-इस्लामिक वास्तुकला। मीनार बांसुरीदार स्तंभों के साथ एक पतला ढांचा है और कई ऐतिहासिक स्मारकों से घिरा हुआ है।",
            "tips": "दोपहर के बाद सबसे अच्छा दृश्य दिखता है। परिसर में स्थित लौह स्तंभ को अवश्य देखें, जो जंग न लगने के लिए प्रसिद्ध है।"
        },
        "OD": {
            "display_name": "କୁତୁବ ମୀନାର",
            "history": "ଦିଲ୍ଲୀରେ ଥିବା ଏକ ୟୁନେସ୍କୋ ବିଶ୍ୱ ଐତିହ୍ୟ ସ୍ଥଳ, ଯାହାର ନିର୍ମାଣ ୧୧୯୨ ମସିହାରେ କୁତବ-ଉଦ-ଦିନ ଆଇବକଙ୍କ ଦ୍ୱାରା ଆରମ୍ଭ କରାଯାଇଥିଲା। ଏହା ଦୁନିଆର ସବୁଠାରୁ ଉଚ୍ଚ ଇଟା ମୀନାର।",
            "arch": "ଭାରତ-ଇସଲାମୀୟ ସ୍ଥାପତ୍ୟ। ଏହି ମୀନାର ଚାରିପାଖରେ ଅନେକ ଐତିହାସିକ ସ୍ମାରକୀ ରହିଛି।",
            "tips": "ଅପରାହ୍ନରେ ଏହାର ଦୃଶ୍ୟ ସର୍ବୋତ୍ତମ। କମ୍ପ୍ଲେକ୍ସରେ ଥିବା ଲୌହ ସ୍ତମ୍ଭକୁ ଦେଖିବାକୁ ଭୁଲନ୍ତୁ ନାହିଁ, ଯାହା ଜଙ୍ଗ ଲାଗି ନଥିବାରୁ ପ୍ରସିଦ୍ଧ।"
        },
        "TE": {
            "display_name": "కుతుబ్ మినార్",
            "history": "ఢిల్లీలోని యునెస్కో ప్రపంచ వారసత్వ ప్రదేశం, దీని నిర్మాణం 1192లో కుతుబ్-ఉద్-దిన్ ఐబక్ చేత ప్రారంభించబడింది. ఇది ప్రపంచంలోనే ఎత్తైన ఇటుక మినార్.",
            "arch": "ఇండో-ఇస్లామిక్ వాస్తుశిల్పం. ఈ టవర్ పలు చారిత్రక స్మారక కట్టడాలతో చుట్టుముట్టబడి ఉంది.",
            "tips": "సాయంత్రం చూడటానికి చాలా బాగుంటుంది. తుప్పు పట్టని ఇనుప స్తంభాన్ని తప్పక చూడండి।"
        }
    },
    # ------------------------------------------------------------------
    # 3. RED FORT
    # ------------------------------------------------------------------
    "Red Fort": {
        "name": "Red Fort",
        "maps_link": "http://googleusercontent.com/maps.google.com/place/Red+Fort",
        "EN": {
            "display_name": "Red Fort",
            "history": "Built in the 17th century by Emperor Shah Jahan as the palace fort of his capital Shahjahanabad. It served as the seat of Mughal power for nearly 200 years.",
            "arch": "Mughal architecture with red sandstone walls. It is a fusion of Persian, Timurid, and Indian styles, known for its extensive use of ornamentation.",
            "tips": "Visit the evening light and sound show for a detailed historical narrative. Be prepared for large crowds, especially on national holidays."
        },
        "HI": {
            "display_name": "लाल क़िला",
            "history": "17वीं शताब्दी में सम्राट शाहजहाँ द्वारा अपनी राजधानी शाहजहानाबाद के महल किले के रूप में बनवाया गया था। यह लगभग 200 वर्षों तक मुगल सत्ता का केंद्र रहा।",
            "arch": "लाल बलुआ पत्थर की दीवारों के साथ मुगल वास्तुकला। यह फारसी, तैमूरिद और भारतीय शैलियों का मिश्रण है, जो अलंकरण के व्यापक उपयोग के लिए जाना जाता है।",
            "tips": "विस्तृत ऐतिहासिक विवरण के लिए शाम के लाइट एंड साउंड शो को देखें। राष्ट्रीय छुट्टियों पर बड़ी भीड़ के लिए तैयार रहें।"
        },
        "OD": {
            "display_name": "ଲାଲ୍ କିଲ୍ଲା",
            "history": "୧୭ଶ ଶତାବ୍ଦୀରେ ସମ୍ରାଟ ଶାହାଜାହାଁଙ୍କ ଦ୍ୱାରା ତାଙ୍କ ରାଜଧାନୀ ଶାହାଜାନାବାଦର ରାଜପ୍ରାସାଦ ଦୁର୍ଗ ଭାବରେ ନିର୍ମିତ ହୋଇଥିଲା। ଏହା ପ୍ରାୟ ୨୦୦ ବର୍ଷ ଧରି ମୋଗଲ ଶାସନର କେନ୍ଦ୍ର ଥିଲା।",
            "arch": "ଲାଲ ବାଲିପଥର କାନ୍ଥ ସହିତ ମୋଗଲ ସ୍ଥାପତ୍ୟ। ଏହା ପାରସୀ, ତୈମୁରିଡ ଏବଂ ଭାରତୀୟ ଶୈଳୀର ମିଶ୍ରଣ।",
            "tips": "ବିସ୍ତୃତ ଐତିହାସିକ ବର୍ଣ୍ଣନା ପାଇଁ ସନ୍ଧ୍ୟା ଲାଇଟ୍ ଆଣ୍ଡ ସାଉଣ୍ଡ୍ ସୋ' ଦେଖନ୍ତୁ। ଜାତୀୟ ଛୁଟିରେ ଅଧିକ ଭିଡ଼ ପାଇଁ ପ୍ରସ୍ତୁତ ରୁହନ୍ତୁ।"
        },
        "TE": {
            "display_name": "ఎర్ర కోట",
            "history": "17వ శతాబ్దంలో చక్రవర్తి షాజహాన్ తన రాజధాని షాజహానాబాద్ ప్యాలెస్ కోటగా నిర్మించారు. ఇది దాదాపు 200 సంవత్సరాలు మొఘల్ శక్తికి కేంద్రంగా పనిచేసింది।",
            "arch": "ఎరుపు ఇసుకరాయి గోడలతో మొఘల్ వాస్తుశిల్పం. ఇది పర్షియన్, తైమూరిడ్ మరియు భారతీయ శైలుల సమ్మేళనం।",
            "tips": "చారిత్రక కథనం కోసం సాయంత్రం లైట్ అండ్ సౌండ్ షో చూడండి. జాతీయ సెలవుల్లో ఎక్కువ మంది జనం ఉంటారు।"
        }
    },
    # ------------------------------------------------------------------
    # 4. KONARK TEMPLE
    # ------------------------------------------------------------------
    "Konark Temple": {
        "name": "Konark Temple",
        "maps_link": "http://googleusercontent.com/maps.google.com/place/Konark+Sun+Temple",
        "EN": {
            "display_name": "Konark Sun Temple",
            "history": "Dedicated to the Sun God Surya, this 13th-century temple was built by King Narasimhadeva I of the Eastern Ganga Dynasty. It is a UNESCO World Heritage Site.",
            "arch": "Kalinga architecture, designed in the shape of a colossal chariot with 12 pairs of intricately carved stone wheels and pulled by seven horses.",
            "tips": "Focus on the detail of the wheels, which serve as accurate sundials. The main temple structure is largely in ruins, but the surviving hall is impressive."
        },
        "HI": {
            "display_name": "कोणार्क सूर्य मंदिर",
            "history": "सूर्य देव को समर्पित, यह 13वीं शताब्दी का मंदिर पूर्वी गंगा राजवंश के राजा नरसिंहदेव प्रथम द्वारा बनवाया गया था। यह यूनेस्को विश्व धरोहर स्थल है।",
            "arch": "कलिंग वास्तुकला, जिसे 12 जोड़ी बारीक नक्काशीदार पत्थर के पहियों वाले एक विशाल रथ के आकार में डिजाइन किया गया है और इसे सात घोड़े खींचते हुए दर्शाया गया है।",
            "tips": "पहियों के विवरण पर ध्यान दें, जो सटीक सूर्यघड़ी के रूप में कार्य करते हैं। मुख्य मंदिर का ढांचा काफी हद तक खंडहर हो चुका है, लेकिन बचा हुआ हॉल प्रभावशाली है।"
        },
        "OD": {
            "display_name": "କୋଣାର୍କ ମନ୍ଦିର",
            "history": "ସୂର୍ଯ୍ୟ ଦେବତାଙ୍କୁ ସମର୍ପିତ ଏହି ୧୩ଶ ଶତାବ୍ଦୀର ମନ୍ଦିରଟି ଗଙ୍ଗା ବଂଶର ରାଜା ନରସିଂହ ଦେବ-୧ଙ୍କ ଦ୍ୱାରା ନିର୍ମିତ ହୋଇଥିଲା। ଏହା ଏକ ୟୁନେସ୍କୋ ବିଶ୍ୱ ଐତିହ୍ୟ ସ୍ଥଳ।",
            "arch": "କଳିଙ୍ଗ ସ୍ଥାପତ୍ୟ, ଏହାକୁ ୧୨ ଯୋଡ଼ା ପଥର ଚକ ଏବଂ ସାତୋଟି ଘୋଡ଼ା ଦ୍ୱାରା ଟଣାଯାଉଥିବା ଏକ ବିଶାଳ ରଥ ଆକାରରେ ପରିକଳ୍ପନା କରାଯାଇଛି।",
            "tips": "ସର୍ବୋତ୍ତମ ଆଲୋକ ପାଇଁ ସୂର୍ଯ୍ୟୋଦୟ କିମ୍ବା ସୂର୍ଯ୍ୟାସ୍ତ ସମୟରେ ପରିଦର୍ଶନ କରନ୍ତୁ। ଶୁକ୍ରବାର ଦିନ ଏହା ବନ୍ଦ ରୁହେ।"
        },
        "TE": {
            "display_name": "కోణార్క్ సూర్య దేవాలయం",
            "history": "సూర్య భగవానుడికి అంకితం చేయబడిన ఈ 13వ శతాబ్దపు ఆలయాన్ని తూర్పు గంగా రాజవంశానికి చెందిన రాజు నరసింహదేవ I నిర్మించారు. ఇది యునెస్కో ప్రపంచ వారసత్వ ప్రదేశం.",
            "arch": "కళింగ వాస్తుశిల్పం, దీనిని 12 జతల రాతి చక్రాలతో కూడిన రథం ఆకారంలో రూపొందించారు, దీనిని ఏడు గుర్రాలు లాగుతున్నట్లుగా చూపబడింది।",
            "tips": "ఖచ్చితమైన సూర్య గడియారాలుగా పనిచేసే చక్రాల వివరాలపై దృష్టి పెట్టండి. ప్రధాన ఆలయ నిర్మాణం శిథిలావస్థలో ఉన్నప్పటికీ, మిగిలిన హాలు అద్భుతంగా ఉంటుంది।"
        }
    },
    # ------------------------------------------------------------------
    # 5. CHARMINAR
    # ------------------------------------------------------------------
    "Charminar": {
        "name": "Charminar",
        "maps_link": "http://googleusercontent.com/maps.google.com/place/Charminar",
        "EN": {
            "display_name": "Charminar",
            "history": "A monument and mosque located in Hyderabad, built in 1591 by Muhammad Quli Qutb Shah to commemorate the end of a deadly plague epidemic.",
            "arch": "Indo-Islamic architecture featuring four grand arches facing the cardinal directions, supporting four minarets. It is the global icon of Hyderabad.",
            "tips": "Climb to the top floor for a panoramic view of the old city. Be aware that the surrounding area is a busy, traditional bazaar."
        },
        "HI": {
            "display_name": "चारमीनार",
            "history": "हैदराबाद में स्थित एक स्मारक और मस्जिद, जिसे 1591 में मुहम्मद कुली कुतुब शाह ने एक घातक प्लेग महामारी के अंत की याद में बनवाया था।",
            "arch": "इंडो-इस्लामिक वास्तुकला जिसमें चार भव्य मेहराब हैं जो चार मीनारों का समर्थन करते हुए दिशाओं का सामना करते हैं। यह हैदराबाद का वैश्विक प्रतीक है।",
            "tips": "पुराने शहर के मनोरम दृश्य के लिए शीर्ष मंजिल पर चढ़ें। ध्यान दें कि आस-पास का क्षेत्र एक व्यस्त, पारंपरिक बाज़ार है।"
        },
        "OD": {
            "display_name": "ଚାରମିନାର",
            "history": "ହାଇଦ୍ରାବାଦରେ ଅବସ୍ଥିତ ଏକ ସ୍ମାରକୀ ଏବଂ ମସଜିଦ, ଯାହାକୁ ୧୫୯୧ ମସିହାରେ ମହମ୍ମଦ କୁଲି କୁତବ ଶାହା ଏକ ଭୟଙ୍କର ମହାମାରୀର ସମାପ୍ତିକୁ ସ୍ମରଣ କରିବା ପାଇଁ ନିର୍ମାଣ କରିଥିଲେ।",
            "arch": "ଭାରତ-ଇସଲାମୀୟ ସ୍ଥାପତ୍ୟ, ଯେଉଁଥିରେ ଚାରୋଟି ମୀନାରକୁ ସମର୍ଥନ କରୁଥିବା ଚାରୋଟି ବୃହତ ଆର୍କ ଅଛି। ଏହା ହାଇଦ୍ରାବାଦର ବିଶ୍ୱସ୍ତରୀୟ ପ୍ରତୀକ।",
            "tips": "ପୁରୁଣା ସହରର ଦୃଶ୍ୟ ପାଇଁ ଉପର ମହଲାକୁ ଚଢ଼ନ୍ତୁ। ଆଖପାଖ ଅଞ୍ଚଳ ଏକ ବ୍ୟସ୍ତବହୁଳ ବଜାର ବୋଲି ଜାଣି ରଖନ୍ତୁ।"
        },
        "TE": {
            "display_name": "చార్మినార్",
            "history": "హైదరాబాద్‌లో ఉన్న ఒక స్మారక చిహ్నం మరియు మసీదు, దీనిని 1591లో ముహమ్మద్ కులీ కుతుబ్ షా ఒక ఘోరమైన ప్లేగు వ్యాధి ముగింపును గుర్తుచేసుకోవడానికి నిర్మించారు.",
            "arch": "ఇండో-ఇస్లామిక్ వాస్తుశిల్పం, నాలుగు మినార్‌లకు మద్దతుగా నాలుగు ప్రధాన వంపులు నాలుగు దిక్కులకు ఎదురుగా ఉంటాయి। ఇది హైదరాబాద్‌కు ప్రపంచ చిహ్నం।",
            "tips": "పాత నగరం యొక్క విశాల దృశ్యం కోసం పై అంతస్తుకు ఎక్కండి. చుట్టుపక్కల ప్రాంతం రద్దీగా ఉండే సాంప్రదాయ బజారు అని తెలుసుకోండి।"
        }
    },
    # ------------------------------------------------------------------
    # 6. GOLCONDA FORT
    # ------------------------------------------------------------------
    "Golconda Fort": {
        "name": "Golconda Fort",
        "maps_link": "http://googleusercontent.com/maps.google.com/place/Golconda+Fort",
        "EN": {
            "display_name": "Golconda Fort",
            "history": "Originally a mud fort built by the Kakatiya dynasty, it was greatly expanded by the Qutb Shahi kings in the 16th century. It was once famous for its diamond trade.",
            "arch": "A massive hill fortress covering several kilometers, known for its intricate acoustic system (clapping hands at the entrance can be heard at the top pavilion).",
            "tips": "Wear comfortable shoes, as there is a lot of walking and climbing. Attend the evening sound and light show for a detailed history of the fort."
        },
        "HI": {
            "display_name": "गोलकोंडा किला",
            "history": "मूल रूप से काकतीय राजवंश द्वारा बनवाया गया एक मिट्टी का किला, इसे 16वीं शताब्दी में कुतुब शाही राजाओं द्वारा बड़े पैमाने पर विस्तारित किया गया था। यह एक समय अपने हीरे के व्यापार के लिए प्रसिद्ध था।",
            "arch": "कई किलोमीटर तक फैला एक विशाल पहाड़ी किला, जो अपनी जटिल ध्वनिक प्रणाली के लिए जाना जाता है (प्रवेश द्वार पर ताली बजाने की आवाज शीर्ष मंडप तक सुनी जा सकती है)।",
            "tips": "आरामदायक जूते पहनें, क्योंकि इसमें बहुत चलना और चढ़ना शामिल है। किले के विस्तृत इतिहास के लिए शाम के लाइट एंड साउंड शो में शामिल हों।"
        },
        "OD": {
            "display_name": "ଗୋଲକୋଣ୍ଡା ଦୁର୍ଗ",
            "history": "ମୂଳତଃ କାକତୀୟ ରାଜବଂଶ ଦ୍ୱାରା ନିର୍ମିତ ଏକ ମାଟି ଦୁର୍ଗ, ଏହା ୧୬ଶ ଶତାବ୍ଦୀରେ କୁତବ ଶାହି ରାଜାମାନଙ୍କ ଦ୍ୱାରା ବୃହତ ଭାବରେ ସମ୍ପ୍ରସାରିତ ହୋଇଥିଲା। ଏହା ଏକଦା ଏହାର ହୀରା ବାଣିଜ୍ୟ ପାଇଁ ପ୍ରସିଦ୍ଧ ଥିଲା।",
            "arch": "ଏକ ବିଶାଳ ପାହାଡ଼ ଦୁର୍ଗ ଯାହା ଏକ ଜଟିଳ ଆକାଉଷ୍ଟିକ ସିଷ୍ଟମ୍ ପାଇଁ ଜଣାଶୁଣା (ପ୍ରବେଶ ଦ୍ୱାରରେ ତାଳି ମାରିଲେ ତାହା ଉପର ପାଭିଲିୟନରେ ଶୁଣାଯାଏ)।",
            "tips": "ଆରାମଦାୟକ ଜୋତା ପିନ୍ଧନ୍ତୁ, କାରଣ ଏଥିରେ ବହୁତ ଚାଲିବା ଏବଂ ଚଢ଼ିବାକୁ ପଡ଼ିଥାଏ। ଦୁର୍ଗର ବିସ୍ତୃତ ଇତିହାସ ପାଇଁ ସନ୍ଧ୍ୟା ଲାଇଟ୍ ଆଣ୍ଡ ସାଉଣ୍ଡ୍ ସୋ'ରେ ଯୋଗ ଦିଅନ୍ତୁ।"
        },
        "TE": {
            "display_name": "గోల్కొండ కోట",
            "history": "వాస్తవానికి కాకతీయ రాజవంశం నిర్మించిన మట్టి కోట, దీనిని 16వ శతాబ్దంలో కుతుబ్ షాహి రాజులు విస్తరించారు। ఇది ఒకప్పుడు వజ్రాల వ్యాపారానికి ప్రసిద్ధి చెందింది।",
            "arch": "సంక్లిష్టమైన ధ్వని వ్యవస్థకు (ప్రవేశద్వారం వద్ద చప్పట్లు కొడితే పైన ఉన్న పెవిలియన్‌లో వినబడుతుంది) ప్రసిద్ధి చెందిన ఒక భారీ కొండ కోట।",
            "tips": "ఎక్కువగా నడవటం మరియు ఎక్కడం ఉంటుంది కాబట్టి సౌకర్యవంతమైన బూట్లు ధరించండి. కోట చరిత్ర కోసం సాయంత్రం లైట్ అండ్ సౌండ్ షో చూడండి।"
        }
    }
}
# --- END MOCK DATA ---
