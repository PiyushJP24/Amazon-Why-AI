"""
Seed reviews for WhyAI. 15-18 paraphrased reviews per product with
inferred use-case cluster tags and sentiment. Positive rates roughly
match the targets in the problem statement.

Clusters: content_creation, gaming, professional, student, photography,
family_general, fitness_health, home_management
"""

REVIEWS = {
    # Samsung Galaxy S25 Ultra — target ~83% positive
    "samsung-galaxy-s25-ultra": [
        ("The 200MP camera and zoom are ridiculous — every travel shot looks pro.", "positive", "photography"),
        ("S Pen is a lifesaver for meeting notes and quick markups on PDFs.", "positive", "professional"),
        ("Battery easily lasts a full day of heavy calendar and email use.", "positive", "professional"),
        ("Now Brief actually surfaces useful reminders in the morning — genuinely helpful.", "positive", "professional"),
        ("Snappy gaming with high frame rates and ray tracing on supported titles.", "positive", "gaming"),
        ("Camera is a beast for content creation — smooth 4K and stabilization.", "positive", "content_creation"),
        ("Gemini Live is great for brainstorming scripts while I'm editing.", "positive", "content_creation"),
        ("Galaxy AI features are more gimmick than useful — I stopped using half of them.", "negative", "professional"),
        ("Price is very steep — you're paying flagship-plus money.", "negative", "family_general"),
        ("Kids love the camera, family photos look incredible.", "positive", "family_general"),
        ("Note-taking with S Pen through lectures is the best I've used.", "positive", "student"),
        ("Overkill for basic use — Now Brief feels bloated for casual family use.", "negative", "family_general"),
        ("Workout tracking works fine, camera catches training clips beautifully.", "positive", "fitness_health"),
        ("The device runs a bit warm during long gaming sessions.", "negative", "gaming"),
        ("Health app integrations are solid, sleep tracking with wearable is smooth.", "positive", "fitness_health"),
        ("Great for managing family calendars and reminders in one place.", "positive", "home_management"),
        ("Camera zoom for spotting birds and wildlife is incredible.", "positive", "photography"),
        ("Battery does drain fast when using AI features constantly.", "negative", "content_creation"),
    ],
    # OnePlus Nord 6 — target ~78% positive
    "oneplus-nord-6": [
        ("Excellent value — feels like a flagship at mid-range price.", "positive", "family_general"),
        ("Camera is great in daylight but low-light shots come out soft.", "negative", "photography"),
        ("Battery management is genuinely good — lasts a full college day.", "positive", "student"),
        ("Real-time translation is handy for casual travel and family chats.", "positive", "family_general"),
        ("Translation is not accurate enough for professional/business calls.", "negative", "professional"),
        ("Great phone for a student on a budget — handles multitasking well.", "positive", "student"),
        ("Adaptive display looks nice, doesn't strain the eyes.", "positive", "student"),
        ("Feels premium in hand and the display is sharp for the price.", "positive", "content_creation"),
        ("AI camera scene mode works well for casual family photos.", "positive", "family_general"),
        ("Gaming performance is decent but not for hardcore titles.", "negative", "gaming"),
        ("Battery genuinely stretches across a whole work day of meetings.", "positive", "professional"),
        ("Camera night mode is disappointing — bad for evening photos.", "negative", "photography"),
        ("Solid all-rounder for household use and family video calls.", "positive", "home_management"),
        ("Video calls stay clear and the mic picks up well on the noise-cancelled calls.", "positive", "professional"),
        ("Fitness tracking apps run smoothly with no lag.", "positive", "fitness_health"),
        ("Charges fast and lasts through a long gym + errands day.", "positive", "fitness_health"),
        ("The 'AI-optimised' claim feels marketing-heavy; performance is just fine.", "negative", "professional"),
    ],
    # HP OmniBook Ultra — target ~80% positive
    "hp-omnibook-ultra": [
        ("Battery life is genuinely 20+ hours in real usage — game changing.", "positive", "professional"),
        ("NPU acceleration makes AI photo edits and video work noticeably faster.", "positive", "content_creation"),
        ("Video compiling and rendering feels snappier than my old i7 laptop.", "positive", "content_creation"),
        ("OLED screen is stunning, but very reflective in bright outdoor light.", "negative", "photography"),
        ("Limited port selection — I need dongles for everything.", "negative", "professional"),
        ("Premium build, feels solid and light for travel.", "positive", "professional"),
        ("Excellent for coding — long compile times don't drain the battery.", "positive", "student"),
        ("Local AI transcription for lectures is a killer feature.", "positive", "student"),
        ("Price is very high — hard to justify vs. a MacBook.", "negative", "professional"),
        ("Handles Lightroom batch edits significantly faster with NPU acceleration.", "positive", "photography"),
        ("Runs cool and quiet even during long exports.", "positive", "content_creation"),
        ("Great laptop for a home-work parent — quiet and light.", "positive", "family_general"),
        ("Bought for kids' school — overkill and expensive for basic use.", "negative", "family_general"),
        ("Home-office champion — 22h battery is not marketing fluff.", "positive", "home_management"),
        ("Wolf Security is reassuring for client work with sensitive data.", "positive", "professional"),
        ("Casual gaming works but this isn't a gaming laptop.", "negative", "gaming"),
        ("Fitness journaling and video coaching runs beautifully.", "positive", "fitness_health"),
    ],
    # Lenovo Yoga Slim 7x — target ~76% positive
    "lenovo-yoga-slim-7x": [
        ("Perfect for remote work — mic noise cancellation is stellar.", "positive", "professional"),
        ("Adaptive performance sometimes lags under heavy load — inconsistent.", "negative", "professional"),
        ("Great value for a Copilot+ PC at this price point.", "positive", "professional"),
        ("Build feels premium but not flagship-tier premium.", "negative", "professional"),
        ("Battery easily gets a full college day of note-taking and browsing.", "positive", "student"),
        ("Great for handling many browser tabs, PDFs, and notes app together.", "positive", "student"),
        ("Video calls sound like a studio recording — huge upgrade from my last laptop.", "positive", "professional"),
        ("Under heavy multitasking, gets warm and fans kick in.", "negative", "professional"),
        ("Home office go-to — quiet, cool, battery lasts.", "positive", "home_management"),
        ("Lightroom slower than expected on complex batch edits.", "negative", "photography"),
        ("Kids can use it for online classes and it lasts a full school day.", "positive", "family_general"),
        ("Fitness journaling and Zoom coaching calls stay clear all day.", "positive", "fitness_health"),
        ("Gaming performance is limited — fine for casual games only.", "negative", "gaming"),
        ("Great for content editing on the go — light and snappy for the price.", "positive", "content_creation"),
        ("Windows-on-ARM has occasional app compatibility hiccups.", "negative", "professional"),
        ("Balances perfectly between speed and battery for daily use.", "positive", "professional"),
    ],
    # Samsung Vision AI QLED TV — target ~87% positive
    "samsung-vision-ai-qled-tv": [
        ("AI upscaling makes old DVDs and 720p content look genuinely great.", "positive", "family_general"),
        ("Cricket matches and IPL look stunning — smooth motion and vivid colors.", "positive", "family_general"),
        ("Picture quality is incredible for the price — QLED contrast is excellent.", "positive", "family_general"),
        ("Menu system is overwhelming — took ages to figure out settings.", "negative", "family_general"),
        ("Vision AI Companion is a fun addition — kids love asking it questions.", "positive", "family_general"),
        ("Gaming mode at 144Hz on the PS5 is buttery smooth.", "positive", "gaming"),
        ("Sound processing keeps dialogue clear even in loud scenes.", "positive", "family_general"),
        ("Handles glare very well — placed near a window and looks great.", "positive", "family_general"),
        ("Perfect movie-night TV — kids and grandparents both enjoy it.", "positive", "family_general"),
        ("Old home videos look upscaled and cleaner than I expected.", "positive", "content_creation"),
        ("Sports mode is fantastic — captures football and cricket motion cleanly.", "positive", "family_general"),
        ("Small niggle: remote isn't backlit, hard to use in dark rooms.", "negative", "family_general"),
        ("Documentary and educational content looks stunning for kids' study.", "positive", "student"),
        ("Great for streaming yoga and workout videos on the big screen.", "positive", "fitness_health"),
        ("Occasional software updates cause hiccups with apps like Prime Video.", "negative", "family_general"),
        ("Voice-searching content and asking about actors is genuinely handy.", "positive", "family_general"),
        ("Photography slideshows look great with rich colors and smooth transitions.", "positive", "photography"),
        ("A bit tricky to wall-mount alone — the panel is thin but wide.", "negative", "home_management"),
    ],
    # Apple Watch Series 11 — target ~85% positive
    "apple-watch-series-11": [
        ("Hypertension alerts flagged issues I would have missed — worth every rupee.", "positive", "fitness_health"),
        ("24-hour battery genuinely enables sleep tracking without daily charging.", "positive", "fitness_health"),
        ("Sleep Score is insightful and consistent — helps me plan recovery.", "positive", "fitness_health"),
        ("Hardware is basically the same as prior gen — evolutionary, not revolutionary.", "negative", "fitness_health"),
        ("Workout Buddy motivates me to hit my move goals during work days.", "positive", "professional"),
        ("Notifications are smart — filters junk during focus/workouts.", "positive", "professional"),
        ("Great for tracking long-term health trends and heart data.", "positive", "fitness_health"),
        ("Hypertension notifications are not a replacement for a real BP cuff.", "negative", "fitness_health"),
        ("Battery is a real improvement over previous generations.", "positive", "family_general"),
        ("Excellent for busy parents — quick alerts without pulling out phone.", "positive", "family_general"),
        ("Workout tracking is precise; running metrics are trustworthy.", "positive", "fitness_health"),
        ("Notifications during meetings are subtle — no more distraction.", "positive", "professional"),
        ("Price feels high for an incremental hardware update.", "negative", "professional"),
        ("Sleep score and nudges reshaped my nightly routine positively.", "positive", "fitness_health"),
        ("Workout Buddy suggestions feel generic sometimes.", "negative", "fitness_health"),
        ("Great for reminding you to move during long content-editing sessions.", "positive", "content_creation"),
        ("Handles daily notifications elegantly for a busy home-life.", "positive", "home_management"),
    ],
    # Ray-Ban Meta Smart Glasses — target ~79% positive
    "rayban-meta-smart-glasses": [
        ("Look and feel like real Ray-Bans — nobody knows it's tech.", "positive", "family_general"),
        ("Real-time translation while traveling is genuinely magical.", "positive", "family_general"),
        ("Battery lasts about 4 hours of active use — limiting for full-day travel.", "negative", "family_general"),
        ("POV vlogging is incredible — hands-free, natural angle.", "positive", "content_creation"),
        ("Camera quality is fine in daylight but noisy in low light.", "negative", "photography"),
        ("Meta AI answers are handy on walks and while commuting.", "positive", "professional"),
        ("Open-ear audio is great — hear music and traffic at once.", "positive", "fitness_health"),
        ("Perfect for commuters — take calls hands-free while walking.", "positive", "professional"),
        ("Kids love watching me use them, POV photos look natural for family memories.", "positive", "family_general"),
        ("Voice control occasionally misses noisy environments.", "negative", "family_general"),
        ("Great for capturing running/hiking POV without holding a phone.", "positive", "fitness_health"),
        ("Battery is a real limitation for full-day content shoots.", "negative", "content_creation"),
        ("Fashion-forward design is a huge win — I actually wear them daily.", "positive", "family_general"),
        ("Real-time translation for restaurant menus while traveling is amazing.", "positive", "family_general"),
        ("Meta AI object recognition is fun but occasionally inaccurate.", "negative", "professional"),
        ("Great for capturing casual content ideas hands-free.", "positive", "content_creation"),
        ("Handy for quick voice-notes during shoots.", "positive", "photography"),
    ],
    # LG AI Convertible AC — target ~81% positive
    "lg-ai-convertible-ac": [
        ("Genuinely lower electricity bills this summer — noticeable savings.", "positive", "home_management"),
        ("Cools quickly and adapts really well as the family moves around.", "positive", "family_general"),
        ("Voice control is inconsistent with accented English.", "negative", "family_general"),
        ("Auto-clean has reduced service calls to almost zero.", "positive", "home_management"),
        ("Great for families running AC most of the day — pattern learning kicks in.", "positive", "family_general"),
        ("Cools evenly even in a 200 sq ft bedroom without cold spots.", "positive", "family_general"),
        ("Installation was a bit tricky — LG service response was slow.", "negative", "home_management"),
        ("Runs quiet enough that we sleep with it on all night.", "positive", "family_general"),
        ("AI mode actually reduces power consumption vs. constant mode.", "positive", "home_management"),
        ("Voice controls work well for the kids to adjust without arguments.", "positive", "family_general"),
        ("Rooms pre-cool exactly when I usually get home from work.", "positive", "professional"),
        ("Remote is basic — no fancy display, but functional.", "negative", "family_general"),
        ("Handles Delhi summer heat impressively at low power draw.", "positive", "home_management"),
        ("Cools the home office room efficiently for a full workday.", "positive", "professional"),
        ("Fine for home workouts — cools sweat-inducing sessions well.", "positive", "fitness_health"),
        ("App connectivity glitches occasionally, needs re-pairing.", "negative", "home_management"),
        ("Kids' bedrooms stay comfortable through hot summer nights.", "positive", "family_general"),
    ],
    # Haier Smart Sense Fridge — target ~80% positive
    "haier-smart-sense-fridge": [
        ("Vegetables and fruits stay noticeably fresher for over a week.", "positive", "home_management"),
        ("Electricity bill dropped after replacing our older fridge.", "positive", "home_management"),
        ("Great fit for a family of 5 doing weekly grocery runs.", "positive", "family_general"),
        ("App connectivity is glitchy — needs re-pairing every few weeks.", "negative", "home_management"),
        ("Smart alerts about door left open have saved us multiple times.", "positive", "family_general"),
        ("Cooling is even across zones — no spoiled produce in months.", "positive", "home_management"),
        ("Meal-prep chicken and greens stay perfect through the week.", "positive", "fitness_health"),
        ("Interior lighting is dim and yellowish — hard to see at night.", "negative", "family_general"),
        ("Quiet enough that we don't hear it running.", "positive", "family_general"),
        ("Storage capacity handles a big family shop with room to spare.", "positive", "family_general"),
        ("Freshness genuinely lasts — less waste every month.", "positive", "home_management"),
        ("Setup instructions were confusing but installer was helpful.", "negative", "home_management"),
        ("Perfect for hostel/apartment life — energy-efficient and reliable.", "positive", "student"),
        ("Ideal for content creators keeping ingredient shots fresh.", "positive", "content_creation"),
        ("Kids can reach shelves easily — thoughtful design.", "positive", "family_general"),
        ("Freezer takes a while to refreeze large loads.", "negative", "home_management"),
        ("Weekly grocery runs stretch further with less waste.", "positive", "home_management"),
    ],
    # Bosch AI Active Water Plus Washing Machine — target ~84% positive
    "bosch-ai-washing-machine": [
        ("Water savings are genuine — smaller loads use way less water.", "positive", "home_management"),
        ("Delicate items last much longer — fabric sensitivity is impressive.", "positive", "home_management"),
        ("Very quiet — safe to run overnight in a small apartment.", "positive", "home_management"),
        ("Wash cycles are a bit longer than expected for standard loads.", "negative", "home_management"),
        ("Perfect for a family running multiple loads a day.", "positive", "family_general"),
        ("Sportswear keeps its stretch and wicking after months of use.", "positive", "fitness_health"),
        ("Detergent dispenser design is a little fiddly to clean.", "negative", "home_management"),
        ("Wash cycles for silks and delicates come out flawless.", "positive", "family_general"),
        ("Small apartment friendly — no vibration, quiet spin cycles.", "positive", "home_management"),
        ("Load balancing works — no thumping even with uneven loads.", "positive", "home_management"),
        ("Energy and water bills both dropped noticeably.", "positive", "home_management"),
        ("Wash timer runs longer than my previous machine.", "negative", "home_management"),
        ("Great for daily gym-wear laundry — quick, quiet, gentle.", "positive", "fitness_health"),
        ("Kids' school uniforms come out looking new week after week.", "positive", "family_general"),
        ("Work shirts get washed at the right intensity — collars last longer.", "positive", "professional"),
        ("Efficient for hostel/student life — small loads use minimal water.", "positive", "student"),
        ("Wash cycles for studio linens and props are perfect.", "positive", "photography"),
    ],
}


def flatten_all_reviews():
    # Merge in the v2 reviews if available
    try:
        from seed_reviews_v2 import NEW_REVIEWS  # noqa: E402
        all_reviews = {**REVIEWS, **NEW_REVIEWS}
    except Exception:
        all_reviews = REVIEWS

    out = []
    idx = 0
    for product_id, revs in all_reviews.items():
        for text, sentiment, cluster in revs:
            out.append({
                "id": f"rev-{idx}",
                "product_id": product_id,
                "review_text": text,
                "sentiment": sentiment,
                "inferred_use_case_cluster": cluster,
            })
            idx += 1
    return out
