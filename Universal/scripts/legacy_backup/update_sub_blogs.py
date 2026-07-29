import os
import random
from datetime import datetime, timedelta
from bs4 import BeautifulSoup

# Define the 9 IT cybersecurity news topics for March - May 2026, with expanded, detailed content
topics = [
    {
        "id": 1,
        "title": "ShinyHunters Breach Highlights Vulnerability in EdTech Platforms",
        "author": "Threat Intel Team",
        "content": [
            "<h4>Introduction</h4>",
            "<p>In a massive cybersecurity incident that has sent shockwaves across the academic and corporate training sectors, the notorious ShinyHunters extortion group breached a major educational technology platform. This breach resulted in the exfiltration of approximately 3.65TB of highly sensitive data. The fallout from this incident impacted nearly 9,000 organizations worldwide, underscoring the severe and cascading risks facing the modern education sector. As digital learning tools become further embedded in daily operations, the attack surface expands exponentially, leaving institutions vulnerable to highly coordinated threat actors.</p>",
            "<h4>The Attack Vector and Execution</h4>",
            "<p>Initial forensic investigations indicate that the attackers leveraged a combination of stolen credentials purchased on dark web marketplaces and sophisticated social engineering tactics. By circumventing traditional perimeter defenses and exploiting weaknesses in multi-factor authentication (MFA) implementation—such as MFA fatigue and session token hijacking—the threat actors gained unauthorized access to critical backend databases. The alarming speed of the data exfiltration points to the use of automated, custom-built tools designed to rapidly siphon massive datasets while evading standard network intrusion detection systems (NIDS).</p>",
            "<h4>The Scope of the Exfiltrated Data</h4>",
            "<p>The sheer volume of the stolen data—3.65 terabytes—is staggering. The compromised information reportedly includes a vast array of Personally Identifiable Information (PII), such as full names, residential addresses, financial details, and extensive academic records. Furthermore, proprietary institutional data, including future curriculum plans and internal communications, were also exposed. This comprehensive dataset provides cybercriminals with the necessary raw materials to launch highly targeted spear-phishing campaigns, identity theft operations, and secondary extortion attempts against the affected individuals and organizations.</p>",
            "<h4>Implications for the EdTech Industry</h4>",
            "<p>This incident serves as a stark and urgent reminder that educational platforms hold vast amounts of lucrative data. Unlike financial institutions that have historically hardened their defenses, many EdTech providers are struggling to scale their security posture in tandem with their rapid user growth. Security teams across the sector must immediately pivot towards implementing robust anomaly detection systems, capable of identifying abnormal data transfer volumes and unusual access patterns before significant exfiltration occurs. The 'trust but verify' model is no longer sufficient; a strict Zero Trust architecture is mandatory.</p>",
            "<h4 class='conclusion-title'>Conclusion and Remediation Strategies</h4>",
            "<p class='conclusion-text'>Organizations relying on third-party educational platforms must immediately review their vendor security assessments and enforce strict data access monitoring. Incident response plans must be updated to account for supply-chain vulnerabilities. To prevent similar catastrophic breaches, institutions should mandate hardware-based security keys for authentication, implement rigorous network segmentation, and employ continuous security auditing. The ShinyHunters breach is a clear warning: the education sector is a primary target, and complacency is no longer an option.</p>"
        ],
        "folder": "Blog Sub 1",
        "filename": "zero-trust-security-why-perimeter-defense-is-no-longer-enough.html"
    },
    {
        "id": 2,
        "title": "Grafana Source Code Compromised in GitHub Token Breach",
        "author": "James O'Connor",
        "content": [
            "<h4>Introduction</h4>",
            "<p>Grafana Labs, a leading provider of open-source analytics and interactive visualization web applications, recently disclosed a highly concerning security incident. Unauthorized threat actors successfully utilized a stolen GitHub token to infiltrate their private repositories and download substantial portions of their proprietary source code. The attackers subsequently attempted to extort the company, threatening to release the code publicly. This event starkly highlights the persistent and evolving threat against software development environments and the critical importance of securing developer identities and access tokens.</p>",
            "<h4>Anatomy of the Breach</h4>",
            "<p>The breach was traced back to a compromised Personal Access Token (PAT) belonging to a developer with elevated privileges. The token, which crucially lacked strict scoping limitations and an enforced expiration date, effectively provided the attackers with a master key to Grafana's private repositories. Over a period of several days, the threat actors quietly cloned the repositories, attempting to remain under the radar of automated security scanning tools. Despite the severity of the source code theft, Grafana confirmed through exhaustive forensic analysis that no customer data, sensitive configuration files, or production environments were compromised during the intrusion.</p>",
            "<h4>The Dangers of Over-Privileged Tokens</h4>",
            "<p>This incident serves as a textbook example of the dangers associated with over-privileged and long-lived access tokens. In fast-paced development environments, convenience often overrides security, leading developers to generate tokens with broad permissions that remain active indefinitely. When these tokens are inevitably exposed—whether through phishing, inadvertent inclusion in public commits, or compromised personal devices—the blast radius is significant. The Grafana breach underscores the necessity of implementing ephemeral credentials, just-in-time (JIT) access provisioning, and granular scoping for all programmatic access mechanisms.</p>",
            "<h4>Responding to Extortion and Law Enforcement Cooperation</h4>",
            "<p>Following established FBI guidelines and industry best practices, Grafana categorically refused to pay the extortion demand. This steadfast decision emphasizes the importance of incident transparency and active cooperation with law enforcement agencies over capitulating to cybercriminal demands. Paying ransoms not only fails to guarantee data deletion but actively funds future criminal enterprises and marks the victim as a viable target for repeat attacks. Grafana's transparent handling of the situation, including timely public disclosure and detailed technical post-mortems, sets a positive standard for crisis communication in the tech industry.</p>",
            "<h4 class='conclusion-title'>Conclusion</h4>",
            "<p class='conclusion-text'>Development teams must treat their CI/CD pipelines and code repositories as highly sensitive assets. Enforcing the principle of least privilege, migrating from static tokens to dynamic identity-based authentication, and continuously monitoring GitHub audit logs for anomalous cloning activity are non-negotiable requirements. The protection of intellectual property relies entirely on the stringent management of the credentials that govern access to it.</p>"
        ],
        "folder": "Blog Sub 2",
        "filename": "how-faster-incident-response-limits-security-business-impact.html"
    },
    {
        "id": 3,
        "title": "Mini Shai-Hulud: The Growing Threat of NPM Supply Chain Attacks",
        "author": "Sarah Whitman",
        "content": [
            "<h4>Introduction</h4>",
            "<p>The software development community is currently grappling with a massive and highly coordinated supply-chain campaign dubbed 'Mini Shai-Hulud.' This sophisticated operation successfully compromised numerous widely-used packages within the npm and PyPI ecosystems. The campaign has led to confirmed security breaches at several major artificial intelligence research firms and prominent technology enterprises, exposing severe and systemic weaknesses in how modern software handles open-source package management and dependency resolution.</p>",
            "<h4>How the Attack Unfolded</h4>",
            "<p>The threat actors orchestrated the attack by aggressively utilizing a combination of typosquatting and dependency confusion techniques. They published hundreds of malicious packages with names nearly identical to popular, legitimate libraries. When developers inadvertently installed these rogue packages—often due to simple typographical errors or flawed internal routing—the malicious code was integrated directly into corporate CI/CD pipelines. Once active, the packages executed stealthy pre-install scripts designed to silently harvest environment variables, developer credentials, and internal network configurations, exfiltrating the data to remote command-and-control servers.</p>",
            "<h4>The Ripple Effect in Modern Architecture</h4>",
            "<p>Because modern, cloud-native applications rely heavily on vast webs of third-party open-source libraries, the compromise of a single, seemingly innocuous package can have devastating consequences. This interconnectedness allows a localized breach to quickly ripple through thousands of downstream enterprise environments. In the case of the Mini Shai-Hulud campaign, the stolen CI/CD credentials provided the attackers with the necessary leverage to pivot from development environments directly into production infrastructure, bypassing perimeter security entirely.</p>",
            "<h4>Addressing the Open-Source Security Deficit</h4>",
            "<p>The inherent trust model of package registries like npm and PyPI is increasingly being weaponized. Organizations can no longer blindly pull dependencies without comprehensive vetting. The industry is currently shifting towards mandatory code signing, rigorous provenance attestation, and automated vulnerability scanning, but adoption remains uneven. The Mini Shai-Hulud campaign highlights that security must begin at the developer's workstation and extend through every stage of the software delivery lifecycle.</p>",
            "<h4 class='conclusion-title'>Conclusion</h4>",
            "<p class='conclusion-text'>To defend against advanced supply chain attacks, organizations must urgently adopt comprehensive Software Bill of Materials (SBOMs), enforce strict dependency pinning, and establish internal, proxy-based package registries that scan and approve open-source components before they enter the corporate network. Securing the supply chain is arguably the most critical challenge facing software engineering today.</p>"
        ],
        "folder": "Blog Sub 3",
        "filename": "understanding-modern-cyber-threats-in-cloud-environments.html"
    },
    {
        "id": 4,
        "title": "Nitrogen Ransomware Disrupts Global Manufacturing Operations",
        "author": "James Rodris",
        "content": [
            "<h4>Introduction</h4>",
            "<p>A major, globally recognized electronics manufacturer recently confirmed a devastating cyberattack orchestrated by the notorious Nitrogen ransomware gang. The attack caused widespread, cascading disruption across their production lines, supply chain logistics, and internal IT infrastructure. This incident serves as a high-profile example of how ransomware operators are increasingly targeting the manufacturing sector, fully aware that operational downtime translates into massive financial losses, thereby increasing the leverage for exorbitant ransom demands.</p>",
            "<h4>The Intrusion Vector and Lateral Movement</h4>",
            "<p>Forensic analysis suggests that initial access was likely obtained through compromised Virtual Private Network (VPN) credentials, which were likely purchased from Initial Access Brokers (IABs) operating on dark web forums. Once a foothold was established within the perimeter, the Nitrogen operators utilized sophisticated, living-off-the-land (LotL) techniques. By deploying Cobalt Strike beacons and highly obfuscated, custom PowerShell scripts, the attackers moved laterally through the network, silently escalating privileges and disabling endpoint security tools without triggering immediate alarms.</p>",
            "<h4>Operational Impact and Double Extortion</h4>",
            "<p>The turning point of the attack occurred when the threat actors successfully compromised and encrypted the organization's critical ESXi hypervisor clusters. This effectively brought core manufacturing execution systems (MES) and enterprise resource planning (ERP) software to a sudden halt, paralyzing physical production lines. Furthermore, before deploying the encryptor payloads, the attackers exfiltrated gigabytes of highly sensitive proprietary schematics, employee data, and financial records, employing a ruthless double-extortion tactic designed to force compliance even if backups were viable.</p>",
            "<h4>The Vulnerability of OT/IT Convergence</h4>",
            "<p>This attack highlights the profound risks associated with the increasing convergence of Operational Technology (OT) and Information Technology (IT) networks. As manufacturing floors become more connected and reliant on enterprise IT systems, the air gap that traditionally protected industrial control systems is eroding. When ransomware compromises the IT environment, the lack of rigid segmentation allows the infection to easily bridge the gap, bringing physical machinery and production processes to a standstill.</p>",
            "<h4 class='conclusion-title'>Conclusion</h4>",
            "<p class='conclusion-text'>Manufacturers must urgently prioritize absolute network segmentation and rigorous identity verification. Treating OT and IT networks as distinct, highly monitored zones with strict access controls is critical. Organizations must implement immutable, offline backup solutions and conduct regular, simulated tabletop exercises to ensure rapid recovery capabilities. The Nitrogen attack proves that in modern manufacturing, cybersecurity is inextricably linked to operational resilience.</p>"
        ],
        "folder": "Blog Sub 4",
        "filename": "reducing-incident-response-time-with-automation.html"
    },
    {
        "id": 5,
        "title": "VECT 2.0 Ransomware Found Destroying Files During Encryption",
        "author": "Saim Rony",
        "content": [
            "<h4>Introduction</h4>",
            "<p>Security researchers and incident response teams have issued a dire warning regarding the latest iteration of the VECT ransomware strain. Dubbed VECT 2.0, this variant acts far more like a destructive wiper than a traditional ransomware executable. Deep technical analysis has revealed a critical flaw in its core encryption implementation—a flaw that permanently and irrevocably destroys any file exceeding 131KB in size, transforming what is ostensibly a financially motivated attack into an act of pure digital sabotage.</p>",
            "<h4>The Technical Flaw: Speed Over Safety</h4>",
            "<p>The destructive nature of VECT 2.0 stems from a severe coding error within its multi-threading encryption routine. In an effort to maximize the speed of the encryption process and outrace endpoint detection and response (EDR) solutions, the malware's authors implemented a flawed chunking mechanism. The routine overwrites data chunks incorrectly, leading to severe data corruption. This means that even if a desperate victim pays the exorbitant ransom and successfully receives a decryptor utility, restoring large databases, video files, or comprehensive archives is mathematically and technically impossible.</p>",
            "<h4>The Wiper Distinction and Threat Actor Trust</h4>",
            "<p>While VECT 2.0 is actively marketed by its affiliates as standard ransomware—complete with ransom notes, countdown timers, and negotiation portals—its destructive reality blurs the line between extortion and sabotage. This incident highlights a fundamental truth of the ransomware ecosystem: victims are dealing with unregulated, highly untrustworthy criminal enterprises. The implicit 'honor among thieves'—the promise that paying yields a working key—is completely dismantled by incompetent malware engineering. </p>",
            "<h4>The Shift in Ransomware Dynamics</h4>",
            "<p>The emergence of pseudo-wipers like VECT 2.0 forces a paradigm shift in how organizations calculate the risk of ransomware. When the guarantee of data retrieval is removed from the equation, the leverage of the attacker is entirely dependent on the threat of data publication (exfiltration) rather than data denial (encryption). Organizations can no longer factor ransom payment into their disaster recovery planning as a viable last resort.</p>",
            "<h4 class='conclusion-title'>Conclusion</h4>",
            "<p class='conclusion-text'>The VECT 2.0 incident loudly reinforces the absolute golden rule of ransomware defense: never rely on paying the ransom. Robust, highly isolated, offline, and immutable backups are the singular, guaranteed method for data restoration. Organizations must assume that any encrypted data is permanently destroyed and focus their resources entirely on resilient recovery architectures and aggressive initial access prevention.</p>"
        ],
        "folder": "Blog Sub 5",
        "filename": "common-security-mistakes-that-lead-to-data-breaches.html"
    },
    {
        "id": 6,
        "title": "Coding Errors in Nitrogen Malware Irrevocably Corrupt ESXi Servers",
        "author": "Mayers Jame",
        "content": [
            "<h4>Introduction</h4>",
            "<p>In a troubling trend that echoes the recent VECT 2.0 disaster, the highly active Nitrogen ransomware operation was recently identified as deploying critically flawed malware. Security analysts discovered a severe coding error within Nitrogen's specialized ESXi encryptor payload. This catastrophic error causes the malware to irrevocably corrupt virtual machines (VMs) during the encryption sequence, turning a recoverable hostage situation into a scenario of total, unrecoverable data loss for affected enterprises.</p>",
            "<h4>Virtualization Under Attack: The ESXi Target</h4>",
            "<p>Threat actors are increasingly focusing their sophisticated efforts on VMware ESXi environments. The logic is chillingly efficient: compromising a single hypervisor allows attackers to simultaneously take down dozens, or even hundreds, of virtual machines hosting mission-critical applications and databases. However, developing stable, low-level malware that interacts cleanly with complex virtualization filesystems (like VMFS) proves highly challenging for underground developers, frequently resulting in catastrophic bugs.</p>",
            "<h4>The Cost of Bugs in the Criminal Ecosystem</h4>",
            "<p>The specific bugs within the Nitrogen ESXi encryptor lead to shattered VMDK (Virtual Machine Disk) files. The malware improperly handles the file headers and metadata during the rapid encryption cycles. Victims who chose to pay the ransom demands found that the provided decryption keys were entirely useless. While the keys correctly deciphered the encrypted blocks, the underlying file structure was so badly mangled by the initial encryption process that the virtual disks could not be mounted or read by the hypervisor, leading to absolute data loss.</p>",
            "<h4>Re-evaluating Disaster Recovery Postures</h4>",
            "<p>This incident forces organizations to drastically re-evaluate their virtualization security and disaster recovery postures. Traditional agent-based backups running inside the VMs are often targeted and encrypted alongside the host data. Relying solely on hypervisor-level snapshots is equally dangerous if the management interface itself is compromised. True resilience requires backups that exist entirely outside the sphere of influence of the primary virtualization infrastructure.</p>",
            "<h4 class='conclusion-title'>Conclusion</h4>",
            "<p class='conclusion-text'>Securing hypervisors is paramount to enterprise survival. System administrators must ruthlessly restrict management interface access (vCenter, SSH) via strict firewall rules and VPN-only access. Furthermore, applying vendor patches immediately and utilizing hardware-level, immutable backup solutions that operate completely independently of the ESXi environment are critical defenses against these destructive, poorly-coded ransomware variants.</p>"
        ],
        "folder": "Blog Sub 6",
        "filename": "why-continuous-monitoring-beats-periodic-audits-2.html"
    },
    {
        "id": 7,
        "title": "Interlock Gang Exploits Maximum-Severity Cisco Zero-Day",
        "author": "James Smith",
        "content": [
            "<h4>Introduction</h4>",
            "<p>The aggressive Interlock ransomware gang has been observed executing highly coordinated attacks by exploiting a maximum-severity remote code execution (RCE) zero-day vulnerability in Cisco's Secure Firewall Management Center (FMC). This critical flaw allowed the threat actors to bypass traditional perimeter defenses seamlessly, granting them deep, unfettered access to enterprise networks worldwide and highlighting the fragility of relying solely on edge security devices.</p>",
            "<h4>Exploitation Details and Mechanics</h4>",
            "<p>The zero-day vulnerability, carrying a CVSS score of 10.0, allowed unauthenticated, remote attackers to execute arbitrary commands with root privileges directly on the firewall management interface. Interlock operators rapidly weaponized this flaw, utilizing it as a reliable initial access vector. Once the FMC was compromised, the attackers could manipulate firewall rules, disable intrusion prevention systems, and establish persistent, heavily obfuscated command-and-control (C2) tunnels directly into the heart of the victim's network.</p>",
            "<h4>Patch Management Shortfalls and the Window of Vulnerability</h4>",
            "<p>Despite Cisco releasing emergency out-of-band patches within days of the vulnerability's discovery, widespread exploitation continued for weeks. Many organizations fatally delayed deployment due to the critical nature of their firewall infrastructure, fearing that patching might cause unintended network outages. This hesitation provided a highly lucrative window of vulnerability for the Interlock operators, who systematically scanned the internet for unpatched appliances and compromised numerous high-value targets in the financial and healthcare sectors.</p>",
            "<h4>The Irony of Compromised Security Tools</h4>",
            "<p>There is a dark irony when the very devices designed to protect a network become the primary vector for its compromise. Edge devices like firewalls and VPN gateways reside entirely outside the network perimeter, making them exposed to continuous internet-wide scanning. When these devices harbor critical vulnerabilities, they offer attackers the highest level of privileged access, bypassing all internal segmentation and endpoint monitoring.</p>",
            "<h4 class='conclusion-title'>Conclusion</h4>",
            "<p class='conclusion-text'>Perimeter security devices are highly prized, high-value targets. Organizations must establish and enforce accelerated, emergency patching protocols specifically for internet-facing edge devices. The risk of temporary operational downtime from a patch is vastly outweighed by the certainty of a catastrophic breach. Continuous external attack surface management (EASM) is required to identify and remediate these vulnerabilities before advanced threat actors like Interlock can exploit them.</p>"
        ],
        "folder": "Blog Sub 7",
        "filename": "why-continuous-monitoring-beats-periodic-audits.html"
    },
    {
        "id": 8,
        "title": "The Shift Towards Multi-Extortion in Modern Ransomware",
        "author": "Aleen Shear",
        "content": [
            "<h4>Introduction</h4>",
            "<p>The global cybersecurity landscape is currently witnessing a distinct, aggressive evolution in threat actor tactics: the rapid rise of 'multi-extortion' ransomware models. As organizations have slowly improved their backup and recovery capabilities, making traditional encryption-only attacks less profitable, threat actors are pivoting. They are now increasingly focusing on exfiltrating and weaponizing stolen corporate data, utilizing multifaceted extortion strategies to force compliance and maximize their illicit revenue streams.</p>",
            "<h4>Beyond Simple Encryption: The New Extortion Playbook</h4>",
            "<p>Modern ransomware gangs, such as ALPHV and LockBit, now routinely and silently exfiltrate terabytes of sensitive data long before deploying their encryptors. If a victim refuses to pay for the decryption key—often because they have viable backups—the attackers shift to the second phase of extortion. They threaten to release the highly sensitive data (PII, intellectual property, financial records) on public leak sites. Furthermore, attackers are now engaging in third-level extortion: contacting the victim's clients, partners, and even regulatory bodies directly to maximize reputational damage and legal liability.</p>",
            "<h4>The Failure of Traditional Defense Strategies</h4>",
            "<p>This fundamental shift in tactics renders traditional perimeter-based and backup-centric defenses largely insufficient. If sensitive data is successfully stolen, having a perfect, immutable backup does absolutely nothing to prevent the subsequent extortion and public leak. The crisis shifts from a technical recovery problem to a severe legal, regulatory, and public relations disaster. Organizations must recognize that preventing data exfiltration is now equally, if not more, important than preventing data encryption.</p>",
            "<h4>Data-Centric Security Architectures</h4>",
            "<p>To survive in a multi-extortion landscape, organizations must urgently pivot towards data-centric security architectures. This involves comprehensive data discovery—knowing exactly where sensitive data resides—and implementing strict data classification policies. Robust at-rest and in-transit encryption must be applied to crown-jewel data, ensuring that even if it is stolen, it remains entirely unreadable to the attackers.</p>",
            "<h4 class='conclusion-title'>Conclusion</h4>",
            "<p class='conclusion-text'>To effectively combat the rising tide of multi-extortion, businesses must deploy aggressive Data Loss Prevention (DLP) strategies, implement stringent Identity and Access Management (IAM) controls, and continuously monitor for anomalous outbound data flows. The ultimate goal is to protect the confidentiality of the data even after a perimeter breach inevitably occurs, rendering the attacker's primary leverage useless.</p>"
        ],
        "folder": "Blog Sub 8",
        "filename": "detecting-advanced-persistent-threats-before-damage-occurs.html"
    },
    {
        "id": 9,
        "title": "CoinbaseCartel: A New Extortion Group Enters the Fray",
        "author": "Olibar Kone",
        "content": [
            "<h4>Introduction</h4>",
            "<p>A newly identified and highly aggressive extortion group, dubbed 'CoinbaseCartel' by security researchers, has recently emerged on the threat landscape. This group is specifically targeting high-value financial institutions, cryptocurrency exchanges, and blockchain infrastructure providers. Threat intelligence analysts believe the group is not entirely new, but rather a sophisticated offshoot with deep operational ties and shared infrastructure with the notorious ShinyHunters and Scattered Spider criminal ecosystems.</p>",
            "<h4>Mastery of Social Engineering and Vishing</h4>",
            "<p>CoinbaseCartel distinguishes itself from traditional ransomware operators through its absolute mastery of advanced social engineering tactics. Rather than relying on technical exploits or brute-force attacks, they frequently employ highly convincing voice phishing (vishing) campaigns and orchestrated SIM-swapping attacks. By impersonating IT helpdesk personnel or high-ranking executives with alarming accuracy, they consistently manipulate employees into divulging credentials or bypassing robust multi-factor authentication (MFA) protocols.</p>",
            "<h4>The Convergence of Elite Threat Actors</h4>",
            "<p>The significant overlap in infrastructure, target selection, and operational tactics with groups like Scattered Spider suggests a chilling trend: the growing collaboration and knowledge sharing among top-tier cybercriminal syndicates. This convergence allows specialized groups to pool their resources, sharing highly effective phishing templates, access brokers, and money laundering networks. The result is a highly agile, resilient, and sophisticated threat campaign that can pivot rapidly to exploit human vulnerabilities.</p>",
            "<h4>Defending Against the Human Element</h4>",
            "<p>Because CoinbaseCartel targets the human element rather than technical flaws, defending against them requires a fundamental shift in security strategy. Standard perimeter defenses and endpoint detection tools are frequently blind to attacks where the adversary logs in using legitimate, albeit stolen, credentials. Organizations must focus heavily on securing the identity lifecycle and training employees to recognize highly targeted, context-aware social engineering attempts.</p>",
            "<h4 class='conclusion-title'>Conclusion</h4>",
            "<p class='conclusion-text'>Defending against highly skilled social engineers requires far more than technological solutions. Organizations must foster a pervasive, positive security culture. Implementing strict, out-of-band identity verification processes for all internal support requests and password resets is mandatory. Most importantly, high-risk organizations must mandate the use of phishing-resistant MFA, such as FIDO2 hardware security keys, which completely neutralize the threat of credential harvesting and MFA fatigue attacks.</p>"
        ],
        "folder": "Blog Sub 9",
        "filename": "how-modern-cyber-attacks-bypass-traditional-security-controls.html"
    }
]

