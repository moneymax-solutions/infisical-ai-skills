# MoneyMax copy of Infisical/ai-skills

Private copy of <https://github.com/Infisical/ai-skills> (MIT, © Infisical) for the MoneyMax Claude organization's
plugin marketplace (claude.ai › Organization settings › Plugins & skills, synced from GitHub). claude.ai syncs only private
repos, so we keep this copy instead of pointing at Infisical's public repo. Owner: Christopher Cai (Claude System owner).

Imported from upstream `main` at **307e888abf17** on 11 Nov 2026.

## Local changes (re-apply on every refresh)

1. **`.github/workflows/` removed.** Infisical's CI shouldn't run in our GitHub org.
2. **`.claude-plugin/marketplace.json`**: `metadata.pluginRoot` removed and every `source` written as `./plugins/<name>`.
   claude.ai ignores `pluginRoot`; without this the sync skips every plugin ("No files found at source path").
3. **Skill descriptions shortened to ≤ 1024 characters** (claude.ai truncates longer ones and warns). Done for
   app-connections, gateway, kms, kubernetes-operator, pam, pki, secret-rotation and setup by condensing the
   "Covers …" lists only. The "Use this skill when …" triggers and "Not for … (other skill)" pointers were kept as is.

Steps 1 and 2 are scripted; step 3 is by hand because upstream wording changes: `python3 moneymax/patch.py` does 1–2
and lists any description still over 1024.

## Refreshing from upstream

Ask Claude ("refresh the Infisical skills") or do it by hand:

1. Clone upstream and diff its `main` against the commit above; review what changed (look for any new scripts, hooks,
   `.mcp.json` or `settings.json`: today the plugins are Markdown only, and anything executable needs a security review
   before it reaches staff).
2. Replace this repo's content with upstream `main`, keep `MONEYMAX.md` and `moneymax/`, run `python3 moneymax/patch.py`,
   shorten any listed descriptions, and update the commit hash and date above.
3. Commit, push to `main`, then click **Re-sync** in the console and check it says "synced" with no skipped plugins.
   Plugin audiences (Available to install / Not available) are kept across syncs; set one for any new plugin.
4. Note the refresh in the AI Register entry / governance Doc.

Pushing with `gh` needs no `workflow` scope as long as `.github/workflows/` stays removed.
