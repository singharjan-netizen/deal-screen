# Zeroeyes — first-pass screen

**Source:** https://www.zeroeyes.com (public site only, scraped 6 pages)

## What they build
ZeroEyes sells software that watches video from a customer's existing IP security cameras and uses computer vision to spot visible firearms. It also detects knives, intruders, left-behind objects and blocked cameras. Every detection is checked by a trained analyst at the company's 24/7 ZeroEyes Operations Center (ZOC) before an alert goes to the customer and law enforcement, "often in a matter of seconds." Customers are schools, universities, government, commercial sites and smart cities. The job is to give responders a warning before a shooting starts. Newer products include ZeroLink (a platform that coordinates response), public-safety alerts, and 3D site maps built from drone and LiDAR scans.

## Sector and category
AI and physical security (public safety, with a federal/defense-adjacent angle). It's a better version of an existing category, security camera monitoring. The new part is detecting a visible gun before a shot is fired, with a human confirming each alert.

## Stage signals
- **Founded 2018** by former Navy SEALs and technologists, after the Marjory Stoneman Douglas shooting. This is a mature company, not an early one.
- **Footprint:** deployed in 40+ U.S. states, with 300K video frames per second analyzed across all active deployments.
- **Named customers:** River Spirit Casino, Merage JCC of Orange County, Vassar Public Schools and Navy Pier (Chicago).
- **Federal:** "ZeroEyes Federal" (ZEF) is hosted in a FedRAMP Moderate Authorized environment. The site doesn't name any agency customers.
- **Certifications:** DHS SAFETY Act Designation (Qualified Anti-Terrorism Technology), SOC 2, ISO 27001, and a BreachBits cyber score.
- **Partners and integrations:** Axis, Verkada, Genetec, Milestone, Hanwha Vision, Avigilon, RapidSOS, Everbridge and CrisisGo.
- **Hiring:** 6 open roles (2 operations, 4 engineering). One is a Senior AI Engineer for Video Search, which hints at a product beyond detection. Analyst roles are listed in Conshohocken, PA and Honolulu, HI, which suggests a second operations site.
- **Products:** says "five products," but the products page lists six tiles.
- **Funding, revenue and headcount:** not stated.
- **Media:** a "covered by national media" newsroom is linked, but no outlets are named in the scrape.

## Claimed technical advantage
- A human analyst verifies every alert, 24/7/365; many analysts have law enforcement or military backgrounds. **[unverified marketing]** The operations center and analyst hiring are real, but staffing and speed aren't shown.
- "The only AI weapon detection platform with a human safety net." **[unverified marketing]**
- Human review is "eliminating false positives." **[unverified marketing]** The technology page softens this to "reduce" and "minimize," and no false-positive or false-negative rates are published.
- Models trained on 5M+ images to work "in any environment or lighting condition." **[unverified marketing]**
- No new hardware; it runs on existing cameras. **[verifiable from site, partially]** The integration partner list supports it; how deep each integration goes is not stated.
- DHS SAFETY Act designation, which gives customers liability protection. **[verifiable from site]** Claimed on the site; it can be checked against DHS's public records.
- FedRAMP Moderate environment, SOC 2 and ISO 27001. **[verifiable from site]** Claimed on the site; each can be checked independently. The FedRAMP wording ("hosted within" an authorized environment) is ambiguous: it could mean ZEF itself is authorized or only its cloud host.
- Patents. **[unverified marketing]** A "Patents" footer link exists, but its contents weren't scraped.

## Risks and open questions
- **Scaling the human step:** every AI detection is reviewed by a person. Analyst headcount and gross margin may grow with camera count rather than with software. Margins are not stated.
- **Liability and reputation:** one missed gun (false negative) in a high-profile shooting could badly damage the brand. SAFETY Act coverage helps the legal side but not the reputational side. Measured accuracy is not stated.
- **Concentration in K-12:** the mission ("end mass shootings in America"), the 40+ state footprint and the testimonials all lean toward schools. That exposes revenue to school budget and grant cycles. Revenue mix is not stated.
- **Partners could compete:** Verkada, Axis, Genetec, Avigilon and Hanwha own the camera and video-management layer and could build weapon detection themselves. This is my inference; the site only calls them partners.
- **Privacy and civil liberties:** the site says it does no facial recognition and stores no biometrics. Continuous AI monitoring of schools and public spaces still invites scrutiny, particularly outside the U.S. International presence is not stated.

## Five questions for the founder
1. Across the 300K frames/sec you analyze, how many AI detections reach the operations center each day, what share do analysts reject, and how have analyst cost per camera and gross margin changed over the last 3 years?
2. What is your measured miss rate (guns on camera that weren't flagged), how do you measure it, and has any customer site had an incident the system failed to catch?
3. What is revenue by segment (K-12, higher ed, government, commercial, smart city), and how much of the K-12 revenue depends on state grants or school-safety legislation?
4. Which federal agencies use ZeroEyes Federal today? Is the FedRAMP Moderate authorization for ZEF itself or its cloud host, and is there a path to FedRAMP High or DoD impact levels?
5. For Verkada, Genetec, Milestone and the other partners: are they sales channels or just technical integrations, and what stops them from shipping native gun detection? How much of the 5M-image training set is proprietary real-world footage versus staged or synthetic?

## Screen verdict
**LOOK CLOSER.** The federal credentials (FedRAMP, SAFETY Act) and a 40+ state footprint show real traction in a defense-adjacent AI market, but the diligence question is whether the human-verification model can reach software-level margins.
