---
domain: sd
topic: lld_oop_design_problems
title: LLD / object-oriented design problems
tags: [lld, ood, design-patterns, class-design]
count: 139
part: 2/2
---
# LLD / object-oriented design problems (part 2)

## Parking, rental, lodging and travel systems
- [SD07-143] Design a parking lot system with multiple floors, vehicle types, spot allocation, ticketing and fee calculation.
- [SD07-144] In a parking lot design, how would you make the spot-allocation policy pluggable (nearest to entrance, cheapest, by vehicle size) without changing the core classes?
- [SD07-145] How would you extend a parking lot design to support different pricing models such as hourly, daily, peak-hour and EV-charging surcharges?
- [SD07-146] How would a parking lot design handle a lost ticket, a full lot, or a vehicle that does not fit the free spot sizes?
- [SD07-147] In your parking lot design, how do you prevent two vehicles from being assigned the same spot when multiple entry gates operate concurrently?
- [SD07-148] Design a car rental system with vehicles, reservations, pricing, payments and branches.
- [SD07-149] Design a car rental application like Zoomcar with vehicles, locations, availability and bookings.
- [SD07-150] How would you support different pricing rules such as per-day, per-kilometre, insurance add-ons and late fees in a rental system model?
- [SD07-151] How would you prevent double-booking of a vehicle for overlapping date ranges in a car rental design?
- [SD07-152] Design a hotel management system with rooms, bookings, check-in/check-out, housekeeping and billing.
- [SD07-153] How would you design room types and dynamic pricing in a hotel management class model?
- [SD07-154] How would you model room availability search and overlapping reservations in a hotel booking design to avoid overbooking?
- [SD07-155] Design an airline management system covering flights, schedules, seat reservation, crew and passengers.
- [SD07-156] How would you model flight search with layovers and fare classes in an airline system class design?
- [SD07-157] How would you design seat selection so that two passengers cannot reserve the same seat concurrently in an airline booking model?
- [SD07-158] Design a library management system with books, members, lending, returns and fines.
- [SD07-159] How would you model multiple copies of the same book, reservations and waiting lists in a library system?
- [SD07-160] How would you design the fine calculation and notification flow in a library management system so new rules can be added easily?
- [SD07-161] Design a package locker service that assigns a locker of sufficient size to each package and handles pickup codes.
- [SD07-162] How would you choose a locker for a package when multiple sizes are available, and how would you handle expiry of uncollected packages?
- [SD07-163] Design an airport runway allocation service that assigns a free runway to landing planes.
- [SD07-164] How do you ensure a runway is never allocated to two aircraft at once, and what happens when none is available?

## Ticketing, appointments and resource scheduling
- [SD07-165] Design a movie ticket booking system like BookMyShow with cinemas, screens, shows, seats and bookings.
- [SD07-166] How would you model city-wise cinema search, show timings and dynamic pricing in a movie ticket booking design?
- [SD07-167] How do you design seat locking, timeout release and payment confirmation so that no seat is double-booked in a movie booking system?
- [SD07-168] Design a concert ticket booking system with events, seat maps, holds and payments.
- [SD07-169] How would you implement temporary seat holds with expiry in a ticket booking design and release them if payment fails?
- [SD07-170] How do you prevent overselling when thousands of users try to book the same seats at the same time in a ticket booking class design?
- [SD07-171] How would you make cancellation and refund policies configurable in a booking system without modifying the booking classes?
- [SD07-172] Design an appointment booking system for a hospital where each doctor can open slots independently for any time period.
- [SD07-173] Design a meeting room scheduler that books a free room for a time interval, notifies attendees and shows booking history.
- [SD07-174] How would you detect room availability and interval conflicts efficiently when there are many meeting rooms and bookings?
- [SD07-175] How would you store the bookings of one resource so an overlap check is faster than a linear scan, for example with a sorted structure or interval tree?
- [SD07-176] Design a university course registration system with courses, students, prerequisites, capacity and waitlists.
- [SD07-177] How would you model prerequisite and schedule-conflict validation in a course registration system?
- [SD07-178] How would you handle concurrent enrollment into a course with limited capacity and automatically promote waitlisted students?
- [SD07-179] Design a restaurant management system with tables, reservations, orders, kitchen workflow and billing.
- [SD07-180] How would you model the order lifecycle from placement to kitchen preparation to serving and billing in a restaurant system?
- [SD07-181] Design an application for restaurants or malls that handles the waiting queue and assigns tables efficiently.
- [SD07-182] How would you assign tables to waiting parties and handle merged or split tables in a restaurant system design?

