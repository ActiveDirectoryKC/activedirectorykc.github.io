---
title: "Beginner's Guide"
---

# Beginner's Guide

A question that comes up a lot is "How do I get started with..." and usually the question is around Active Directory, Identity, Entra ID, or PKI. At least for me it is.

Below are some resources tailored to each topic. This is by far not the one-stop-shop guide and it will be updated as time goes on. At the end are some general references that may be worth looking into.

Above all else though, we cannot recommend labbing and practicing as much as possible. If you can get a lab to do some playing, we highly recommend it.

> NOTE: As of 2026-09 the homelab market is crushed due to unreasonable hardware costs. As we find alternative resources, we'll update as we can.

## Subreddits to Follow
https://www.reddit.com/r/activedirectory  
https://www.reddit.com/r/sysadmin  
https://www.reddit.com/r/WindowsServer  
https://www.reddit.com/r/IdentityManagement/  

## Discords to Join/Follow

- Black Hills Information Security - https://discord.gg/bhis
- Antisyphon Training - https://discord.gg/antisyphon
- Horizon Secured - https://discord.gg/XnpRW7btg
- ZeroToSec - https://discord.gg/f7jxtv23bQ

## Active Directory (AD) Beginner Resources

- Community Resources
    - AD Community Youtube - https://www.youtube.com/@ActiveDirectoryCommunity
    - AD Community Events Page - https://events.humanitix.com/host/active-directory-subreddit-community
    - Active Directory Community Wiki
        - Reddit - https://www.reddit.com/r/activedirectory/wiki/index
        - Github - https://github.com/ActiveDirectoryKC/RedditADWiki
- Resources
    - \#video #free From Zero to Hero: A Beginner's Guide to Active Directory (Antisyphon + Black Hills Infosec)
        - https://www.youtube.com/watch?v=XwOV7HpVLEA
    - \#training #video Antisyphon Pay What You can
        - Check this series as every so often there is an Identity-related training for super cheap.
        - https://www.antisyphontraining.com/pay-what-you-can/
    - \#training #free MS Learn: Active Directory Domain Services
        - https://learn.microsoft.com/en-us/training/paths/active-directory-domain-services/
    - \#training #free Deploy and manage identity infrastructure
        - https://learn.microsoft.com/en-us/training/paths/deploy-manage-identity-infrastructure/
    - \#training #free Deploy and manage Active Directory Domain Services
        - https://learn.microsoft.com/en-us/training/paths/deploy-manage-active-directory-domain-services/
    - \#training #free MS Learn: Administer Active Directory Domain Services
        - https://learn.microsoft.com/en-us/training/paths/administer-active-directory-domain-services/
    - \#training #free MS Learn: Deploy and Manage Identity Infrastructure
        - https://learn.microsoft.com/en-us/training/paths/deploy-manage-identity-infrastructure/
    - \#training #free Active Directory Domain Services Modules on Microsoft Learn
        - https://techcommunity.microsoft.com/blog/itopstalkblog/active-directory-domain-services-modules-on-microsoft-learn/4547604
    - \#article #free Install Active Directory Domain Services
        - https://learn.microsoft.com/en-us/windows-server/identity/ad-ds/deploy/install-active-directory-domain-services--level-100-
    - \#article #free Active Directory Domain Services Overview
        - Focus on the "AD DS Getting Started Section"
        - https://learn.microsoft.com/en-us/windows-server/identity/ad-ds/get-started/virtual-dc/active-directory-domain-services-overview
    - \#article #free How to configure firewall for AD domains and trusts
        - Includes details on general AD firewall rules.
        - https://learn.microsoft.com/en-us/troubleshoot/windows-server/active-directory/config-firewall-for-ad-domains-and-trusts
    - \#blog #article #free Kerberos for the Busy Admin
        - https://techcommunity.microsoft.com/blog/askds/kerberos-for-the-busy-admin/395083
    - \#article #free Active Directory Replication Concepts
        - https://learn.microsoft.com/en-us/windows-server/identity/ad-ds/get-started/replication/active-directory-replication-concepts
    - \#training #free Understanding Active Directory Group Policy Security Settings
        - https://learn.microsoft.com/en-us/training/modules/understand-active-directory-security-policies/
    - \#training #free Understand Windows Server service accounts
        - https://learn.microsoft.com/en-us/training/modules/understand-windows-service-accounts/
    - \#article #free #3rdParty Securing AD Service Accounts
        - https://github.com/dcdiagfix/AD-ServiceAccounts-FUNdamentals/blob/main/AD-ServiceAccounts-FUNdamentals.md
    - \#article #free Monitoring AD for Signs of Compromise
        - https://learn.microsoft.com/en-us/windows-server/identity/ad-ds/plan/security-best-practices/monitoring-active-directory-for-signs-of-compromise
    - \#article #free Tier Model for Active Directory Domain Services
        - https://learn.microsoft.com/en-us/windows-server/identity/ad-ds/tier-model
    - \#book Exam Ref AZ-800
        - This is a book that is tied to a soon to be retired exam (AZ-800), but it is still a good reference for AD even if the exam no longer exists
        - https://www.amazon.com/AZ-800-Administering-Windows-Infrastructure-3570357-ebook-dp-B09Z7R89C9/dp/B09Z7R89C9/
    - \#book Exam Ref AZ-742
        - This exam was retired awhile back. However, AD hasn't changed dramatically since and the content is still relevant.
        - https://www.amazon.com/Exam-70-742-Identity-Windows-Server-ebook/dp/B06XS2R7T8
    - \#book Exam Ref AZ-802 (TBD)
        - Replacement book for the AZ-800 book.
    - \#book AD: Designing, Deploying, and Running AD 5th Edition
        - This book is the corner stone of AD resources still. It covers topics that go further than beginners need.
        - This book is also mildly out of date but most of the content is still relevant to modern AD.
        - https://www.amazon.com/Active-Directory-Designing-Deploying-Running-ebook-dp-B00CBM1WES/dp/B00CBM1WES
