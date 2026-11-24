"""Text of the Terms & Conditions and Privacy Policy pages.

Each entry is (anchor id, heading, HTML body). build_site.py turns these into pages.
Edit the wording here, then run: python scripts/build_site.py
"""
EMAIL = '<a href="mailto:info@amplumbing.uk">info@amplumbing.uk</a>'
PHONE = '<a href="tel:+447838628381">+44 7838 628381</a>'

TERMS_INTRO = 'The terms on which AM Plumbing &amp; Heating Ltd supplies plumbing, heating, gas and air conditioning services, and the rules for using this website.'

TERMS = [
('about', '1. About these terms', '''
<p>These terms apply to (a) your use of this website and (b) every quotation, booking and job we carry out (&ldquo;the Work&rdquo;), unless we agree otherwise in writing. Please read them before you accept a quotation or ask us to start work. If anything is unclear, ask us before you go ahead.</p>
<p><strong>Your quotation comes first.</strong> Each job is set out in a written quotation, estimate or job sheet (&ldquo;the Quote&rdquo;). If the Quote and these terms differ on price, scope, timing or any guarantee, the Quote applies to that point. These terms fill in everything else.</p>
<p><strong>How they become part of your contract.</strong> We will send you these terms, or a link to this page, with each Quote. By accepting the Quote, instructing us to proceed, or allowing us to start after we have given you these terms, you agree to them. The version in force on the date of the Quote applies to that job.</p>
<p><strong>Two kinds of customer.</strong> A &ldquo;Consumer&rdquo; is an individual who is buying the Work wholly or mainly for purposes outside their trade, business or profession (for example a homeowner or tenant). A &ldquo;Business Customer&rdquo; is anyone else, including landlords letting property as a business, managing agents, developers and contractors. Where a term applies to only one of them, it says so. Nothing in these terms takes away a Consumer&rsquo;s legal rights.</p>
<p>&ldquo;Existing Installation&rdquo; means every pipe, fitting, joint, valve, cylinder, tank, appliance, control, radiator, fixture, structure or service already at the property when we arrive, including anything hidden or concealed (inside or behind walls, floors, ceilings, boxing-in, ducts or voids, or otherwise not visible), and anything installed by someone other than us.</p>'''),

('company', '2. Who we are', '''
<p>AM PLUMBING &amp; HEATING LTD is registered in England &amp; Wales, company number 10809396, VAT registration number 378119079. Our address is 662 High Road, N12 0NL. Email: ''' + EMAIL + '''. Telephone: ''' + PHONE + '''.</p>
<p>We are a Gas Safe registered business; see our <a href="Health-and-Safety.html">health &amp; safety page</a> for a link to check our registration. We hold public liability insurance for our work. Our insurer is Zurich and the cover applies in the United Kingdom. Ask us if you would like more detail.</p>'''),

('website', '3. Using this website', '''
<p>The website gives general information about our services. We aim to keep it accurate, but it can change and it is <strong>not</strong> a substitute for a professional inspection or advice specific to your property. Nothing on the website, including service descriptions, photographs and examples of past work, is a quotation, a guarantee or an assurance about your job. Any price, timescale or specification binds us only when it is in a Quote we have sent you.</p>
<p>Please use the website lawfully and do not interfere with it or try to gain unauthorised access to it. Project photographs and other content belong to us or the relevant rights holder and must not be reproduced for commercial use without permission. We are not responsible for external websites we link to, such as the Gas Safe Register; they have their own terms and privacy practices.</p>'''),

('enquiries', '4. Enquiries, quotations and booking', '''
<p>Calling, emailing, messaging us or preparing an enquiry on the website does not create a booking or a contract. The enquiry form prepares a draft in your own email application; you must send it for us to receive it.</p>
<p>A telephone or message price is only an indication. A written Quote is an offer that stays open for <strong>30 days</strong> unless it says otherwise, after which we may withdraw or re-price it. A contract is made when you accept the Quote in writing (email and text count) or instruct us to proceed and we agree. The Quote will say whether the price is fixed or an estimate.</p>
<p>Emergency attendance depends on availability and the circumstances of the job. A 24/7 emergency service does not guarantee a particular arrival time. For urgent work, we will agree the scope with you at the time and record it on our job record or invoice.</p>'''),

('scope', '5. What the Work includes', '''
<p>We carry out the Work described in the Quote (or, for urgent callouts, as agreed with you on the day and recorded). We choose the methods, tools and order of work unless the Quote says otherwise.</p>
<ul>
<li><strong>Only the agreed Work.</strong> Unless the Quote says so, we are not engaged to inspect, test, survey, certify, repair, replace or report on any part of the property or its systems that is outside the agreed Work. A simple repair, installation or check does not include examining the rest of the system (see section 6).</li>
<li><strong>Surveys are separate.</strong> If you want a wider check, such as a condition survey of the whole system or its pipework, ask us. It is a separate, chargeable service and must be named in the Quote.</li>
<li><strong>Not included unless stated:</strong> builder&rsquo;s work, plastering, tiling, flooring, decorating and other making good, electrical work, structural work, asbestos surveys and removal, and work on shared or landlord-owned parts of a building.</li>
<li><strong>Opening up.</strong> Where we need to cut into floors, walls or ceilings, we will reinstate them only as far as the Quote states.</li>
<li><strong>Subcontractors.</strong> We may use competent subcontractors. We remain responsible to you for the Work.</li>
</ul>'''),

('existing', '6. Existing and concealed pipework', '''
<p>Many properties contain old, hidden or undocumented pipework, fittings and joints (for example push-fit, compression, soldered, lead or galvanised). We cannot see, assess or verify what is concealed without opening it up, and we can only assess what is reasonably visible and accessible in the course of the agreed Work.</p>
<ul>
<li><strong>No responsibility for what we did not install or work on.</strong> Unless the Quote expressly says we have inspected, tested, replaced or taken responsibility for it, we have not installed, supplied, inspected, certified or guaranteed any Existing Installation. We are not responsible for a failure, leak or damage that starts in a part of the Existing Installation we did not install, replace or work on, even where it shows itself after we connect to, alter, pressurise or reuse it, <strong>to the extent that it is caused by that part and not by our breach or negligence</strong>.</li>
<li><strong>Scope sets the standard.</strong> We carry out all Work with reasonable skill and care. What that requires depends on the agreed scope. It does not require us to inspect, trace, test or report on every pipe, joint, fitting or appliance in the property. We are not required to open up, uncover, dismantle or survey concealed parts, or to look beyond the agreed Work, unless the Quote says so.</li>
<li><strong>A check is a limited check.</strong> A &ldquo;check&rdquo;, &ldquo;inspection&rdquo;, &ldquo;test&rdquo;, &ldquo;visit&rdquo; or &ldquo;look over&rdquo; covers only the item, area or purpose named in the Quote or agreed on the day, and only what is visible and reasonably accessible without removing fixtures, finishes or panels. It is not a survey or a statement about the condition of the rest of the system. A clear result means only that we found no problem in what we checked.</li>
<li><strong>What we will do.</strong> If, in the course of the agreed Work, we notice something that is plainly unsafe or likely to cause damage, we will tell you. We will put it in writing where we can, and we will not leave it unmentioned. This does not extend our duty to look for such things beyond the agreed Work.</li>
<li><strong>Our recommendations.</strong> If we notice, or you tell us about, an old, doubtful or higher-risk component that matters to the Work, we may recommend inspecting, repairing or replacing it. We will put the recommendation in writing (in the Quote, invoice, email, text or job record). Replacement is an optional extra unless the Quote includes it.</li>
<li><strong>If you decline or defer.</strong> If you decline or postpone a recommended step, the Work goes ahead on the basis that you accept the risk of that component. To the extent the law allows, we are not responsible for loss caused by the condition we recommended you address.</li>
<li><strong>Tell us what you know.</strong> Please tell us before we start about any concealed or unusual pipework, previous leaks, repairs or DIY work, other trades&rsquo; work, and anything else you know that could affect the job. Give us any plans or records you have.</li>
</ul>'''),

('pressure', '7. Changes to system pressure and flow', '''
<p>Some jobs change the pressure or flow in your pipework, for example converting from tank-fed to mains-pressure hot water, fitting an unvented cylinder, a combination boiler, a pump or a shower booster. Higher pressure puts extra stress on every part of the system that stays in use, especially older fittings, joints, valves and concealed pipework, and an old component can fail under the new conditions even when the new work is sound.</p>
<ul>
<li>Before such work we will recommend that you consider inspecting or replacing old, accessible pipework and fittings (see section 6). Replacement is not included unless the Quote says so.</li>
<li>Components that remain in use stay at your risk as set out in section 6, subject to your legal rights.</li>
<li>Unvented hot water storage must comply with the Building Regulations and the manufacturer&rsquo;s instructions. We will notify the work as required, and you must have the system serviced as the manufacturer requires and keep the records.</li>
</ul>'''),

('testing', '8. Testing, commissioning and records', '''
<p>Before handing the Work back we test and commission it to a standard appropriate to the installation, the manufacturer&rsquo;s instructions and the regulations that apply, for example by pressure or tightness testing. We record the key details in our job record (date, test type, pressure and duration, which parts were tested, who carried it out and the result), and you can have a copy on request.</p>
<p>A passed test shows that the part tested held at the test conditions at that time. It does not guarantee the condition of parts we did not install or test, or how any part will behave in the future, and it cannot reveal defects that only appear with time or changes in pressure, temperature or use. Where we isolate or leave out part of a system from a test, we will say so.</p>
<p>We may photograph the condition of the property and Existing Installation before, during and after the Work for our records (see our <a href="Privacy-Policy.html">Privacy Policy</a>).</p>'''),

('customer', '9. Your responsibilities', '''
<p>To let us carry out the Work safely and properly, you must:</p>
<ul>
<li>give us safe, clear access to the work area and tell us where the stopcock, isolation valves, consumer unit and meters are;</li>
<li>tell us about hazards you know of, such as asbestos, structural problems, damp, hidden services, known leaks and unsafe appliances;</li>
<li>give us accurate information and any plans, certificates and manufacturer documents you have;</li>
<li>make sure you have the right to authorise the Work (if you are a tenant or leaseholder, that you have your landlord&rsquo;s or freeholder&rsquo;s permission) and tell us who else lives at or uses the property;</li>
<li>protect or remove valuables and fragile items from the work area;</li>
<li>keep your own buildings and contents insurance in place, and tell us promptly of any incident, claim or complaint relating to the Work.</li>
</ul>'''),

('aftercare', '10. After the Work: checking for leaks and empty properties', '''
<ul>
<li><strong>Know your stopcock.</strong> Make sure you know where to turn the water off.</li>
<li><strong>Check in the first week.</strong> After Work on water or heating systems, especially if system pressure has changed, we recommend that you check visible pipework, joints and ceilings below for drips, damp or staining each day for the first week and after any change in use.</li>
<li><strong>Empty or unoccupied property.</strong> If the property will be empty soon after the Work (holiday, void period, between tenants), please tell us before we finish, and we recommend that you turn the water off at the stopcock while it is empty or arrange for someone to check it regularly. Check your own insurance for any unoccupied-property conditions.</li>
<li><strong>If you find a leak:</strong> turn the water off at the stopcock, turn off electricity to affected areas if it is safe to do so, call 999 if there is danger to anyone, then <strong>call us straight away</strong> on ''' + PHONE + ''' and tell your insurer.</li>
</ul>'''),

('defects', '11. Reporting problems and keeping evidence', '''
<p>If you think there is a fault, leak or damage connected with the Work, please tell us <strong>as soon as you reasonably can</strong>, by telephone and by email to ''' + EMAIL + ''' with the address, the date you noticed it and photographs or video. Delay can make the cause harder to establish and can increase the damage.</p>
<ul>
<li><strong>In an emergency</strong> take reasonable steps to limit the damage (see section 10). You may call another engineer for an emergency repair; ask them to keep any failed part and to tell you what they found.</li>
<li><strong>Keep the evidence.</strong> Please photograph the scene before anything is moved, and do not throw away, clean or alter any failed or removed pipe, fitting or component. Keep it somewhere safe and tell us where it is. Where practicable, let us inspect before permanent repairs begin.</li>
<li><strong>If evidence is lost.</strong> Where evidence is discarded or altered, and this makes it harder for us to establish the cause, this may be taken into account when deciding responsibility, to the extent the law allows.</li>
<li><strong>Our own records.</strong> Where we remove or disturb a fitting, joint or other component whose condition may later matter, we may keep it, labelled and photographed, for a reasonable period. You may ask us in writing, before the Work starts, to keep removed parts for you. Otherwise removed materials are waste and we may dispose of them lawfully.</li>
<li><strong>No admission.</strong> Visiting, inspecting, advising or carrying out goodwill repairs does not mean we accept responsibility.</li>
</ul>'''),

('remedy', '12. Our workmanship and putting things right', '''
<p>We carry out the Work with reasonable skill and care, use materials of satisfactory quality, and deliver the Work as described in the Quote. If the Work falls short, a Consumer has the legal right to ask us to repeat or put right the Work, and if that is not done in a reasonable time and without significant inconvenience, to a price reduction. These rights are in the Consumer Rights Act 2015 and are not limited by these terms.</p>
<ul>
<li><strong>Guarantees.</strong> Any guarantee period is stated in the Quote or invoice. We do not offer a guarantee unless the Quote or invoice says so, but your legal rights always apply. For Business Customers, we will put right any defect in the Work that results from our failure to use reasonable skill and care and that you tell us about within a reasonable time.</li>
<li><strong>Manufacturers&rsquo; warranties.</strong> Where a product has a manufacturer&rsquo;s warranty, we will pass on the paperwork. Its conditions, such as annual servicing, are for you to meet.</li>
<li><strong>What is not a defect in our Work:</strong> fair wear and tear; misuse; failure to service or maintain; changes or repairs by others; frost damage; scale, sludge or magnetite from an existing system; the quality of your water supply; and faults in the Existing Installation (see section 6). We recommend cleansing and protecting an existing heating system when fitting a new boiler.</li>
</ul>'''),

('price', '13. Price, variations and payment', '''
<ul>
<li><strong>Price.</strong> The Quote states the price in pounds sterling and whether it includes VAT.</li>
<li><strong>Variations.</strong> If the scope changes, or we find something unforeseen (for example a concealed defect or a different pipework layout), we will explain the effect on price and time before going on, where practicable. For urgent safety work, we may carry out the minimum necessary to make the situation safe, with your agreement (verbal agreement is enough; we will record it).</li>
<li><strong>Payment.</strong> Payment is due on the date and in the instalments the Quote or invoice states. If none is stated, payment is due within <strong>14 days</strong> of the invoice. The invoice shows how to pay.</li>
<li><strong>Late payment.</strong> If you pay late we may charge interest and recovery costs as the law permits. For Business Customers this includes interest and compensation under the Late Payment of Commercial Debts (Interest) Act 1998.</li>
<li><strong>Materials.</strong> Risk in materials passes to you when delivered to the property. Ownership passes to you when you have paid for them in full.</li>
</ul>'''),

('gas', '14. Gas and other safety requirements', '''
<ul>
<li>Gas work is carried out only by Gas Safe registered engineers, and we issue the records the regulations require.</li>
<li>If, during any visit, we find a gas appliance or installation that is unsafe, we must follow industry procedure. We may turn off, disconnect and label the appliance, explain the risk, and report it as required. We cannot leave an immediately dangerous appliance in use.</li>
<li>Servicing your appliances as the manufacturer requires, and fitting working carbon monoxide alarms, is your responsibility. Landlords are responsible for their own legal gas safety duties; arranging a landlord gas safety check is a separate service.</li>
<li>Safety is covered further in our <a href="Health-and-Safety.html">health &amp; safety statement</a>.</li>
</ul>'''),

('liability', '15. Our liability', '''
<p><strong>What these terms never limit.</strong> Nothing excludes or limits liability for death or personal injury caused by negligence, for fraud or fraudulent misrepresentation, for anything that the law does not allow us to limit, or a Consumer&rsquo;s statutory rights.</p>
<p><strong>Consumers.</strong> If we break these terms or are negligent, we are responsible for loss or damage you suffer that is a foreseeable result. Loss is foreseeable if it is obvious or if you and we contemplated it when the contract was made. We supply the Work for domestic and private use only and are not liable for loss of profit, business interruption or any business loss.</p>
<p><strong>Business Customers.</strong> We are not liable for indirect or consequential loss, loss of profit, revenue, rent, goodwill or business, or loss of use, however it arises. Our total liability for all claims arising from a job, whether in contract, tort (including negligence) or otherwise, is limited to the limit of indemnity of our public liability insurance in force at the time. You agree this is reasonable.</p>
<p><strong>Causation.</strong> We are not responsible for loss or damage to the extent that it is caused by: (a) the condition of Existing Installation as described in section 6; (b) work by others; (c) a recommendation we made that you declined or deferred; (d) your failure to give us accurate information, to follow reasonable instructions or to comply with sections 9 to 11; (e) fair wear and tear, misuse, lack of maintenance, frost or the quality of your water supply; or (f) events outside our reasonable control (section 17).</p>
<p><strong>Mitigation.</strong> You must take reasonable steps to limit your loss. Compensation may be reduced to the extent that loss was caused or made worse by your own acts or omissions, or by failure to take such steps.</p>'''),

('insurers', '16. Claims, insurers and other people', '''
<ul>
<li><strong>Tell us promptly.</strong> If you intend to make a claim, if damage has occurred, or if you or your insurer have instructed solicitors or a loss adjuster, please tell us <strong>as soon as you know</strong>, in writing to ''' + EMAIL + ''' and to 662 High Road, N12 0NL, marked &ldquo;Claims&rdquo;. Please give the date, address, what happened and any evidence. Prompt notice lets us notify our insurers and investigate while evidence is fresh.</li>
<li><strong>Claims through your insurer.</strong> If an insurer or anyone else makes a claim through you or in your name, they take your rights subject to these terms, and have no greater rights than you.</li>
<li><strong>Admissions.</strong> No one is authorised to make an admission or settlement on our behalf. We may pass any claim to our insurers and share relevant records with them and our advisers (see our <a href="Privacy-Policy.html">Privacy Policy</a>).</li>
<li><strong>Third parties.</strong> Only you and we can enforce these terms. The Contracts (Rights of Third Parties) Act 1999 does not give anyone else rights under them. This does not affect any rights a third party has independently of this contract.</li>
</ul>'''),

('delays', '17. Delays and events outside our control', '''
<p>We are not in breach of these terms, and not liable for delay or failure to perform, if it results from events outside our reasonable control, including severe weather, utility or supply failures, shortages of materials, access being refused or unsafe, accidents, strikes, or an emergency. We will tell you as soon as we reasonably can and will carry out the Work as soon as reasonably possible. If the delay is very long, either of us may end the contract for the part not yet done and you will pay for the Work done and materials supplied or ordered.</p>'''),

('cancellation', '18. Cancelling', '''
<p><strong>Consumers.</strong> If you are a Consumer and a service contract is made online, by telephone or away from our business premises (including at your home), you generally have a <strong>14-day cancellation period</strong> from the day the contract is made, subject to legal exceptions. We will give you the cancellation information, and a cancellation form, before the Work is agreed.</p>
<ul>
<li>If you ask us to start within the 14 days and then cancel, you may need to pay a proportionate amount for the work done up to the time you tell us you are cancelling.</li>
<li>The right to cancel ends once the service is fully performed, if you asked us to start within the period and acknowledged that you would lose the right.</li>
<li>A request for a visit to carry out urgent repairs or maintenance is exempt from the cancellation right. Additional goods or services beyond what is needed for the urgent work may still carry a right to cancel.</li>
<li>Materials ordered specially for you at your request may be chargeable if you cancel after we have ordered them, where the law allows.</li>
</ul>
<p>To cancel, contact ''' + EMAIL + ''' with your name, contact details and the job concerned. These terms do not remove your statutory rights. See the <a href="https://www.legislation.gov.uk/uksi/2013/3134/contents">Consumer Contracts Regulations 2013</a>.</p>
<p><strong>Business Customers.</strong> You may cancel only with our written agreement. We may charge for work done, materials ordered or supplied, and reasonable costs we have incurred.</p>'''),

('complaints', '19. Complaints', '''
<p>If you have a concern, contact us at ''' + EMAIL + ''' or on ''' + PHONE + ''' with the job address, what went wrong and what you would like us to do. We aim to acknowledge within 5 working days and to respond in full as soon as we reasonably can after we have been able to look into it. For free consumer advice you can contact Citizens Advice. For a complaint about how we use personal information, see our <a href="Privacy-Policy.html">Privacy Policy</a>.</p>'''),

('privacy', '20. Personal information', '''
<p>Our <a href="Privacy-Policy.html">Privacy Policy</a> explains how we use personal information, including job records, photographs and information we share with insurers.</p>'''),

('general', '21. General', '''
<ul>
<li><strong>Whole agreement.</strong> The Quote and these terms are the whole agreement between us for the job. This does not affect information we gave you before the contract that you relied on, or any Consumer&rsquo;s rights under law.</li>
<li><strong>Changes.</strong> A change to the contract must be in writing and agreed by both of us (email and text are enough).</li>
<li><strong>Notices.</strong> We may send notices by email or post to the details you gave us. An email is treated as received on the next working day.</li>
<li><strong>If a term is unenforceable,</strong> the rest still applies. If we do not enforce a term straight away, we can still do so later.</li>
<li><strong>Your own terms.</strong> If you are a Business Customer, your terms and conditions do not apply, even if they are sent with an order.</li>
</ul>'''),

('law', '22. Governing law and updates', '''
<p>These terms, and any dispute about them or the Work, are governed by the law of England &amp; Wales. Business Customers submit to the exclusive jurisdiction of the courts of England &amp; Wales. A Consumer may bring proceedings in the courts of the part of the United Kingdom where they live, or in England &amp; Wales.</p>
<p>We may update these terms. The date and version above identify the latest revision; the version in force on the date of your Quote applies to that job, and an update does not change a contract already agreed. Earlier versions are available on request.</p>'''),
]

