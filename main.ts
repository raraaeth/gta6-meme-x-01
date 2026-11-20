// gta6-meme-x-01 entry (Node 22, standard library only).
//
// The entry is the post itself: POST.json at the repository root names the
// X post that carries the meme, and this program's whole job is to deliver
// that file, unchanged, to /output/POST.json, where the gate reads it. The
// house then reads the post from X (its first picture and its text) and
// hands that to the judge; nothing this program writes about the post is
// judged.
//
// The kit's starter copied the file blind. This version first reads
// POST.json back and checks that it really names an X post — a JSON object
// whose "url" is an https x.com or twitter.com status address with a
// numeric id — so a leftover placeholder or a mistyped address fails loudly
// here, at run time, instead of being refused quietly at the gate. The copy
// itself stays byte for byte, so two runs write the same bytes.
//
// Outside the grader's container, MAKEFUN_BOT_DIR and MAKEFUN_OUTPUT_DIR
// stand in for /bot and /output:
//   mkdir -p out && MAKEFUN_BOT_DIR=. MAKEFUN_OUTPUT_DIR=out node main.ts

import { copyFileSync, mkdirSync, readFileSync } from 'node:fs';
import { join } from 'node:path';

const BOT_DIR = process.env.MAKEFUN_BOT_DIR ?? '/bot';
const OUTPUT_DIR = process.env.MAKEFUN_OUTPUT_DIR ?? '/output';

// An X post's address: https://x.com/<handle>/status/<digits>, or the same
// on twitter.com. The handle is one path segment of word characters, dots
// or dashes; the id is digits only, as X shows it.
const POST_URL_PATTERN = /^https:\/\/(x\.com|twitter\.com)\/[\w.-]+\/status\/\d+$/;

let post: unknown;
try {
  post = JSON.parse(readFileSync(join(BOT_DIR, 'POST.json'), 'utf8'));
} catch (err) {
  console.error(`POST.json could not be read or parsed: ${(err as Error).message}`);
  process.exit(1);
}

const url = (post as { url?: unknown } | null)?.url;
if (typeof url !== 'string' || !POST_URL_PATTERN.test(url)) {
  console.error(`POST.json does not name an X post: ${JSON.stringify(post)}`);
  process.exit(1);
}

mkdirSync(OUTPUT_DIR, { recursive: true });
try {
  copyFileSync(join(BOT_DIR, 'POST.json'), join(OUTPUT_DIR, 'POST.json'));
} catch (err) {
  console.error(`POST.json could not be copied from ${BOT_DIR}: ${(err as Error).message}`);
  process.exit(1);
}
