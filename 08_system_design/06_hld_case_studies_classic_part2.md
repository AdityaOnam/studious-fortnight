---
domain: sd
topic: hld_case_studies_classic
title: HLD case studies (classic)
tags: [hld, case-study, design-x]
count: 103
part: 2/3
---
# HLD case studies (classic) (part 2)

## Twitter and news feed
- [SD06-104] Design the Twitter home timeline and search for hundreds of millions of users.
- [SD06-105] Design the data model and API for posting a tweet, following a user and fetching a newsfeed.
- [SD06-106] Design Facebook News Feed.
- [SD06-107] What best practices and scaling issues should you keep in mind when building a news feed for a social network?
- [SD06-108] Compare fan-out on write and fan-out on read for a social news feed. How do you handle celebrity accounts with millions of followers?
- [SD06-109] How would you store the home timeline for each user in a cache, and how large can that cache get?
- [SD06-110] How would you rank items in a newsfeed using recency, engagement and relationship signals?
- [SD06-111] How would you design tweet search so that new tweets are searchable within seconds?
- [SD06-112] How would you support retweets and mutual friends computation in a Twitter-like system?
- [SD06-113] Which entities would you shard in a Twitter-like system and by what keys?
- [SD06-114] How would you deliver notifications for mentions, likes and new followers at social-network scale?
- [SD06-115] In a Twitter-like feed, what consistency do users expect for their own tweets versus other people's tweets, and how do you provide it?
- [SD06-116] In a news feed system, how do you recover when the cache holding precomputed timelines fails, and what is the load impact on the database?
- [SD06-117] At 10x traffic, which components of a fan-out-on-write feed break first, and how would you scale them?
- [SD06-118] How do you handle a user deleting a post or blocking another user in a precomputed feed design?
- [SD06-119] Design a feed system for an Instagram or Pinterest style product that mixes photos from followed accounts with recommendations.
- [SD06-120] Design Instagram.
- [SD06-121] Design Pinterest: pins, boards, following users and a home feed.
- [SD06-122] Design a short-video sharing platform like TikTok, including its feed and recommendation path.

## Social graph and connections
- [SD06-123] Design the data structures for a social network so a user can see the shortest connection path to another user.
- [SD06-124] How would you run a bidirectional breadth-first search on a social graph that is sharded across machines?
- [SD06-125] Design a follow-graph service for a 50 million user social network that efficiently answers who I follow and who follows me.
- [SD06-126] Design a social graph store like TAO optimized for read-heavy workloads with a 500:1 read-to-write ratio.
- [SD06-127] Design a read-heavy social media profile service that handles 500 reads per write with a graph-aware cache layer.
- [SD06-128] For a social graph service, how do you keep friend counts and mutual-friend queries consistent and fast?
- [SD06-129] Design LinkedIn's suggested connections feature.
- [SD06-130] Design a feature for tagging people in photos with an optional rectangular region of interest.

## Hashtags, trending and engagement counters
- [SD06-131] Design a hashtag service for a photo-sharing network handling 5 million uploads per hour with about 8 hashtags each, showing the photo count and top 50 photos per hashtag.
- [SD06-132] How do you maintain the top 50 photos per hashtag and the total photo count under heavy write skew for trending hashtags?
- [SD06-133] How do you identify trending topics in a Twitter-like system?
- [SD06-134] How would you keep an exact or approximate like counter for a viral post receiving millions of likes per minute?
- [SD06-135] Design a realtime clap counter for an article platform where all readers of an article see updates instantly, with up to 10,000 concurrent readers per article.

## Discussion forums and Q&A sites
- [SD06-136] How would you design Stack Overflow?
- [SD06-137] Design a discussion forum that supports posting, upvotes and ranking by popularity at scale.
- [SD06-138] Design Reddit-style nested comment threads with voting. How do you store the tree and rank comments efficiently?

## Chat and messaging
- [SD06-139] Design a chat application like WhatsApp, Messenger or WeChat that supports one-to-one and group messaging.
- [SD06-140] How would you design a globally distributed chat system?
- [SD06-141] Design a simple chat application using Redis pub-sub and sorted sets, and discuss its limits.
- [SD06-142] How do you deliver messages in real time to online users and store them for offline users in a chat system?
- [SD06-143] How would you implement message delivery and read receipts in a chat system?
- [SD06-144] How would you guarantee messages are delivered in order and exactly once from the user's point of view in a chat system?
- [SD06-145] What consistency model applies to message ordering within a conversation versus across conversations?
- [SD06-146] A user's phone goes offline mid-send and reconnects on another network. How do you avoid lost, duplicate or reordered messages?
- [SD06-147] How would you scale persistent WebSocket connections to hundreds of millions of concurrent users?
- [SD06-148] When a chat server holding thousands of WebSocket connections crashes, how do clients reconnect and how is state restored?
- [SD06-149] How do you design group chat with thousands of members, including fan-out and ordering?
- [SD06-150] Which database would you choose for chat message storage, and how would you partition it?
- [SD06-151] How would you store and serve media attachments in a chat system, and how would end-to-end encryption change the design?
- [SD06-152] How would you handle inter-service communication and service discovery in a chat application architecture?
- [SD06-153] Design Slack's real-time messaging, including channels, presence, typing indicators, message history and fan-out to connected clients.
- [SD06-154] What is the journey of a message in Slack, from sender to every recipient?
- [SD06-155] Design a video conferencing service. How does media flow between participants, and when do you need a media server?
- [SD06-156] Design a real-time translation layer for a chat or meeting product. What latency and quality trade-offs arise?

