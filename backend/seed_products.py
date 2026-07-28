"""
Seed data for WhyAI: 10 real AI-powered products from Amazon India's AI Store.
Each product has 5 real AI feature bullets. Each feature has a technical_meaning
and benefit_templates covering all 8 use-case clusters.

Use-case clusters:
  content_creation, gaming, professional, student,
  photography, family_general, fitness_health, home_management
"""

CLUSTERS = [
    "content_creation", "gaming", "professional", "student",
    "photography", "family_general", "fitness_health", "home_management",
]

PRODUCTS = [
    # 1. Samsung Galaxy S25 Ultra
    {
        "id": "samsung-galaxy-s25-ultra",
        "brand": "Samsung",
        "name": "Samsung Galaxy S25 Ultra 5G AI Smartphone",
        "category": "Smartphones",
        "price_inr": 118999,
        "rating": 4.3,
        "review_count": 1687,
        "image": "https://images.unsplash.com/photo-1512941937669-90a1b58e7e9c?crop=entropy&cs=srgb&fm=jpg&w=800&q=80",
        "tagline": "Titanium build, S Pen, Galaxy AI, 200MP camera",
        "features": [
            {
                "feature_name": "Galaxy AI & Now Brief",
                "technical_meaning": "A conversational AI companion integrated into One UI that surfaces daily schedule, reminders, battery status, and an 'Energy Score' — all in a single glanceable brief.",
                "benefit_templates": {
                    "content_creation": "See your posting schedule, filming reminders, and phone battery in one Now Brief before every shoot.",
                    "gaming": "Get a quick heads-up on battery and thermal state before you jump into a long gaming session.",
                    "professional": "Start your workday with a single brief of meetings, follow-ups, and device readiness — no app-switching.",
                    "student": "Wake up to a Now Brief of your class schedule, assignment deadlines, and reminders without opening five apps.",
                    "photography": "Check upcoming golden-hour reminders, battery for shoots, and calendar in one place.",
                    "family_general": "One glance in the morning shows you the family calendar, kids' reminders, and phone status.",
                    "fitness_health": "See your workout reminder, recovery status, and sleep summary alongside daily reminders.",
                    "home_management": "Grocery reminders, bill due-dates, and household tasks land in a single AI-curated brief every morning.",
                }
            },
            {
                "feature_name": "Gemini Live",
                "technical_meaning": "Real-time conversational AI you can talk to naturally, share images with, and get adaptive spoken responses from without typing.",
                "benefit_templates": {
                    "content_creation": "Brainstorm scripts and thumbnail ideas out loud while editing — Gemini answers back like a co-writer.",
                    "gaming": "Ask about game guides, builds, or lore hands-free while playing on another screen.",
                    "professional": "Talk through emails, meeting prep, and quick research on your commute — hands-free.",
                    "student": "Explain a concept, upload a page from your textbook, and get a spoken walkthrough.",
                    "photography": "Point your camera at a scene and ask for shooting-mode suggestions in real time.",
                    "family_general": "Ask for dinner ideas, kids' homework help, or travel tips just by talking.",
                    "fitness_health": "Get workout form tips or recipe swaps by speaking — no need to stop training.",
                    "home_management": "Voice-plan groceries, chores, and errands while doing something else.",
                }
            },
            {
                "feature_name": "200MP AI ProVisual Engine Camera",
                "technical_meaning": "A 200MP main sensor paired with an AI-enhanced processing engine that keeps clarity high from ultra-wide to 100x telephoto zoom.",
                "benefit_templates": {
                    "content_creation": "Shoot cinematic B-roll and crisp 4K vlogs from wide to zoomed shots without switching lenses.",
                    "gaming": "Capture crisp screen recordings and gameplay highlights with vivid color detail.",
                    "professional": "Photograph whiteboards, documents, and event details with 200MP clarity.",
                    "student": "Snap textbook pages and lecture slides from the back of the classroom and still read every word.",
                    "photography": "One phone covers ultra-wide landscapes to 100x zoom wildlife — with AI keeping detail sharp.",
                    "family_general": "Capture kids running, birthdays, and school events in high detail without a separate camera.",
                    "fitness_health": "Record clean training clips outdoors, even in tough light, for form analysis.",
                    "home_management": "Take clear photos of receipts, warranty cards, and household inventory.",
                }
            },
            {
                "feature_name": "Snapdragon 8 Elite with Ray Tracing",
                "technical_meaning": "A custom-tuned flagship chip supporting real-time hardware ray tracing and Vulkan optimizations for demanding mobile games.",
                "benefit_templates": {
                    "content_creation": "Render 4K video previews and heavy editing timelines without lag.",
                    "gaming": "Play console-grade titles with ray-traced lighting and steady frame rates on mobile.",
                    "professional": "Multitask 20+ tabs, spreadsheets, and calls without stutter.",
                    "student": "Handle multitasking between notes apps, PDFs, video lectures, and browser research smoothly.",
                    "photography": "Process large RAW files and AI edits directly on the phone.",
                    "family_general": "Keep the phone snappy even after years of app installs and kids' games.",
                    "fitness_health": "Track live workouts and stream music without performance drops.",
                    "home_management": "Run smart-home apps, calendars, and lists side-by-side smoothly.",
                }
            },
            {
                "feature_name": "Knox Security & Samsung Wallet",
                "technical_meaning": "Defense-grade hardware-backed security layer with encrypted storage for cards, IDs, and payment credentials in Samsung Wallet.",
                "benefit_templates": {
                    "content_creation": "Store client contracts, brand deals, and payout details behind hardware-level protection.",
                    "gaming": "Keep in-game wallets, subscriptions, and gift cards safe from account theft.",
                    "professional": "Corporate emails, VPN credentials, and payment cards live inside a defense-grade vault.",
                    "student": "Digital ID, hostel access cards, and scholarship payment info stay protected.",
                    "photography": "Client invoices and payment records are stored safely on-device.",
                    "family_general": "Family cards, health IDs, and kids' school documents stay in one secure wallet.",
                    "fitness_health": "Insurance cards, gym memberships, and medical IDs are securely accessible.",
                    "home_management": "Utility payment cards and rent transfers happen from a hardware-encrypted wallet.",
                }
            },
        ]
    },
    # 2. OnePlus Nord 6
    {
        "id": "oneplus-nord-6",
        "brand": "OnePlus",
        "name": "OnePlus Nord 6",
        "category": "Smartphones",
        "price_inr": 31999,
        "rating": 4.3,
        "review_count": 942,
        "image": "https://images.unsplash.com/photo-1634403665481-74948d815f03?crop=entropy&cs=srgb&fm=jpg&w=800&q=80",
        "tagline": "Flagship-feeling mid-ranger with on-device AI",
        "features": [
            {
                "feature_name": "AI Camera Scene Optimisation",
                "technical_meaning": "Camera automatically detects the scene (portrait, low-light, food, landscape) and adjusts exposure, HDR, and color per shot.",
                "benefit_templates": {
                    "content_creation": "Point-and-shoot content for Reels and Shorts with auto-tuned exposure per scene.",
                    "gaming": "Capture in-game screenshots that stay sharp even during motion.",
                    "professional": "Great-looking headshots and product photos without a photographer.",
                    "student": "Photos of notes, whiteboards, and projects look clean and readable.",
                    "photography": "The camera does most of the tuning so you focus on framing.",
                    "family_general": "Every family photo turns out well without fiddling with settings.",
                    "fitness_health": "Track transformation photos in consistent lighting.",
                    "home_management": "Snap clear photos of appliance labels, meter readings, and receipts.",
                }
            },
            {
                "feature_name": "Smart Battery Management",
                "technical_meaning": "AI-driven power allocation that learns your daily app usage patterns and throttles background drain, extending real-world battery life.",
                "benefit_templates": {
                    "content_creation": "A single charge covers a full day of shooting, editing previews, and uploads.",
                    "gaming": "AI protects headroom so late-day gaming sessions don't die at 20%.",
                    "professional": "Get through back-to-back meetings and calls without a mid-day top-up.",
                    "student": "College-day battery lasts through classes, notes, and video lectures.",
                    "photography": "Long shoot days without hunting for a power outlet.",
                    "family_general": "One charge lasts a busy family day — school runs, errands, and evening calls.",
                    "fitness_health": "Battery survives full-day GPS tracking on hikes and long workouts.",
                    "home_management": "Stays alive across cooking, calls, delivery tracking, and grocery apps.",
                }
            },
            {
                "feature_name": "Real-time Language Translation",
                "technical_meaning": "On-device / cloud-assisted translation for live calls and messages across major Indian and global languages.",
                "benefit_templates": {
                    "content_creation": "Interview subjects in any language and get instant subtitles for your videos.",
                    "gaming": "Chat with international teammates in your language during voice-comms.",
                    "professional": "Take client calls across regions without a language barrier.",
                    "student": "Read foreign-language research papers translated in real time.",
                    "photography": "Communicate with subjects on travel shoots without a phrasebook.",
                    "family_general": "Talk to relatives abroad and read messages from any dialect naturally.",
                    "fitness_health": "Follow foreign-language workout videos with live translation.",
                    "home_management": "Read appliance manuals or foreign product labels instantly.",
                }
            },
            {
                "feature_name": "Adaptive Display Tuning",
                "technical_meaning": "AI adjusts screen brightness, contrast, and color temperature to your surroundings and the content on screen.",
                "benefit_templates": {
                    "content_creation": "Colors stay true when editing photos or videos indoors and outdoors.",
                    "gaming": "Shadow detail in dark games stays visible without cranking brightness.",
                    "professional": "Documents stay easy on the eyes across bright cafes and dim offices.",
                    "student": "Reading eBooks and PDFs is comfortable for long study sessions.",
                    "photography": "You see photos as they'll actually look — not overly boosted.",
                    "family_general": "Screen adapts nicely from bright daylight to bedtime reading.",
                    "fitness_health": "Outdoor runs — the screen stays readable in direct sunlight.",
                    "home_management": "Easy-to-read screen for recipe apps in kitchen light.",
                }
            },
            {
                "feature_name": "AI-optimised Chipset",
                "technical_meaning": "Mid-range SoC with an on-device AI accelerator that keeps multitasking, camera processing, and games smooth.",
                "benefit_templates": {
                    "content_creation": "Edit short videos and switch between apps without lag.",
                    "gaming": "Smooth frame rates in popular titles at medium-high settings.",
                    "professional": "Multi-app work — email, docs, and calls — flows without stutter.",
                    "student": "Handle browser tabs, PDFs, and notes apps side-by-side.",
                    "photography": "Camera app responds quickly and processes shots fast.",
                    "family_general": "Phone stays smooth even 2 years in with family photos, kids' games, and streaming.",
                    "fitness_health": "Fitness apps track live without lag or GPS drops.",
                    "home_management": "Smart-home dashboards and delivery apps stay responsive.",
                }
            },
        ]
    },
    # 3. HP OmniBook Ultra
    {
        "id": "hp-omnibook-ultra",
        "brand": "HP",
        "name": "HP OmniBook Ultra 14",
        "category": "Laptops",
        "price_inr": 189999,
        "rating": 4.4,
        "review_count": 512,
        "image": "https://images.unsplash.com/photo-1496181133206-80ce9b88a853?crop=entropy&cs=srgb&fm=jpg&w=800&q=80",
        "tagline": "Copilot+ PC with 48 TOPS NPU and 22-hour battery",
        "features": [
            {
                "feature_name": "48 TOPS Dedicated NPU",
                "technical_meaning": "Onboard neural processing unit delivering up to 48 TOPS, offloading AI tasks (background blur, transcription, image edits) from CPU/GPU.",
                "benefit_templates": {
                    "content_creation": "Local AI image/video edits and transcription run instantly without cloud round-trips.",
                    "gaming": "AI upscaling and background noise removal on calls happen without stealing GPU frames.",
                    "professional": "Meeting transcription, live captions, and background blur run on-device — no lag.",
                    "student": "Instantly summarize lecture recordings and PDFs locally, even offline.",
                    "photography": "AI-powered photo edits (denoise, subject select) finish in seconds.",
                    "family_general": "Family photo cleanups and video edits happen fast, without waiting.",
                    "fitness_health": "Local voice-to-text for journaling workouts, hands-free.",
                    "home_management": "Local automations, receipts OCR, and doc summarisation without uploads.",
                }
            },
            {
                "feature_name": "22+ Hour Battery Life",
                "technical_meaning": "Large-capacity battery with 65W USB-C fast charging that hits ~50% in about 45 minutes.",
                "benefit_templates": {
                    "content_creation": "Edit and export on a long flight without a charger.",
                    "gaming": "Casual gaming and streaming on the go without hunting for outlets.",
                    "professional": "A full workday of Teams calls, docs, and travel on a single charge.",
                    "student": "College day of classes, notes, and library work without carrying a charger.",
                    "photography": "Cull and edit shoots on-location for hours without power.",
                    "family_general": "Family movie night or a weekend trip — one charge covers it.",
                    "fitness_health": "Live workout streaming and journaling all day, off the wall.",
                    "home_management": "Manage the household from anywhere without worrying about outlets.",
                }
            },
            {
                "feature_name": "High-Accuracy OLED Display",
                "technical_meaning": "OLED panel with wide color gamut and high color accuracy suited for creative and content work.",
                "benefit_templates": {
                    "content_creation": "Video and photo edits show accurate colors that hold up when exported.",
                    "gaming": "Deep blacks and vivid HDR make casual gaming look premium.",
                    "professional": "Presentations, dashboards, and design mockups look sharp in client meetings.",
                    "student": "Textbooks, PDFs, and lecture videos look crisp for long study sessions.",
                    "photography": "Trustworthy color rendering for grading photos before publishing.",
                    "family_general": "Family movies and photos look stunning on the OLED screen.",
                    "fitness_health": "Workout videos and dashboards are vivid and easy to follow.",
                    "home_management": "Home-management dashboards and photos look great at any brightness.",
                }
            },
            {
                "feature_name": "Sustained Thermal Performance",
                "technical_meaning": "Redesigned cooling system that maintains full performance under sustained loads instead of throttling.",
                "benefit_templates": {
                    "content_creation": "Long exports and renders finish at full speed without slowdowns.",
                    "gaming": "Sustained performance during longer gaming sessions.",
                    "professional": "Heavy Excel models and Zoom + apps stay smooth all day.",
                    "student": "Coding compiles and simulations don't throttle in long sessions.",
                    "photography": "Batch photo processing runs at full speed without heat throttling.",
                    "family_general": "Handles kids' school projects, video calls, and media all afternoon.",
                    "fitness_health": "Video conferencing for training/coaching stays crisp all day.",
                    "home_management": "Handles budgeting spreadsheets and family docs without heating up.",
                }
            },
            {
                "feature_name": "HP Wolf Security + On-device AI",
                "technical_meaning": "Hardware-anchored security with on-device AI processing so sensitive data never has to leave the laptop.",
                "benefit_templates": {
                    "content_creation": "Client footage and unreleased work stay on-device with hardware-level protection.",
                    "gaming": "Game accounts and payment info stay isolated from malware.",
                    "professional": "Enterprise-grade protection for confidential documents and calls.",
                    "student": "Assignments, thesis work, and IDs stay private on-device.",
                    "photography": "Client shoots and RAW files never need to upload for AI edits.",
                    "family_general": "Family photos and documents are encrypted and secure.",
                    "fitness_health": "Personal health notes and journal entries stay private.",
                    "home_management": "Bills, taxes, and household records stay on-device and encrypted.",
                }
            },
        ]
    },
    # 4. Lenovo Yoga Slim 7x
    {
        "id": "lenovo-yoga-slim-7x",
        "brand": "Lenovo",
        "name": "Lenovo Yoga Slim 7x Copilot+ PC",
        "category": "Laptops",
        "price_inr": 129999,
        "rating": 4.2,
        "review_count": 386,
        "image": "https://images.unsplash.com/photo-1611186871348-b1ce696e52c9?crop=entropy&cs=srgb&fm=jpg&w=800&q=80",
        "tagline": "Snapdragon X, AI noise-cancellation, remote-work ready",
        "features": [
            {
                "feature_name": "Dynamic AI Performance Adjustment",
                "technical_meaning": "System watches the workload and shifts between power/performance profiles automatically instead of running flat-out.",
                "benefit_templates": {
                    "content_creation": "Photo edits get the boost they need; note-taking stays quiet and cool.",
                    "gaming": "Casual games get a performance boost while lighter apps run quiet.",
                    "professional": "Zoom + docs stays cool; Excel modelling gets full speed automatically.",
                    "student": "Study sessions stay silent; coding builds get bursts of performance.",
                    "photography": "Photo culling runs fast, then throttles back for long RAW viewing.",
                    "family_general": "Adapts to browsing, streaming, and school projects without you thinking about it.",
                    "fitness_health": "Silent during long video-training sessions.",
                    "home_management": "Quiet for everyday tasks; kicks in for spreadsheets and taxes.",
                }
            },
            {
                "feature_name": "AI Noise Cancellation",
                "technical_meaning": "Neural-network-powered noise cancellation for the mic and speakers on calls, removing background chatter, keyboards, and traffic.",
                "benefit_templates": {
                    "content_creation": "Record clean voiceovers even in noisy rooms.",
                    "gaming": "Team voice-comms stay clear with keyboard clatter filtered out.",
                    "professional": "Client calls sound studio-clean from cafes, homes, and travel.",
                    "student": "Group study calls stay clear even in hostels or cafes.",
                    "photography": "Client review calls and travel calls sound professional.",
                    "family_general": "Family video calls with grandparents stay clear over kids' background noise.",
                    "fitness_health": "Live coaching calls stay clear even with gym background noise.",
                    "home_management": "Home-office calls stay professional even with doorbells and household noise.",
                }
            },
            {
                "feature_name": "Smart Adaptive Power Management",
                "technical_meaning": "Battery optimization that learns your usage rhythm — charging habits, high-use apps — and adjusts power delivery to extend total battery life.",
                "benefit_templates": {
                    "content_creation": "Battery adapts to editing sessions and long shoots — more juice when you need it.",
                    "gaming": "Battery gets prioritized for gaming sessions when you plug in later.",
                    "professional": "Battery outlasts back-to-back client days.",
                    "student": "Battery survives a full campus day without a plug.",
                    "photography": "On-location editing days stretch further on one charge.",
                    "family_general": "Battery holds up across a full family day of use.",
                    "fitness_health": "Streaming a whole workout on battery is comfortable.",
                    "home_management": "Household admin days run fully on battery.",
                }
            },
            {
                "feature_name": "Adaptive Performance Tuning",
                "technical_meaning": "The system balances peak speed vs. battery life automatically based on whether you're plugged in and what you're doing.",
                "benefit_templates": {
                    "content_creation": "Fast when you plug in for a big export; quiet on battery for note-taking.",
                    "gaming": "Push performance when plugged in for gaming; conserve on the go.",
                    "professional": "Big spreadsheets get speed; docs get battery.",
                    "student": "Battery-friendly notes mode; performance-mode compiles when needed.",
                    "photography": "RAW batch edits get performance; browsing culls get battery.",
                    "family_general": "Balances performance for kids' Zoom classes vs. simple browsing.",
                    "fitness_health": "Fast video calls when plugged; efficient for long journaling.",
                    "home_management": "Fast for tax season, quiet for daily household tasks.",
                }
            },
            {
                "feature_name": "AI-assisted Multitasking",
                "technical_meaning": "AI features like smart window snapping, focus modes, and app-switch prediction to help juggle many apps.",
                "benefit_templates": {
                    "content_creation": "Timelines, references, and previews snap into place for a clean editing workspace.",
                    "gaming": "Discord, guides, and gameplay side-by-side without hunting for windows.",
                    "professional": "Meeting + notes + docs stay arranged; focus mode kills distractions.",
                    "student": "Notes, PDF reader, and browser research fit neatly on one screen.",
                    "photography": "Lightroom + reference + browser laid out cleanly.",
                    "family_general": "School app + video call + browser stay organised for kids' classes.",
                    "fitness_health": "Workout video + tracker + notes visible together.",
                    "home_management": "Bills, calendar, and email side-by-side for household admin.",
                }
            },
        ]
    },
    # 5. Samsung Vision AI QLED TV
    {
        "id": "samsung-vision-ai-qled-tv",
        "brand": "Samsung",
        "name": "Samsung 138cm (55\") Vision AI QLED 4K TV",
        "category": "Televisions",
        "price_inr": 89990,
        "rating": 4.5,
        "review_count": 2145,
        "image": "https://images.unsplash.com/photo-1593359677879-a4bb92f829d1?crop=entropy&cs=srgb&fm=jpg&w=800&q=80",
        "tagline": "NQ4 AI Processor, upscaling, Vision AI Companion",
        "features": [
            {
                "feature_name": "AI Upscaling Pro (NQ4)",
                "technical_meaning": "The NQ4 AI Processor upscales lower-resolution content (SD/HD) toward 4K in real time using neural models.",
                "benefit_templates": {
                    "content_creation": "Preview older SD footage sharpened as if it were shot in HD.",
                    "gaming": "Older consoles and games look sharper on the big screen.",
                    "professional": "Client videos and demos look crisp even from lower-res source files.",
                    "student": "YouTube lectures and older documentaries look watchable in 4K quality.",
                    "photography": "Slideshows of older photos look upscaled and vibrant.",
                    "family_general": "Old family videos, classic films, and cricket highlights look sharper than ever.",
                    "fitness_health": "Older workout DVDs and streams look clean on a big screen.",
                    "home_management": "Any content — CCTV, tutorials, streams — comes out sharper.",
                }
            },
            {
                "feature_name": "Color Booster Pro",
                "technical_meaning": "Scene-by-scene color enhancement powered by AI that adjusts saturation and vibrance based on what's on screen.",
                "benefit_templates": {
                    "content_creation": "Colors in your reels and films pop the way you graded them.",
                    "gaming": "Vivid HDR colors in modern games make worlds come alive.",
                    "professional": "Presentations, product demos, and charts look punchy in client rooms.",
                    "student": "Documentary and educational content looks vivid and engaging.",
                    "photography": "Portfolio photos on the big screen look true-to-life.",
                    "family_general": "Family movies, cartoons, and cricket matches look rich and vivid.",
                    "fitness_health": "Live sports and workout streams have punchy, motivating visuals.",
                    "home_management": "Streaming content looks vibrant without menu-diving to fix colors.",
                }
            },
            {
                "feature_name": "AI Sound Optimisation",
                "technical_meaning": "Automatic scene-aware audio processing that emphasizes dialogue clarity and adapts to your room's acoustics.",
                "benefit_templates": {
                    "content_creation": "Dialogue in reference films comes through crystal clear.",
                    "gaming": "Directional audio and footsteps stand out in competitive games.",
                    "professional": "Presentation audio and client demos are always clearly audible.",
                    "student": "Lecture audio and documentaries are easy to follow.",
                    "photography": "Photography tutorials and interviews are perfectly clear.",
                    "family_general": "Every family movie night — dialogue is clear over background scenes.",
                    "fitness_health": "Workout instructions and trainer voices cut through the music.",
                    "home_management": "News and everyday content stay audible over household noise.",
                }
            },
            {
                "feature_name": "Vision AI Companion",
                "technical_meaning": "Built-in AI assistant (Bixby with Copilot/Perplexity) that answers spoken questions and surfaces contextual info about what's on screen.",
                "benefit_templates": {
                    "content_creation": "Ask what a film, cameo, or director's other work is — hands-free.",
                    "gaming": "Ask for game guides, hints, and unlocks by voice.",
                    "professional": "Look up news, market updates, and info without picking up a device.",
                    "student": "Ask questions about documentaries and get quick explanations.",
                    "photography": "Get info about locations and shooting setups on screen.",
                    "family_general": "Kids ask questions about cartoons or shows and get instant answers.",
                    "fitness_health": "Ask for recipe swaps or workout variations while watching.",
                    "home_management": "Voice-check weather, news, and traffic without leaving the couch.",
                }
            },
            {
                "feature_name": "144Hz Motion Enhancement for Gaming",
                "technical_meaning": "Up to 144Hz refresh on supported models with AI motion smoothing and low input lag for fast-paced console/PC gaming.",
                "benefit_templates": {
                    "content_creation": "Smooth motion for previewing 60/120fps content and slow-motion clips.",
                    "gaming": "Buttery-smooth 144Hz on PS5/Xbox/PC — competitive-grade responsiveness.",
                    "professional": "Smooth scrolling and animations for professional media playback.",
                    "student": "Smooth playback of any content, tutorials, and games.",
                    "photography": "Smooth slideshows and video reels.",
                    "family_general": "Live sports, especially cricket and football, look buttery-smooth.",
                    "fitness_health": "Follow fast workout videos without motion blur.",
                    "home_management": "Everything from streaming to fast-scrolling smart-home dashboards feels crisp.",
                }
            },
        ]
    },
    # 6. Apple Watch Series 11
    {
        "id": "apple-watch-series-11",
        "brand": "Apple",
        "name": "Apple Watch Series 11",
        "category": "Smartwatches",
        "price_inr": 46900,
        "rating": 4.5,
        "review_count": 3120,
        "image": "https://images.unsplash.com/photo-1546868871-7041f2a55e12?crop=entropy&cs=srgb&fm=jpg&w=800&q=80",
        "tagline": "Hypertension alerts, Sleep Score, Workout Buddy, 24h battery",
        "features": [
            {
                "feature_name": "Hypertension Notifications",
                "technical_meaning": "AI analyzes 30 days of heart and blood-vessel sensor data to flag patterns consistent with chronic high blood pressure. Not a replacement for a BP cuff.",
                "benefit_templates": {
                    "content_creation": "Long editing days and stress spikes — the watch quietly monitors patterns.",
                    "gaming": "Long sessions and stress — the watch flags concerning patterns over weeks.",
                    "professional": "Deadlines and travel stress get caught early before they hurt your health.",
                    "student": "Exam and thesis-stress patterns are quietly monitored.",
                    "photography": "Shoot days, deadlines — watch flags chronic BP patterns you'd miss.",
                    "family_general": "Peace of mind — a warning if long-term BP patterns need a doctor.",
                    "fitness_health": "Multi-week trend detection that a one-time cuff reading can't catch.",
                    "home_management": "The pressure of running a household — the watch quietly monitors trends.",
                }
            },
            {
                "feature_name": "Sleep Score & Insights",
                "technical_meaning": "Advanced sleep tracking with a nightly Sleep Score derived from duration, stages, HR, and breathing metrics.",
                "benefit_templates": {
                    "content_creation": "Late-night edits — see how they hit your recovery and creativity.",
                    "gaming": "Late gaming nights — quantified impact on next-day focus.",
                    "professional": "See how travel and long work weeks affect deep sleep.",
                    "student": "Study late? See how your recovery is really doing before exams.",
                    "photography": "Early shoot days — plan around good sleep-recovery scores.",
                    "family_general": "Kids waking you up? See how it affects your recovery.",
                    "fitness_health": "Directly links sleep quality to next-day training readiness.",
                    "home_management": "Track how erratic days affect rest and plan quieter nights.",
                }
            },
            {
                "feature_name": "Workout Buddy (Apple Intelligence)",
                "technical_meaning": "AI-powered contextual workout coaching — motivation, form insights, and workout planning informed by your recent activity.",
                "benefit_templates": {
                    "content_creation": "Move breaks scheduled around your editing routine.",
                    "gaming": "Prompts to move and stretch between gaming sessions.",
                    "professional": "Micro-workouts and reminders around a busy work calendar.",
                    "student": "Study breaks turned into short workouts that fit exam timetables.",
                    "photography": "Suggests movement after long standing/shooting sessions.",
                    "family_general": "Family-friendly walks and short workouts planned around your day.",
                    "fitness_health": "Real coaching cues, planning insights, and adaptive recovery advice.",
                    "home_management": "Move breaks between chores — the watch gently prompts you.",
                }
            },
            {
                "feature_name": "24-Hour Battery Life",
                "technical_meaning": "All-day battery designed to last through night-time sleep tracking without needing a mid-day charge.",
                "benefit_templates": {
                    "content_creation": "Track a full 12h+ shoot day plus night without recharging.",
                    "gaming": "Full-day battery for tracking screen breaks, plus overnight sleep.",
                    "professional": "Day of meetings + night of sleep tracking without a plug.",
                    "student": "Track a full study day, evening, and overnight sleep in one charge.",
                    "photography": "A full shoot day and overnight recovery, all tracked.",
                    "family_general": "One charge covers school runs, day, and night for the whole family.",
                    "fitness_health": "Continuous 24h tracking of workouts and sleep — no missed data.",
                    "home_management": "All-day chores + evening + overnight, all in one charge.",
                }
            },
            {
                "feature_name": "Smarter Notifications",
                "technical_meaning": "Context-aware notification prioritization that filters what you see on the wrist based on activity, time, and priority.",
                "benefit_templates": {
                    "content_creation": "During shoots, only urgent brand/client alerts come through.",
                    "gaming": "Alerts stay quiet during gaming sessions but urgent ones still surface.",
                    "professional": "Meetings surface urgent client messages, hide everything else.",
                    "student": "During classes, only messages from set contacts come through.",
                    "photography": "Silences distractions during shoots but keeps urgent alerts visible.",
                    "family_general": "Silences most notifications; kids' school and family stay prioritized.",
                    "fitness_health": "Workouts stay uninterrupted except by critical alerts.",
                    "home_management": "Only bills, deliveries, and household alerts break through the noise.",
                }
            },
        ]
    },
    # 7. Ray-Ban Meta Smart Glasses
    {
        "id": "rayban-meta-smart-glasses",
        "brand": "Ray-Ban Meta",
        "name": "Ray-Ban Meta Smart Glasses",
        "category": "Smart Glasses",
        "price_inr": 24990,
        "rating": 4.1,
        "review_count": 678,
        "image": "https://images.unsplash.com/photo-1508296695146-257a814070b4?crop=entropy&cs=srgb&fm=jpg&w=800&q=80",
        "tagline": "Meta AI, real-time translation, 12MP camera, open-ear audio",
        "features": [
            {
                "feature_name": "Meta AI Real-time Assistance",
                "technical_meaning": "Voice-triggered AI that identifies objects/places in your view, answers questions, and gives contextual info hands-free.",
                "benefit_templates": {
                    "content_creation": "Get idea prompts, framing tips, and hands-free voice notes while filming POV content.",
                    "gaming": "Voice-lookup game guides while sitting away from the console.",
                    "professional": "Hands-free reminders and quick lookups during site visits and meetings.",
                    "student": "Ask about landmarks, art, and objects on campus tours — hands-free.",
                    "photography": "Ask about locations, subjects, and lighting while composing.",
                    "family_general": "Hands-free answers for kids' questions while playing with them.",
                    "fitness_health": "Voice-log workouts, ask for form tips on the go.",
                    "home_management": "Ask about product labels, recipes, or how-to's while your hands are busy.",
                }
            },
            {
                "feature_name": "Real-time Language Translation",
                "technical_meaning": "Spoken conversation translation delivered to the wearer via the open-ear audio system.",
                "benefit_templates": {
                    "content_creation": "Interview local subjects while traveling and get live translation in your ear.",
                    "gaming": "Chat with international friends in games / streams naturally.",
                    "professional": "Meet clients across languages without breaking eye contact.",
                    "student": "Study abroad and understand daily conversations naturally.",
                    "photography": "Direct models and locals on travel shoots in their language.",
                    "family_general": "Talk to family and friends who speak different languages naturally.",
                    "fitness_health": "Follow foreign-language yoga or workout classes live.",
                    "home_management": "Talk to service staff and vendors across languages easily.",
                }
            },
            {
                "feature_name": "12MP AI-enhanced Camera",
                "technical_meaning": "12MP camera with AI-enhanced HDR, letting you capture POV photos and videos without pulling out a phone.",
                "benefit_templates": {
                    "content_creation": "First-person vlogs and Reels captured hands-free from your literal eyeline.",
                    "gaming": "Capture funny IRL reactions while streaming or playing at events.",
                    "professional": "Document walkthroughs and site visits hands-free.",
                    "student": "Capture campus events, whiteboards, and lab work POV.",
                    "photography": "Grab candid POV shots to complement main-camera work.",
                    "family_general": "Capture family moments naturally without holding up a phone.",
                    "fitness_health": "Record hikes, runs, and workouts POV-style.",
                    "home_management": "Snap product labels and household details without stopping.",
                }
            },
            {
                "feature_name": "Open-ear Audio System",
                "technical_meaning": "Speakers built into the temples deliver audio to your ears while keeping ears open to the environment.",
                "benefit_templates": {
                    "content_creation": "Listen to reference audio while shooting without blocking your surroundings.",
                    "gaming": "Hear game audio and the real world around you simultaneously.",
                    "professional": "Take calls while remaining aware of your surroundings on the move.",
                    "student": "Listen to lectures or podcasts while walking safely across campus.",
                    "photography": "Stay aware of your surroundings on street shoots and travel.",
                    "family_general": "Answer calls while keeping ears open for kids and household sounds.",
                    "fitness_health": "Music and coaching audio while running — with full traffic awareness.",
                    "home_management": "Take calls while cooking without losing awareness of the kitchen.",
                }
            },
            {
                "feature_name": "Hands-free Voice Control",
                "technical_meaning": "Voice-activated commands for calls, navigation, reminders, and Meta AI queries — nothing to tap.",
                "benefit_templates": {
                    "content_creation": "Start/stop recording, take photos, and ask for prompts by voice.",
                    "gaming": "Trigger reminders and calls without leaving your gaming setup.",
                    "professional": "Voice-take notes and calls while driving or walking between meetings.",
                    "student": "Set study reminders and quick queries without pulling out your phone.",
                    "photography": "Trigger the shutter and voice-note captions while composing.",
                    "family_general": "Answer family calls and set reminders without stopping what you're doing.",
                    "fitness_health": "Log exercises and set timers hands-free during workouts.",
                    "home_management": "Add grocery items and set reminders while cooking or cleaning.",
                }
            },
        ]
    },
    # 8. LG AI Convertible AC
    {
        "id": "lg-ai-convertible-ac",
        "brand": "LG",
        "name": "LG AI Convertible Series 1.5 Ton Inverter AC",
        "category": "Home Appliances",
        "price_inr": 42990,
        "rating": 4.3,
        "review_count": 1830,
        "image": "https://images.unsplash.com/photo-1631545308451-8de11a68eb15?crop=entropy&cs=srgb&fm=jpg&w=800&q=80",
        "tagline": "AI Dual Inverter, voice control, energy-saving AI modes",
        "features": [
            {
                "feature_name": "AI Dual Inverter Technology",
                "technical_meaning": "Compressor speed and cooling intensity adapt in real time to room load, occupancy, and outside temperature — no fixed cycles.",
                "benefit_templates": {
                    "content_creation": "Studio stays at a stable temperature so gear doesn't overheat during long shoots.",
                    "gaming": "Room stays cool for long gaming sessions without wild temperature swings.",
                    "professional": "Home office stays consistently comfortable through the workday.",
                    "student": "Study room stays cool through long revision sessions.",
                    "photography": "Editing room stays comfortable for hours of on-screen work.",
                    "family_general": "Living room stays comfortable for the whole family, all day.",
                    "fitness_health": "Home workout room stays cool without freezing sweaty air.",
                    "home_management": "AC adapts as the family moves in and out of rooms.",
                }
            },
            {
                "feature_name": "Energy-saving AI Modes",
                "technical_meaning": "AI reduces power draw based on usage patterns, learned schedules, and time-of-day cost of electricity.",
                "benefit_templates": {
                    "content_creation": "Long shoot days without wrecking the electricity bill.",
                    "gaming": "Long gaming weekends without a spike on the monthly bill.",
                    "professional": "Home office cooling that doesn't wreck the electricity bill.",
                    "student": "Study through summers without huge electricity bills at home.",
                    "photography": "All-day editing without an electricity-bill hangover.",
                    "family_general": "Family-friendly cooling with noticeably lower summer bills.",
                    "fitness_health": "Home workouts run cool without penalising the electricity bill.",
                    "home_management": "Real, measurable reductions on monthly household bills.",
                }
            },
            {
                "feature_name": "Smart Voice Control",
                "technical_meaning": "Compatible with major voice assistants for hands-free control of temperature, mode, and timers.",
                "benefit_templates": {
                    "content_creation": "Adjust temperature mid-shoot without breaking a take.",
                    "gaming": "Voice-tweak the AC without pausing the game.",
                    "professional": "Voice-adjust cooling between calls, hands-free.",
                    "student": "Change temperature without breaking study flow.",
                    "photography": "Adjust cooling in the edit room without leaving your desk.",
                    "family_general": "Kids and family can voice-adjust the AC easily.",
                    "fitness_health": "Voice-adjust temperature mid-workout without breaking form.",
                    "home_management": "Voice-set schedules and modes while cooking or cleaning.",
                }
            },
            {
                "feature_name": "Auto-clean Functionality",
                "technical_meaning": "AI-scheduled maintenance cycles that dry the coils and reduce dust/mold buildup — reducing servicing needs.",
                "benefit_templates": {
                    "content_creation": "Cleaner air keeps allergies and dust off camera gear.",
                    "gaming": "Cleaner air keeps the room dust-free for long sessions.",
                    "professional": "Cleaner air keeps home-office air quality high.",
                    "student": "Cleaner air keeps allergies down during exam prep.",
                    "photography": "Dust-free room protects sensors and lenses.",
                    "family_general": "Cleaner, healthier air for kids and elderly family members.",
                    "fitness_health": "Cleaner air improves comfort during home workouts.",
                    "home_management": "Fewer service calls — the AC cleans itself on a schedule.",
                }
            },
            {
                "feature_name": "Usage-Pattern Learning",
                "technical_meaning": "Over time, the AC learns your household's daily rhythms and pre-cools rooms just before you use them.",
                "benefit_templates": {
                    "content_creation": "Studio's pre-cooled by the time you start editing.",
                    "gaming": "Room's already cool by your usual gaming hour.",
                    "professional": "Home office is comfortable exactly when your workday starts.",
                    "student": "Study room is pre-cooled to your usual study hours.",
                    "photography": "Edit room is comfortable when you start working every evening.",
                    "family_general": "Living areas are cool when the family gathers, off when nobody's home.",
                    "fitness_health": "Workout room is set to workout-temperature at your usual session time.",
                    "home_management": "AC schedules align with real household patterns — no manual tweaks.",
                }
            },
        ]
    },
    # 9. Haier Smart Sense Fridge
    {
        "id": "haier-smart-sense-fridge",
        "brand": "Haier",
        "name": "Haier Smart Sense AI Series 531L Fridge",
        "category": "Home Appliances",
        "price_inr": 54990,
        "rating": 4.2,
        "review_count": 921,
        "image": "https://images.unsplash.com/photo-1584568694244-14fbdf83bd30?crop=entropy&cs=srgb&fm=jpg&w=800&q=80",
        "tagline": "AI cooling, humidity balance, app-connected freshness",
        "features": [
            {
                "feature_name": "AI-based Temperature Control",
                "technical_meaning": "Multi-zone sensors adjust temperature in real time by section (fresh food, deli, freezer) based on what's inside.",
                "benefit_templates": {
                    "content_creation": "Ingredients for food/content shoots stay perfectly fresh.",
                    "gaming": "Snacks and drinks stay properly chilled through long sessions.",
                    "professional": "Meal-prep and lunches stay fresh across a busy work week.",
                    "student": "Weekly grocery stays fresh even without daily attention.",
                    "photography": "Fresh food for props stays looking great longer.",
                    "family_general": "Family groceries stay fresher longer across every zone.",
                    "fitness_health": "Meal-prep meals and proteins keep optimal texture and taste.",
                    "home_management": "Weekly bulk groceries stay fresher — fewer wasted vegetables.",
                }
            },
            {
                "feature_name": "Humidity Balancing",
                "technical_meaning": "Dedicated humidity control in the crisper drawer keeps leafy greens and fruits fresher for days longer.",
                "benefit_templates": {
                    "content_creation": "Fresh produce for cooking content and shoots stays photogenic longer.",
                    "gaming": "Fruits and snacks stay crisp across long weekends of gaming.",
                    "professional": "Salads and prepped lunches stay fresh through the whole work week.",
                    "student": "Fruits last through a fortnight of hostel/apartment life.",
                    "photography": "Fresh props stay picture-perfect longer.",
                    "family_general": "Vegetables and fruits last noticeably longer between grocery runs.",
                    "fitness_health": "Greens, berries, and prepped meals stay fresh for full meal-prep weeks.",
                    "home_management": "Fewer trips to the market and less wasted produce every month.",
                }
            },
            {
                "feature_name": "Smart App Connectivity",
                "technical_meaning": "Companion app monitors temperature, alerts you to door-open events, and lets you tweak settings from your phone.",
                "benefit_templates": {
                    "content_creation": "Check that ingredients are fine while away on shoots.",
                    "gaming": "Quick tweak temperatures without leaving your setup.",
                    "professional": "Alerts about power outages while at work protect groceries.",
                    "student": "Check on your fridge remotely while at college.",
                    "photography": "Peace of mind when you're away on shoots.",
                    "family_general": "Kids left the door open? You get an alert on your phone.",
                    "fitness_health": "Verify meal-prep temperatures remotely for consistency.",
                    "home_management": "Manage the fridge from anywhere — check status, get alerts.",
                }
            },
            {
                "feature_name": "Energy Efficiency Optimization",
                "technical_meaning": "AI-adjusted compressor cycles reduce electricity draw compared to non-AI comparable-size fridges.",
                "benefit_templates": {
                    "content_creation": "Studio kitchen appliance that doesn't spike your electricity bill.",
                    "gaming": "Efficient background appliance — bills stay predictable.",
                    "professional": "Lower monthly electricity spend across a busy household.",
                    "student": "Cheaper monthly bills for a shared apartment kitchen.",
                    "photography": "Predictable, low monthly bills for a home-studio kitchen.",
                    "family_general": "Meaningful savings for a family running the fridge 24/7.",
                    "fitness_health": "Meal-prep-heavy fridge stays efficient across weeks of use.",
                    "home_management": "Lower monthly electricity bills for the whole household.",
                }
            },
            {
                "feature_name": "Freshness-preservation AI",
                "technical_meaning": "AI monitors how food is stored and adjusts airflow to extend shelf life of perishables.",
                "benefit_templates": {
                    "content_creation": "Ingredients look picture-fresh even days after purchase.",
                    "gaming": "Snacks and drinks stay fresh across weekend sessions.",
                    "professional": "Lunches and prepped meals last through a full work week.",
                    "student": "Groceries survive a two-week hostel shopping cycle.",
                    "photography": "Fresh food props last long enough for repeat shoots.",
                    "family_general": "Family groceries last longer with noticeably less spoilage.",
                    "fitness_health": "Prepped clean meals stay tasty and safe through the week.",
                    "home_management": "Grocery runs stretch further — less waste, more savings.",
                }
            },
        ]
    },
    # 10. Bosch AI Active Water Plus Washing Machine
    {
        "id": "bosch-ai-washing-machine",
        "brand": "Bosch",
        "name": "Bosch AI Active Water Plus 8kg Washing Machine",
        "category": "Home Appliances",
        "price_inr": 38990,
        "rating": 4.4,
        "review_count": 1245,
        "image": "https://images.unsplash.com/photo-1626806787461-102c1bfaaea1?crop=entropy&cs=srgb&fm=jpg&w=800&q=80",
        "tagline": "Auto water level, fabric-sensitive AI, quiet operation",
        "features": [
            {
                "feature_name": "Automatic Water Level Adjustment",
                "technical_meaning": "AI-based load sensing measures how much laundry is inside and adjusts water usage accordingly — no manual selection.",
                "benefit_templates": {
                    "content_creation": "Small quick washes for shoot outfits use only the water they need.",
                    "gaming": "Small solo loads for hoodies/gaming shirts don't waste a full tank.",
                    "professional": "Just work shirts? Only the water needed is used.",
                    "student": "Small hostel loads don't waste a full wash's worth of water.",
                    "photography": "Studio linens and props washed efficiently, whatever the load size.",
                    "family_general": "Full family loads and small kids' loads are both handled efficiently.",
                    "fitness_health": "Frequent workout-clothes loads use only the water they need.",
                    "home_management": "Water bills genuinely drop across small and large loads alike.",
                }
            },
            {
                "feature_name": "Fabric-sensitive Wash Programs",
                "technical_meaning": "AI selects wash intensity based on fabric type — delicate silks, denim, sportswear — so nothing gets over- or under-washed.",
                "benefit_templates": {
                    "content_creation": "On-camera outfits — silks, denim, athleisure — all wash safely.",
                    "gaming": "Gaming shirts and hoodies keep their colors longer.",
                    "professional": "Work shirts and suits are washed at the right intensity every time.",
                    "student": "Uni clothes — hoodies, jeans, delicates — all handled correctly.",
                    "photography": "Studio props and delicate wardrobe stay in shape.",
                    "family_general": "Everything from kids' clothes to delicates is washed correctly.",
                    "fitness_health": "Sportswear and technical fabrics keep their stretch and wicking properties.",
                    "home_management": "One machine handles the household's varied fabrics correctly.",
                }
            },
            {
                "feature_name": "Energy Efficiency",
                "technical_meaning": "Water and power usage optimized per load — smaller loads run shorter, cooler cycles automatically.",
                "benefit_templates": {
                    "content_creation": "Small loads don't wreck the electricity/water bill.",
                    "gaming": "Efficient background chore — bills stay predictable.",
                    "professional": "Lower monthly household utility spend.",
                    "student": "Cheaper monthly bills for shared/apartment life.",
                    "photography": "Efficient loads for the home studio.",
                    "family_general": "Meaningful savings for a family running frequent loads.",
                    "fitness_health": "Frequent workout-load users see real savings.",
                    "home_management": "Water + electricity bills both come down noticeably.",
                }
            },
            {
                "feature_name": "Quiet Operation",
                "technical_meaning": "AI-tuned motor cycles reduce vibration and running noise — designed for small apartments and shared walls.",
                "benefit_templates": {
                    "content_creation": "Run a wash during editing without picking up motor noise.",
                    "gaming": "Wash cycles don't leak into your voice chat.",
                    "professional": "Run washes during work-from-home meetings without noise.",
                    "student": "Hostel/apartment friendly — safe to run at night.",
                    "photography": "Run washes during quiet edit sessions without noise interference.",
                    "family_general": "Safe to run overnight or during nap times without waking anyone.",
                    "fitness_health": "Wash workout clothes late at night without disturbing anyone.",
                    "home_management": "Small-apartment friendly — safe for shared walls and late-night runs.",
                }
            },
            {
                "feature_name": "Load-balancing AI",
                "technical_meaning": "AI redistributes uneven loads during spin cycles to reduce vibration and long-term wear.",
                "benefit_templates": {
                    "content_creation": "Machine doesn't shake — perfect for a home-studio setting.",
                    "gaming": "No vibrations disturbing your gaming setup on the same floor.",
                    "professional": "No shaking or noise even in a work-from-home apartment.",
                    "student": "Balanced spin cycles — no vibration issues in shared spaces.",
                    "photography": "Stable spin cycles — no vibration reaching studio equipment.",
                    "family_general": "No thumping or shaking — safe for kids nearby.",
                    "fitness_health": "Frequent workout-wear loads stay balanced and quiet.",
                    "home_management": "Long-term durability — the machine lasts longer with less wear.",
                }
            },
        ]
    },
]


def get_product(product_id: str):
    for p in PRODUCTS:
        if p["id"] == product_id:
            return p
    return None


def all_products_summary():
    """Returns product list without heavy nested features (for grid page)."""
    return [{
        "id": p["id"],
        "brand": p.get("brand", ""),
        "name": p["name"],
        "category": p["category"],
        "price_inr": p["price_inr"],
        "rating": p["rating"],
        "review_count": p["review_count"],
        "image": p["image"],
        "tagline": p["tagline"],
    } for p in PRODUCTS]
