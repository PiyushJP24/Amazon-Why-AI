"""New products (iteration 3) — extends PRODUCTS with real AI-powered devices.

8 products across all 6 categories, each with 5 features × 8 cluster benefit_templates.
"""

NEW_PRODUCTS = [
    # --- SMARTPHONES ---
    {
        "id": "xiaomi-14-ultra",
        "brand": "Xiaomi",
        "name": "Xiaomi 14 Ultra 5G AI Photography Smartphone",
        "category": "Smartphones",
        "price_inr": 99999,
        "rating": 4.4,
        "review_count": 1123,
        "image": "https://images.unsplash.com/photo-1580910051074-3eb694886505?crop=entropy&cs=srgb&fm=jpg&w=800&q=80",
        "tagline": "Leica quad camera, 1-inch sensor, AI HyperOS 2",
        "features": [
            {
                "feature_name": "Leica Quad Camera with 1-inch Sensor",
                "technical_meaning": "A 50MP Leica-tuned main sensor at 1-inch size with variable aperture, paired with 3 additional Leica lenses (ultrawide, 3.2x floating tele, 5x periscope) — designed for professional-grade photography.",
                "benefit_templates": {
                    "content_creation": "Shoot cinematic B-roll and portraits with a phone that behaves like a Leica kit.",
                    "gaming": "Capture crisp gameplay reactions and streams with pro-grade optics.",
                    "professional": "Business event photos and product shots look editorial-quality.",
                    "student": "Notes, whiteboards, and campus events look sharp in any light.",
                    "photography": "One phone gives you 4 focal lengths, all Leica-tuned — replaces most day-to-day glass.",
                    "family_general": "Family photos look professional even in tricky indoor light.",
                    "fitness_health": "Track outdoor training with crisp video for form review.",
                    "home_management": "Warranty cards, receipts, and inventory shots come out sharp.",
                }
            },
            {
                "feature_name": "HyperOS 2 with On-device AI",
                "technical_meaning": "HyperOS 2 runs on-device generative-AI features (AI Portrait, AI Erase, AI Interpreter) locally without needing cloud upload for common tasks.",
                "benefit_templates": {
                    "content_creation": "AI Erase and AI Portrait let you retouch content shots in seconds, on-device.",
                    "gaming": "AI resource scheduling keeps games smooth without spiking battery.",
                    "professional": "On-device AI Interpreter for calls keeps client data private.",
                    "student": "AI note summarisation happens locally — works even offline in class.",
                    "photography": "AI Erase removes photobombers cleanly without cloud round-trips.",
                    "family_general": "AI Portrait for group family shots — everyone looks their best.",
                    "fitness_health": "Local voice-to-text for workout journals without sending data anywhere.",
                    "home_management": "OCR receipts and household lists locally — no cloud, no waiting.",
                }
            },
            {
                "feature_name": "AI Real-Time Interpreter",
                "technical_meaning": "Cross-language live translation for calls and in-person conversations, powered by an on-device translation model with cloud fallback for less common languages.",
                "benefit_templates": {
                    "content_creation": "Interview foreign-language subjects and get live translation for subtitles.",
                    "gaming": "Play with international teammates without a language barrier.",
                    "professional": "Take cross-border client calls without a translator in the room.",
                    "student": "Watch foreign lectures with live translation running quietly.",
                    "photography": "Direct subjects on travel shoots — no phrasebook needed.",
                    "family_general": "Talk to relatives who speak different languages naturally.",
                    "fitness_health": "Follow foreign-language yoga or running coaches live.",
                    "home_management": "Communicate with international sellers and service staff easily.",
                }
            },
            {
                "feature_name": "5000mAh Battery with 90W HyperCharge",
                "technical_meaning": "A 5000mAh cell with 90W wired HyperCharge that hits full in ~35 minutes, plus 50W wireless charging.",
                "benefit_templates": {
                    "content_creation": "Long shoot days — 30-min top-up in-between takes.",
                    "gaming": "Full-day gaming with quick pit-stops keeping you above 60%.",
                    "professional": "Between meetings, a quick top-up gets you back to 100% in a coffee break.",
                    "student": "College day of classes, notes, and streaming without a mid-day charge.",
                    "photography": "All-day travel shoots without carrying a power bank.",
                    "family_general": "One quick top-up covers a family day out with photos and calls.",
                    "fitness_health": "Full-day GPS tracking + music without battery anxiety.",
                    "home_management": "Never scramble for a charger — always ready for calls and deliveries.",
                }
            },
            {
                "feature_name": "AI ProCut Video Mode",
                "technical_meaning": "On-device AI video editor that scans your clips, cuts to the best moments, and assembles a shareable edit with music — inspired by the phone's Leica movie modes.",
                "benefit_templates": {
                    "content_creation": "Assemble travel and vlog cuts on the phone before you land at your desk.",
                    "gaming": "Quick highlight reels from long gameplay recording sessions.",
                    "professional": "Client demo cuts assembled between meetings, no laptop needed.",
                    "student": "Trip and event edits for social while you're commuting home.",
                    "photography": "Behind-the-scenes videos from shoots edited in minutes.",
                    "family_general": "Family holiday videos edited and shared before you're home.",
                    "fitness_health": "Weekly training reels for your journal, cut automatically.",
                    "home_management": "Home project videos edited on the go for sharing with family.",
                }
            },
        ]
    },
    # --- LAPTOPS ---
    {
        "id": "dell-xps-14-ai",
        "brand": "Dell",
        "name": "Dell XPS 14 (2026) Copilot+ AI Laptop",
        "category": "Laptops",
        "price_inr": 159999,
        "rating": 4.3,
        "review_count": 421,
        "image": "https://images.unsplash.com/photo-1593642632559-0c6d3fc62b89?crop=entropy&cs=srgb&fm=jpg&w=800&q=80",
        "tagline": "Snapdragon X Elite, 45 TOPS NPU, 3K OLED",
        "features": [
            {
                "feature_name": "Snapdragon X Elite with 45 TOPS NPU",
                "technical_meaning": "Qualcomm Snapdragon X Elite ARM chip with a dedicated 45 TOPS NPU that offloads AI workloads (transcription, generative edits, background blur) from CPU/GPU.",
                "benefit_templates": {
                    "content_creation": "AI photo/video edits and local transcription run on-device — no cloud lag.",
                    "gaming": "AI upscaling on supported games without stealing GPU frames.",
                    "professional": "Live captions, background blur, and Copilot recall run locally on-device.",
                    "student": "Summarise lectures and research papers locally, even offline.",
                    "photography": "Denoise and select-subject edits complete in seconds.",
                    "family_general": "Family photo cleanups and AI edits happen without waiting.",
                    "fitness_health": "Hands-free voice journaling with local speech-to-text.",
                    "home_management": "OCR receipts and household docs on-device — private and fast.",
                }
            },
            {
                "feature_name": "Copilot+ Recall & AI Assist",
                "technical_meaning": "Windows Copilot+ features including Recall (timeline of past sessions), Cocreator (image generation), Live Captions, and Studio Effects — all NPU-accelerated.",
                "benefit_templates": {
                    "content_creation": "Recall a project from 2 weeks ago instantly; Cocreator drafts thumbnails and art.",
                    "gaming": "Studio Effects clean up your voice and camera on Discord automatically.",
                    "professional": "Recall past meetings and docs by describing them — never lose context.",
                    "student": "Recall old research and Cocreator drafts diagrams and figures for essays.",
                    "photography": "Cocreator drafts mood-boards; Studio Effects for client-review calls.",
                    "family_general": "Recall recipes, family docs, and school info in seconds.",
                    "fitness_health": "Recall your last training plans instantly; auto-clean video coaching calls.",
                    "home_management": "Recall bills and household docs by memory of when you saw them.",
                }
            },
            {
                "feature_name": "3.2K InfinityEdge OLED Display",
                "technical_meaning": "3200×2000 OLED touchscreen with 120Hz refresh, 100% DCI-P3 color coverage, and near-zero bezels — ideal for creative and cinematic work.",
                "benefit_templates": {
                    "content_creation": "Grading and editing with true-to-source colors on a bezel-less OLED.",
                    "gaming": "Smooth 120Hz OLED for casual gaming — deep blacks and vivid HDR.",
                    "professional": "Client presentations and dashboards look premium.",
                    "student": "PDFs and lecture videos on a sharp, bezel-less display for long sessions.",
                    "photography": "Trustworthy color rendering with a wide DCI-P3 gamut.",
                    "family_general": "Family movie nights and streaming look cinema-quality.",
                    "fitness_health": "Coaching videos and dashboards render smoothly and vividly.",
                    "home_management": "Everyday admin looks crisp with easy-to-read text at any zoom.",
                }
            },
            {
                "feature_name": "AI-optimised Battery (up to 27 hours)",
                "technical_meaning": "ARM-native architecture combined with AI-driven power scheduling delivers ~27 hours of local video playback, ~18 hours real productivity.",
                "benefit_templates": {
                    "content_creation": "Edit and export on a full-day travel without a charger.",
                    "gaming": "Long casual gaming sessions plus streaming without the outlet.",
                    "professional": "A workday of meetings, docs, and travel on one charge — easily.",
                    "student": "Full campus day of classes, PDFs, and research without a charger.",
                    "photography": "On-location editing days stretch further than any x86 laptop.",
                    "family_general": "A weekend of family use — movies, browsing, kids' work — on one charge.",
                    "fitness_health": "Live workout streaming and journaling all day, off the wall.",
                    "home_management": "Manage the household from anywhere — battery lasts full days.",
                }
            },
            {
                "feature_name": "Zero-Lattice Keyboard + Haptic Touchpad",
                "technical_meaning": "Edge-to-edge lattice-less keys with per-key backlighting, and a glass haptic touchpad that provides consistent click feedback anywhere on the surface.",
                "benefit_templates": {
                    "content_creation": "Every touchpad click feels precise for pixel-level editing.",
                    "gaming": "Snappy backlit keys for casual gaming and typing in dim rooms.",
                    "professional": "Fastest touch-typing surface for long email and doc sessions.",
                    "student": "Comfortable long-typing sessions for notes, essays, and coding.",
                    "photography": "Haptic touchpad gives Lightroom slider control ultra-precisely.",
                    "family_general": "Kids and adults both find the layout easy and comfortable.",
                    "fitness_health": "Journal workouts and plan meals with a comfortable keyboard.",
                    "home_management": "Every household spreadsheet feels effortless to punch through.",
                }
            },
        ]
    },
    # --- TELEVISIONS ---
    {
        "id": "sony-bravia-8-ai",
        "brand": "Sony",
        "name": "Sony Bravia 8 II AI OLED 4K TV (65\")",
        "category": "Televisions",
        "price_inr": 179990,
        "rating": 4.6,
        "review_count": 892,
        "image": "https://images.unsplash.com/photo-1461151304267-38535e780c79?crop=entropy&cs=srgb&fm=jpg&w=800&q=80",
        "tagline": "XR AI Cognitive Processor, QD-OLED, Studio Calibrated",
        "features": [
            {
                "feature_name": "XR AI Cognitive Processor",
                "technical_meaning": "Sony's XR chip uses cognitive AI to analyze scenes by focal point, reconstructing detail, contrast, and color like the human eye — rather than one pixel at a time.",
                "benefit_templates": {
                    "content_creation": "Review your own footage as the director intended — depth and detail preserved.",
                    "gaming": "Console games look like their reference visuals — cognitive HDR for atmosphere.",
                    "professional": "Client demos of visual content shine on a reference-grade panel.",
                    "student": "Documentaries and lectures look crisp and easy to focus on.",
                    "photography": "Portfolio reviews on this TV come very close to a mastering monitor.",
                    "family_general": "Movies feel like theatre-grade — depth, colors, and shadows are natural.",
                    "fitness_health": "Live sports feel immersive with smooth motion and crisp detail.",
                    "home_management": "Every content type — movies, news, home videos — looks its best.",
                }
            },
            {
                "feature_name": "QD-OLED Panel",
                "technical_meaning": "Quantum Dot OLED panel — combines OLED's perfect black with quantum-dot color to deliver wider gamut and higher peak brightness than standard OLED.",
                "benefit_templates": {
                    "content_creation": "Every color in your edit is faithful — QD-OLED covers cinema gamuts.",
                    "gaming": "Blazing colors and infinite contrast for modern HDR gaming.",
                    "professional": "Presentations and demos look truly premium in client rooms.",
                    "student": "Study documentaries feel immersive with rich HDR.",
                    "photography": "Reviewing prints and portfolios — colors match your monitor closely.",
                    "family_general": "Family movies, cricket, and animations look reference-quality.",
                    "fitness_health": "Fitness streams look vibrant with vivid coaching visuals.",
                    "home_management": "Everyday content just looks better without any manual tweaking.",
                }
            },
            {
                "feature_name": "Acoustic Surface Audio+",
                "technical_meaning": "The entire OLED panel acts as a speaker via strategically-placed actuators, with AI room-tuning matching audio to your seating position.",
                "benefit_templates": {
                    "content_creation": "Audio comes from where the action is — dialogue and effects lock to picture.",
                    "gaming": "Directional in-game audio matches on-screen movement precisely.",
                    "professional": "Presentation audio locks to the speaker on screen for realism.",
                    "student": "Dialogue in documentaries and lectures is clearer and more directional.",
                    "photography": "Interviews and tutorial audio comes from natural on-screen positions.",
                    "family_general": "Every family-movie voice comes from the mouth on screen.",
                    "fitness_health": "Trainer voice and music are naturally positioned for immersion.",
                    "home_management": "News and TV feel more natural — audio locked to the picture.",
                }
            },
            {
                "feature_name": "PlayStation 5 Perfect Gaming Mode",
                "technical_meaning": "Native PS5 optimisation with Auto HDR Tone Mapping and Auto Genre Picture Mode — the TV negotiates picture settings with the console automatically.",
                "benefit_templates": {
                    "content_creation": "Preview your capture in a mode tuned specifically for HDR content.",
                    "gaming": "PS5 games look exactly how developers intended — zero manual tweaking.",
                    "professional": "Great console-gaming experience if you unwind after work.",
                    "student": "Perfect settings for game-based learning content.",
                    "photography": "Auto HDR tone mapping shows off your captured HDR shots optimally.",
                    "family_general": "Family game nights look and feel their best out of the box.",
                    "fitness_health": "Fitness games (VR Fit, Just Dance) look immersive and responsive.",
                    "home_management": "Kids' gaming setup requires zero settings-fiddling from you.",
                }
            },
            {
                "feature_name": "AI Voice + Google TV",
                "technical_meaning": "Built-in Google TV with hands-free Google Assistant and AI-powered content recommendations across streaming services.",
                "benefit_templates": {
                    "content_creation": "Voice-lookup reference films and cinematographers hands-free.",
                    "gaming": "Voice-search game trailers and reviews without a phone.",
                    "professional": "Voice-open weather, news, and market summaries in the morning.",
                    "student": "Voice-search educational content across all streaming services.",
                    "photography": "Voice-search photography documentaries, tutorials, and interviews.",
                    "family_general": "Kids and grandparents can voice-navigate to their shows easily.",
                    "fitness_health": "Voice-launch workout streams and yoga videos across apps.",
                    "home_management": "Voice-control your smart home right from the couch.",
                }
            },
        ]
    },
    {
        "id": "lg-c4-oled-ai-tv",
        "brand": "LG",
        "name": "LG C4 evo AI OLED 4K TV (55\")",
        "category": "Televisions",
        "price_inr": 149990,
        "rating": 4.5,
        "review_count": 1420,
        "image": "https://images.unsplash.com/photo-1593359677879-a4bb92f829d1?crop=entropy&cs=srgb&fm=jpg&w=800&q=80",
        "tagline": "α9 AI Processor Gen7, 144Hz OLED, Dolby Vision",
        "features": [
            {
                "feature_name": "α9 AI Processor Gen7",
                "technical_meaning": "LG's 7th-gen AI processor with deep-learning-based scene analysis, dynamic tone mapping, and object enhancement — trained on millions of image samples.",
                "benefit_templates": {
                    "content_creation": "Review your work on a panel that auto-tunes for accurate creator playback.",
                    "gaming": "AI enhances shadow detail and motion for competitive gaming.",
                    "professional": "Presentation and demo content looks vivid and sharp for clients.",
                    "student": "Lecture videos and educational content stay crisp and vivid.",
                    "photography": "AI upscaling makes older photo slideshows look upgraded.",
                    "family_general": "Every content type looks great without diving into menus.",
                    "fitness_health": "Workout streams and live sports look smooth and vivid.",
                    "home_management": "News, streaming, home videos — all improved automatically.",
                }
            },
            {
                "feature_name": "144Hz OLED with Dolby Vision Gaming",
                "technical_meaning": "OLED evo panel supporting 144Hz refresh rate with Dolby Vision at up to 4K/120Hz for gaming — G-Sync, FreeSync Premium, and VRR all supported.",
                "benefit_templates": {
                    "content_creation": "Slow-motion and high-refresh footage plays back exactly as shot.",
                    "gaming": "Reference-grade 144Hz gaming with Dolby Vision — pro-tier console/PC play.",
                    "professional": "Ultra-smooth scrolling for professional presentations.",
                    "student": "Smooth playback of any content or games.",
                    "photography": "Smooth slideshows and reference video playback.",
                    "family_general": "Live sports and cinema look buttery-smooth for the whole family.",
                    "fitness_health": "Fast workout videos play back without motion blur.",
                    "home_management": "Everything from streaming to fast-scrolling smart-home dashboards feels crisp.",
                }
            },
            {
                "feature_name": "AI Sound Pro (11.1.2 upmixing)",
                "technical_meaning": "AI Sound Pro upmixes any audio source to virtual 11.1.2 surround using scene-aware processing, without external speakers.",
                "benefit_templates": {
                    "content_creation": "Preview audio mixes with a rich, natural sound stage from just the TV.",
                    "gaming": "Immersive directional audio without a soundbar or headset.",
                    "professional": "Presentation audio sounds theatre-quality in client rooms.",
                    "student": "Lecture and documentary audio is clearer and easier to follow.",
                    "photography": "Photography interviews and tutorials sound immersive.",
                    "family_general": "Family-movie audio fills the room — no soundbar needed.",
                    "fitness_health": "Workout audio surrounds you for a class-like experience.",
                    "home_management": "Even news and everyday TV sounds richer with AI upmixing.",
                }
            },
            {
                "feature_name": "webOS 24 with AI Chatbot",
                "technical_meaning": "webOS 24 includes an AI Chatbot that answers TV/settings questions, plus AI-driven content recommendations and voice search.",
                "benefit_templates": {
                    "content_creation": "Ask the TV to find that specific film reference you half-remember.",
                    "gaming": "Voice-navigate gaming apps and store hands-free.",
                    "professional": "Voice-launch news, market updates, and weather in seconds.",
                    "student": "Ask the TV chatbot to find learning content across services.",
                    "photography": "Voice-search photography documentaries and location clips.",
                    "family_general": "Even kids and grandparents can find shows via voice.",
                    "fitness_health": "Voice-launch specific workout classes and yoga sessions.",
                    "home_management": "Voice-control smart-home devices without picking up a phone.",
                }
            },
            {
                "feature_name": "AI Concierge & Genre Detection",
                "technical_meaning": "The TV detects what genre of content is on screen and adapts picture/sound settings automatically — with an AI concierge suggesting related content.",
                "benefit_templates": {
                    "content_creation": "Your own edits get sensitive treatment — cinema/documentary/music modes selected right.",
                    "gaming": "Auto-detects games and enables gaming mode with low input lag.",
                    "professional": "Auto-detects presentation content and boosts clarity.",
                    "student": "Auto-tunes documentary/lecture content for readability.",
                    "photography": "Auto-detects photography and slideshow content for accurate colors.",
                    "family_general": "Family movies get warmth; kids' shows get bright vivid modes.",
                    "fitness_health": "Auto-detects fitness content and tunes for smooth motion.",
                    "home_management": "Every content type gets its ideal settings — you never tweak menus.",
                }
            },
        ]
    },
    # --- SMARTWATCHES ---
    {
        "id": "samsung-galaxy-watch-8",
        "brand": "Samsung",
        "name": "Samsung Galaxy Watch 8 Classic (46mm)",
        "category": "Smartwatches",
        "price_inr": 42990,
        "rating": 4.3,
        "review_count": 987,
        "image": "https://images.unsplash.com/photo-1523275335684-37898b6baf30?crop=entropy&cs=srgb&fm=jpg&w=800&q=80",
        "tagline": "Rotating bezel, Galaxy AI Health, BP monitoring",
        "features": [
            {
                "feature_name": "Galaxy AI Wellness Coach",
                "technical_meaning": "An on-device AI coach that reads recent heart-rate, HRV, sleep, and activity data to give daily energy scores and personalized wellness recommendations.",
                "benefit_templates": {
                    "content_creation": "Get told to step away and stretch before your creative fatigue hits.",
                    "gaming": "AI prompts you to move between sessions to protect long-term health.",
                    "professional": "AI-scheduled breaks aligned with your calendar keep focus sharp.",
                    "student": "Study intervals and rest timings are optimized to your patterns.",
                    "photography": "Micro-breaks scheduled during long shoots keep you sharp.",
                    "family_general": "Personalized wellness for busy family life — small nudges that add up.",
                    "fitness_health": "Deep, per-body coaching from HRV, sleep, and training load data.",
                    "home_management": "Reminders to move and hydrate during long household admin days.",
                }
            },
            {
                "feature_name": "Blood Pressure Monitoring",
                "technical_meaning": "The watch measures blood pressure via a calibrated cuff-and-watch pairing, giving on-wrist readings with a monthly calibration.",
                "benefit_templates": {
                    "content_creation": "Track stress spikes on shoot days to protect long-term health.",
                    "gaming": "Notice BP trends during long gaming sessions.",
                    "professional": "Track BP through busy quarter-end without extra visits to the clinic.",
                    "student": "Track exam-week stress patterns as they happen.",
                    "photography": "Long shoot-day BP monitoring in real time.",
                    "family_general": "Peace of mind for family — BP trends visible on your wrist.",
                    "fitness_health": "Direct BP data alongside training load for informed decisions.",
                    "home_management": "See how everyday stress affects your BP through the week.",
                }
            },
            {
                "feature_name": "Advanced Sleep Coaching",
                "technical_meaning": "Multi-week sleep pattern analysis with personalized coaching that adapts to your rhythms, snoring detection, and skin-temperature-based cycle insights.",
                "benefit_templates": {
                    "content_creation": "See how late edits affect your creativity and adapt.",
                    "gaming": "Quantify how late gaming affects next-day focus.",
                    "professional": "Optimize sleep for peak client-day performance.",
                    "student": "Understand which routines lead to your best exam-prep sleep.",
                    "photography": "Recovery scores tell you when you're ready for a big shoot day.",
                    "family_general": "See how kids waking you up affects recovery — plan quieter nights.",
                    "fitness_health": "Direct sleep-to-training feedback loops for real results.",
                    "home_management": "Understand which household routines protect your sleep quality.",
                }
            },
            {
                "feature_name": "Rotating Bezel Navigation",
                "technical_meaning": "The physical rotating bezel returns as the primary navigation input — designed for eyes-off use and glove/wet conditions.",
                "benefit_templates": {
                    "content_creation": "Skip tracks and answer calls hands-off during shoots.",
                    "gaming": "Quick-glance rotate to check timers/reminders during play.",
                    "professional": "Silent scroll through notifications during a meeting.",
                    "student": "Discreet navigation during classes and studies.",
                    "photography": "Adjust settings without pulling out your phone during shoots.",
                    "family_general": "Kids-safe rotate-to-answer works even with wet hands.",
                    "fitness_health": "Rotate to change music or lap-mark mid-run — no touchscreen needed.",
                    "home_management": "Quick-glance timers and reminders while cooking or cleaning.",
                }
            },
            {
                "feature_name": "3-Day Battery with AOD",
                "technical_meaning": "New efficient chipset delivers ~3 days of battery with always-on display enabled, or ~5 days with AOD off.",
                "benefit_templates": {
                    "content_creation": "A weekend of shooting without recharging the watch.",
                    "gaming": "Long weekend gaming with the watch always on.",
                    "professional": "A full business trip without a watch charger in your bag.",
                    "student": "College week goes by without daily watch charging.",
                    "photography": "Multi-day shoots without needing to charge the watch.",
                    "family_general": "3-day family trip without a spare charger.",
                    "fitness_health": "Continuous tracking across marathon weekends.",
                    "home_management": "One watch charge covers most weekly routines end-to-end.",
                }
            },
        ]
    },
    {
        "id": "garmin-venu-4-ai",
        "brand": "Garmin",
        "name": "Garmin Venu 4 AI Sports Smartwatch",
        "category": "Smartwatches",
        "price_inr": 45990,
        "rating": 4.6,
        "review_count": 645,
        "image": "https://images.unsplash.com/photo-1508685096489-7aacd43bd3b1?crop=entropy&cs=srgb&fm=jpg&w=800&q=80",
        "tagline": "AI Coach, Elevate 5 sensor, 11-day battery",
        "features": [
            {
                "feature_name": "Garmin AI Coach",
                "technical_meaning": "Personalized AI training coach that adapts daily workouts based on your recovery, training load, HRV, and fitness goals — with actual voice-guided workouts.",
                "benefit_templates": {
                    "content_creation": "Move breaks scheduled into your creative routine automatically.",
                    "gaming": "AI prompts you to move between sessions with tailored short workouts.",
                    "professional": "Micro-workouts scheduled around meetings for peak focus.",
                    "student": "Study-break workouts adapted to exam-week stress levels.",
                    "photography": "Recovery-aware training for shoot-day energy.",
                    "family_general": "Family-friendly workouts adapted to your recovery.",
                    "fitness_health": "True per-body AI coaching — training load, VO2, HRV all factored in.",
                    "home_management": "Movement breaks that fit around chores and errands.",
                }
            },
            {
                "feature_name": "Elevate Gen 5 Multi-Sensor",
                "technical_meaning": "New optical sensor stack with ECG, SpO2, skin temperature, and continuous HRV — feeding richer data than previous Venu generations.",
                "benefit_templates": {
                    "content_creation": "Track stress and recovery during long editing weeks.",
                    "gaming": "Real-time stress detection during long gaming sessions.",
                    "professional": "See true workday stress from HRV and skin temperature signals.",
                    "student": "Detailed stress and recovery tracking during exam preparation.",
                    "photography": "Long-shoot recovery and stress visible through the day.",
                    "family_general": "Household stress and recovery visible for the whole family.",
                    "fitness_health": "Full-spectrum health tracking — training, recovery, illness signals.",
                    "home_management": "Track stress patterns from household demands over weeks.",
                }
            },
            {
                "feature_name": "11-Day Battery",
                "technical_meaning": "Up to 11 days of battery life in smartwatch mode; ~5 days with continuous SpO2; ~20 hours in full GPS/HR/music mode.",
                "benefit_templates": {
                    "content_creation": "A full production week tracked continuously without recharging.",
                    "gaming": "The watch just… works. Barely think about charging.",
                    "professional": "A week of business travel without a watch charger.",
                    "student": "College week without daily charging — one weekend charge covers it.",
                    "photography": "Multi-day expedition shoots tracked continuously.",
                    "family_general": "Family holiday tracked end-to-end without carrying a charger.",
                    "fitness_health": "Marathon-week training tracked without missing a beat.",
                    "home_management": "Weekly rhythm needs one Sunday charge — that's it.",
                }
            },
            {
                "feature_name": "AI Workout Detection & Auto-log",
                "technical_meaning": "The watch automatically detects the start of a workout (running, cycling, swimming, strength), classifies it, and logs metrics — no manual start required.",
                "benefit_templates": {
                    "content_creation": "Move-breaks between edits auto-log — see your true movement across the day.",
                    "gaming": "Post-game walks and stretches auto-log without you thinking.",
                    "professional": "Between-meeting stair climbs and walks all count automatically.",
                    "student": "Campus walks and cycles auto-log into your fitness data.",
                    "photography": "Walking shoots log as active minutes automatically.",
                    "family_general": "Family walks, playground time, chores all auto-tracked.",
                    "fitness_health": "Never forget to log a workout — the watch handles it.",
                    "home_management": "Household movement (cleaning, cooking) counts automatically.",
                }
            },
            {
                "feature_name": "Body Battery + Morning Report",
                "technical_meaning": "AI 'body battery' score based on HRV, stress, activity, and sleep, delivered as a morning report with priorities for the day.",
                "benefit_templates": {
                    "content_creation": "Know if today's a big-creativity day or a lighter one before you start.",
                    "gaming": "Body battery tells you when to keep sessions short.",
                    "professional": "Match your calendar priorities to your energy budget.",
                    "student": "Prioritise study topics based on your morning energy score.",
                    "photography": "Plan long shoots on high-battery days; edits on low ones.",
                    "family_general": "Balance family obligations against your energy budget.",
                    "fitness_health": "Direct training decisions from a personalized morning report.",
                    "home_management": "Batch heavy household admin on higher-energy mornings.",
                }
            },
        ]
    },
    # --- SMART GLASSES ---
    {
        "id": "xreal-one-pro-ai",
        "brand": "XREAL",
        "name": "XREAL One Pro AI AR Smart Glasses",
        "category": "Smart Glasses",
        "price_inr": 44990,
        "rating": 4.2,
        "review_count": 312,
        "image": "https://images.unsplash.com/photo-1577803645773-f96470509666?crop=entropy&cs=srgb&fm=jpg&w=800&q=80",
        "tagline": "0.55\" Sony micro-OLED, X1 spatial chip, 6-DoF",
        "features": [
            {
                "feature_name": "Sony 0.55\" micro-OLED with 3D Display",
                "technical_meaning": "Sony micro-OLED displays delivering 700-nit peak, wide color gamut, and stereoscopic 3D output that turns the glasses into a private theater screen.",
                "benefit_templates": {
                    "content_creation": "Review your 4K edits and 3D content on a huge private screen anywhere.",
                    "gaming": "Play console/PC games on a 200-inch virtual screen while traveling.",
                    "professional": "Multi-monitor productivity mode while on flights or in cafes.",
                    "student": "Study PDFs and lecture videos as if on a big screen — anywhere.",
                    "photography": "Review portfolios and edits on a large virtual monitor while traveling.",
                    "family_general": "Watch films and family videos on a huge private screen.",
                    "fitness_health": "Follow full-screen workout videos with hands-free virtual display.",
                    "home_management": "Manage docs and household admin on a virtual multi-monitor setup.",
                }
            },
            {
                "feature_name": "X1 Spatial AI Chip",
                "technical_meaning": "XREAL's proprietary spatial computing chip enabling 6-DoF head tracking, anchored virtual windows, and low-latency AI scene understanding — on-device.",
                "benefit_templates": {
                    "content_creation": "Anchor timelines and previews around you like a floating studio.",
                    "gaming": "Head-tracked immersion for supported games — feels like AR gaming.",
                    "professional": "Pin virtual windows to physical spots — meeting notes stay in place.",
                    "student": "Pin study apps to different desk zones — natural mental separation.",
                    "photography": "Pin reference photos and edit tools around you spatially.",
                    "family_general": "Pin family photo galleries in mid-air for immersive viewing.",
                    "fitness_health": "Workout tutorial pinned in your field of view — hands-free.",
                    "home_management": "Pin recipe, timer, and shopping list around the kitchen.",
                }
            },
            {
                "feature_name": "AI Assistant with Multimodal Vision",
                "technical_meaning": "Built-in AI assistant that can see what you see and answer questions about it, powered by a multimodal vision-language model.",
                "benefit_templates": {
                    "content_creation": "Ask for framing/lighting ideas about what you're looking at — hands-free.",
                    "gaming": "Ask about IRL objects while playing without pausing.",
                    "professional": "Voice-lookup during site visits, meetings, and events.",
                    "student": "Point-and-ask about diagrams, plants, or historical sites on tours.",
                    "photography": "Ask about locations and shooting setups in your field of view.",
                    "family_general": "Hands-free answers for kids' questions while you're doing chores.",
                    "fitness_health": "Voice-log workouts and ask for form tips on the go.",
                    "home_management": "Point at appliance labels or receipts — ask for info instantly.",
                }
            },
            {
                "feature_name": "Prescription Compatible + Lightweight",
                "technical_meaning": "84g weight with insert-based prescription lens support (up to -10D) — designed for extended all-day wear.",
                "benefit_templates": {
                    "content_creation": "Wear all day during shoots and edits — no fatigue.",
                    "gaming": "Long gaming sessions without headset pressure or heat.",
                    "professional": "All-day travel wear for a productive commute or flight.",
                    "student": "All-day study wear — study sessions and campus life combined.",
                    "photography": "All-day travel-shoot wear with prescription support.",
                    "family_general": "Comfortable enough to wear during family activities and evenings in.",
                    "fitness_health": "Light enough for indoor training and yoga sessions.",
                    "home_management": "Wear while doing chores and cooking with recipes pinned nearby.",
                }
            },
            {
                "feature_name": "USB-C DisplayPort — Plug and Play",
                "technical_meaning": "Single USB-C connection to phones, laptops, Steam Deck, PS5, and Xbox with DisplayPort support — no separate compute puck needed.",
                "benefit_templates": {
                    "content_creation": "Plug into your laptop and get a virtual studio wherever you are.",
                    "gaming": "Plug into Steam Deck or console — instant 200-inch gaming.",
                    "professional": "Plug into your laptop for multi-monitor productivity anywhere.",
                    "student": "Plug into your laptop for a big virtual study monitor.",
                    "photography": "Plug into your laptop for a big virtual editing display.",
                    "family_general": "Plug into a phone and enjoy shared big-screen viewing.",
                    "fitness_health": "Plug into a fitness console for immersive workouts.",
                    "home_management": "Plug into any device for a virtual big screen at home.",
                }
            },
        ]
    },
    # --- HOME APPLIANCES ---
    {
        "id": "samsung-bespoke-ai-oven",
        "brand": "Samsung",
        "name": "Samsung Bespoke AI Steam Oven with Cam",
        "category": "Home Appliances",
        "price_inr": 79990,
        "rating": 4.4,
        "review_count": 512,
        "image": "https://images.unsplash.com/photo-1585659722983-3a675dabf23d?crop=entropy&cs=srgb&fm=jpg&w=800&q=80",
        "tagline": "Interior camera, AI recipe guidance, steam + convection",
        "features": [
            {
                "feature_name": "AI Camera with Food Recognition",
                "technical_meaning": "An interior camera streams to your phone AND uses AI to recognize what's inside — suggesting recipes and adjusting cook programs automatically.",
                "benefit_templates": {
                    "content_creation": "Time cooking-content shoots perfectly — camera streams to your phone.",
                    "gaming": "Snacks and pizzas get automatic cook programs — no interruption.",
                    "professional": "Between meetings, oven identifies leftovers and reheats correctly.",
                    "student": "The oven suggests dorm-friendly recipes based on what you put in.",
                    "photography": "Food-content ingredients cook perfectly for photo shoots.",
                    "family_general": "Family dinners cook automatically — the AI handles temps and time.",
                    "fitness_health": "Meal-prep proteins and veggies get texture-perfect cooking.",
                    "home_management": "Reduces the mental load of dinner — the oven decides how to cook.",
                }
            },
            {
                "feature_name": "AI Recipe Guidance",
                "technical_meaning": "SmartThings connectivity with an AI recipe library that pushes step-by-step programs directly to the oven based on your dietary preferences and calendar.",
                "benefit_templates": {
                    "content_creation": "AI-picked recipes for cooking content — programs auto-sync.",
                    "gaming": "Quick game-night snack recipes with one-tap oven programs.",
                    "professional": "Weeknight-friendly programs synced to your calendar.",
                    "student": "Hostel-friendly recipes with automatic oven programs.",
                    "photography": "Food-photography recipes with perfect cook programs.",
                    "family_general": "Family meal recipes that pre-program the oven from your phone.",
                    "fitness_health": "Macro-friendly recipes with automatic oven programs.",
                    "home_management": "Weekly meal plan → programmed oven schedules automatically.",
                }
            },
            {
                "feature_name": "Steam + Convection Cooking",
                "technical_meaning": "Combines convection heat with steam injection for restaurant-quality bread, protein, and vegetables — retaining moisture while browning.",
                "benefit_templates": {
                    "content_creation": "Food-content quality — restaurant-like plating and texture.",
                    "gaming": "Game-night dishes come out juicy and perfectly done.",
                    "professional": "Impress dinner guests with restaurant-quality home cooking.",
                    "student": "Cheap ingredients transform into restaurant-quality meals.",
                    "photography": "Photograph-perfect food thanks to consistent moisture.",
                    "family_general": "Family Sunday roasts and bread turn out consistently amazing.",
                    "fitness_health": "Prepped chicken, fish, and veggies keep moisture and texture.",
                    "home_management": "Consistent great results — less second-guessing.",
                }
            },
            {
                "feature_name": "Smart Preheat & Auto-off",
                "technical_meaning": "Learns your daily cooking patterns and pre-heats before you usually cook. Auto-off triggers if the oven stays idle beyond a safe threshold.",
                "benefit_templates": {
                    "content_creation": "Oven is ready right when you start a cooking-content shoot.",
                    "gaming": "Game-night starts don't wait for oven warm-up.",
                    "professional": "Weeknight dinners are ready faster — oven pre-heats to your schedule.",
                    "student": "Weeknight meals are ready faster — oven learns your patterns.",
                    "photography": "Food-shoot prep is faster with pre-heated oven ready.",
                    "family_general": "Family dinners are on the table faster; safe auto-off for kids.",
                    "fitness_health": "Meal-prep Sundays go faster with pre-heated ovens.",
                    "home_management": "Household routine faster — plus safety auto-off peace of mind.",
                }
            },
            {
                "feature_name": "Energy-saving AI Modes",
                "technical_meaning": "AI adjusts convection fan speed, steam dosing, and heater cycling to reduce power draw while maintaining cook quality.",
                "benefit_templates": {
                    "content_creation": "Long shoot days without inflating the electricity bill.",
                    "gaming": "Snack ovens don't spike your monthly bill.",
                    "professional": "Home dinner-parties without a bill hangover.",
                    "student": "Frequent cooking without punishing your electricity meter.",
                    "photography": "Long food-shoot days without inflating bills.",
                    "family_general": "Weekly family cooking with lower electricity bills.",
                    "fitness_health": "Frequent meal-prep sessions run efficient.",
                    "home_management": "Real, measurable savings across a heavy-cooking household.",
                }
            },
        ]
    },
]


def merge_into_products(existing):
    """Return existing + NEW_PRODUCTS."""
    return existing + NEW_PRODUCTS