## Presence and unread indicators
- [SD06-157] Design an online/offline presence indicator for a chat application that shows within about 10 seconds whether a user is online, for 5 million concurrent users.
- [SD06-158] How would you use heartbeats and TTL-based keys to implement presence, and how lenient can you be in marking users offline?
- [SD06-159] How do you fan out presence changes to a user's friends without a thundering herd of updates?
- [SD06-160] Design a newly-unread-message indicator showing the number of distinct users who sent new messages, resetting to zero when clicked, for 1 million daily active users.

## Video upload and processing
- [SD06-161] How does YouTube handle massive video uploads?
- [SD06-162] Design a video processing pipeline for a streaming service covering upload, storage, transcoding, post-processing and caching, processing thousands of videos in parallel.
- [SD06-163] Describe the video upload pipeline: transcoding into multiple resolutions and codecs, chunking and storing the results.
- [SD06-164] Design a robust, resumable upload flow for large video files, including users on low-bandwidth networks.
- [SD06-165] How does on-demand video optimization work in a video streaming service?
- [SD06-166] In a video platform, how do you handle a failed transcoding job in the middle of a long video?
- [SD06-167] How do you ensure uploaded videos are durable and not lost if a storage node fails?
- [SD06-168] Design a system that blurs license plates and faces in street-level imagery at scale.

## Video streaming and CDNs
- [SD06-169] Design YouTube or Netflix: users upload or watch videos, with search, comments and recommendations.
- [SD06-170] Design Amazon Prime Video.
- [SD06-171] How does adaptive bitrate streaming work, and what does the server need to produce for it?
- [SD06-172] How do you use CDNs and regional caches to serve popular video and reduce origin load?
- [SD06-173] How do geo-blocking and licensing restrictions fit into a video streaming platform?
- [SD06-174] Estimate storage and egress bandwidth for a video platform with 200 million users each watching an hour a day.
- [SD06-175] Design the service that stores viewing history, playback position and the currently active viewers on an account.
- [SD06-176] Why would you keep active view state in memory partitioned by account, and how do you cope with node failure and hot partitions?
- [SD06-177] How would you store users' viewing events at scale, with billions of events per day, for a streaming service?
- [SD06-178] How do you identify trending content in a video streaming service?
- [SD06-179] Design a video search and recommendation capability for a streaming service.
- [SD06-180] How does live streaming differ architecturally from video on demand? Walk through capture, encoding, segmenting and CDN delivery.
- [SD06-181] Compare RTMP, HLS and DASH for live streaming.
- [SD06-182] A newly released popular title lands on cold CDN caches and traffic surges. How do you handle it?
- [SD06-183] What is the difference between Netflix's Open Connect and a traditional CDN?
- [SD06-184] Design a music streaming service like Spotify, including catalog, playlists and offline downloads.
- [SD06-185] Design a content delivery network. How do edge caches, origin shielding and request routing work?
- [SD06-186] How does a CDN decide what to cache at the edge, and how do you purge or invalidate content globally?
- [SD06-187] How does a CDN route a user to the nearest healthy edge location, and what happens when an edge location fails?

## Object storage, file sync and sharing
- [SD06-188] Design a global file storage system such as Dropbox with chunking, deduplication and sync conflict resolution.
- [SD06-189] Design a file sharing and distribution system.
- [SD06-190] Design a remote file sync service that syncs files up to 4 GB across all of a user's devices with resumable, bandwidth-efficient transfers.
- [SD06-191] How would chunking, content hashing and delta sync reduce bandwidth in a file sync service?
- [SD06-192] How do you detect and resolve conflicting edits made on two devices while offline in a file sync service?
- [SD06-193] Design a Dropbox-like metadata service. How do you represent files, versions and chunks in the metadata store?
- [SD06-194] Design a distributed cloud object store like S3 with durability across failures.
- [SD06-195] How do you protect against silent data corruption and ensure durability in a photo or file storage system?
- [SD06-196] Design a photo storage service for billions of images with low-latency reads.
- [SD06-197] Design a torrent service end to end.
- [SD06-198] Design a repository hosting service with millions of git repos where individual files are tens to hundreds of GB.
- [SD06-199] Design an image service that handles 5 million uploads per hour and serves device-optimized images with near-optimal bandwidth.
- [SD06-200] Should device-specific image variants be generated on demand or at upload time, and what are the cost trade-offs?
- [SD06-201] Design a service that gives every user one stable image URL that always shows their current profile picture, with 50,000 uploads per minute and a 100000:1 read-to-write ratio.

## Collaboration and email
- [SD06-202] Design a real-time collaborative document editor such as Google Docs, including conflict handling.
- [SD06-203] Design an online code editor that supports multiple users editing and running code.
- [SD06-204] Compare operational transformation and CRDTs for collaborative editing. When would you choose each?
- [SD06-205] Design an email system like Gmail. What happens when one user sends an email to another across providers?
- [SD06-206] In an email system, how do you handle spam filtering, large attachments and mailbox storage growth?
