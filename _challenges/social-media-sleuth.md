---
layout: challenge
title: "Social Media Sleuth"
difficulty: Easy
category: Social Media
questions:
  - title: "Identify the Target's Location"
    description: "Based on the social media posts and metadata, what city is the target located in?"
    answer: "seattle"
  - title: "Professional Background"
    description: "What is the target's current job title according to their LinkedIn profile?"
    answer: "software engineer"
  - title: "Hidden Connection"
    description: "Which organization appears in both their Twitter bio and GitHub contributions?"
    answer: "mozilla"
files:
  - name: "social_media_data.json"
    path: "/assets/challenges/social-media-sleuth/social_media_data.json"
  - name: "profile_metadata.txt"
    path: "/assets/challenges/social-media-sleuth/profile_metadata.txt"
hints:
  - "Look for location tags in their recent Instagram posts"
  - "Check the company information section on LinkedIn"
  - "Cross-reference their GitHub organizations with Twitter bio"
---

## Background
A target individual has been identified using the handle "@digitalshadow" across various social media platforms. Your task is to gather intelligence about this person using only publicly available information.

## Objective
Using the provided social media data exports and profile metadata, you need to:
1. Determine their current location
2. Identify their professional role
3. Find connections between their different social media accounts

## Resources
The provided files contain:
- JSON export of their social media activity
- Metadata from profile pictures and posts
- Public profile information

## Notes
- All information needed can be found through OSINT techniques
- No direct contact with the target is allowed
- Document your methodology

Remember to follow ethical OSINT practices and respect privacy boundaries while completing this challenge.