PRIVACY_INTRO = 'How AM Plumbing &amp; Heating Ltd uses personal information about customers, enquirers, job applicants, suppliers and website visitors.'

PRIVACY = [
('controller', '1. Who we are', '''
<p>AM PLUMBING &amp; HEATING LTD (company number 10809396) of 662 High Road, N12 0NL is the controller of the personal information described here. This policy applies to customers and prospective customers, people at the properties where we work, website visitors, job applicants, suppliers, subcontractors and anyone who contacts us or makes a claim or complaint.</p>
<p>For privacy questions or requests, email ''' + EMAIL + ''' or call ''' + PHONE + '''.</p>'''),

('data', '2. What we collect and where it comes from', '''
<ul>
<li><strong>Contact details:</strong> name, address, email, telephone number and preferred contact method.</li>
<li><strong>Property and access details:</strong> job address, access arrangements, who lives at or manages the property, and information about the existing systems.</li>
<li><strong>Job and payment records:</strong> quotations, invoices, payment status, job sheets, certificates, test and commissioning records, and notes.</li>
<li><strong>Photographs and video:</strong> images of the work and of the condition of the property and Existing Installation before, during and after the work. These may incidentally show people or personal belongings.</li>
<li><strong>Communications:</strong> emails, texts, messaging-app messages, call notes and any correspondence about a complaint, fault or claim.</li>
<li><strong>Claims and incident information:</strong> details of damage, incidents and insurer or solicitor correspondence, and health and safety incident records.</li>
<li><strong>Recruitment information:</strong> CVs, experience, qualifications, contact details and references.</li>
<li><strong>Website technical data:</strong> IP address and browser details processed by our hosting provider when you visit the site.</li>
</ul>
<p>We get this information from you, from people acting for you (such as a landlord, managing agent, insurer or solicitor), from referees you give us, from other people at the property, and from public sources such as the Gas Safe Register and Companies House. We do not ask you for special category information (such as health or ethnicity). If you give us any, we use it only as needed to deal with your matter or a claim.</p>
<p><strong>Our enquiry form</strong> prepares an email in your own email application. Nothing you type in it is sent to a form-processing server or saved in your browser by our website code. We receive it when you send the email. Your email provider handles that message under its own terms. We do not collect payment card details through this website.</p>
<p>If you give us another person&rsquo;s details (a tenant, a neighbour, a family member), please make sure they know and are happy for you to do so.</p>'''),

('use', '3. Why we use it and our legal basis', '''
<ul>
<li><strong>To respond to enquiries, quote, and carry out and manage the Work</strong> (including scheduling, invoicing and payment): to take steps at your request before a contract, and to perform a contract.</li>
<li><strong>To keep legally required records</strong> (accounting and tax records, gas safety and commissioning records, Building Regulations and health and safety records): legal obligation.</li>
<li><strong>To keep a record of our work, handle faults, complaints and aftercare, and to protect and run our business:</strong> our legitimate interests in running a safe, accountable and properly documented business, balanced against your rights.</li>
<li><strong>To notify, investigate, defend and settle claims, and deal with insurers, brokers, loss adjusters, solicitors and courts:</strong> our legitimate interests in establishing, exercising or defending legal claims and meeting our insurance obligations. If special category information is involved incidentally, we rely on the legal claims condition in the UK GDPR.</li>
<li><strong>To consider job applications:</strong> steps at your request toward a contract, and our legitimate interests in recruiting staff.</li>
<li><strong>To deal with suppliers and subcontractors:</strong> performance of a contract and our legitimate interests.</li>
<li><strong>Where we ask for your consent</strong> (for example to publish photographs that identify you or your property): your consent, which you can withdraw at any time without affecting earlier use.</li>
</ul>
<p>We do not make decisions about you using solely automated processes.</p>
<p><strong>Marketing.</strong> We do not use the enquiry form to subscribe you to marketing. We do not send marketing emails or texts without your consent, or, for business or existing-customer contacts where the law allows, without an easy way to opt out each time. You can object to marketing at any time.</p>'''),

('sharing', '4. Who we share it with', '''
<ul>
<li><strong>Our insurers, insurance brokers and advisers</strong>, loss adjusters and solicitors, where needed to notify, investigate, defend or settle a claim or to comply with our policy conditions. This can include claimants&rsquo; insurers and solicitors where a claim is made.</li>
<li><strong>Email, IT, accounting and software providers</strong> and professional advisers who help us run the business.</li>
<li><strong>Subcontractors, suppliers and manufacturers</strong>, where needed to carry out the job or register a warranty.</li>
<li><strong>Regulators and scheme operators</strong>, such as the Gas Safe Register, building control or competent person schemes, the Health and Safety Executive and utilities, where required.</li>
<li><strong>Banks and payment providers</strong>, to take and reconcile payments.</li>
<li><strong>Courts, tax authorities, the police and others</strong> where the law requires or permits it.</li>
<li><strong>Prospective buyers or successors</strong> of the business, subject to confidentiality.</li>
</ul>
<p>We do not sell personal information.</p>
<p>The website is hosted on GitHub Pages. GitHub may process technical request information such as IP addresses and browser details to deliver and secure the site. See the <a href="https://docs.github.com/en/site-policy/privacy-policies/github-general-privacy-statement">GitHub Privacy Statement</a>. Messaging apps and email providers you use to contact us process your messages under their own terms. Following an external link takes you to a separate service with its own privacy practices.</p>'''),

('transfers', '5. Transfers outside the UK', '''
<p>Some providers (including hosting, email and messaging services) may process information outside the UK. Where UK data protection law applies to a transfer we arrange, we make sure it is covered by an adequacy decision or other appropriate safeguard, such as approved standard contractual clauses. Contact us for details of the safeguards for your information.</p>'''),

('retention', '6. How long we keep information', '''
<p>We keep information only as long as we need it for the purposes above. Our standard periods are:</p>
<ul>
<li><strong>Enquiries and quotations that do not become a job:</strong> 12 months after our last contact.</li>
<li><strong>Customer and job records</strong> (quotes, invoices, job notes, photographs, certificates, test and commissioning records): 6 years after the Work is completed. We may keep core safety, test and commissioning records and related photographs for up to 15 years, because a claim about hidden or latent damage can be made many years after the Work.</li>
<li><strong>Accounting and tax records:</strong> at least 6 years from the end of the accounting period.</li>
<li><strong>Claims, complaints and insurance files:</strong> until the matter is finally resolved and for 6 years afterwards.</li>
<li><strong>Health and safety incident records:</strong> at least 3 years, and longer where a claim is possible.</li>
<li><strong>Unsuccessful job applications:</strong> 6 months after the recruitment decision, or longer if you agree to us keeping your details for future vacancies.</li>
<li><strong>Website hosting logs:</strong> held by GitHub under its own policies.</li>
</ul>
<p>If a claim, complaint or dispute is notified or reasonably anticipated, we keep the relevant records until it is resolved, even if the period above has ended. After that we delete or anonymise information securely.</p>'''),

('security', '7. Keeping information secure', '''
<p>We use appropriate technical and organisational measures to protect personal information, such as access controls, password protection and secure storage. We only give access to people who need it. If a personal data breach occurs that is likely to result in a risk to you, we will notify you and the Information Commissioner&rsquo;s Office as the law requires.</p>'''),

('cookies', '8. Cookies and website storage', '''
<p>This website does not use analytics, advertising scripts, embedded maps or third-party fonts. Its code does not set cookies or use local storage to track visitors or keep enquiry details. The gallery filters and the mobile menu work in page memory only. Hosting services may process technical requests as described above, and external websites and your email application operate separately.</p>
<p>If we introduce analytics, tracking or any optional cookies, we will update this policy and ask for your consent first where the law requires it.</p>'''),

('rights', '9. Your rights', '''
<p>Depending on the circumstances you can ask us to give you a copy of your information, correct it, erase it, restrict how we use it, or provide it in a portable format. You can object to processing based on our legitimate interests, and you have an absolute right to object to direct marketing. You can withdraw consent at any time where we rely on it. These rights have conditions and exceptions: for example we may need to keep records required by law, or needed for a legal claim.</p>
<p>To make a request, contact ''' + EMAIL + '''. We may ask you to verify your identity. We will respond within one month, or tell you if we need up to two more months because the request is complex or you have made several requests. We do not normally charge a fee.</p>'''),

('children', '10. Children', '''
<p>Our website and services are not aimed at children under 18, and we do not knowingly collect their personal information, other than incidentally where they live at a property we work in.</p>'''),

('complaints', '11. Concerns and complaints', '''
<p>Please contact us first if you are unhappy about how we use your information, and we will acknowledge your complaint within 30 days and look into it. You can also complain to the UK Information Commissioner&rsquo;s Office: <a href="https://ico.org.uk/make-a-complaint/">ico.org.uk/make-a-complaint</a>.</p>'''),

('changes', '12. Changes to this policy', '''
<p>We may update this policy when our website, services or legal obligations change. The date and version above identify the latest revision. Earlier versions are available on request.</p>'''),
]