## E-commerce, auctions and payments
- [SD07-183] Design an online shopping system like Amazon with catalog, cart, orders, payments, inventory and shipping.
- [SD07-184] How would you structure discounts, coupons and tax calculation in a shopping cart design to keep pricing rules extensible?
- [SD07-185] How would you design the order state machine and shipping integration in an e-commerce class model?
- [SD07-186] In a shopping cart design, what happens when an item's price or stock changes between add-to-cart and checkout, and where do you re-validate?
- [SD07-187] How would you design inventory reservation and order placement so stock never goes negative under concurrent checkouts?
- [SD07-188] Design an e-commerce product review and rating system.
- [SD07-189] Design an online auction system with listings, bidding, auction closing and winner selection.
- [SD07-190] How would you support different auction types (English, Dutch, sealed-bid) using the strategy pattern in an auction design?
- [SD07-191] How do you handle two bids arriving at the same instant or a last-second bid in an online auction design?
- [SD07-192] Design an eBay-style billing and auctioning system where sellers pay listing and sale fees and buyers bid.
- [SD07-193] Design a digital wallet service with accounts, top-ups, transfers and transaction history.
- [SD07-194] How would you model multi-currency support and transaction limits in a digital wallet design?
- [SD07-195] How would you guarantee atomic, deadlock-free money transfers between two wallets in a class-level design?
- [SD07-196] How would you make wallet operations idempotent so that retries do not double-debit?
- [SD07-197] Design a payment system with multiple payment methods, transactions, refunds and statuses.
- [SD07-198] How would you design a payment gateway class model with pluggable processors, retry logic and idempotent charge requests?
- [SD07-199] How would you model partial refunds and chargebacks so the original transaction record stays consistent and auditable?
- [SD07-200] Design a generic coupon and promo code system supporting percentage and flat discounts, minimum cart sizes, customer and merchant targeting, and usage limits.
- [SD07-201] How would you design composable coupon rules so combinations of conditions and discount types can be added without code changes in a promo system?
- [SD07-202] How would you enforce a per-user usage limit on coupons under concurrent redemption in a coupon system?
- [SD07-203] Design an expense-sharing application like Splitwise with groups, equal, exact and percentage splits, and balances.
- [SD07-204] How would you apply the strategy pattern to different split types in an expense-sharing application?
- [SD07-205] How would you handle rounding errors and currency in an expense-splitting design?
- [SD07-206] How would you implement debt simplification to minimize the number of settlement transactions in an expense-sharing design?

## Ride-hailing, delivery and trading
- [SD07-207] Design a ride-sharing service like Uber with riders, drivers, ride requests, matching, pricing and payments.
- [SD07-208] How would the state pattern model the lifecycle of a ride from requested to completed or cancelled?
- [SD07-209] How would you design pluggable driver-matching and surge pricing strategies in a ride-sharing class model?
- [SD07-210] How would you handle concurrent ride requests competing for the same nearby driver in a ride-sharing design?
- [SD07-211] How would you index driver locations in memory so nearby-driver lookup does not scan every driver?
- [SD07-212] Design a ride-sharing matching component where drivers offer rides with seats and riders request rides, and the best overlapping match is chosen.
- [SD07-213] Design a food delivery service like Swiggy with restaurants, menus, orders, delivery partners and tracking.
- [SD07-214] How would you support promotions, surge fees and order cancellations in a food delivery design?
- [SD07-215] How would you design delivery partner assignment and order-status tracking in a food delivery class model?
- [SD07-216] Design an online stock brokerage or trading system with accounts, portfolios, buy and sell orders and an order book.
- [SD07-217] Design a personal stock and investment portfolio system.
- [SD07-218] Design a system where a user can create price alerts on stock options.
- [SD07-219] Design a stock exchange matching engine that matches buy and sell orders and outputs executed trades.
- [SD07-220] Design a limit order book for a trading system, and explain how the data structure supports add, cancel and match efficiently.
- [SD07-221] How would you design order matching for market and limit orders in a brokerage or exchange class model?
- [SD07-222] How would you ensure price-time priority and thread safety in an order book implementation?
- [SD07-223] How would you ensure fairness and determinism in an order matching engine when orders arrive concurrently?
- [SD07-224] How does your matching engine handle partial fills, order amendments and cancellations of resting orders?

