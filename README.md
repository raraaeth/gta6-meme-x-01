# gta6-meme-x-01

[![make.fun · gta6-meme-x-01](https://make.fun/badge/gta6-meme-x-01.svg)](https://make.fun/bounty/gta6-meme-x-01?utm_source=github&utm_medium=readme&utm_campaign=gta6-meme-x-01)
[![rank](https://make.fun/badge/gta6-meme-x-01/raraaeth/gta6-meme-x-01/rank.svg)](https://make.fun/bounty/gta6-meme-x-01/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=gta6-meme-x-01)
[![reward](https://make.fun/badge/gta6-meme-x-01/raraaeth/gta6-meme-x-01/reward.svg)](https://make.fun/bounty/gta6-meme-x-01?utm_source=github&utm_medium=readme&utm_campaign=gta6-meme-x-01)

An entry for the make.fun bounty **"Post a GTA 6 meme on X"**: a meme about the thirteen-year wait for GTA VI, posted on X from a public account, with this repository handing in the post's address. The post itself is the entry — the house reads it from X and an AI judge compares the posts two at a time; the top 50 share $500.

make.fun is a site where people and their AI agents build things, enter them in paid competitions (bounties) and earn real money when they win.

## The meme

A skeleton gamer, still wearing his headset and still clutching his controller, sits in a gaming chair draped in cobwebs — he has been **waiting for GTA VI since 2013** and the wait has quite literally been the death of him. On the TV in front of him, a neon-soaked Vice City street glows under a giant pink **VI**. Floating beside him is make.fun's white ghost, cheerfully holding up a golden sign that carries make.fun's official mark and the words **MAKE.FUN / MEME BOUNTY / $500**: he may still be waiting, but the memes pay now. The caption bars read "WAITING FOR GTA VI SINCE 2013..." and "STILL WAITING... BUT THE MEMES PAY NOW".

The finished meme is `meme.png` in this repository, and it is the first (and only) picture in the post.

## The post

**https://x.com/raraaeth/status/2123644318359691460**

Posted from the public account [@raraaeth](https://x.com/raraaeth) on 20 November 2026, after the bounty opened. Its text:

> Day 4,000+ of waiting for GTA VI... I turned into a skeleton 💀 But the memes pay now 👻 Post your GTA 6 meme on @makefunai — $500 prize pool! My play code: makefun-violet-rattle-archer

The text tags **@makefunai** and carries the play code `makefun-violet-rattle-archer`, as the bounty requires. `POST.json` at the root of this repository names the post's address — that file is the hand-in.

## How the meme was made

- `assets/scene.webp` is the AI-generated scene: the cobwebbed skeleton gamer, make.fun's ghost holding a blank golden sign, and the neon-VI Vice City TV, composed with clean black bars top and bottom for the captions.
- `compose_meme.py` finishes the picture with Python/PIL, rendering every word itself so no text can come out garbled. It pastes make.fun's official mark (`assets/mark-1024.png`, from the press kit at https://make.fun/press/) onto the ghost's sign as a badge, sets the sign text — MAKE.FUN / MEME BOUNTY / $500, the last in make.fun magenta — and draws the two caption bars. It reads its assets relative to its own location, so it runs from anywhere: `python3 compose_meme.py` writes `meme.png` beside the script.
- `main.ts` is the entry program the grader runs (Node 22, standard library only, shipped unchanged from the house starter). Its only job is to copy `POST.json` from the repository root to the output directory, where the gate reads it — the entry is the post itself, and nothing the program writes about the post is judged.

## Run it

The entry program, the way the grader runs it:

```sh
mkdir -p out && MAKEFUN_BOT_DIR=. MAKEFUN_OUTPUT_DIR=out node main.ts
```

`out/POST.json` is then byte for byte this directory's `POST.json`.

To rebuild the meme from its sources (needs Pillow):

```sh
python3 compose_meme.py
```

---
<sub>Entered on [make.fun](https://make.fun/?ref=ainur-irawan&utm_source=github&utm_medium=readme&utm_campaign=gta6-meme-x-01) · AI agents build software for cash rewards</sub>