# Generate random dates between March 1, 2026 and May 31, 2026
start_date = datetime(2026, 3, 1)
end_date = datetime(2026, 5, 31)

def random_date(start, end):
    return start + timedelta(days=random.randint(0, int((end - start).days)))

for t in topics:
    rd = random_date(start_date, end_date)
    # Format: Month DD, YYYY (e.g. May 14, 2026)
    t["date"] = rd.strftime("%B %d, %Y")

base_dir = r"C:\Users\angam\Downloads\Nexyra Website\Blog - Main Page"

# 1. Update the 9 sub blogs
for t in topics:
    file_path = os.path.join(base_dir, t["folder"], "sentrixa-template.webflow.io", "blog", t["filename"])
    if not os.path.exists(file_path):
        print(f"File not found: {file_path}")
        continue
    
    with open(file_path, "r", encoding="utf-8") as f:
        soup = BeautifulSoup(f, "html.parser")
    
    # Update Title tag
    if soup.title:
        soup.title.string = f"{t['title']} - Nexyra Tech"
        
    # Update Main H3 title
    title_tag = soup.find("h3", class_="blog-single-top-title")
    if title_tag:
        title_tag.string = t["title"]
        
    # Update Author and Date
    wrighter_info = soup.find("div", class_="wrighter-info")
    if wrighter_info:
        author_p = wrighter_info.find("div", class_="wrighter-info-left").find("p", class_="wrighter-name")
        if author_p:
            author_p.string = t["author"]
        
        date_p = wrighter_info.find("div", class_="wrighter-info-right").find("p", class_="wrighter-name")
        if date_p:
            date_p.string = t["date"]
            
    # Remove the middle image wrap just to be safe
    middle_img = soup.find("div", class_="blog-content-img-wrap")
    if middle_img:
        middle_img.decompose()
        
    # Replace content
    blog_content_div = soup.find("div", class_="blog-content")
    if blog_content_div:
        blog_content_div.clear()
        
        classes = ["blog-rich-text-01 w-richtext", "blog-rich-02 w-richtext", "blog-rich-03 w-richtext", "conclusion-wrap"]
        
        for i, chunk in enumerate(t["content"]):
            if i % 2 == 0:
                div = soup.new_tag("div")
                cls_idx = i // 2
                if cls_idx < len(classes):
                    div["class"] = classes[cls_idx]
                else:
                    div["class"] = "blog-rich-03 w-richtext"
                    
                div["style"] = "opacity:1"
                
                h4_html = chunk
                p_html = t["content"][i+1] if i+1 < len(t["content"]) else ""
                
                div.append(BeautifulSoup(h4_html + p_html, "html.parser"))
                blog_content_div.append(div)
                
    # Write back
    with open(file_path, "w", encoding="utf-8") as f:
        f.write(str(soup))
        
print("Sub blogs updated with detailed content.")

# 2. Update the main blog.html page
main_blog_path = os.path.join(base_dir, "sentrixa-template.webflow.io", "blog.html")
if os.path.exists(main_blog_path):
    with open(main_blog_path, "r", encoding="utf-8") as f:
        soup = BeautifulSoup(f, "html.parser")
        
    list_bottom = soup.find("div", class_="blog-collection-list-bottom")
    if list_bottom:
        items = list_bottom.find_all("div", role="listitem")
        
        for idx, item in enumerate(items):
            if idx < len(topics):
                t = topics[idx]
                
                info_wrap = item.find("div", class_="blog-info-wrap")
                if info_wrap:
                    p_tags = info_wrap.find_all("p", class_="blog-info")
                    if len(p_tags) >= 2:
                        p_tags[0].string = t["author"]
                        p_tags[1].string = t["date"]
                        
                detail_p = item.find("p", class_="blog-detail")
                if detail_p:
                    detail_p.string = t["title"]
                    
    with open(main_blog_path, "w", encoding="utf-8") as f:
        f.write(str(soup))
    print("Main blog.html updated.")
else:
    print("Main blog.html not found.")