## Social, Q&A and media platforms
- [SD07-225] Design a Q&A platform like Stack Overflow covering questions, answers, comments, tags, votes and reputation.
- [SD07-226] How would you design tag-based search and the accepted-answer workflow in a Q&A platform class model?
- [SD07-227] In a Stack Overflow style design, how would you model voting and reputation so the logic is extensible and safe under concurrent votes?
- [SD07-228] Design a product Q&A application like the Q&A on Amazon or Walmart with questions, answers, voting and moderation.
- [SD07-229] Design a professional networking platform like LinkedIn with profiles, connections, posts, jobs and messaging.
- [SD07-230] How would you design the notification and feed-update mechanism for a professional network at the class level?
- [SD07-231] How would you model connection requests, degrees of connection and job recommendations in a LinkedIn style class design?
- [SD07-232] Design a social network like Facebook with users, friends, posts, comments, likes and a news feed.
- [SD07-233] How would the observer pattern apply to notifications for likes and comments in a social network design?
- [SD07-234] How would you design the news feed generation and privacy settings in a social network class model?
- [SD07-235] Design a chat application like WhatsApp with users, one-to-one and group conversations, and message status.
- [SD07-236] How would you model sent, delivered and read message states and group membership changes in a chat design?
- [SD07-237] Design a call center with employees, escalation levels and call routing.
- [SD07-238] Design a Truecaller-like caller-ID and spam-detection service with contacts, number lookup and spam reporting.
- [SD07-239] Design a music streaming service like Spotify with songs, playlists, users, playback and recommendations.
- [SD07-240] How would you model playback queue, shuffle and repeat behaviours with the strategy or state pattern in a music player design?
- [SD07-241] How would you design the recommendation hook so different algorithms can be plugged into a music streaming model?
- [SD07-242] Design a system that recommends songs from a music library based on a user's preferences (genre, singer, tempo) and their current playlist.
- [SD07-243] Design a live cricket scoring and information system like CricInfo with matches, innings, overs, balls and scorecards.
- [SD07-244] How would you model player and team statistics aggregation in a sports scoring system so new statistics can be added easily?
- [SD07-245] How would you design live score updates and commentary delivery to many viewers in a cricket scoring model?
- [SD07-246] Design a subscription-based sports website that can display scores, game status and history for any game.

## Productivity and workflow tools
- [SD07-247] Design a task management system like Trello with tasks, users, priorities, status and assignments.
- [SD07-248] How would you model task state transitions, subtasks and dependencies in a task management system without hard-coding the workflow?
- [SD07-249] How would you add notifications, activity history and undo to a task management system design, and which patterns would you choose?
- [SD07-250] Design a Jira-like issue tracker with stories, features, bugs, subtasks, sprints and status changes.
- [SD07-251] Design a task planner with bug, feature and story types, each with its own attributes, where a sprint is a collection of tasks.
- [SD07-252] How would you generate sprint reports such as delayed tasks, tasks per user and sprint summary without bloating the core classes?
- [SD07-253] Design a calendar application like Google Calendar with events, invitations, accept and reject states and per-user calendars.
- [SD07-254] How would you model recurring events and time zones in a calendar class design?
- [SD07-255] How would you find a common free time slot for a set of users in a calendar design, and what is the complexity?
- [SD07-256] Design a service to view, add and remove viewers of a document, like the sharing feature in Google Docs.
- [SD07-257] How would you model owner, editor and viewer permissions on shared documents so new roles can be added easily?
- [SD07-258] Design a notification service that notifies a list of users of different types (delivery agents, employees, end users) and sends to iOS, Android and email channels.
- [SD07-259] How would you design a notification system so that adding a new delivery channel does not require changing existing code?
- [SD07-260] How do you add retries, rate limiting, user preferences and deduplication to a notification class design?
- [SD07-261] Design a service that returns the recently viewed listings of a user on a website.
- [SD07-262] Design a system that keeps track of the leaders of a contest, such as a referral leaderboard.
- [SD07-263] Design a maps navigation client that builds a route between two points for walking, driving, bus and cycling.
- [SD07-264] How would the strategy pattern help a navigation client support different transport modes and routing preferences?

## Enterprise, inventory and learning systems
- [SD07-265] Design an inventory management system with stock levels, reorder points and multiple warehouses.
- [SD07-266] Design a warehouse management system with receiving, putaway, picking and shipping.
- [SD07-267] How would you model on-hand versus reserved stock in an inventory design so concurrent picks never oversell?
- [SD07-268] Design a guitar inventory system where instruments are searchable by attributes.
- [SD07-269] How would you design flexible attribute-based search for an inventory system so new criteria do not require new methods?
- [SD07-270] Design a system for storing chemicals with their constituents in an efficiently retrievable format.
- [SD07-271] Design a logistics system with shipments, hubs, vehicles and tracking.
- [SD07-272] Design an applicant tracking system like Greenhouse with job postings, candidates, pipeline stages and recruiters.
- [SD07-273] Design an employee management platform with payroll, benefits and IT provisioning modules.
- [SD07-274] Design an electronic signature workflow with documents, signers, ordering and audit trail.
- [SD07-275] Design a mock interview matching platform like Pramp.
- [SD07-276] Design an online book reader system with users, libraries, bookmarks and reading sessions.
- [SD07-277] Design a learning management system with courses, lessons, enrollments and progress tracking, where teachers upload content and students view it.
- [SD07-278] Build an object-oriented system for managing courses, grades and students.
- [SD07-279] Design an online assessment platform for timed exams with question banks, attempts, scoring, past results and rankings.
- [SD07-280] Design a survey application like Google Forms or SurveyMonkey with question types, responses and analytics.
- [SD07-281] Build the task-lifecycle core of an annotation platform: start simple, then add consensus of k annotators, priority re-review and annotator cooldowns.