- Plan
    - The references above are laid out essentially in order that they should be looked into, excluding the books.
    - The books section is really optional resources in case you're interested in more content filler.

## PKI / AD Certificate Services Beginner Resources

- \#video #free #3rdParty PKI Foundations for Security Professionals
    - Disclosure: This is a training I was part of, but it really is targeted at new/inexperienced teams.
    - https://www.youtube.com/watch?v=8jEZ3l6dR6c
- \#training #free MS Learn: Implement and manage Active Directory Certificate Services
    - https://learn.microsoft.com/en-us/training/modules/implement-manage-active-directory-certificate-services/
- \#article #free Cryptography for Non-Math People
    - https://michaelwaterman.nl/2026/01/15/cryptography-for-non-math-people/
- \#article #3rdParty What's a Certificate Anyway
    - https://michaelwaterman.nl/2026/07/16/whats-a-certificate-anyway/
- \#article #3rdParty Top 10 PKI Recommendations by a Former MS Security Engineer
    - https://michaelwaterman.nl/2026/02/15/top-10-pki-recommendations-by-a-former-microsoft-security-engineer/
- \#tool #free PurpleKnight
    - https://semperis.com/downloads/tools/pk/PurpleKnight-Community.zip
- \#tool #free Locksmith
    - [https://github.com/jakehildreth/Locksmith](https://github.com/jakehildreth/Locksmith)
- \#article #free How to - Build a PKI with PowerShell
    - https://michaelwaterman.nl/2025/12/31/how-to-build-a-pki-with-powershell-part-1-preparation/

## Entra ID Beginner Resources

- \#training #free Introduction to Microsoft Entra
    - https://learn.microsoft.com/en-us/training/paths/describe-capabilities-of-microsoft-identity-access/
- \#training #free Microsoft Entra Overview
    - https://learn.microsoft.com/en-us/training/entra/
- \#training #free Manage Identity and Access in Microsoft Entra ID
    - https://learn.microsoft.com/en-us/training/paths/manage-identity-and-access/
- \#training #free Deploy and manage identity infrastructure
    - https://learn.microsoft.com/en-us/training/paths/deploy-manage-identity-infrastructure/
- \#training #free Explore Identity in Microsoft Entra ID
    - https://learn.microsoft.com/en-us/training/modules/explore-identity-azure-active-directory/
- \#training #free Develop a security and compliance plan
    - https://learn.microsoft.com/en-us/training/paths/az-400-develop-security-compliance-plan/
- \#tool #free Microsoft 365 Licensing
    - https://m365maps.com/

## Lab Resources / Guides

- \#training #labs #free Getting Started - Identity and Access Labs
    - https://learn.microsoft.com/en-us/training/modules/get-started-identity-access-labs/
- \#training #free Configure and Manage Hyper-V
    - https://learn.microsoft.com/en-us/training/modules/configure-manage-hyper-v/
- \#guide #free Microsoft Zero Trust Lab
    - https://microsoft.github.io/cloudlab/
- \#tool #free AutomatedLab
    - https://github.com/AutomatedLab/AutomatedLab
- \#tool #free Ludus
    - https://docs.ludus.cloud/docs/intro
- \#guide #free SC-300 Identity and Access Administrator Lab Guide
    - https://microsoftlearning.github.io/SC-300-Identity-and-Access-Administrator/
- \#article #free Building Windows Images with Packer on Hyper-V
    - https://michaelwaterman.nl/2026/04/29/building-windows-images-with-packer-on-hyper-v/
- \#article #free How to - Configure Windows Server Core with PowerShell
    - https://michaelwaterman.nl/2026/01/11/how-to-configuring-windows-server-core-with-powershell/

## Other Identity Topics
> Note: These links range from being paid to not and are just grouped by technology.

- Duo Security
    - https://duo.com/docs
    - https://community.duo.com
    - https://duo.com/blog
    - https://duo.com/support/training
- Okta
    - [https://developer.okta.com/docs/](https://developer.okta.com/docs/)
    - https://support.okta.com/help/s/community?language=en_US
    - [https://www.okta.com/blog/](https://www.okta.com/blog/)
    - [https://learning.okta.com/](https://learning.okta.com/)
- CyberArk
    - https://docs.cyberark.com
    - [https://community.cyberark.com/](https://community.cyberark.com/)
    - [https://www.cyberark.com/resources/blog/](https://www.cyberark.com/resources/blog/)
    - [https://www.cyberark.com/services/training/](https://www.cyberark.com/services/training/)
